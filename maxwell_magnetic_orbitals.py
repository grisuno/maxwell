#!/usr/bin/env python3
"""
maxwell_magnetic_orbitals.py

Experimental probe of hydrogen orbital isomorphism in Maxwell spectral networks.

Inspired by Salcuni (2025): "Magnetic Orbitals -- The First Visual Revelation
of Quantum Geometries in the Macroscopic World" (Zenodo 19024395).

Corrected implementation addressing:
  Fix 1: theta = pi/2 in equatorial plane (not arccos(x/r))
  Fix 2: Analytical dipole B-field from vector potential, not ad-hoc Y_lm modulation
  Fix 3: Hall sensor at theta = pi/2 (equatorial) with multi-angle averaging
  Fix 4: Multipole source hierarchy -- dipole for l=1, quadrupole for l=2, etc.

Includes analytical control validation (no neural network) to establish the
theoretical isomorphism baseline before testing the trained model.

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date: 2026
License: AGPL v3
"""

import argparse, glob, json, logging, math, os, warnings
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
class IsomorphismConfig:
    """Configuration for the magnetic orbital isomorphism experiment."""
    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    FIELD_COMPONENTS: int = 3
    DEFAULT_IMAGINARY_RATIO: float = 0.3
    HBAR: float = 1.0
    ELECTRON_MASS: float = 1.0
    C_LIGHT: float = 137.035999084
    ALPHA_FS: float = 1.0 / 137.035999084
    PERMEABILITY_FACTOR: float = 1.0
    EQUATORIAL_THETA: float = 1.5707963267948966
    SPATIAL_EXTENT: float = 3.141592653589793
    ORBITAL_R_MAX_FACTOR: float = 4.0
    ORBITAL_R_MAX_OFFSET: float = 10.0
    ORBITAL_PROBABILITY_SAFETY_FACTOR: float = 1.05
    MONTE_CARLO_BATCH_SIZE: int = 100000
    MONTE_CARLO_MAX_PARTICLES: int = 500000
    MONTE_CARLO_MIN_PARTICLES: int = 5000
    TOMOGRAPHIC_SLICES: int = 16
    TOMOGRAPHIC_ATTENUATION_RATE: float = 0.1
    HALL_SENSOR_NUM_ANGLES: int = 8
    DIPOLE_MOMENT_MAGNITUDE: float = 1.0
    DIPOLE_REGULARIZATION: float = 0.3
    SOURCE_AMPLITUDE_SCALE: float = 0.1
    ISOMORPHISM_HISTOGRAM_BINS: int = 200
    ISOMORPHISM_GAMMA_EXPONENT: float = 0.3
    ISOMORPHISM_NODE_THRESHOLD: float = 0.01
    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    RANDOM_SEED: int = 42
    LOG_LEVEL: str = 'INFO'
    FIGURE_DPI: int = 150
    FIGURE_SIZE_X: int = 24
    FIGURE_SIZE_Y: int = 20
    SAVE_FORMAT: str = 'png'
    OUTPUT_DIRECTORY: str = 'magnetic_orbital_analysis'
    NORMALIZATION_EPS: float = 1e-10
    CHECKPOINT_DIR: str = 'checkpoints_maxwell_phase3'


class LoggerFactory:
    """Factory for creating configured logger instances."""
    @staticmethod
    def create_logger(name: str, level: str = 'INFO') -> logging.Logger:
        """Create and return a configured logger."""
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            logger.addHandler(handler)
        return logger


class SpectralLayer(nn.Module):
    """Spectral convolution layer with tuneable imaginary ratio."""
    def __init__(self, channels: int, grid_size: int, imaginary_ratio: float = 0.3):
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
        kr = F.interpolate(self.kernel_real.mean(dim=0).unsqueeze(0).unsqueeze(0).squeeze(0), size=(fh, fw), mode='bilinear', align_corners=False)
        ki = F.interpolate(self.kernel_imag.mean(dim=0).unsqueeze(0).unsqueeze(0).squeeze(0), size=(fh, fw), mode='bilinear', align_corners=False)
        rp = x_fft.real * kr - x_fft.imag * ki
        ip = x_fft.real * ki + x_fft.imag * kr
        return torch.fft.irfft2(torch.complex(rp, ip), s=(self.grid_size, self.grid_size))


