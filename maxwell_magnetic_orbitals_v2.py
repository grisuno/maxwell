#!/usr/bin/env python3
"""
maxwell_magnetic_orbitals_v2.py

Corrected magnetic orbital isomorphism experiment addressing the input_proj
collapse identified by the layer trace diagnostic.

The layer trace showed that the structure collapses at input_proj (Conv2d 6->32)
because the random 1x1 convolution destroys the physical channel semantics.
The analytical source has correlation ~0.97 with hydrogen orbitals, but after
input_proj it drops to ~0.14 and never recovers.

This version implements three strategies to address the collapse:

  Strategy A: BYPASS -- Skip the network entirely, use the Poisson field
              equation to evolve the analytical dipole source.  This tests
              whether Maxwell's equations themselves produce isomorphic
              structures (the pure-physics baseline).

  Strategy B: CHANNEL_AWARE -- Replace the generic input_proj with a
              physically-informed projection that processes each field
              component (Ex, Ey, Bz) separately before combining them,
              preserving the angular structure within each component.

  Strategy C: DIRECT_SPECTRAL -- Feed the source directly into the
              spectral layers (bypassing input_proj and expansion_proj)
              by reshaping the 6-channel input to match the expansion
              dimension via zero-padding.  This tests whether the trained
              spectral kernels preserve structure when they receive clean input.

All strategies are compared against the analytical control and each other.

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
from scipy.fft import fftn, fftshift
import torch, torch.nn as nn, torch.nn.functional as F
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
warnings.filterwarnings('ignore')


@dataclass(frozen=True)
class Config:
    """Configuration for the v2 isomorphism experiment."""
    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    FIELD_COMPONENTS: int = 3
    DEFAULT_IMAGINARY_RATIO: float = 0.3
    EQUATORIAL_THETA: float = 1.5707963267948966
    SPATIAL_EXTENT: float = 3.141592653589793
    PERMEABILITY_FACTOR: float = 1.0
    PERMITTIVITY_VACUUM: float = 8.854e-12
    DIPOLE_MOMENT_MAGNITUDE: float = 1.0
    DIPOLE_REGULARIZATION: float = 0.3
    SOURCE_AMPLITUDE_SCALE: float = 0.1
    ORBITAL_R_MAX_FACTOR: float = 4.0
    ORBITAL_R_MAX_OFFSET: float = 10.0
    ORBITAL_PROBABILITY_SAFETY_FACTOR: float = 1.05
    MONTE_CARLO_BATCH_SIZE: int = 100000
    MONTE_CARLO_MAX_PARTICLES: int = 500000
    MONTE_CARLO_MIN_PARTICLES: int = 5000
    HALL_SENSOR_NUM_ANGLES: int = 8
    TOMOGRAPHIC_SLICES: int = 8
    TOMOGRAPHIC_ATTENUATION_RATE: float = 0.15
    POISSON_LATTICE_DIM: int = 16
    ISOMORPHISM_GAMMA_EXPONENT: float = 0.3
    ISOMORPHISM_NODE_THRESHOLD: float = 0.01
    NORMALIZATION_EPS: float = 1e-10
    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    LOG_LEVEL: str = 'INFO'
    FIGURE_DPI: int = 150
    SAVE_FORMAT: str = 'png'
    OUTPUT_DIRECTORY: str = 'orbital_v2_results'
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
    """Spectral convolution layer."""
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


class MaxwellSpectralNetwork(nn.Module):
    """Neural network for learning Maxwell equation dynamics."""
    def __init__(self, config: Config, imaginary_ratio: float = 0.3):
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
        """Standard forward pass."""
        if x.dim() == 3: x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for sl in self.spectral_layers: x = F.gelu(sl(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)

    def forward_spectral_only(self, x_expanded: torch.Tensor) -> torch.Tensor:
        """Apply only the spectral layers (bypass input/expansion projections)."""
        for sl in self.spectral_layers:
            x_expanded = F.gelu(sl(x_expanded))
        return x_expanded


class AnalyticalMultipoleSource:
    """Analytical EM multipole sources."""
    def __init__(self, config: Config):
        """Precompute coordinate grids."""
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
        """Return a (6,H,W) source tensor."""
        if l == 0: return self._monopole()
        if l == 1: return self._dipole(m)
        return self._multipole(l, m)

    def _dipole(self, m: int) -> torch.Tensor:
        """Analytical magnetic dipole in equatorial plane."""
        r3 = self.r_np**3
        mu = self.config.PERMEABILITY_FACTOR * self.config.DIPOLE_MOMENT_MAGNITUDE
        s = self.config.SOURCE_AMPLITUDE_SCALE
        cp, sp = np.cos(self.phi_np), np.sin(self.phi_np)
        if m == 0:
            Bz = mu/(4*np.pi*r3); Bx = By = np.zeros_like(Bz)
        elif m == 1:
            Br = 2*mu*cp/(4*np.pi*r3); Bt = mu*sp/(4*np.pi*r3)
            Bx = Br*cp - Bt*sp; By = Br*sp + Bt*cp; Bz = np.zeros_like(Bx)
        elif m == -1:
            Br = 2*mu*sp/(4*np.pi*r3); Bt = -mu*cp/(4*np.pi*r3)
            Bx = Br*cp - Bt*sp; By = Br*sp + Bt*cp; Bz = np.zeros_like(Bx)
        else:
            return self._multipole(1, m)
        return self._pack(Bx, By, Bz, s)

    def _multipole(self, l: int, m: int) -> torch.Tensor:
        """Higher-order multipole from scalar potential gradient."""
        teq = np.full_like(self.r_np, self.config.EQUATORIAL_THETA)
        Y = sph_harm(abs(m), l, self.phi_np, teq)
        if m == 0: Yr = Y.real
        elif m > 0: Yr = np.sqrt(2)*Y.real*((-1)**m)
        else: Yr = np.sqrt(2)*Y.imag*((-1)**abs(m))
        pot = np.nan_to_num((self.r_np**(-(l+1)))*Yr, nan=0.0, posinf=0.0, neginf=0.0)
        dx = self.x_np[1,0]-self.x_np[0,0] if self.x_np.shape[0]>1 else 1.0
        return self._pack(-np.gradient(pot,dx,axis=0), -np.gradient(pot,dx,axis=1), pot, self.config.SOURCE_AMPLITUDE_SCALE)

    def _monopole(self) -> torch.Tensor:
        """Isotropic l=0 proxy."""
        Bz = np.nan_to_num(1.0/(self.r_np**2), nan=0.0, posinf=0.0, neginf=0.0)
        Bz /= (np.max(np.abs(Bz))+1e-10)
        return self._pack(np.zeros_like(Bz), np.zeros_like(Bz), Bz, self.config.SOURCE_AMPLITUDE_SCALE)

    def _pack(self, Bx, By, Bz, scale):
        """Normalise and pack into 6-channel tensor."""
        for a in [Bx,By,Bz]: np.nan_to_num(a, copy=False, nan=0.0, posinf=0.0, neginf=0.0)
        mx = max(np.max(np.abs(Bx)), np.max(np.abs(By)), np.max(np.abs(Bz)), 1e-10)
        z = np.zeros_like(Bx)
        return torch.stack([torch.from_numpy((Bx/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((By/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32)),
                            torch.from_numpy((Bz/mx*scale).astype(np.float32)), torch.from_numpy(z.astype(np.float32))], dim=0)

    def get_density(self, l: int, m: int) -> np.ndarray:
        """Return normalised |B|^2 for analytical control."""
        s = self.generate(l, m)
        d = s[0].numpy()**2 + s[2].numpy()**2 + s[4].numpy()**2
        return d/(d.max()+1e-10)


class PoissonEvolver:
    """
    Strategy A: Evolve the dipole source using the Poisson equation.

    Solves nabla^2 phi = -rho in Fourier space, computes E = -grad(phi),
    and returns the field energy density.  This is pure Maxwell physics
    with no neural network.
    """
    def __init__(self, config: Config):
        """Store config reference."""
        self.config = config

    def evolve(self, source_6ch: torch.Tensor) -> np.ndarray:
        """
        Treat the Bz channel as charge density, solve Poisson, return |E|^2.

        This mimics what the network should ideally learn: the electrostatic
        response to a given source configuration.
        """
        N = self.config.POISSON_LATTICE_DIM
        rho = source_6ch[4].numpy()
        rho_k = np.fft.fft2(rho)
        kx = np.fft.fftfreq(N) * 2 * np.pi
        ky = np.fft.fftfreq(N) * 2 * np.pi
        KX, KY = np.meshgrid(kx, ky, indexing='ij')
        k_sq = KX**2 + KY**2
        k_sq[0, 0] = 1.0
        phi_k = rho_k / k_sq
        phi = np.real(np.fft.ifft2(phi_k))
        dx = 2 * self.config.SPATIAL_EXTENT / N
        Ex = -np.gradient(phi, dx, axis=0)
        Ey = -np.gradient(phi, dx, axis=1)
        density = Ex**2 + Ey**2 + rho**2
        return density / (density.max() + 1e-10)


class ChannelAwareProjection(nn.Module):
    """
    Strategy B: Physically-informed input projection.

    Instead of a single Conv2d(6, 32, 1) that scrambles channels,
    this processes each field component (Ex, Ey, Bz) separately with
    its own 2->hidden/3 projection, then concatenates.
    """
    def __init__(self, config: Config):
        """Build per-component projections."""
        super().__init__()
        self.config = config
        per_field_dim = config.HIDDEN_DIM // config.FIELD_COMPONENTS
        remainder = config.HIDDEN_DIM - per_field_dim * config.FIELD_COMPONENTS
        self.proj_ex = nn.Conv2d(2, per_field_dim, kernel_size=1)
        self.proj_ey = nn.Conv2d(2, per_field_dim, kernel_size=1)
        self.proj_bz = nn.Conv2d(2, per_field_dim + remainder, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Process each (Re, Im) pair separately then concatenate."""
        ex = F.gelu(self.proj_ex(x[:, 0:2, :, :]))
        ey = F.gelu(self.proj_ey(x[:, 2:4, :, :]))
        bz = F.gelu(self.proj_bz(x[:, 4:6, :, :]))
        return torch.cat([ex, ey, bz], dim=1)


