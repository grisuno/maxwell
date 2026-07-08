#!/usr/bin/env python3
"""
maxwell_orbital_diagnostic.py

Layer-by-layer diagnostic for the Maxwell magnetic orbital isomorphism experiment.

Three operating modes:

  1. PASSTHROUGH -- Identity-initialised network (spectral kernels = delta function).
     If isomorphism survives passthrough, the architecture is compatible.
     If not, the projection/comparison pipeline has a bug.

  2. LAYER_TRACE -- Feed the dipole source through the trained network one layer
     at a time, measuring spatial correlation with the hydrogen orbital after each.
     Identifies the exact layer where the angular structure collapses.

  3. SYMMETRY_LOSS_TRAINING -- Short training run with an additional rotational
     symmetry preservation loss that penalises the network for breaking the
     angular structure of the input.  Tests whether symmetry-aware training
     can recover the isomorphism.

Also fixes the m=0 sph_harm phase convention issue by ensuring Y_l^0 is
computed with the correct real-part extraction (scipy uses theta as polar
and phi as azimuthal, matching physics convention).

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date: 2026
License: AGPL v3
"""

import argparse, glob, json, logging, os, warnings, math
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any
from dataclasses import dataclass
import numpy as np
from scipy.special import sph_harm, factorial, genlaguerre
import torch, torch.nn as nn, torch.nn.functional as F
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
warnings.filterwarnings('ignore')


@dataclass(frozen=True)
class DiagnosticConfig:
    """Configuration for the diagnostic suite."""
    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    FIELD_COMPONENTS: int = 3
    DEFAULT_IMAGINARY_RATIO: float = 0.3
    EQUATORIAL_THETA: float = 1.5707963267948966
    SPATIAL_EXTENT: float = 3.141592653589793
    PERMEABILITY_FACTOR: float = 1.0
    DIPOLE_MOMENT_MAGNITUDE: float = 1.0
    DIPOLE_REGULARIZATION: float = 0.3
    SOURCE_AMPLITUDE_SCALE: float = 0.1
    ORBITAL_R_MAX_FACTOR: float = 4.0
    ORBITAL_R_MAX_OFFSET: float = 10.0
    HALL_SENSOR_NUM_ANGLES: int = 8
    ISOMORPHISM_NODE_THRESHOLD: float = 0.01
    ISOMORPHISM_GAMMA_EXPONENT: float = 0.3
    NORMALIZATION_EPS: float = 1e-10
    SYMMETRY_LOSS_WEIGHT: float = 0.5
    SYMMETRY_TRAINING_EPOCHS: int = 200
    SYMMETRY_TRAINING_LR: float = 1e-4
    SYMMETRY_NUM_ROTATIONS: int = 4
    IDENTITY_KERNEL_SCALE: float = 0.001
    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    LOG_LEVEL: str = 'INFO'
    FIGURE_DPI: int = 150
    SAVE_FORMAT: str = 'png'
    OUTPUT_DIRECTORY: str = 'orbital_diagnostic'
    CHECKPOINT_DIR: str = 'checkpoints_maxwell_phase3'


class LoggerFactory:
    """Factory for creating configured logger instances."""
    @staticmethod
    def create_logger(name: str, level: str = 'INFO') -> logging.Logger:
        """Create and return a configured logger."""
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        if not logger.handlers:
            h = logging.StreamHandler()
            h.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(h)
        return logger