class MaxwellSpectralNetwork(nn.Module):
    """Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz)."""
    def __init__(self, config: IsomorphismConfig, imaginary_ratio: float = 0.3):
        super().__init__()
        self.config = config
        self.grid_size = config.GRID_SIZE
        self.input_channels = config.FIELD_COMPONENTS * 2
        self.output_channels = config.FIELD_COMPONENTS * 2
        self.imaginary_ratio = imaginary_ratio
        self.input_proj = nn.Conv2d(self.input_channels, config.HIDDEN_DIM, kernel_size=1)
        self.expansion_proj = nn.Conv2d(config.HIDDEN_DIM, config.EXPANSION_DIM, kernel_size=1)
        self.spectral_layers = nn.ModuleList([SpectralLayer(config.EXPANSION_DIM, config.GRID_SIZE, imaginary_ratio) for _ in range(config.NUM_SPECTRAL_LAYERS)])
        self.contraction_proj = nn.Conv2d(config.EXPANSION_DIM, config.HIDDEN_DIM, kernel_size=1)
        self.output_proj = nn.Conv2d(config.HIDDEN_DIM, self.output_channels, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.dim() == 3: x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for sl in self.spectral_layers: x = F.gelu(sl(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)


class ModelLoader:
    """Load the best Maxwell checkpoint."""
    def __init__(self, config: IsomorphismConfig):
        self.config = config
        self.logger = LoggerFactory.create_logger("ModelLoader", config.LOG_LEVEL)

    def load(self, checkpoint_dir: str = None) -> Tuple[nn.Module, Dict[str, Any]]:
        """Return (model, info_dict) from the best available checkpoint."""
        cdir = checkpoint_dir or self.config.CHECKPOINT_DIR
        if not os.path.exists(cdir):
            self.logger.warning(f"Checkpoint directory not found: {cdir}")
            return self._fallback(), {'status': 'analytical'}
        cp = None
        for p in [os.path.join(cdir, 'latest.pth'), os.path.join(cdir, 'best.pth')]:
            if os.path.exists(p): cp = p; break
        if cp is None:
            files = sorted(glob.glob(os.path.join(cdir, '*.pth')), key=os.path.getmtime, reverse=True)
            if files: cp = files[0]
        if cp is None:
            return self._fallback(), {'status': 'analytical'}
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
        for p in model.parameters(): p.requires_grad = False
        metrics = ckpt.get('metrics', {}) if isinstance(ckpt, dict) else {}
        epoch = ckpt.get('epoch', '?') if isinstance(ckpt, dict) else '?'
        return model, {'status': 'loaded', 'path': cp, 'epoch': epoch, 'delta': metrics.get('delta'), 'alpha': metrics.get('alpha')}

    def _fallback(self) -> nn.Module:
        m = MaxwellSpectralNetwork(self.config, self.config.DEFAULT_IMAGINARY_RATIO).to(self.config.DEVICE)
        m.eval(); return m


class AnalyticalMultipoleSource:
    """
    Analytical electromagnetic multipole sources.

    Fix 2: Real dipole B-field from B = (mu0/4pi)(3(m.r_hat)r_hat - m)/r^3.
    Fix 1: theta = pi/2 (equatorial) for all 2D projections.
    Fix 4: Proper multipole hierarchy -- l=1 dipole, l=2 quadrupole, etc.
    """
    def __init__(self, config: IsomorphismConfig):
        """Precompute coordinate grids in the equatorial plane."""
        self.config = config
        N = config.GRID_SIZE
        ext = config.SPATIAL_EXTENT
        x = torch.linspace(-ext, ext, N)
        y = torch.linspace(-ext, ext, N)
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
        return self._normalise_and_pack(Bx, By, Bz, s)

    def _multipole(self, l: int, m: int) -> torch.Tensor:
        """Higher-order multipole from scalar potential gradient."""
        theta_eq = np.full_like(self.r_np, self.config.EQUATORIAL_THETA)
        Y = sph_harm(abs(m), l, self.phi_np, theta_eq)
        if m == 0: Y_real = Y.real
        elif m > 0: Y_real = np.sqrt(2) * Y.real * ((-1)**m)
        else: Y_real = np.sqrt(2) * Y.imag * ((-1)**abs(m))
        pot = (self.r_np**(-(l+1))) * Y_real
        pot = np.nan_to_num(pot, nan=0.0, posinf=0.0, neginf=0.0)
        dx = self.x_np[1,0] - self.x_np[0,0] if self.x_np.shape[0] > 1 else 1.0
        Bx = -np.gradient(pot, dx, axis=0)
        By = -np.gradient(pot, dx, axis=1)
        return self._normalise_and_pack(Bx, By, pot, self.config.SOURCE_AMPLITUDE_SCALE)

    def _monopole_proxy(self) -> torch.Tensor:
        """Isotropic l=0 proxy (current loop)."""
        Bz = 1.0 / (self.r_np**2)
        Bz = np.nan_to_num(Bz, nan=0.0, posinf=0.0, neginf=0.0)
        Bz /= (np.max(np.abs(Bz)) + 1e-10)
        return self._normalise_and_pack(np.zeros_like(Bz), np.zeros_like(Bz), Bz, self.config.SOURCE_AMPLITUDE_SCALE)

    def _normalise_and_pack(self, Bx, By, Bz, scale):
        """Sanitise, normalise, and pack into 6-channel tensor."""
        for arr in [Bx, By, Bz]:
            np.nan_to_num(arr, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
        mx = max(np.max(np.abs(Bx)), np.max(np.abs(By)), np.max(np.abs(Bz)), 1e-10)
        z = np.zeros_like(Bx)
        return torch.stack([torch.from_numpy((Bx/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((By/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((Bz/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32))], dim=0)

    def get_analytical_density(self, l: int, m: int) -> np.ndarray:
        """Return normalised |B|^2 for analytical control (no network)."""
        src = self.generate(l, m)
        d = src[0].numpy()**2 + src[2].numpy()**2 + src[4].numpy()**2
        return d / (d.max() + 1e-10)


class HallProjectionCalculator:
    """
    Fix 3: Multi-angle averaged Hall projection at equatorial theta = pi/2.

    At theta=pi/2: nx=cos(phi), ny=sin(phi), nz=0.
    We average over HALL_SENSOR_NUM_ANGLES phi values and add |Bz|^2.
    """
    def __init__(self, config: IsomorphismConfig):
        self.config = config

    def project(self, model_output: torch.Tensor) -> torch.Tensor:
        """Multi-angle averaged Hall projection."""
        if model_output.dim() == 4: model_output = model_output[0]
        Ex = torch.complex(model_output[0], model_output[1])
        Ey = torch.complex(model_output[2], model_output[3])
        Bz = torch.complex(model_output[4], model_output[5])
        Ex_sq, Ey_sq, Bz_sq = torch.abs(Ex)**2, torch.abs(Ey)**2, torch.abs(Bz)**2
        n = self.config.HALL_SENSOR_NUM_ANGLES
        acc = torch.zeros_like(Ex_sq)
        for i in range(n):
            phi = 2.0 * np.pi * i / n
            acc += np.cos(phi) * Ex_sq + np.sin(phi) * Ey_sq
        return acc / n + Bz_sq


class TomographicScanner:
    """Generate tomographic slices at different effective distances."""
    def __init__(self, config: IsomorphismConfig):
        self.config = config

    def scan(self, model: nn.Module, source: torch.Tensor, n_slices: int = None) -> List[torch.Tensor]:
        """Return a list of 2D Hall projection slices."""
        if n_slices is None: n_slices = self.config.TOMOGRAPHIC_SLICES
        hall = HallProjectionCalculator(self.config)
        slices = []
        for z in range(n_slices):
            att = float(np.exp(-z * self.config.TOMOGRAPHIC_ATTENUATION_RATE))
            inp = (source * att).unsqueeze(0).to(self.config.DEVICE)
            with torch.no_grad(): resp = model(inp)
            slices.append(hall.project(resp.cpu()))
        return slices


class HydrogenOrbitalCalculator:
    """Analytical hydrogen orbital wavefunctions."""
    def __init__(self, config: IsomorphismConfig):
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
        """
        Fix 1: |psi(r, theta=pi/2, phi)|^2 in equatorial plane.
        """
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

    def sample_orbital_3d(self, n: int, l: int, m: int, num_samples: int) -> Dict[str, np.ndarray]:
        """Monte Carlo rejection sampling of |psi|^2."""
        num_samples = max(self.config.MONTE_CARLO_MIN_PARTICLES, min(self.config.MONTE_CARLO_MAX_PARTICLES, num_samples))
        r_max = self.config.ORBITAL_R_MAX_FACTOR * n**2 + self.config.ORBITAL_R_MAX_OFFSET
        max_prob = 0.0
        for r in np.linspace(0.01, r_max, 30):
            for th in np.linspace(0.01, np.pi-0.01, 15):
                for ph in np.linspace(0, 2*np.pi, 15):
                    p = abs(self.radial_wavefunction(n,l,np.array([r]))[0] * self.spherical_harmonic_real(l,m,np.array([th]),np.array([ph]))[0])**2 * r**2 * np.sin(th)
                    if p > max_prob: max_prob = p
        if max_prob < 1e-15: max_prob = 1e-10
        Pt = max_prob * self.config.ORBITAL_PROBABILITY_SAFETY_FACTOR
        px,py,pz,pp,pph = [],[],[],[],[]
        tot = 0
        while len(px) < num_samples and tot < num_samples * 200:
            tot += self.config.MONTE_CARLO_BATCH_SIZE
            rb = r_max * (np.random.uniform(0,1,self.config.MONTE_CARLO_BATCH_SIZE)**(1/3))
            tb = np.arccos(1 - 2*np.random.uniform(0,1,self.config.MONTE_CARLO_BATCH_SIZE))
            pb = np.random.uniform(0, 2*np.pi, self.config.MONTE_CARLO_BATCH_SIZE)
            psi = self.radial_wavefunction(n,l,rb) * self.spherical_harmonic_real(l,m,tb,pb)
            pv = np.abs(psi)**2 * rb**2 * np.sin(tb)
            acc = np.random.uniform(0, Pt, self.config.MONTE_CARLO_BATCH_SIZE) < pv
            st = np.sin(tb[acc])
            px.extend((rb[acc]*st*np.cos(pb[acc])).tolist())
            py.extend((rb[acc]*st*np.sin(pb[acc])).tolist())
            pz.extend((rb[acc]*np.cos(tb[acc])).tolist())
            pp.extend(np.abs(psi[acc])**2); pph.extend(np.real(psi[acc]).tolist())
        return {'x':np.array(px[:num_samples]),'y':np.array(py[:num_samples]),'z':np.array(pz[:num_samples]),
                'prob':np.array(pp[:num_samples]),'phase':np.array(pph[:num_samples]),'n':n,'l':l,'m':m}


class IsomorphismMetricsCalculator:
    """Quantify structural similarity between EM field patterns and hydrogen orbitals."""
    def __init__(self, config: IsomorphismConfig):
        self.config = config

    def compute(self, em_density: np.ndarray, quantum_density: np.ndarray) -> Dict[str, float]:
        """Return spatial correlation, node overlap, symmetry correlation, KL divergence."""
        ef, qf = em_density.flatten(), quantum_density.flatten()
        if ef.shape != qf.shape:
            from scipy.ndimage import zoom
            ef = zoom(em_density, len(qf)/len(ef)).flatten()
        en = ef/(np.linalg.norm(ef)+self.config.NORMALIZATION_EPS)
        qn = qf/(np.linalg.norm(qf)+self.config.NORMALIZATION_EPS)
        sc = float(np.dot(en, qn))
        thr = self.config.ISOMORPHISM_NODE_THRESHOLD
        em_n = np.abs(ef) < thr*(np.max(np.abs(ef))+1e-10)
        q_n = np.abs(qf) < thr*(np.max(np.abs(qf))+1e-10)
        inter = np.logical_and(em_n, q_n).sum()
        union = np.logical_or(em_n, q_n).sum()
        no = float(inter/(union+self.config.NORMALIZATION_EPS)) if union > 0 else 1.0
        cc = np.corrcoef(np.abs(np.fft.fft(en)), np.abs(np.fft.fft(qn)))
        sy = float(cc[0,1]) if cc.shape==(2,2) and np.isfinite(cc[0,1]) else 0.0
        ep = np.clip(np.abs(ef)/(np.sum(np.abs(ef))+1e-10), 1e-10, None)
        qp = np.clip(np.abs(qf)/(np.sum(np.abs(qf))+1e-10), 1e-10, None)
        kl = float(np.sum(qp*np.log(qp/ep)))
        return {'spatial_correlation':sc,'node_overlap':no,'symmetry_correlation':sy,'kl_divergence':kl if np.isfinite(kl) else float('inf')}


class OrbitalVisualizer:
    """Side-by-side EM field vs hydrogen orbital visualisation."""
    def __init__(self, config: IsomorphismConfig):
        self.config = config

    def visualize_comparison(self, em_density, quantum_density, metrics, label, tomo_slices,
                             orbital_3d=None, save_path=None, analytical_density=None):
        """Render comparison figure with analytical control row."""
        g = self.config.ISOMORPHISM_GAMMA_EXPONENT
        has_ctrl = analytical_density is not None
        has_3d = orbital_3d is not None and len(orbital_3d.get('x',[])) > 0
        nr = 2 + int(has_ctrl) + int(has_3d)
        fig = plt.figure(figsize=(self.config.FIGURE_SIZE_X, 5*nr), dpi=self.config.FIGURE_DPI)
        fig.patch.set_facecolor('#000010')
        gs = GridSpec(nr, 4, figure=fig, hspace=0.4, wspace=0.35)
        row = 0

        for ax_idx, (data, cmap, title) in enumerate([
            (em_density, 'inferno', 'EM (Network)'), (quantum_density, 'viridis', f'H orbital {label}')]):
            ax = fig.add_subplot(gs[row, ax_idx]); ax.set_facecolor('#000010')
            ax.imshow(data**g, cmap=cmap, aspect='equal'); ax.set_title(title, color='white', fontweight='bold')

        ax_d = fig.add_subplot(gs[row, 2]); ax_d.set_facecolor('#000010')
        if em_density.shape == quantum_density.shape:
            d1 = em_density/(em_density.max()+1e-10); d2 = quantum_density/(quantum_density.max()+1e-10)
            ax_d.imshow(d1-d2, cmap='coolwarm', aspect='equal', vmin=-1, vmax=1)
        ax_d.set_title('Difference', color='white', fontweight='bold')

        ax_m = fig.add_subplot(gs[row, 3]); ax_m.set_facecolor('#000010'); ax_m.axis('off')
        sc = metrics['spatial_correlation']
        strength = "STRONG" if sc>0.7 else "MODERATE" if sc>0.4 else "WEAK" if sc>0.15 else "NONE"
        txt = f"Isomorphism\n{'='*22}\nSpatial:  {sc:.4f}\nNodes:    {metrics['node_overlap']:.4f}\nSymmetry: {metrics['symmetry_correlation']:.4f}\nKL:       {metrics['kl_divergence']:.4f}\n\n{strength}"
        ax_m.text(0.05, 0.95, txt, transform=ax_m.transAxes, fontsize=10, va='top', fontfamily='monospace', color='white',
                  bbox=dict(boxstyle='round', facecolor='#1a1a2e', alpha=0.9))
        row += 1

        for i in range(min(len(tomo_slices), 4)):
            ax = fig.add_subplot(gs[row, i]); ax.set_facecolor('#000010')
            ax.imshow(tomo_slices[i].numpy()**g, cmap='hot', aspect='equal'); ax.set_title(f'Slice {i}', color='white')
        row += 1

        if has_ctrl:
            for ax_idx, (data, cmap, title) in enumerate([
                (analytical_density, 'inferno', 'Analytical Dipole'), (quantum_density, 'viridis', 'H orbital (ref)')]):
                ax = fig.add_subplot(gs[row, ax_idx]); ax.set_facecolor('#000010')
                ax.imshow(data**g, cmap=cmap, aspect='equal'); ax.set_title(title, color='white', fontweight='bold')
            ax_cd = fig.add_subplot(gs[row, 2]); ax_cd.set_facecolor('#000010')
            if analytical_density.shape == quantum_density.shape:
                ax_cd.imshow(analytical_density/(analytical_density.max()+1e-10) - d2, cmap='coolwarm', aspect='equal', vmin=-1, vmax=1)
            ax_cd.set_title('Analytical Diff', color='white', fontweight='bold')
            ax_ci = fig.add_subplot(gs[row, 3]); ax_ci.set_facecolor('#000010'); ax_ci.axis('off')
            cm = IsomorphismMetricsCalculator(self.config).compute(analytical_density, quantum_density)
            ax_ci.text(0.05, 0.95, f"CONTROL\n{'='*22}\nSpatial:  {cm['spatial_correlation']:.4f}\nNodes:    {cm['node_overlap']:.4f}\nSymmetry: {cm['symmetry_correlation']:.4f}",
                       transform=ax_ci.transAxes, fontsize=10, va='top', fontfamily='monospace', color='white',
                       bbox=dict(boxstyle='round', facecolor='#1a2e1a', alpha=0.9))
            row += 1

        if has_3d:
            ax3 = fig.add_subplot(gs[row, 0], projection='3d'); ax3.set_facecolor('#000010')
            X,Y,Z = orbital_3d['x'],orbital_3d['y'],orbital_3d['z']
            ph = orbital_3d['phase']; c = np.zeros((len(X),4))
            c[ph>=0]=[1,.3,0,.4]; c[ph<0]=[0,.5,1,.4]
            pr = orbital_3d['prob']; mp = max(np.max(pr),1e-10)
            ax3.scatter(X,Y,Z, c=c, s=1+(pr/mp)*5, alpha=0.4, depthshade=True)
            ax3.set_title(f'3D {label}', color='white', fontweight='bold')
            for proj_idx, (a,b,bins_label,cmap) in enumerate([(X,Y,'XY','inferno'),(X,Z,'XZ','viridis')]):
                ax_p = fig.add_subplot(gs[row, proj_idx+1]); ax_p.set_facecolor('#000010')
                H,xe,ye = np.histogram2d(a,b,bins=self.config.ISOMORPHISM_HISTOGRAM_BINS,weights=pr)
                ax_p.imshow(H.T**g, extent=[xe[0],xe[-1],ye[0],ye[-1]], origin='lower', cmap=cmap, aspect='equal')
                ax_p.set_title(f'{bins_label} Projection', color='white')

        plt.suptitle(f'Magnetic Orbital Isomorphism: {label}', color='white', fontsize=16, fontweight='bold')
        if save_path: plt.savefig(save_path, dpi=self.config.FIGURE_DPI, facecolor='#000010', bbox_inches='tight')
        plt.close()


class MagneticOrbitalExperiment:
    """
    Main experiment: analytical control + network response for each orbital.

    Fix 4: Only l=1 (p orbitals) use true dipole sources.
    l=0 uses monopole proxy, l>=2 uses multipole scalar potential.
    """
    def __init__(self, config: IsomorphismConfig):
        self.config = config
        self.logger = LoggerFactory.create_logger("Experiment", config.LOG_LEVEL)
        self.loader = ModelLoader(config)
        self.source = AnalyticalMultipoleSource(config)
        self.hydrogen = HydrogenOrbitalCalculator(config)
        self.hall = HallProjectionCalculator(config)
        self.tomo = TomographicScanner(config)
        self.metrics = IsomorphismMetricsCalculator(config)
        self.viz = OrbitalVisualizer(config)

    def run(self, output_dir=None, checkpoint_dir=None):
        """Execute the full protocol."""
        output_dir = output_dir or self.config.OUTPUT_DIRECTORY
        os.makedirs(output_dir, exist_ok=True)
        self.logger.info("="*70)
        self.logger.info("MAGNETIC ORBITAL ISOMORPHISM (CORRECTED)")
        self.logger.info("Fixes: equatorial theta, analytical dipole, multi-angle Hall, multipole hierarchy")
        self.logger.info("="*70)
        model, info = self.loader.load(checkpoint_dir)
        self.logger.info(f"Model: {info['status']}")

        orbitals = [
            ('1s',1,0,0), ('2s',2,0,0),
            ('2p_m0',2,1,0), ('2p_m1',2,1,1), ('2p_m-1',2,1,-1),
            ('3s',3,0,0), ('3p_m0',3,1,0),
            ('3d_m0',3,2,0), ('3d_m1',3,2,1), ('3d_m2',3,2,2),
        ]
        results = []
        for label, n, l, m in orbitals:
            self.logger.info(f"\n--- {label} (n={n}, l={l}, m={m}) ---")
            r = self._analyze(model, n, l, m, label, output_dir)
            results.append(r)
            self.logger.info(f"  ANALYTICAL: {r['analytical_metrics']['spatial_correlation']:.4f}")
            self.logger.info(f"  NETWORK:    {r['network_metrics']['spatial_correlation']:.4f}")

        summary = self._summary(results, info)
        with open(os.path.join(output_dir, 'isomorphism_summary.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        self._print(summary)

    def _analyze(self, model, n, l, m, label, out):
        """Full protocol for one orbital."""
        src = self.source.generate(l, m)
        ad = self.source.get_analytical_density(l, m)
        with torch.no_grad(): resp = model(src.unsqueeze(0).to(self.config.DEVICE))
        hp = self.hall.project(resp.cpu()).numpy()
        em = np.abs(hp)/(np.abs(hp).max()+self.config.NORMALIZATION_EPS)
        qd = self.hydrogen.probability_density_2d(n, l, m, self.config.GRID_SIZE)
        am = self.metrics.compute(ad, qd)
        nm = self.metrics.compute(em, qd)
        ts = self.tomo.scan(model, src)
        o3d = self.hydrogen.sample_orbital_3d(n, l, m, 50000)
        self.viz.visualize_comparison(em, qd, nm, label, ts, o3d,
            os.path.join(out, f"isomorphism_{label}.{self.config.SAVE_FORMAT}"), ad)
        return {'label':label,'n':n,'l':l,'m':m,'analytical_metrics':am,'network_metrics':nm}

    def _summary(self, results, info):
        """Aggregate."""
        ac = [r['analytical_metrics']['spatial_correlation'] for r in results]
        nc = [r['network_metrics']['spatial_correlation'] for r in results]
        p_a = [r['analytical_metrics']['spatial_correlation'] for r in results if r['l']==1]
        p_n = [r['network_metrics']['spatial_correlation'] for r in results if r['l']==1]
        ba, bn = int(np.argmax(ac)), int(np.argmax(nc))
        return {
            'experiment':'Magnetic Orbital Isomorphism (Corrected)',
            'fixes':['theta=pi/2','analytical dipole','multi-angle Hall','multipole hierarchy'],
            'model_info':info, 'timestamp':datetime.now().isoformat(),
            'orbitals':len(results), 'per_orbital':results,
            'analytical':{'mean':float(np.mean(ac)),'max':float(np.max(ac)),'best':results[ba]['label']},
            'network':{'mean':float(np.mean(nc)),'max':float(np.max(nc)),'best':results[bn]['label']},
            'p_orbitals':{'analytical':float(np.mean(p_a)) if p_a else 0,'network':float(np.mean(p_n)) if p_n else 0},
            'interpretation':self._interp(float(np.mean(ac)),float(np.mean(nc)),float(np.mean(p_a)) if p_a else 0)
        }

    def _interp(self, ma, mn, mp):
        """Narrative interpretation."""
        parts = []
        if mp > 0.7: parts.append("ANALYTICAL CONTROL: Strong p-orbital isomorphism confirmed -- dipole field geometry mirrors hydrogen angular structure (Salcuni validated).")
        elif mp > 0.3: parts.append("ANALYTICAL CONTROL: Moderate p-orbital isomorphism.")
        else: parts.append("ANALYTICAL CONTROL: Weak isomorphism -- equatorial projection may not capture full 3D structure.")
        if mn > ma * 0.8: parts.append("NETWORK: Crystallized spectral layers preserve the isomorphism.")
        elif mn > 0.2: parts.append("NETWORK: Partial preservation -- further crystallization may help.")
        else: parts.append("NETWORK: Isomorphism destroyed by network transformation at current training stage.")
        return " ".join(parts)

    def _print(self, s):
        """Log summary."""
        self.logger.info("\n"+"="*70)
        self.logger.info("RESULTS SUMMARY")
        self.logger.info("="*70)
        self.logger.info(f"  ANALYTICAL: mean={s['analytical']['mean']:.4f}, best={s['analytical']['best']}")
        self.logger.info(f"  NETWORK:    mean={s['network']['mean']:.4f}, best={s['network']['best']}")
        self.logger.info(f"  P-ORBITALS: analytical={s['p_orbitals']['analytical']:.4f}, network={s['p_orbitals']['network']:.4f}")
        self.logger.info(f"\n  {s['interpretation']}")
        self.logger.info("="*70)


def main():
    """Parse arguments and run the experiment."""
    parser = argparse.ArgumentParser(description='Maxwell Magnetic Orbital Isomorphism (Corrected)')
    parser.add_argument('--checkpoint_dir', '-c', default='checkpoints_maxwell_phase3')
    parser.add_argument('--output_dir', '-o', default='magnetic_orbital_analysis')
    parser.add_argument('--grid_size', type=int, default=16)
    parser.add_argument('--hidden_dim', type=int, default=32)
    parser.add_argument('--expansion_dim', type=int, default=64)
    parser.add_argument('--spectral_layers', type=int, default=2)
    parser.add_argument('--imaginary_ratio', type=float, default=0.3)
    parser.add_argument('--tomographic_slices', type=int, default=16)
    parser.add_argument('--log_level', default='INFO')
    args = parser.parse_args()
    config = IsomorphismConfig(
        GRID_SIZE=args.grid_size, HIDDEN_DIM=args.hidden_dim,
        EXPANSION_DIM=args.expansion_dim, NUM_SPECTRAL_LAYERS=args.spectral_layers,
        DEFAULT_IMAGINARY_RATIO=args.imaginary_ratio,
        TOMOGRAPHIC_SLICES=args.tomographic_slices,
        LOG_LEVEL=args.log_level, CHECKPOINT_DIR=args.checkpoint_dir,
        OUTPUT_DIRECTORY=args.output_dir)
    MagneticOrbitalExperiment(config).run(args.output_dir, args.checkpoint_dir)


if __name__ == "__main__":
    main()