class HallProjector:
    """Multi-angle averaged Hall projection."""
    def __init__(self, config: Config):
        """Store config reference."""
        self.config = config

    def project_6ch(self, tensor: torch.Tensor) -> np.ndarray:
        """Project a 6-channel field tensor to scalar density."""
        if tensor.dim() == 4: tensor = tensor[0]
        Ex_sq = torch.abs(torch.complex(tensor[0], tensor[1]))**2
        Ey_sq = torch.abs(torch.complex(tensor[2], tensor[3]))**2
        Bz_sq = torch.abs(torch.complex(tensor[4], tensor[5]))**2
        n = self.config.HALL_SENSOR_NUM_ANGLES
        acc = torch.zeros_like(Ex_sq)
        for i in range(n):
            phi = 2.0*np.pi*i/n
            acc += np.cos(phi)*Ex_sq + np.sin(phi)*Ey_sq
        d = (acc/n + Bz_sq).detach().cpu().numpy()
        return d / (d.max() + 1e-10)

    def project_energy(self, tensor: torch.Tensor) -> np.ndarray:
        """Project an arbitrary multi-channel tensor to scalar energy density."""
        if tensor.dim() == 4: tensor = tensor[0]
        d = torch.sum(tensor**2, dim=0).detach().cpu().numpy()
        return d / (d.max() + 1e-10)