class SpectralLayer(nn.Module):
    """Spectral convolution layer with tuneable imaginary ratio."""
    def __init__(self, channels: int, grid_size: int, imaginary_ratio: float = 0.3):
        """Initialise real and imaginary kernel parameters."""
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        self.imaginary_ratio = imaginary_ratio
        self.kernel_real = nn.Parameter(torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1)
        self.kernel_imag = nn.Parameter(torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply spectral convolution in Fourier space."""
        x_fft = torch.fft.rfft2(x)
        b, c, fh, fw = x_fft.shape
        kr = F.interpolate(self.kernel_real.mean(dim=0).unsqueeze(0).unsqueeze(0).squeeze(0),
                           size=(fh, fw), mode='bilinear', align_corners=False)
        ki = F.interpolate(self.kernel_imag.mean(dim=0).unsqueeze(0).unsqueeze(0).squeeze(0),
                           size=(fh, fw), mode='bilinear', align_corners=False)
        rp = x_fft.real * kr - x_fft.imag * ki
        ip = x_fft.real * ki + x_fft.imag * kr
        return torch.fft.irfft2(torch.complex(rp, ip), s=(self.grid_size, self.grid_size))

    def init_identity(self, scale: float = 0.001):
        """Initialise kernels near identity: real=small, imag=0."""
        with torch.no_grad():
            self.kernel_real.data.zero_()
            n = min(self.channels, self.kernel_real.shape[2], self.kernel_real.shape[3])
            for i in range(n):
                if i < self.kernel_real.shape[2] and i < self.kernel_real.shape[3]:
                    self.kernel_real.data[:, :, 0, 0] = torch.eye(self.channels) * (1.0 + scale)
            self.kernel_imag.data.zero_()


class MaxwellSpectralNetwork(nn.Module):
    """Neural network for learning Maxwell equation dynamics."""
    def __init__(self, config: DiagnosticConfig, imaginary_ratio: float = 0.3):
        """Build all sub-layers."""
        super().__init__()
        self.config = config
        self.grid_size = config.GRID_SIZE
        self.input_channels = config.FIELD_COMPONENTS * 2
        self.output_channels = config.FIELD_COMPONENTS * 2
        self.imaginary_ratio = imaginary_ratio
        self.input_proj = nn.Conv2d(self.input_channels, config.HIDDEN_DIM, kernel_size=1)
        self.expansion_proj = nn.Conv2d(config.HIDDEN_DIM, config.EXPANSION_DIM, kernel_size=1)
        self.spectral_layers = nn.ModuleList([
            SpectralLayer(config.EXPANSION_DIM, config.GRID_SIZE, imaginary_ratio)
            for _ in range(config.NUM_SPECTRAL_LAYERS)])
        self.contraction_proj = nn.Conv2d(config.EXPANSION_DIM, config.HIDDEN_DIM, kernel_size=1)
        self.output_proj = nn.Conv2d(config.HIDDEN_DIM, self.output_channels, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass."""
        if x.dim() == 3: x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for sl in self.spectral_layers: x = F.gelu(sl(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)

    def forward_with_intermediates(self, x: torch.Tensor) -> List[torch.Tensor]:
        """Forward pass returning the output after every sub-layer."""
        if x.dim() == 3: x = x.unsqueeze(0)
        intermediates = [x.clone()]
        x = F.gelu(self.input_proj(x)); intermediates.append(x.clone())
        x = F.gelu(self.expansion_proj(x)); intermediates.append(x.clone())
        for i, sl in enumerate(self.spectral_layers):
            x = F.gelu(sl(x)); intermediates.append(x.clone())
        x = F.gelu(self.contraction_proj(x)); intermediates.append(x.clone())
        x = self.output_proj(x); intermediates.append(x.clone())
        return intermediates

    def init_identity(self):
        """Initialise all layers near identity / passthrough."""
        scale = self.config.IDENTITY_KERNEL_SCALE
        with torch.no_grad():
            nn.init.eye_(self.input_proj.weight[:, :min(self.input_channels, self.config.HIDDEN_DIM), 0, 0])
            if self.input_proj.bias is not None: self.input_proj.bias.zero_()
            nn.init.eye_(self.expansion_proj.weight[:, :min(self.config.HIDDEN_DIM, self.config.EXPANSION_DIM), 0, 0])
            if self.expansion_proj.bias is not None: self.expansion_proj.bias.zero_()
            for sl in self.spectral_layers: sl.init_identity(scale)
            nn.init.eye_(self.contraction_proj.weight[:, :min(self.config.EXPANSION_DIM, self.config.HIDDEN_DIM), 0, 0])
            if self.contraction_proj.bias is not None: self.contraction_proj.bias.zero_()
            nn.init.eye_(self.output_proj.weight[:, :min(self.config.HIDDEN_DIM, self.output_channels), 0, 0])
            if self.output_proj.bias is not None: self.output_proj.bias.zero_()


class AnalyticalMultipoleSource:
    """Analytical EM multipole sources (same as corrected main script)."""
    def __init__(self, config: DiagnosticConfig):
        """Precompute coordinate grids in the equatorial plane."""
        self.config = config
        N = config.GRID_SIZE
        ext = config.SPATIAL_EXTENT
        x = torch.linspace(-ext, ext, N); y = torch.linspace(-ext, ext, N)
        self.X, self.Y = torch.meshgrid(x, y, indexing='ij')
        self.R = torch.sqrt(self.X**2 + self.Y**2) + config.DIPOLE_REGULARIZATION
        self.PHI = torch.atan2(self.Y, self.X)
        self.x_np, self.y_np = self.X.numpy(), self.Y.numpy()
        self.r_np, self.phi_np = self.R.numpy(), self.PHI.numpy()

    def generate(self, l: int, m: int) -> torch.Tensor:
        """Return a (6,H,W) source tensor for the l-th multipole."""
        if l == 0: return self._monopole_proxy()
        if l == 1: return self._dipole(m)
        return self._multipole(l, m)

    def _dipole(self, m: int) -> torch.Tensor:
        """Analytical magnetic dipole B-field in equatorial plane."""
        r3 = self.r_np**3
        mu = self.config.PERMEABILITY_FACTOR * self.config.DIPOLE_MOMENT_MAGNITUDE
        s = self.config.SOURCE_AMPLITUDE_SCALE
        cos_p, sin_p = np.cos(self.phi_np), np.sin(self.phi_np)
        if m == 0:
            Bz = mu / (4*np.pi*r3); Bx = By = np.zeros_like(Bz)
        elif m == 1:
            Br = 2*mu*cos_p/(4*np.pi*r3); Bt = mu*sin_p/(4*np.pi*r3)
            Bx = Br*cos_p - Bt*sin_p; By = Br*sin_p + Bt*cos_p; Bz = np.zeros_like(Bx)
        elif m == -1:
            Br = 2*mu*sin_p/(4*np.pi*r3); Bt = -mu*cos_p/(4*np.pi*r3)
            Bx = Br*cos_p - Bt*sin_p; By = Br*sin_p + Bt*cos_p; Bz = np.zeros_like(Bx)
        else:
            return self._multipole(1, m)
        return self._pack(Bx, By, Bz, s)

    def _multipole(self, l: int, m: int) -> torch.Tensor:
        """Higher-order multipole from scalar potential gradient."""
        theta_eq = np.full_like(self.r_np, self.config.EQUATORIAL_THETA)
        Y = sph_harm(abs(m), l, self.phi_np, theta_eq)
        if m == 0: Y_real = Y.real
        elif m > 0: Y_real = np.sqrt(2) * Y.real * ((-1)**m)
        else: Y_real = np.sqrt(2) * Y.imag * ((-1)**abs(m))
        pot = np.nan_to_num((self.r_np**(-(l+1))) * Y_real, nan=0.0, posinf=0.0, neginf=0.0)
        dx = self.x_np[1,0] - self.x_np[0,0] if self.x_np.shape[0] > 1 else 1.0
        Bx = -np.gradient(pot, dx, axis=0); By = -np.gradient(pot, dx, axis=1)
        return self._pack(Bx, By, pot, self.config.SOURCE_AMPLITUDE_SCALE)

    def _monopole_proxy(self) -> torch.Tensor:
        """Isotropic l=0 proxy."""
        Bz = np.nan_to_num(1.0 / (self.r_np**2), nan=0.0, posinf=0.0, neginf=0.0)
        Bz /= (np.max(np.abs(Bz)) + 1e-10)
        return self._pack(np.zeros_like(Bz), np.zeros_like(Bz), Bz, self.config.SOURCE_AMPLITUDE_SCALE)

    def _pack(self, Bx, By, Bz, scale):
        """Sanitise, normalise, pack into 6 channels."""
        for a in [Bx, By, Bz]: np.nan_to_num(a, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
        mx = max(np.max(np.abs(Bx)), np.max(np.abs(By)), np.max(np.abs(Bz)), 1e-10)
        z = np.zeros_like(Bx)
        return torch.stack([torch.from_numpy((Bx/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((By/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((Bz/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32))], dim=0)

    def get_analytical_density(self, l: int, m: int) -> np.ndarray:
        """Return normalised |B|^2."""
        src = self.generate(l, m)
        d = src[0].numpy()**2 + src[2].numpy()**2 + src[4].numpy()**2
        return d / (d.max() + 1e-10)


class HallProjectionCalculator:
    """Multi-angle averaged Hall projection at equatorial theta = pi/2."""
    def __init__(self, config: DiagnosticConfig):
        """Store config reference."""
        self.config = config

    def project(self, tensor: torch.Tensor) -> torch.Tensor:
        """Multi-angle averaged Hall projection."""
        if tensor.dim() == 4: tensor = tensor[0]
        Ex_sq = torch.abs(torch.complex(tensor[0], tensor[1]))**2
        Ey_sq = torch.abs(torch.complex(tensor[2], tensor[3]))**2
        Bz_sq = torch.abs(torch.complex(tensor[4], tensor[5]))**2
        n = self.config.HALL_SENSOR_NUM_ANGLES
        acc = torch.zeros_like(Ex_sq)
        for i in range(n):
            phi = 2.0 * np.pi * i / n
            acc += np.cos(phi) * Ex_sq + np.sin(phi) * Ey_sq
        return acc / n + Bz_sq

    def project_intermediate(self, tensor: torch.Tensor) -> np.ndarray:
        """Project an intermediate activation to a scalar energy density."""
        if tensor.dim() == 4: tensor = tensor[0]
        energy = torch.sum(tensor**2, dim=0)
        e_np = energy.detach().cpu().numpy()
        return e_np / (e_np.max() + 1e-10)


class HydrogenOrbitalCalculator:
    """Analytical hydrogen orbital wavefunctions."""
    def __init__(self, config: DiagnosticConfig):
        """Store config reference."""
        self.config = config

    def radial_wavefunction(self, n: int, l: int, r: np.ndarray) -> np.ndarray:
        """Non-relativistic radial wavefunction R_nl(r)."""
        if l >= n or l < 0: return np.zeros_like(r)
        norm = np.sqrt((2.0/n)**3 * factorial(n-l-1) / (2*n*factorial(n+l)))
        rho = 2.0 * r / n
        R = norm * np.power(rho, l) * genlaguerre(n-l-1, 2*l+1)(rho) * np.exp(-rho/2)
        return np.nan_to_num(R, nan=0.0, posinf=0.0, neginf=0.0)

    def spherical_harmonic_real(self, l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
        """Real spherical harmonic Y_l^m."""
        Y = sph_harm(abs(m), l, phi, theta)
        if m == 0: return Y.real
        if m > 0: return np.sqrt(2) * Y.real * ((-1)**m)
        return np.sqrt(2) * Y.imag * ((-1)**abs(m))

    def probability_density_2d(self, n: int, l: int, m: int, grid_size: int) -> np.ndarray:
        """2D |psi|^2 in equatorial plane (theta=pi/2)."""
        ext = self.config.SPATIAL_EXTENT
        r_max = self.config.ORBITAL_R_MAX_FACTOR * n**2 + self.config.ORBITAL_R_MAX_OFFSET
        x = np.linspace(-ext, ext, grid_size)
        X, Y = np.meshgrid(x, x, indexing='ij')
        R_xy = np.sqrt(X**2 + Y**2) + self.config.NORMALIZATION_EPS
        r_scaled = R_xy * (r_max / ext)
        theta_xy = np.full_like(R_xy, self.config.EQUATORIAL_THETA)
        phi_xy = np.arctan2(Y, X)
        psi_sq = (self.radial_wavefunction(n, l, r_scaled) * self.spherical_harmonic_real(l, m, theta_xy, phi_xy))**2
        return psi_sq / (psi_sq.max() + self.config.NORMALIZATION_EPS)


def compute_spatial_correlation(a: np.ndarray, b: np.ndarray, eps: float = 1e-10) -> float:
    """Cosine similarity between two flattened density maps."""
    af, bf = a.flatten(), b.flatten()
    an = af / (np.linalg.norm(af) + eps)
    bn = bf / (np.linalg.norm(bf) + eps)
    return float(np.dot(an, bn))


class PassthroughTest:
    """
    Mode 1: Identity-initialised network.

    If isomorphism survives passthrough, the projection pipeline is correct.
    """
    def __init__(self, config: DiagnosticConfig):
        """Initialise sub-components."""
        self.config = config
        self.logger = LoggerFactory.create_logger("PassthroughTest", config.LOG_LEVEL)
        self.source = AnalyticalMultipoleSource(config)
        self.hall = HallProjectionCalculator(config)
        self.hydrogen = HydrogenOrbitalCalculator(config)

    def run(self, output_dir: str) -> Dict[str, Any]:
        """Test all orbitals with an identity-initialised network."""
        self.logger.info("=" * 60)
        self.logger.info("MODE 1: PASSTHROUGH TEST (Identity Network)")
        self.logger.info("=" * 60)
        model = MaxwellSpectralNetwork(self.config).to(self.config.DEVICE)
        model.init_identity()
        model.eval()
        orbitals = [('1s',1,0,0),('2p_m0',2,1,0),('2p_m1',2,1,1),('3d_m0',3,2,0),('3d_m2',3,2,2)]
        results = []
        for label, n, l, m in orbitals:
            src = self.source.generate(l, m).unsqueeze(0).to(self.config.DEVICE)
            with torch.no_grad(): resp = model(src)
            em_density = self.hall.project(resp.cpu()).numpy()
            em_density = np.abs(em_density) / (np.abs(em_density).max() + 1e-10)
            qd = self.hydrogen.probability_density_2d(n, l, m, self.config.GRID_SIZE)
            ad = self.source.get_analytical_density(l, m)
            corr_network = compute_spatial_correlation(em_density, qd)
            corr_analytical = compute_spatial_correlation(ad, qd)
            corr_passthrough_vs_analytical = compute_spatial_correlation(em_density, ad)
            self.logger.info(
                f"  {label:>8s}: analytical={corr_analytical:.4f}  "
                f"passthrough={corr_network:.4f}  "
                f"pass_vs_anal={corr_passthrough_vs_analytical:.4f}"
            )
            results.append({
                'label': label, 'n': n, 'l': l, 'm': m,
                'corr_analytical': corr_analytical,
                'corr_passthrough': corr_network,
                'corr_passthrough_vs_analytical': corr_passthrough_vs_analytical
            })
        self.logger.info("=" * 60)
        mean_pass = np.mean([r['corr_passthrough'] for r in results])
        mean_anal = np.mean([r['corr_analytical'] for r in results])
        if mean_pass > 0.5:
            verdict = "PASS: Identity network preserves isomorphism. Pipeline is correct."
        elif mean_pass > 0.2:
            verdict = "PARTIAL: Some structure survives passthrough. GELU nonlinearity may distort."
        else:
            verdict = "FAIL: Even identity network destroys structure. Pipeline bug suspected."
        self.logger.info(f"  Verdict: {verdict}")
        self.logger.info(f"  Mean passthrough corr: {mean_pass:.4f}")
        self.logger.info(f"  Mean analytical corr:  {mean_anal:.4f}")
        return {'mode': 'passthrough', 'results': results, 'verdict': verdict,
                'mean_passthrough': mean_pass, 'mean_analytical': mean_anal}


class LayerTraceTest:
    """
    Mode 2: Layer-by-layer trace through a trained network.

    Measures spatial correlation after every sub-layer to find where
    the angular structure collapses.
    """
    def __init__(self, config: DiagnosticConfig):
        """Initialise sub-components."""
        self.config = config
        self.logger = LoggerFactory.create_logger("LayerTraceTest", config.LOG_LEVEL)
        self.source = AnalyticalMultipoleSource(config)
        self.hall = HallProjectionCalculator(config)
        self.hydrogen = HydrogenOrbitalCalculator(config)

    def run(self, checkpoint_dir: str, output_dir: str) -> Dict[str, Any]:
        """Trace a trained model layer by layer."""
        self.logger.info("=" * 60)
        self.logger.info("MODE 2: LAYER TRACE (Trained Network)")
        self.logger.info("=" * 60)
        model = self._load_model(checkpoint_dir)
        if model is None:
            self.logger.warning("No checkpoint found, skipping layer trace.")
            return {'mode': 'layer_trace', 'error': 'no checkpoint'}
        layer_names = ['input', 'input_proj', 'expansion_proj'] + \
                      [f'spectral_{i}' for i in range(self.config.NUM_SPECTRAL_LAYERS)] + \
                      ['contraction_proj', 'output_proj']
        orbitals = [('1s',1,0,0),('2p_m1',2,1,1),('3d_m0',3,2,0)]
        all_traces = {}
        for label, n, l, m in orbitals:
            src = self.source.generate(l, m).unsqueeze(0).to(self.config.DEVICE)
            qd = self.hydrogen.probability_density_2d(n, l, m, self.config.GRID_SIZE)
            with torch.no_grad():
                intermediates = model.forward_with_intermediates(src)
            trace = []
            for idx, (name, tensor) in enumerate(zip(layer_names, intermediates)):
                density = self.hall.project_intermediate(tensor)
                corr = compute_spatial_correlation(density, qd)
                energy = float(torch.sum(tensor**2).item())
                trace.append({'layer': name, 'correlation': corr, 'energy': energy})
            all_traces[label] = trace
            self.logger.info(f"\n  {label}:")
            for t in trace:
                bar = '#' * int(max(0, t['correlation']) * 40)
                self.logger.info(f"    {t['layer']:>20s}: corr={t['correlation']:+.4f}  E={t['energy']:.2e}  {bar}")
            collapse_idx = self._find_collapse(trace)
            if collapse_idx is not None:
                self.logger.info(f"    >>> Structure collapses at: {trace[collapse_idx]['layer']}")
        self._plot_traces(all_traces, output_dir)
        return {'mode': 'layer_trace', 'traces': all_traces}

    def _find_collapse(self, trace: List[Dict]) -> Optional[int]:
        """Find the layer where correlation drops most sharply."""
        if len(trace) < 2: return None
        max_drop = 0.0
        max_idx = None
        for i in range(1, len(trace)):
            drop = trace[i-1]['correlation'] - trace[i]['correlation']
            if drop > max_drop:
                max_drop = drop
                max_idx = i
        return max_idx if max_drop > 0.05 else None

    def _plot_traces(self, all_traces: Dict, output_dir: str):
        """Plot correlation vs layer index for all orbitals."""
        fig, ax = plt.subplots(figsize=(12, 6), dpi=self.config.FIGURE_DPI)
        fig.patch.set_facecolor('#000010')
        ax.set_facecolor('#000010')
        colors = ['#FF6B6B', '#4ECDC4', '#FFE66D', '#95E1D3', '#F38181']
        for i, (label, trace) in enumerate(all_traces.items()):
            layers = [t['layer'] for t in trace]
            corrs = [t['correlation'] for t in trace]
            ax.plot(range(len(corrs)), corrs, 'o-', color=colors[i % len(colors)],
                    label=label, linewidth=2, markersize=8)
        ax.set_xticks(range(len(layers)))
        ax.set_xticklabels(layers, rotation=45, ha='right', color='white', fontsize=9)
        ax.set_ylabel('Spatial Correlation', color='white', fontsize=12)
        ax.set_title('Layer-by-Layer Isomorphism Trace', color='white', fontsize=14, fontweight='bold')
        ax.tick_params(colors='white')
        ax.legend(facecolor='#1a1a2e', labelcolor='white')
        ax.grid(True, alpha=0.2)
        ax.axhline(y=0.0, color='gray', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'layer_trace.{self.config.SAVE_FORMAT}'),
                    dpi=self.config.FIGURE_DPI, facecolor='#000010')
        plt.close()

    def _load_model(self, checkpoint_dir: str) -> Optional[nn.Module]:
        """Load the trained model."""
        cdir = checkpoint_dir or self.config.CHECKPOINT_DIR
        if not os.path.exists(cdir): return None
        cp = None
        for p in [os.path.join(cdir, 'latest.pth'), os.path.join(cdir, 'best.pth')]:
            if os.path.exists(p): cp = p; break
        if cp is None:
            files = sorted(glob.glob(os.path.join(cdir, '*.pth')), key=os.path.getmtime, reverse=True)
            if files: cp = files[0]
        if cp is None: return None
        self.logger.info(f"Loading: {cp}")
        ckpt = torch.load(cp, map_location=self.config.DEVICE, weights_only=False)
        ir = self.config.DEFAULT_IMAGINARY_RATIO
        if isinstance(ckpt, dict):
            cfg = ckpt.get('config', {})
            if isinstance(cfg, dict): ir = cfg.get('imaginary_ratio', ir)
        model = MaxwellSpectralNetwork(self.config, imaginary_ratio=ir).to(self.config.DEVICE)
        if isinstance(ckpt, dict) and 'model_state_dict' in ckpt:
            model.load_state_dict(ckpt['model_state_dict'], strict=False)
        elif isinstance(ckpt, dict):
            try: model.load_state_dict(ckpt, strict=False)
            except: pass
        model.eval()
        return model


class SymmetryTrainingTest:
    """
    Mode 3: Short training with rotational symmetry preservation loss.

    Loss = MSE(output, target) + weight * SymmetryLoss
    where SymmetryLoss penalises changes in the angular power spectrum
    between input and output.
    """
    def __init__(self, config: DiagnosticConfig):
        """Initialise sub-components."""
        self.config = config
        self.logger = LoggerFactory.create_logger("SymmetryTraining", config.LOG_LEVEL)
        self.source = AnalyticalMultipoleSource(config)
        self.hall = HallProjectionCalculator(config)
        self.hydrogen = HydrogenOrbitalCalculator(config)

    def compute_angular_power(self, tensor: torch.Tensor) -> torch.Tensor:
        """Compute the angular power spectrum of a 2D field via azimuthal FFT."""
        if tensor.dim() == 4: tensor = tensor[0]
        energy = torch.sum(tensor**2, dim=0)
        fft_az = torch.fft.fft(energy, dim=-1)
        return torch.abs(fft_az).mean(dim=0)

    def symmetry_loss(self, input_tensor: torch.Tensor, output_tensor: torch.Tensor) -> torch.Tensor:
        """Penalise angular power spectrum distortion."""
        ps_in = self.compute_angular_power(input_tensor)
        ps_out = self.compute_angular_power(output_tensor)
        return F.mse_loss(ps_out, ps_in)

    def run(self, output_dir: str) -> Dict[str, Any]:
        """Train a fresh model with symmetry loss and track isomorphism."""
        self.logger.info("=" * 60)
        self.logger.info("MODE 3: SYMMETRY-AWARE TRAINING")
        self.logger.info("=" * 60)
        model = MaxwellSpectralNetwork(self.config).to(self.config.DEVICE)
        model.init_identity()
        model.train()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.config.SYMMETRY_TRAINING_LR)
        orbitals = [('2p_m1',2,1,1), ('1s',1,0,0), ('3d_m0',3,2,0)]
        sources = []
        targets_qd = []
        for label, n, l, m in orbitals:
            src = self.source.generate(l, m).unsqueeze(0).to(self.config.DEVICE)
            sources.append(src)
            targets_qd.append(self.hydrogen.probability_density_2d(n, l, m, self.config.GRID_SIZE))
        history = []
        for epoch in range(1, self.config.SYMMETRY_TRAINING_EPOCHS + 1):
            total_loss = 0.0
            for src in sources:
                optimizer.zero_grad()
                output = model(src)
                mse = F.mse_loss(output, src)
                sym = self.symmetry_loss(src, output)
                loss = mse + self.config.SYMMETRY_LOSS_WEIGHT * sym
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            if epoch % 20 == 0 or epoch == 1:
                model.eval()
                corrs = []
                for i, (label, n, l, m) in enumerate(orbitals):
                    with torch.no_grad(): resp = model(sources[i])
                    em = self.hall.project(resp.cpu()).numpy()
                    em = np.abs(em) / (np.abs(em).max() + 1e-10)
                    corrs.append(compute_spatial_correlation(em, targets_qd[i]))
                mean_corr = np.mean(corrs)
                history.append({'epoch': epoch, 'loss': total_loss / len(sources), 'mean_corr': mean_corr,
                                'per_orbital': {orbitals[j][0]: corrs[j] for j in range(len(orbitals))}})
                self.logger.info(f"  Epoch {epoch:>4d}: loss={total_loss/len(sources):.6f}  mean_corr={mean_corr:.4f}  {[f'{c:.3f}' for c in corrs]}")
                model.train()
        self._plot_history(history, output_dir)
        return {'mode': 'symmetry_training', 'history': history}

    def _plot_history(self, history: List[Dict], output_dir: str):
        """Plot training loss and correlation over epochs."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), dpi=self.config.FIGURE_DPI)
        fig.patch.set_facecolor('#000010')
        for ax in [ax1, ax2]: ax.set_facecolor('#000010')
        epochs = [h['epoch'] for h in history]
        losses = [h['loss'] for h in history]
        corrs = [h['mean_corr'] for h in history]
        ax1.plot(epochs, losses, 'o-', color='#FF6B6B', linewidth=2)
        ax1.set_xlabel('Epoch', color='white'); ax1.set_ylabel('Loss', color='white')
        ax1.set_title('Training Loss', color='white', fontweight='bold')
        ax1.tick_params(colors='white'); ax1.grid(True, alpha=0.2)
        ax2.plot(epochs, corrs, 'o-', color='#4ECDC4', linewidth=2)
        ax2.set_xlabel('Epoch', color='white'); ax2.set_ylabel('Mean Correlation', color='white')
        ax2.set_title('Isomorphism During Training', color='white', fontweight='bold')
        ax2.tick_params(colors='white'); ax2.grid(True, alpha=0.2)
        ax2.axhline(y=0.7, color='green', linestyle='--', alpha=0.5, label='Strong threshold')
        ax2.legend(facecolor='#1a1a2e', labelcolor='white')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'symmetry_training.{self.config.SAVE_FORMAT}'),
                    dpi=self.config.FIGURE_DPI, facecolor='#000010')
        plt.close()


class DiagnosticSuite:
    """Orchestrate all three diagnostic modes."""
    def __init__(self, config: DiagnosticConfig):
        """Initialise all test modes."""
        self.config = config
        self.logger = LoggerFactory.create_logger("DiagnosticSuite", config.LOG_LEVEL)
        self.passthrough = PassthroughTest(config)
        self.layer_trace = LayerTraceTest(config)
        self.symmetry = SymmetryTrainingTest(config)

    def run_all(self, output_dir: str, checkpoint_dir: str):
        """Execute all three diagnostic modes and save results."""
        os.makedirs(output_dir, exist_ok=True)
        self.logger.info("=" * 70)
        self.logger.info("MAXWELL ORBITAL DIAGNOSTIC SUITE")
        self.logger.info("3 modes: Passthrough, Layer Trace, Symmetry Training")
        self.logger.info("=" * 70)
        results = {}
        results['passthrough'] = self.passthrough.run(output_dir)
        results['layer_trace'] = self.layer_trace.run(checkpoint_dir, output_dir)
        results['symmetry_training'] = self.symmetry.run(output_dir)
        with open(os.path.join(output_dir, 'diagnostic_results.json'), 'w') as f:
            json.dump(results, f, indent=2, default=str)
        self.logger.info("\n" + "=" * 70)
        self.logger.info("DIAGNOSTIC COMPLETE")
        self.logger.info(f"Results in: {output_dir}")
        self.logger.info("=" * 70)


def main():
    """Parse arguments and run the diagnostic suite."""
    parser = argparse.ArgumentParser(description='Maxwell Orbital Diagnostic Suite')
    parser.add_argument('--checkpoint_dir', '-c', default='checkpoints_maxwell_phase3')
    parser.add_argument('--output_dir', '-o', default='orbital_diagnostic')
    parser.add_argument('--grid_size', type=int, default=16)
    parser.add_argument('--hidden_dim', type=int, default=32)
    parser.add_argument('--expansion_dim', type=int, default=64)
    parser.add_argument('--spectral_layers', type=int, default=2)
    parser.add_argument('--imaginary_ratio', type=float, default=0.3)
    parser.add_argument('--symmetry_epochs', type=int, default=200)
    parser.add_argument('--log_level', default='INFO')
    parser.add_argument('--mode', choices=['all', 'passthrough', 'trace', 'symmetry'], default='all')
    args = parser.parse_args()
    config = DiagnosticConfig(
        GRID_SIZE=args.grid_size, HIDDEN_DIM=args.hidden_dim,
        EXPANSION_DIM=args.expansion_dim, NUM_SPECTRAL_LAYERS=args.spectral_layers,
        DEFAULT_IMAGINARY_RATIO=args.imaginary_ratio,
        SYMMETRY_TRAINING_EPOCHS=args.symmetry_epochs,
        LOG_LEVEL=args.log_level, CHECKPOINT_DIR=args.checkpoint_dir,
        OUTPUT_DIRECTORY=args.output_dir)
    suite = DiagnosticSuite(config)
    os.makedirs(args.output_dir, exist_ok=True)
    if args.mode == 'all':
        suite.run_all(args.output_dir, args.checkpoint_dir)
    elif args.mode == 'passthrough':
        suite.passthrough.run(args.output_dir)
    elif args.mode == 'trace':
        suite.layer_trace.run(args.checkpoint_dir, args.output_dir)
    elif args.mode == 'symmetry':
        suite.symmetry.run(args.output_dir)


if __name__ == "__main__":
    main()