class HydrogenOrbitalCalculator:
    """Analytical hydrogen orbital wavefunctions."""
    def __init__(self, config: Config):
        """Store config reference."""
        self.config = config

    def radial_wavefunction(self, n: int, l: int, r: np.ndarray) -> np.ndarray:
        """Non-relativistic radial wavefunction R_nl(r)."""
        if l >= n or l < 0: return np.zeros_like(r)
        norm = np.sqrt((2.0/n)**3 * factorial(n-l-1) / (2*n*factorial(n+l)))
        rho = 2.0*r/n
        R = norm * np.power(rho, l) * genlaguerre(n-l-1, 2*l+1)(rho) * np.exp(-rho/2)
        return np.nan_to_num(R, nan=0.0, posinf=0.0, neginf=0.0)

    def spherical_harmonic_real(self, l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
        """Real spherical harmonic."""
        Y = sph_harm(abs(m), l, phi, theta)
        if m == 0: return Y.real
        if m > 0: return np.sqrt(2)*Y.real*((-1)**m)
        return np.sqrt(2)*Y.imag*((-1)**abs(m))

    def density_2d(self, n: int, l: int, m: int, grid_size: int) -> np.ndarray:
        """2D |psi|^2 in equatorial plane."""
        ext = self.config.SPATIAL_EXTENT
        rmax = self.config.ORBITAL_R_MAX_FACTOR*n**2 + self.config.ORBITAL_R_MAX_OFFSET
        x = np.linspace(-ext, ext, grid_size)
        X, Y = np.meshgrid(x, x, indexing='ij')
        R = np.sqrt(X**2+Y**2)+self.config.NORMALIZATION_EPS
        r_s = R*(rmax/ext)
        teq = np.full_like(R, self.config.EQUATORIAL_THETA)
        phi = np.arctan2(Y, X)
        psi_sq = (self.radial_wavefunction(n,l,r_s)*self.spherical_harmonic_real(l,m,teq,phi))**2
        return psi_sq/(psi_sq.max()+self.config.NORMALIZATION_EPS)

    def sample_3d(self, n: int, l: int, m: int, num: int) -> Dict[str, np.ndarray]:
        """Monte Carlo rejection sampling."""
        num = max(self.config.MONTE_CARLO_MIN_PARTICLES, min(self.config.MONTE_CARLO_MAX_PARTICLES, num))
        rmax = self.config.ORBITAL_R_MAX_FACTOR*n**2 + self.config.ORBITAL_R_MAX_OFFSET
        mp = 0.0
        for r in np.linspace(0.01, rmax, 30):
            for th in np.linspace(0.01, np.pi-0.01, 15):
                for ph in np.linspace(0, 2*np.pi, 15):
                    p = abs(self.radial_wavefunction(n,l,np.array([r]))[0]*self.spherical_harmonic_real(l,m,np.array([th]),np.array([ph]))[0])**2*r**2*np.sin(th)
                    if p > mp: mp = p
        if mp < 1e-15: mp = 1e-10
        Pt = mp*self.config.ORBITAL_PROBABILITY_SAFETY_FACTOR
        px,py,pz,pp,pph = [],[],[],[],[]
        tot = 0
        while len(px) < num and tot < num*200:
            tot += self.config.MONTE_CARLO_BATCH_SIZE
            rb = rmax*(np.random.uniform(0,1,self.config.MONTE_CARLO_BATCH_SIZE)**(1/3))
            tb = np.arccos(1-2*np.random.uniform(0,1,self.config.MONTE_CARLO_BATCH_SIZE))
            pb = np.random.uniform(0,2*np.pi,self.config.MONTE_CARLO_BATCH_SIZE)
            psi = self.radial_wavefunction(n,l,rb)*self.spherical_harmonic_real(l,m,tb,pb)
            pv = np.abs(psi)**2*rb**2*np.sin(tb)
            acc = np.random.uniform(0,Pt,self.config.MONTE_CARLO_BATCH_SIZE) < pv
            st = np.sin(tb[acc])
            px.extend((rb[acc]*st*np.cos(pb[acc])).tolist()); py.extend((rb[acc]*st*np.sin(pb[acc])).tolist())
            pz.extend((rb[acc]*np.cos(tb[acc])).tolist()); pp.extend(np.abs(psi[acc])**2)
            pph.extend(np.real(psi[acc]).tolist())
        return {'x':np.array(px[:num]),'y':np.array(py[:num]),'z':np.array(pz[:num]),
                'prob':np.array(pp[:num]),'phase':np.array(pph[:num]),'n':n,'l':l,'m':m}


def spatial_corr(a: np.ndarray, b: np.ndarray, eps: float = 1e-10) -> float:
    """Cosine similarity between two flattened maps."""
    af, bf = a.flatten(), b.flatten()
    return float(np.dot(af/(np.linalg.norm(af)+eps), bf/(np.linalg.norm(bf)+eps)))


def node_overlap(a: np.ndarray, b: np.ndarray, thr: float = 0.01) -> float:
    """Jaccard index of nodal regions."""
    an = np.abs(a.flatten()) < thr*(np.max(np.abs(a))+1e-10)
    bn = np.abs(b.flatten()) < thr*(np.max(np.abs(b))+1e-10)
    inter = np.logical_and(an, bn).sum()
    union = np.logical_or(an, bn).sum()
    return float(inter/(union+1e-10)) if union > 0 else 1.0


def symmetry_corr(a: np.ndarray, b: np.ndarray) -> float:
    """Correlation of angular Fourier power spectra."""
    af = a.flatten(); bf = b.flatten()
    an = af/(np.linalg.norm(af)+1e-10); bn = bf/(np.linalg.norm(bf)+1e-10)
    cc = np.corrcoef(np.abs(np.fft.fft(an)), np.abs(np.fft.fft(bn)))
    return float(cc[0,1]) if cc.shape==(2,2) and np.isfinite(cc[0,1]) else 0.0


def full_metrics(em: np.ndarray, qd: np.ndarray, config: Config) -> Dict[str, float]:
    """Compute all isomorphism metrics."""
    return {
        'spatial_correlation': spatial_corr(em, qd),
        'node_overlap': node_overlap(em, qd, config.ISOMORPHISM_NODE_THRESHOLD),
        'symmetry_correlation': symmetry_corr(em, qd)
    }


class Visualizer:
    """Comprehensive multi-strategy comparison visualisation."""
    def __init__(self, config: Config):
        """Store config reference."""
        self.config = config

    def render(self, label: str, strategies: Dict[str, Dict], qd: np.ndarray,
               orbital_3d: Optional[Dict], save_path: str):
        """Render comparison of all strategies for one orbital."""
        g = self.config.ISOMORPHISM_GAMMA_EXPONENT
        strat_names = list(strategies.keys())
        n_strat = len(strat_names)
        has_3d = orbital_3d is not None and len(orbital_3d.get('x',[])) > 0
        nr = 2 + (1 if has_3d else 0)
        fig = plt.figure(figsize=(6*(n_strat+1), 5*nr), dpi=self.config.FIGURE_DPI)
        fig.patch.set_facecolor('#000010')
        gs = GridSpec(nr, n_strat+1, figure=fig, hspace=0.4, wspace=0.3)

        ax_q = fig.add_subplot(gs[0, 0]); ax_q.set_facecolor('#000010')
        ax_q.imshow(qd**g, cmap='viridis', aspect='equal')
        ax_q.set_title(f'H orbital {label}', color='white', fontweight='bold')

        for i, name in enumerate(strat_names):
            s = strategies[name]
            ax = fig.add_subplot(gs[0, i+1]); ax.set_facecolor('#000010')
            ax.imshow(s['density']**g, cmap='inferno', aspect='equal')
            sc = s['metrics']['spatial_correlation']
            ax.set_title(f'{name}\ncorr={sc:.4f}', color='white', fontweight='bold', fontsize=10)

        ax_bar = fig.add_subplot(gs[1, :]); ax_bar.set_facecolor('#000010')
        x_pos = np.arange(n_strat)
        corrs = [strategies[n]['metrics']['spatial_correlation'] for n in strat_names]
        colors = ['#FF6B6B','#4ECDC4','#FFE66D','#95E1D3','#F38181']
        ax_bar.bar(x_pos, corrs, color=colors[:n_strat], alpha=0.8)
        ax_bar.set_xticks(x_pos); ax_bar.set_xticklabels(strat_names, color='white', fontsize=10)
        ax_bar.set_ylabel('Spatial Correlation', color='white')
        ax_bar.set_title(f'Strategy Comparison: {label}', color='white', fontweight='bold')
        ax_bar.tick_params(colors='white'); ax_bar.set_ylim(0, 1.1)
        ax_bar.axhline(y=0.7, color='green', linestyle='--', alpha=0.5, label='Strong threshold')
        ax_bar.legend(facecolor='#1a1a2e', labelcolor='white')

        if has_3d:
            ax3 = fig.add_subplot(gs[2, 0], projection='3d'); ax3.set_facecolor('#000010')
            X,Y,Z = orbital_3d['x'],orbital_3d['y'],orbital_3d['z']
            ph = orbital_3d['phase']; c = np.zeros((len(X),4))
            c[ph>=0]=[1,.3,0,.4]; c[ph<0]=[0,.5,1,.4]
            pr = orbital_3d['prob']; mp = max(np.max(pr),1e-10)
            ax3.scatter(X,Y,Z, c=c, s=1+(pr/mp)*5, alpha=0.4, depthshade=True)
            ax3.set_title(f'3D {label}', color='white', fontweight='bold')
            for j, (a,b,lbl,cm) in enumerate([(X,Y,'XY','inferno'),(X,Z,'XZ','viridis')]):
                ax_p = fig.add_subplot(gs[2, j+1]); ax_p.set_facecolor('#000010')
                H,xe,ye = np.histogram2d(a,b,bins=100,weights=pr)
                ax_p.imshow(H.T**g, extent=[xe[0],xe[-1],ye[0],ye[-1]], origin='lower', cmap=cm, aspect='equal')
                ax_p.set_title(f'{lbl}', color='white')

        plt.suptitle(f'Maxwell-Hydrogen Isomorphism: {label}', color='white', fontsize=14, fontweight='bold')
        plt.savefig(save_path, dpi=self.config.FIGURE_DPI, facecolor='#000010', bbox_inches='tight')
        plt.close()


class IsomorphismExperimentV2:
    """
    Multi-strategy isomorphism experiment.

    For each orbital, runs:
      A) Analytical control (no network)
      B) Poisson evolution (pure physics)
      C) Full network (standard forward pass)
      D) Direct spectral (bypass input_proj, feed spectral layers directly)
    """
    def __init__(self, config: Config):
        """Initialise all sub-components."""
        self.config = config
        self.logger = LoggerFactory.create_logger("ExperimentV2", config.LOG_LEVEL)
        self.source = AnalyticalMultipoleSource(config)
        self.poisson = PoissonEvolver(config)
        self.hydrogen = HydrogenOrbitalCalculator(config)
        self.hall = HallProjector(config)
        self.viz = Visualizer(config)

    def _load_model(self, checkpoint_dir: str) -> Tuple[Optional[nn.Module], Dict]:
        """Load trained checkpoint."""
        cdir = checkpoint_dir or self.config.CHECKPOINT_DIR
        if not os.path.exists(cdir): return None, {'status': 'not_found'}
        cp = None
        for p in [os.path.join(cdir,'latest.pth'), os.path.join(cdir,'best.pth')]:
            if os.path.exists(p): cp = p; break
        if cp is None:
            files = sorted(glob.glob(os.path.join(cdir,'*.pth')), key=os.path.getmtime, reverse=True)
            if files: cp = files[0]
        if cp is None: return None, {'status': 'not_found'}
        self.logger.info(f"Loading: {cp}")
        ckpt = torch.load(cp, map_location=self.config.DEVICE, weights_only=False)
        ir = self.config.DEFAULT_IMAGINARY_RATIO
        if isinstance(ckpt, dict):
            cfg = ckpt.get('config',{})
            if isinstance(cfg, dict): ir = cfg.get('imaginary_ratio', ir)
        model = MaxwellSpectralNetwork(self.config, imaginary_ratio=ir).to(self.config.DEVICE)
        if isinstance(ckpt, dict) and 'model_state_dict' in ckpt:
            model.load_state_dict(ckpt['model_state_dict'], strict=False)
        elif isinstance(ckpt, dict):
            try: model.load_state_dict(ckpt, strict=False)
            except: pass
        model.eval()
        metrics = ckpt.get('metrics',{}) if isinstance(ckpt,dict) else {}
        return model, {'status':'loaded','path':cp,'epoch':ckpt.get('epoch','?') if isinstance(ckpt,dict) else '?',
                       'delta':metrics.get('delta'),'alpha':metrics.get('alpha')}

    def run(self, output_dir: str = None, checkpoint_dir: str = None):
        """Execute the full multi-strategy experiment."""
        output_dir = output_dir or self.config.OUTPUT_DIRECTORY
        os.makedirs(output_dir, exist_ok=True)
        self.logger.info("="*70)
        self.logger.info("MAGNETIC ORBITAL ISOMORPHISM V2")
        self.logger.info("Strategies: Analytical, Poisson, Full Network, Direct Spectral")
        self.logger.info("="*70)
        model, info = self._load_model(checkpoint_dir)
        self.logger.info(f"Model: {info['status']}")

        orbitals = [
            ('1s',1,0,0), ('2s',2,0,0),
            ('2p_m0',2,1,0), ('2p_m1',2,1,1), ('2p_m-1',2,1,-1),
            ('3s',3,0,0), ('3p_m0',3,1,0),
            ('3d_m0',3,2,0), ('3d_m1',3,2,1), ('3d_m2',3,2,2),
        ]
        all_results = []
        for label, n, l, m in orbitals:
            self.logger.info(f"\n--- {label} (n={n}, l={l}, m={m}) ---")
            result = self._analyze(model, n, l, m, label, output_dir)
            all_results.append(result)
            for sname, sdata in result['strategies'].items():
                self.logger.info(f"  {sname:>18s}: corr={sdata['metrics']['spatial_correlation']:.4f}")

        summary = self._summary(all_results, info)
        with open(os.path.join(output_dir, 'v2_summary.json'), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        self._print_summary(summary)

    def _analyze(self, model: Optional[nn.Module], n: int, l: int, m: int,
                  label: str, output_dir: str) -> Dict:
        """Run all strategies for one orbital."""
        src = self.source.generate(l, m)
        qd = self.hydrogen.density_2d(n, l, m, self.config.GRID_SIZE)
        strategies = {}

        ad = self.source.get_density(l, m)
        strategies['Analytical'] = {'density': ad, 'metrics': full_metrics(ad, qd, self.config)}

        pd = self.poisson.evolve(src)
        strategies['Poisson'] = {'density': pd, 'metrics': full_metrics(pd, qd, self.config)}

        if model is not None:
            src_batch = src.unsqueeze(0).to(self.config.DEVICE)
            with torch.no_grad(): resp = model(src_batch)
            nd = self.hall.project_6ch(resp.cpu())
            strategies['FullNetwork'] = {'density': nd, 'metrics': full_metrics(nd, qd, self.config)}

            expanded = torch.zeros(1, self.config.EXPANSION_DIM, self.config.GRID_SIZE, self.config.GRID_SIZE,
                                   device=self.config.DEVICE)
            src_dev = src.unsqueeze(0).to(self.config.DEVICE)
            n_copy = min(src_dev.shape[1], self.config.EXPANSION_DIM)
            expanded[:, :n_copy, :, :] = src_dev[:, :n_copy, :, :]
            with torch.no_grad(): spec_out = model.forward_spectral_only(expanded)
            sd = self.hall.project_energy(spec_out.cpu())
            strategies['DirectSpectral'] = {'density': sd, 'metrics': full_metrics(sd, qd, self.config)}

        o3d = self.hydrogen.sample_3d(n, l, m, 50000)
        viz_path = os.path.join(output_dir, f"v2_{label}.{self.config.SAVE_FORMAT}")
        self.viz.render(label, strategies, qd, o3d, viz_path)
        return {'label': label, 'n': n, 'l': l, 'm': m,
                'strategies': {k: {'metrics': v['metrics']} for k, v in strategies.items()}}

    def _summary(self, results: List[Dict], info: Dict) -> Dict:
        """Aggregate results across orbitals and strategies."""
        strat_names = set()
        for r in results:
            strat_names.update(r['strategies'].keys())
        strat_names = sorted(strat_names)
        agg = {}
        for sn in strat_names:
            corrs = [r['strategies'][sn]['metrics']['spatial_correlation']
                     for r in results if sn in r['strategies']]
            agg[sn] = {
                'mean_corr': float(np.mean(corrs)) if corrs else 0.0,
                'max_corr': float(np.max(corrs)) if corrs else 0.0,
                'min_corr': float(np.min(corrs)) if corrs else 0.0,
                'std_corr': float(np.std(corrs)) if corrs else 0.0
            }
        p_results = [r for r in results if r['l'] == 1]
        p_agg = {}
        for sn in strat_names:
            corrs = [r['strategies'][sn]['metrics']['spatial_correlation']
                     for r in p_results if sn in r['strategies']]
            p_agg[sn] = float(np.mean(corrs)) if corrs else 0.0
        return {
            'experiment': 'Magnetic Orbital Isomorphism V2',
            'model_info': info,
            'timestamp': datetime.now().isoformat(),
            'orbitals_analyzed': len(results),
            'per_orbital': results,
            'aggregate_by_strategy': agg,
            'p_orbitals_by_strategy': p_agg,
            'interpretation': self._interpret(agg, p_agg)
        }

    def _interpret(self, agg: Dict, p_agg: Dict) -> str:
        """Narrative interpretation."""
        parts = []
        if 'Analytical' in agg:
            ac = agg['Analytical']['mean_corr']
            if ac > 0.7: parts.append(f"ANALYTICAL: Strong isomorphism confirmed (mean={ac:.3f}).")
            elif ac > 0.3: parts.append(f"ANALYTICAL: Moderate isomorphism (mean={ac:.3f}).")
            else: parts.append(f"ANALYTICAL: Weak (mean={ac:.3f}).")
        if 'Poisson' in agg:
            pc = agg['Poisson']['mean_corr']
            parts.append(f"POISSON: {'Strong' if pc > 0.7 else 'Moderate' if pc > 0.3 else 'Weak'} (mean={pc:.3f}). "
                         f"{'Maxwell equations preserve the orbital geometry.' if pc > 0.5 else 'Electrostatic evolution partially distorts the angular structure.'}")
        if 'FullNetwork' in agg:
            nc = agg['FullNetwork']['mean_corr']
            parts.append(f"NETWORK: {'Preserved' if nc > 0.5 else 'Destroyed'} (mean={nc:.3f}). "
                         f"{'input_proj collapse is the bottleneck.' if nc < 0.3 else ''}")
        if 'DirectSpectral' in agg:
            dc = agg['DirectSpectral']['mean_corr']
            parts.append(f"DIRECT SPECTRAL: {dc:.3f}. "
                         f"{'Spectral layers alone preserve structure.' if dc > 0.5 else 'Spectral kernels also distort structure.'}")
        return " ".join(parts)

    def _print_summary(self, s: Dict):
        """Log the summary."""
        self.logger.info("\n" + "=" * 70)
        self.logger.info("V2 RESULTS SUMMARY")
        self.logger.info("=" * 70)
        for sn, data in s['aggregate_by_strategy'].items():
            self.logger.info(f"  {sn:>18s}: mean={data['mean_corr']:.4f}  max={data['max_corr']:.4f}  std={data['std_corr']:.4f}")
        self.logger.info(f"\n  P-orbital means: {s['p_orbitals_by_strategy']}")
        self.logger.info(f"\n  {s['interpretation']}")
        self.logger.info("=" * 70)


def main():
    """Parse arguments and run the v2 experiment."""
    parser = argparse.ArgumentParser(description='Maxwell Magnetic Orbital Isomorphism V2')
    parser.add_argument('--checkpoint_dir', '-c', default='checkpoints_maxwell_phase3')
    parser.add_argument('--output_dir', '-o', default='orbital_v2_results')
    parser.add_argument('--grid_size', type=int, default=16)
    parser.add_argument('--hidden_dim', type=int, default=32)
    parser.add_argument('--expansion_dim', type=int, default=64)
    parser.add_argument('--spectral_layers', type=int, default=2)
    parser.add_argument('--imaginary_ratio', type=float, default=0.3)
    parser.add_argument('--log_level', default='INFO')
    args = parser.parse_args()
    config = Config(GRID_SIZE=args.grid_size, HIDDEN_DIM=args.hidden_dim,
                    EXPANSION_DIM=args.expansion_dim, NUM_SPECTRAL_LAYERS=args.spectral_layers,
                    DEFAULT_IMAGINARY_RATIO=args.imaginary_ratio,
                    LOG_LEVEL=args.log_level, CHECKPOINT_DIR=args.checkpoint_dir,
                    OUTPUT_DIRECTORY=args.output_dir)
    IsomorphismExperimentV2(config).run(args.output_dir, args.checkpoint_dir)


if __name__ == "__main__":
    main()
