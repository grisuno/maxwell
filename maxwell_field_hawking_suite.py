#!/usr/bin/env python3
"""
maxwell_field_hawking_suite.py

Combined electromagnetic field analysis and Hawking radiation thermodynamics
for Maxwell spectral network checkpoints.

Implements two complementary physical analyses on trained neural network weights:

1. Hawking Radiation Thermodynamics
   Maps weight tensors to gravitational analogs (G_eff, hbar_eff, k_B_eff,
   c_eff, M_eff, A_eff) and computes Bekenstein-Hawking entropy, Hawking
   temperature, radiation power, Schwarzschild radius, evaporation timescale,
   surface gravity, tidal forces, and information escape rate.

2. Maxwell / Poisson Electromagnetic Field Analysis
   Maps weights to a 3D dielectric lattice, solves the Poisson equation for
   the electrostatic potential, computes EM scattering intensity (Bragg peaks
   vs Rayleigh diffuse), dielectric tensor anisotropy, photonic entropy, and
   bandgap estimation.  Crystal phases show sharp Bragg peaks, low entropy,
   and high anisotropy; glass phases show diffuse scattering, high entropy,
   and isotropy.

Both analyses operate on the kernel_real and kernel_imag parameters of the
SpectralLayer modules inside a MaxwellSpectralNetwork checkpoint.

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date: 2026
License: AGPL v3
"""

import argparse
import glob
import json
import logging
import math
import os
import pickle
import io
import re
import time
import warnings
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any, Protocol, runtime_checkable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from scipy.fft import fftn, fftshift
from scipy.stats import entropy as scipy_entropy
from scipy.linalg import eigh

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

warnings.filterwarnings('ignore')


@dataclass(frozen=True)
class AnalysisConfig:
    """Immutable master configuration for the combined analysis suite."""

    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    FIELD_COMPONENTS: int = 3
    DEFAULT_IMAGINARY_RATIO: float = 0.3

    PLANCK_SI: float = 1.054571817e-34
    SPEED_OF_LIGHT_SI: float = 299792458.0
    GRAVITATIONAL_CONSTANT_SI: float = 6.67430e-11
    BOLTZMANN_CONSTANT_SI: float = 1.380649e-23
    SOLAR_MASS_SI: float = 1.98847e30

    DISCRETIZATION_MARGIN: float = 0.1
    OPTIMAL_DELTA_THRESHOLD: float = 0.01
    INDUSTRIAL_DELTA_THRESHOLD: float = 0.1
    ALPHA_CRYSTAL_THRESHOLD: float = 7.0
    DELTA_GLASS_THRESHOLD: float = 0.4
    KAPPA_CRYSTAL_THRESHOLD: float = 1.5
    TEMPERATURE_CRYSTAL_THRESHOLD: float = 1e-9

    ENTROPY_BINS: int = 50
    TEMPERATURE_WINDOW: int = 100
    SPECTRAL_REGULARIZATION: float = 1e-6
    ACTIVE_PARAM_THRESHOLD: float = 0.01
    NORMALIZATION_EPS: float = 1e-8
    EIGENVALUE_TOL: float = 1e-10
    PARAM_FLATTEN_LIMIT: int = 2000

    LATTICE_DIMENSION: int = 16
    PERMITTIVITY_VACUUM: float = 8.854e-12
    PERMEABILITY_VACUUM: float = 1.2566370614e-6
    PERMITTIVITY_WEIGHT_SCALE: float = 1.0
    CRYSTALLINITY_ENTROPY_THRESHOLD: float = 2.0
    BRAGG_PEAK_PROMINENCE: float = 0.8
    BRAGG_PEAK_INTENSITY_FRACTION: float = 0.5
    BANDGAP_DEPTH_THRESHOLD: float = 0.01

    HAWKING_UNCERTAINTY_WEIGHT_CRYSTAL: float = 0.6
    HAWKING_ACTION_WEIGHT_CRYSTAL: float = 0.25
    HAWKING_CONDUCTANCE_WEIGHT_CRYSTAL: float = 0.1
    HAWKING_INFORMATION_WEIGHT_CRYSTAL: float = 0.05
    HAWKING_UNCERTAINTY_WEIGHT_INDUSTRIAL: float = 0.5
    HAWKING_ACTION_WEIGHT_INDUSTRIAL: float = 0.3
    HAWKING_CONDUCTANCE_WEIGHT_INDUSTRIAL: float = 0.15
    HAWKING_INFORMATION_WEIGHT_INDUSTRIAL: float = 0.05
    HAWKING_UNCERTAINTY_WEIGHT_DEFAULT: float = 0.25
    HAWKING_ACTION_WEIGHT_DEFAULT: float = 0.25
    HAWKING_CONDUCTANCE_WEIGHT_DEFAULT: float = 0.25
    HAWKING_INFORMATION_WEIGHT_DEFAULT: float = 0.25

    RADIATION_POWER_DENOMINATOR: float = 15360.0
    EVAPORATION_TIME_NUMERATOR: float = 5120.0
    SURFACE_GRAVITY_DENOMINATOR: float = 4.0
    BEKENSTEIN_HAWKING_DENOMINATOR: float = 4.0
    HAWKING_TEMPERATURE_DENOMINATOR: float = 8.0

    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    RANDOM_SEED: int = 42
    LOG_LEVEL: str = 'INFO'
    FIGURE_DPI: int = 200
    SAVE_FORMAT: str = 'png'
    OUTPUT_DIRECTORY: str = 'maxwell_hawking_analysis'

    VIZ_COLOR_PRIMARY: str = '#2E86AB'
    VIZ_COLOR_SECONDARY: str = '#A23B72'
    VIZ_COLOR_ACCENT: str = '#06A77D'
    VIZ_COLOR_DANGER: str = '#D62828'
    VIZ_COLOR_WARNING: str = '#F18F01'
    VIZ_BAR_ALPHA: float = 0.7


class LoggerFactory:
    """Factory for creating configured logger instances."""

    @staticmethod
    def create_logger(name: str, level: str = 'INFO') -> logging.Logger:
        """Create and return a configured logger."""
        logger = logging.getLogger(name)
        logger.setLevel(getattr(logging, level.upper()))
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger


class CustomUnpickler(pickle.Unpickler):
    """Unpickler that handles unknown classes by creating dummy dict-like objects."""

    def find_class(self, module, name):
        """Override to handle missing classes gracefully."""
        try:
            return super().find_class(module, name)
        except (AttributeError, ModuleNotFoundError):
            return self._create_dummy_class(name)

    def _create_dummy_class(self, name):
        """Return a dummy class that acts like a dictionary."""
        class DummyClass:
            def __init__(self, *args, **kwargs):
                self._name = name
                self._kwargs = kwargs
                for k, v in kwargs.items():
                    setattr(self, k, v)
            def get(self, key, default=None):
                return self._kwargs.get(key, default)
            def keys(self):
                return self._kwargs.keys()
            def items(self):
                return self._kwargs.items()
        return DummyClass


def load_checkpoint_robust(path: str, device: str = 'cpu') -> Any:
    """Load a checkpoint with multiple fallback strategies."""
    try:
        return torch.load(path, map_location=device, weights_only=False)
    except Exception:
        pass
    try:
        with open(path, 'rb') as f:
            return CustomUnpickler(f).load()
    except Exception:
        pass
    try:
        return torch.load(path, map_location=device, weights_only=True)
    except Exception:
        pass
    try:
        with open(path, 'rb') as f:
            return CustomUnpickler(io.BytesIO(f.read())).load()
    except Exception:
        raise RuntimeError(f"All loading strategies failed for {path}")


class SpectralLayer(nn.Module):
    """Spectral convolution layer with tuneable imaginary ratio."""

    def __init__(self, channels: int, grid_size: int, imaginary_ratio: float = 0.3):
        """Initialise real and imaginary kernel parameters."""
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        self.imaginary_ratio = imaginary_ratio
        self.kernel_real = nn.Parameter(
            torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1
        )
        self.kernel_imag = nn.Parameter(
            torch.randn(channels, channels, grid_size // 2 + 1, grid_size) * 0.1
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Apply spectral convolution in Fourier space."""
        x_fft = torch.fft.rfft2(x)
        batch, channels, freq_h, freq_w = x_fft.shape
        kernel_real = self.kernel_real.mean(dim=0)
        kernel_imag = self.kernel_imag.mean(dim=0)
        kr_interp = F.interpolate(
            kernel_real.unsqueeze(0).unsqueeze(0).squeeze(0),
            size=(freq_h, freq_w), mode='bilinear', align_corners=False
        )
        ki_interp = F.interpolate(
            kernel_imag.unsqueeze(0).unsqueeze(0).squeeze(0),
            size=(freq_h, freq_w), mode='bilinear', align_corners=False
        )
        real_part = x_fft.real * kr_interp - x_fft.imag * ki_interp
        imag_part = x_fft.real * ki_interp + x_fft.imag * kr_interp
        return torch.fft.irfft2(torch.complex(real_part, imag_part), s=(self.grid_size, self.grid_size))


class MaxwellSpectralNetwork(nn.Module):
    """Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz)."""

    def __init__(self, config: AnalysisConfig, imaginary_ratio: float = 0.3):
        """Build all sub-layers."""
        super().__init__()
        self.config = config
        self.grid_size = config.GRID_SIZE
        self.field_components = config.FIELD_COMPONENTS
        self.input_channels = config.FIELD_COMPONENTS * 2
        self.output_channels = config.FIELD_COMPONENTS * 2
        self.imaginary_ratio = imaginary_ratio
        self.input_proj = nn.Conv2d(self.input_channels, config.HIDDEN_DIM, kernel_size=1)
        self.expansion_proj = nn.Conv2d(config.HIDDEN_DIM, config.EXPANSION_DIM, kernel_size=1)
        self.spectral_layers = nn.ModuleList([
            SpectralLayer(config.EXPANSION_DIM, config.GRID_SIZE, imaginary_ratio)
            for _ in range(config.NUM_SPECTRAL_LAYERS)
        ])
        self.contraction_proj = nn.Conv2d(config.EXPANSION_DIM, config.HIDDEN_DIM, kernel_size=1)
        self.output_proj = nn.Conv2d(config.HIDDEN_DIM, self.output_channels, kernel_size=1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward pass through the full spectral network."""
        if x.dim() == 3:
            x = x.unsqueeze(0)
        x = F.gelu(self.input_proj(x))
        x = F.gelu(self.expansion_proj(x))
        for sl in self.spectral_layers:
            x = F.gelu(sl(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)

    def get_flat_parameters(self) -> torch.Tensor:
        """Return all parameters as a single flat tensor."""
        return torch.cat([p.detach().flatten() for p in self.parameters()])

    def get_weight_dict(self) -> Dict[str, np.ndarray]:
        """Return all named parameter tensors as numpy arrays."""
        return {name: param.detach().cpu().numpy() for name, param in self.named_parameters()}


class MetadataExtractor:
    """Extract metadata (epoch, loss, delta) from checkpoint dicts."""

    @staticmethod
    def extract(checkpoint: Any) -> Dict[str, Any]:
        """Return a standardised metadata dict from any checkpoint format."""
        metadata = {'epoch': 'unknown', 'loss': 1.0, 'loss_history': [], 'delta': None}
        if hasattr(checkpoint, '_kwargs'):
            checkpoint = checkpoint._kwargs
        if not isinstance(checkpoint, dict):
            return metadata
        for key in ['epoch', 'epochs', 'current_epoch', 'global_step']:
            if key in checkpoint:
                metadata['epoch'] = checkpoint[key]
                break
        for key in ['loss', 'current_loss', 'final_loss', 'train_loss', 'val_loss']:
            if key in checkpoint and isinstance(checkpoint[key], (int, float)):
                metadata['loss'] = checkpoint[key]
                break
        for key in ['loss_history', 'train_losses', 'losses']:
            if key in checkpoint and isinstance(checkpoint[key], list):
                metadata['loss_history'] = [float(x) for x in checkpoint[key] if isinstance(x, (int, float))]
                break
        delta = MetadataExtractor._find_delta(checkpoint)
        if delta is not None:
            metadata['delta'] = delta
        return metadata

    @staticmethod
    def _find_delta(data: Any, depth: int = 0) -> Optional[float]:
        """Recursively search for a delta value."""
        if depth > 5:
            return None
        if hasattr(data, '_kwargs'):
            data = data._kwargs
        if isinstance(data, dict):
            if 'delta' in data and isinstance(data['delta'], (int, float)):
                return float(data['delta'])
            if 'metrics' in data and isinstance(data['metrics'], dict):
                if 'delta' in data['metrics']:
                    return float(data['metrics']['delta'])
            for value in data.values():
                result = MetadataExtractor._find_delta(value, depth + 1)
                if result is not None:
                    return result
        return None


class GravitationalConstantCalculator:
    """G_eff from weight distance to discrete attractor and gradient magnitude."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights: torch.Tensor, delta: float) -> Dict[str, float]:
        """Return G_alg, force, and crystallisation pressure."""
        rounded = torch.round(all_weights)
        distances = torch.abs(all_weights - rounded)
        mask = distances > self.config.NORMALIZATION_EPS
        valid_distances = distances[mask]
        if len(valid_distances) == 0:
            return {
                'G_alg': float('inf'), 'avg_distance': 0.0,
                'force': float('inf'), 'crystallization_pressure': 0.0,
                'delta': float(delta), 'is_crystallized': delta < self.config.DISCRETIZATION_MARGIN
            }
        avg_distance = torch.mean(valid_distances).item()
        grad_magnitude = torch.std(all_weights).item()
        if avg_distance < 1e-10:
            G_alg = float('inf')
            force = float('inf')
        else:
            force = grad_magnitude / (avg_distance ** 2)
            G_alg = force
        crystallization_pressure = grad_magnitude / (delta + 1e-10) if grad_magnitude > 0 else 0.0
        return {
            'G_alg': float(G_alg), 'avg_distance': float(avg_distance),
            'force': float(force), 'crystallization_pressure': float(crystallization_pressure),
            'delta': float(delta), 'is_crystallized': delta < self.config.DISCRETIZATION_MARGIN
        }


class PlanckConstantCalculator:
    """hbar_eff from uncertainty, action quantisation, conductance, and information entropy."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights: torch.Tensor, delta: float, loss: float) -> Dict[str, float]:
        """Return four estimates of hbar and their weighted unification."""
        total_norm = torch.norm(all_weights).item()
        lambda_eff = 1.0 / (total_norm ** 2 + 1e-10)
        h_bar_uncertainty = 2.0 * (delta ** 2) * lambda_eff
        omega = np.sqrt(lambda_eff) if lambda_eff > 0 else 1.0
        period = 2.0 * np.pi / omega
        T_kinetic = loss
        V_potential = lambda_eff * (delta ** 2)
        action = abs(T_kinetic - V_potential) * period
        h_bar_action = action
        accuracy_proxy = 1.0 - min(delta, 1.0)
        conductance = accuracy_proxy / (loss + 1e-10) if loss > 0 else 0.0
        h_bar_conductance = 1.0 / conductance if conductance > 0 else 0.0
        n_params = all_weights.numel()
        information = np.log2(max(n_params, 2))
        energy_total = T_kinetic + V_potential
        h_bar_information = (energy_total / information) * period if information > 0 else 0.0
        if delta < self.config.OPTIMAL_DELTA_THRESHOLD:
            w = (self.config.HAWKING_UNCERTAINTY_WEIGHT_CRYSTAL, self.config.HAWKING_ACTION_WEIGHT_CRYSTAL,
                 self.config.HAWKING_CONDUCTANCE_WEIGHT_CRYSTAL, self.config.HAWKING_INFORMATION_WEIGHT_CRYSTAL)
        elif delta < self.config.INDUSTRIAL_DELTA_THRESHOLD:
            w = (self.config.HAWKING_UNCERTAINTY_WEIGHT_INDUSTRIAL, self.config.HAWKING_ACTION_WEIGHT_INDUSTRIAL,
                 self.config.HAWKING_CONDUCTANCE_WEIGHT_INDUSTRIAL, self.config.HAWKING_INFORMATION_WEIGHT_INDUSTRIAL)
        else:
            w = (self.config.HAWKING_UNCERTAINTY_WEIGHT_DEFAULT, self.config.HAWKING_ACTION_WEIGHT_DEFAULT,
                 self.config.HAWKING_CONDUCTANCE_WEIGHT_DEFAULT, self.config.HAWKING_INFORMATION_WEIGHT_DEFAULT)
        h_bar_unified = (w[0] * h_bar_uncertainty + w[1] * h_bar_action +
                         w[2] * h_bar_conductance + w[3] * h_bar_information) / sum(w)
        ratio_to_si = h_bar_unified / self.config.PLANCK_SI if self.config.PLANCK_SI > 0 else 0.0
        return {
            'h_bar_uncertainty': float(h_bar_uncertainty), 'h_bar_action': float(h_bar_action),
            'h_bar_conductance': float(h_bar_conductance), 'h_bar_information': float(h_bar_information),
            'h_bar_unified': float(h_bar_unified), 'lambda_eff': float(lambda_eff),
            'ratio_to_si_planck': float(ratio_to_si),
            'is_quantum_regime': h_bar_unified < 1.0
        }


class BoltzmannConstantCalculator:
    """k_B_eff from configuration entropy and thermal fluctuations."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights_np: np.ndarray, loss: float,
                  loss_history: Optional[List[float]] = None) -> Dict[str, float]:
        """Return entropy-based and thermal k_B estimates."""
        hist, _ = np.histogram(all_weights_np, bins=self.config.ENTROPY_BINS, density=True)
        hist = hist[hist > 0]
        config_entropy = float(scipy_entropy(hist)) if len(hist) > 0 else 0.0
        if loss_history and len(loss_history) >= self.config.TEMPERATURE_WINDOW:
            energy = np.var(loss_history[-self.config.TEMPERATURE_WINDOW:])
        else:
            energy = loss
        k_b_entropy = config_entropy / energy if energy > 1e-10 else float('inf')
        weight_variance = np.var(all_weights_np)
        k_b_thermal = weight_variance / energy if energy > 1e-10 else float('inf')
        k_b_unified = (k_b_entropy + k_b_thermal) / 2.0
        return {
            'k_b_entropy': float(k_b_entropy), 'k_b_thermal': float(k_b_thermal),
            'k_b_unified': float(k_b_unified), 'config_entropy': config_entropy,
            'energy_proxy': float(energy), 'weight_variance': float(weight_variance)
        }


class SpeedOfLightCalculator:
    """c_eff from Planck relation and spectral velocity of weight matrices."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights_np: np.ndarray, h_bar: float, G_alg: float) -> Dict[str, float]:
        """Return multiple c estimates."""
        c_from_planck = self.config.SPEED_OF_LIGHT_SI * (h_bar / self.config.PLANCK_SI)
        try:
            n = min(len(all_weights_np), self.config.PARAM_FLATTEN_LIMIT)
            w = all_weights_np[:n]
            outer = np.outer(w[:min(64, n)], w[:min(64, n)])
            eigenvalues = np.abs(np.linalg.eigvals(outer))
            spectral_velocity = float(np.sqrt(np.max(eigenvalues)))
        except Exception:
            spectral_velocity = 1.0
        c_unified = c_from_planck
        return {
            'c_from_planck': float(c_from_planck), 'c_spectral': spectral_velocity,
            'c_unified': float(c_unified),
            'ratio_to_si_c': float(c_unified / self.config.SPEED_OF_LIGHT_SI)
        }


class InformationalMassCalculator:
    """M_eff from Planck mass formula, active parameter count, and energy-mass relation."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights: torch.Tensor, G_alg: float,
                  c_eff: float, h_bar: float) -> Dict[str, float]:
        """Return multiple mass estimates."""
        active_mask = torch.abs(all_weights) > self.config.ACTIVE_PARAM_THRESHOLD
        n_active = int(torch.sum(active_mask).item())
        n_total = all_weights.numel()
        all_np = all_weights.cpu().numpy()
        hist, _ = np.histogram(all_np, bins=self.config.ENTROPY_BINS, density=True)
        hist = hist[hist > 0]
        information = float(scipy_entropy(hist)) if len(hist) > 0 else 0.0
        G_safe = G_alg if 0 < G_alg < float('inf') else 1.0
        c_safe = c_eff if c_eff > 0 else 1.0
        h_safe = h_bar if h_bar > 0 else 1.0
        m_planck = np.sqrt(h_safe * c_safe / G_safe)
        m_from_info = n_active * information
        weight_energy = float(torch.var(all_weights).item())
        m_from_energy = weight_energy / (c_safe ** 2)
        m_unified = m_planck if m_planck > 0 else max(m_from_info, m_from_energy)
        return {
            'm_planck_eff': float(m_planck), 'm_from_info': float(m_from_info),
            'm_from_energy': float(m_from_energy), 'm_unified': float(m_unified),
            'n_active_params': n_active, 'n_total_params': n_total,
            'sparsity': float(1.0 - n_active / max(n_total, 1)),
            'information_content': information
        }


class HorizonAreaCalculator:
    """A_eff from active parameter counts and entropy proxy."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, all_weights: torch.Tensor) -> Dict[str, float]:
        """Return effective area from active parameters and weight entropy."""
        active = int(torch.sum(torch.abs(all_weights) > self.config.ACTIVE_PARAM_THRESHOLD).item())
        entropy_proxy = -torch.sum(
            all_weights * torch.log(torch.abs(all_weights) + 1e-10)
        ).item()
        a_from_entropy = self.config.BEKENSTEIN_HAWKING_DENOMINATOR * abs(entropy_proxy)
        return {
            'a_unified': float(active), 'a_from_entropy': float(a_from_entropy),
            'active_params': active
        }


class HawkingRadiationCalculator:
    """Full Hawking radiation thermodynamic analysis."""

    def __init__(self, config: AnalysisConfig):
        """Instantiate all sub-calculators."""
        self.config = config
        self.G_calc = GravitationalConstantCalculator(config)
        self.hbar_calc = PlanckConstantCalculator(config)
        self.kb_calc = BoltzmannConstantCalculator(config)
        self.c_calc = SpeedOfLightCalculator(config)
        self.M_calc = InformationalMassCalculator(config)
        self.A_calc = HorizonAreaCalculator(config)

    def calculate(self, model: nn.Module, loss: float = 1.0,
                  loss_history: Optional[List[float]] = None,
                  precomputed_delta: Optional[float] = None) -> Dict[str, Any]:
        """Run the full Hawking radiation pipeline and return all results."""
        all_weights = model.get_flat_parameters()
        all_np = all_weights.cpu().numpy()
        if precomputed_delta is not None:
            delta = precomputed_delta
        else:
            delta = float(torch.max(torch.abs(all_weights - torch.round(all_weights))).item())
        G_result = self.G_calc.calculate(all_weights, delta)
        G_alg = G_result['G_alg']
        hbar_result = self.hbar_calc.calculate(all_weights, delta, loss)
        h_bar = hbar_result['h_bar_unified']
        kb_result = self.kb_calc.calculate(all_np, loss, loss_history)
        k_B = kb_result['k_b_unified']
        c_result = self.c_calc.calculate(all_np, h_bar, G_alg)
        c_eff = c_result['c_unified']
        M_result = self.M_calc.calculate(all_weights, G_alg, c_eff, h_bar)
        M_eff = M_result['m_unified']
        A_result = self.A_calc.calculate(all_weights)
        A_eff = A_result['a_unified']

        G_s = G_alg if 0 < G_alg < float('inf') else 1.0
        M_s = M_eff if M_eff > 0 else 1.0
        k_s = k_B if k_B > 0 else 1.0
        c_s = c_eff if c_eff > 0 else 1.0
        h_s = h_bar if h_bar > 0 else 1.0
        A_s = A_eff if A_eff > 0 else 1.0

        S_bh = (A_s * k_s * (c_s ** 3)) / (self.config.BEKENSTEIN_HAWKING_DENOMINATOR * G_s * h_s)
        T_hawking = (h_s * (c_s ** 3)) / (self.config.HAWKING_TEMPERATURE_DENOMINATOR * np.pi * G_s * M_s * k_s)
        r_schwarzschild = 2.0 * G_s * M_s / (c_s ** 2)
        P_radiation = (h_s * (c_s ** 6)) / (self.config.RADIATION_POWER_DENOMINATOR * np.pi * (G_s ** 2) * (M_s ** 2))
        tau_evaporation = (self.config.EVAPORATION_TIME_NUMERATOR * np.pi * (G_s ** 2) * (M_s ** 3)) / (h_s * (c_s ** 4))
        surface_gravity = (c_s ** 4) / (self.config.SURFACE_GRAVITY_DENOMINATOR * G_s * M_s)
        tidal_force = 1.0 / (r_schwarzschild ** 3) if r_schwarzschild > 0 and r_schwarzschild < float('inf') else 0.0
        info_escape = P_radiation / (T_hawking * k_s) if T_hawking > 0 and T_hawking < float('inf') and k_s > 0 else 0.0

        state = "frozen_crystal" if delta < self.config.OPTIMAL_DELTA_THRESHOLD and T_hawking < 0.01 else \
                "hot_crystal" if delta < self.config.OPTIMAL_DELTA_THRESHOLD else \
                "polycrystal" if delta < self.config.INDUSTRIAL_DELTA_THRESHOLD else \
                "glass" if delta < 0.5 else "amorphous"

        return {
            'constants': {
                'G_alg': G_result, 'h_bar': hbar_result, 'k_B': kb_result,
                'c_eff': c_result, 'M_eff': M_result, 'A_eff': A_result
            },
            'hawking': {
                'S_BH': float(S_bh), 'T_H': float(T_hawking),
                'r_schwarzschild': float(r_schwarzschild), 'P_radiation': float(P_radiation),
                'tau_evaporation': float(tau_evaporation), 'surface_gravity': float(surface_gravity),
                'tidal_force': float(tidal_force), 'info_escape_rate': float(info_escape)
            },
            'diagnostics': {
                'delta': float(delta), 'crystallization_state': state,
                'is_evaporating': 0 < P_radiation < float('inf'),
                'temperature_regime': 'hot' if T_hawking > 1 else ('cold' if T_hawking < 0.01 else 'moderate')
            }
        }


class WeightLatticeMapper:
    """Map neural network weights to a 3D dielectric lattice."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def map(self, weight_dict: Dict[str, np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Return (charge_density, permittivity) as 3D arrays.

        Weights are flattened and embedded into a cubic grid.
        Permittivity = 1 + scale * w_i.
        Charge density = w_i.
        """
        N = self.config.LATTICE_DIMENSION
        flat = np.concatenate([w.flatten() for w in weight_dict.values()])
        permittivity = np.ones((N, N, N), dtype=np.float64)
        charge_density = np.zeros((N, N, N), dtype=np.float64)
        idx = 0
        for x in range(N):
            for y in range(N):
                for z in range(N):
                    if idx < len(flat):
                        permittivity[x, y, z] = 1.0 + self.config.PERMITTIVITY_WEIGHT_SCALE * flat[idx]
                        charge_density[x, y, z] = flat[idx]
                        idx += 1
        return charge_density, permittivity


class PoissonSolver:
    """Spectral Poisson solver: nabla^2 phi = -rho / eps_0."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def solve(self, charge_density: np.ndarray, permittivity: np.ndarray) -> np.ndarray:
        """Return the electrostatic potential phi on the 3D grid."""
        N = self.config.LATTICE_DIMENSION
        rho_k = fftn(charge_density)
        kx = np.fft.fftfreq(N) * 2 * np.pi
        ky = np.fft.fftfreq(N) * 2 * np.pi
        kz = np.fft.fftfreq(N) * 2 * np.pi
        KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing='ij')
        k_squared = KX ** 2 + KY ** 2 + KZ ** 2
        k_squared[0, 0, 0] = 1.0
        eps_avg = np.mean(permittivity) * self.config.PERMITTIVITY_VACUUM
        phi_k = rho_k / (eps_avg * k_squared)
        return np.real(np.fft.ifftn(phi_k))

    def compute_electric_field(self, potential: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Return E = -grad(phi)."""
        return -np.gradient(potential, axis=0), -np.gradient(potential, axis=1), -np.gradient(potential, axis=2)


class ScatteringSolver:
    """EM scattering from dielectric contrast: S(k) ~ |FT(delta_eps)|^2."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def compute(self, permittivity: np.ndarray) -> Dict[str, Any]:
        """Return scattering intensity map, central slice, and peak analysis."""
        eps_avg = np.mean(permittivity)
        delta_eps = permittivity - eps_avg
        F_eps = fftshift(fftn(delta_eps))
        intensity = np.abs(F_eps) ** 2
        max_intensity = np.max(intensity)
        if max_intensity > 0:
            intensity /= max_intensity
        N = self.config.LATTICE_DIMENSION
        center = N // 2
        slice_2d = intensity[:, :, center]
        threshold = self.config.BRAGG_PEAK_INTENSITY_FRACTION * np.max(intensity)
        peak_indices = np.where(intensity > threshold)
        peak_count = len(peak_indices[0])
        prominence = float(np.max(intensity) / np.mean(intensity[intensity > 0.01])) if np.any(intensity > 0.01) else 0.0
        return {
            'intensity_3d': intensity, 'slice_xy': slice_2d,
            'fourier_coefficients': F_eps,
            'peak_count': peak_count, 'prominence': prominence,
            'is_bragg_pattern': peak_count > 5 and prominence > self.config.BRAGG_PEAK_PROMINENCE
        }


class DielectricTensorAnalyzer:
    """Anisotropy analysis of the dielectric medium via the structure tensor."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def analyze(self, permittivity: np.ndarray) -> Dict[str, Any]:
        """Return eigenvalues of the gradient structure tensor and anisotropy ratio."""
        grad_x = np.gradient(permittivity, axis=0)
        grad_y = np.gradient(permittivity, axis=1)
        grad_z = np.gradient(permittivity, axis=2)
        J = np.zeros((3, 3))
        grads = [grad_x, grad_y, grad_z]
        for i in range(3):
            for j in range(i, 3):
                val = np.sum(grads[i] * grads[j])
                J[i, j] = val
                J[j, i] = val
        eigenvalues = np.linalg.eigvalsh(J)
        total = np.sum(eigenvalues)
        anisotropy = (eigenvalues[-1] - eigenvalues[0]) / total if total > 1e-10 else 0.0
        return {
            'dielectric_eigenvalues': eigenvalues.tolist(),
            'anisotropy_ratio': float(anisotropy),
            'mean_permittivity': float(np.mean(permittivity)),
            'variance_permittivity': float(np.var(permittivity)),
            'is_isotropic': anisotropy < 0.1
        }


class PhotonicEntropyCalculator:
    """Shannon entropy of the EM field energy distribution and density of modes."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def calculate(self, potential: np.ndarray, intensity_3d: np.ndarray) -> Dict[str, float]:
        """Return field entropy, mode entropy, and their sum."""
        energy_density = potential ** 2
        hist, _ = np.histogram(energy_density.flatten(), bins=self.config.ENTROPY_BINS, density=True)
        hist = hist[hist > 0]
        field_entropy = float(scipy_entropy(hist))
        dos = intensity_3d.flatten()
        dos_sum = np.sum(dos)
        if dos_sum > 0:
            dos_norm = dos / dos_sum
            dos_norm = dos_norm[dos_norm > 0]
            mode_entropy = float(scipy_entropy(dos_norm))
        else:
            mode_entropy = 0.0
        return {
            'field_entropy': field_entropy, 'mode_entropy': mode_entropy,
            'total_photonic_entropy': field_entropy + mode_entropy
        }


class BandgapAnalyzer:
    """Photonic bandgap estimation from radial Fourier profile."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def analyze(self, fourier_coeffs: np.ndarray) -> Dict[str, Any]:
        """Return radial profile, gap depth, and boolean bandgap detection."""
        N = self.config.LATTICE_DIMENSION
        center = N // 2
        z, y, x = np.ogrid[:N, :N, :N]
        r = np.sqrt((x - center) ** 2 + (y - center) ** 2 + (z - center) ** 2).astype(int)
        intensity = np.abs(fourier_coeffs) ** 2
        radial_sum = np.bincount(r.ravel(), intensity.ravel())
        radial_count = np.bincount(r.ravel())
        radial_count[radial_count == 0] = 1
        radial_profile = radial_sum / radial_count
        profile_smooth = radial_profile[1:len(radial_profile) // 2]
        if len(profile_smooth) > 0:
            min_val = np.min(profile_smooth)
            max_val = np.max(profile_smooth)
            gap_ratio = min_val / (max_val + 1e-10)
        else:
            gap_ratio = 1.0
        return {
            'radial_profile': radial_profile.tolist(),
            'has_bandgap': bool(gap_ratio < self.config.BANDGAP_DEPTH_THRESHOLD),
            'gap_depth': float(gap_ratio)
        }


class ElectromagneticPhaseClassifier:
    """Crystal vs Glass classification from EM observables."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def classify(self, anisotropy: Dict, scattering: Dict,
                 photonic_entropy: Dict, delta: float, alpha: float) -> Dict[str, Any]:
        """Return phase name, crystal/glass flags, and confidence score."""
        high_alpha = alpha > self.config.ALPHA_CRYSTAL_THRESHOLD
        high_anisotropy = anisotropy['anisotropy_ratio'] > 0.5
        bragg = scattering['is_bragg_pattern']
        low_entropy = photonic_entropy['total_photonic_entropy'] < self.config.CRYSTALLINITY_ENTROPY_THRESHOLD
        score = int(high_alpha) + int(high_anisotropy) + 2 * int(bragg) + int(low_entropy)
        if score >= 3:
            phase = "EM_Crystal"
            is_crystal = True
        elif score >= 1:
            phase = "EM_Glass"
            is_crystal = False
        else:
            phase = "EM_Disordered"
            is_crystal = False
        return {
            'phase': phase, 'is_crystal': is_crystal,
            'confidence': float(score / 5.0),
            'criteria': {
                'high_alpha': high_alpha, 'high_anisotropy': high_anisotropy,
                'bragg_peaks': bragg, 'low_entropy': low_entropy
            }
        }


class MaxwellFieldAnalyzer:
    """Full Maxwell / Poisson electromagnetic field analysis pipeline."""

    def __init__(self, config: AnalysisConfig):
        """Instantiate all sub-components."""
        self.config = config
        self.mapper = WeightLatticeMapper(config)
        self.poisson = PoissonSolver(config)
        self.scattering_solver = ScatteringSolver(config)
        self.dielectric_analyzer = DielectricTensorAnalyzer(config)
        self.entropy_calc = PhotonicEntropyCalculator(config)
        self.bandgap_analyzer = BandgapAnalyzer(config)
        self.classifier = ElectromagneticPhaseClassifier(config)

    def analyze(self, model: nn.Module) -> Dict[str, Any]:
        """Run the full EM pipeline on the model weights."""
        weight_dict = model.get_weight_dict()
        charge, permittivity = self.mapper.map(weight_dict)
        potential = self.poisson.solve(charge, permittivity)
        Ex, Ey, Ez = self.poisson.compute_electric_field(potential)
        scattering = self.scattering_solver.compute(permittivity)
        dielectric = self.dielectric_analyzer.analyze(permittivity)
        photonic_entropy = self.entropy_calc.calculate(potential, scattering['intensity_3d'])
        bandgap = self.bandgap_analyzer.analyze(scattering['fourier_coefficients'])
        all_weights = model.get_flat_parameters()
        rounded = torch.round(all_weights)
        delta = float(torch.max(torch.abs(all_weights - rounded)).item())
        alpha = -np.log(delta + 1e-15)
        classification = self.classifier.classify(dielectric, scattering, photonic_entropy, delta, alpha)
        E_magnitude = np.sqrt(Ex ** 2 + Ey ** 2 + Ez ** 2)
        return {
            'potential': {
                'max_potential': float(np.max(np.abs(potential))),
                'mean_potential': float(np.mean(potential)),
                'potential_variance': float(np.var(potential))
            },
            'electric_field': {
                'max_E': float(np.max(E_magnitude)),
                'mean_E': float(np.mean(E_magnitude)),
                'E_variance': float(np.var(E_magnitude))
            },
            'dielectric': dielectric,
            'scattering': {
                'peak_count': scattering['peak_count'],
                'prominence': scattering['prominence'],
                'is_bragg_pattern': scattering['is_bragg_pattern']
            },
            'photonic_entropy': photonic_entropy,
            'bandgap': bandgap,
            'purity': {'delta': delta, 'alpha': alpha},
            'classification': classification,
            '_scattering_slice': scattering['slice_xy'],
            '_potential_slice': potential[self.config.LATTICE_DIMENSION // 2, :, :]
        }


class CombinedVisualizer:
    """Generate multi-panel dashboard combining Hawking and Maxwell analyses."""

    def __init__(self, config: AnalysisConfig):
        """Store config reference."""
        self.config = config

    def render(self, hawking: Dict, maxwell: Dict, metadata: Dict, output_path: str):
        """Save a comprehensive 4x4 figure to disk."""
        fig = plt.figure(figsize=(22, 18), dpi=self.config.FIGURE_DPI)
        gs = GridSpec(4, 4, figure=fig, hspace=0.4, wspace=0.4)
        epoch = metadata.get('epoch', '?')
        fig.suptitle(f'Maxwell Field + Hawking Radiation Analysis -- Epoch {epoch}', fontsize=14, fontweight='bold')

        self._plot_hawking_summary(hawking, fig.add_subplot(gs[0, 0]))
        self._plot_hawking_temperature(hawking, fig.add_subplot(gs[0, 1]))
        self._plot_hawking_entropy(hawking, fig.add_subplot(gs[0, 2]))
        self._plot_hawking_constants(hawking, fig.add_subplot(gs[0, 3]))
        self._plot_potential_slice(maxwell, fig.add_subplot(gs[1, 0]))
        self._plot_scattering_slice(maxwell, fig.add_subplot(gs[1, 1]))
        self._plot_dielectric_anisotropy(maxwell, fig.add_subplot(gs[1, 2]))
        self._plot_photonic_entropy(maxwell, fig.add_subplot(gs[1, 3]))
        self._plot_bandgap(maxwell, fig.add_subplot(gs[2, 0]))
        self._plot_electric_field(maxwell, fig.add_subplot(gs[2, 1]))
        self._plot_em_classification(maxwell, fig.add_subplot(gs[2, 2]))
        self._plot_combined_summary(hawking, maxwell, metadata, fig.add_subplot(gs[2, 3]))
        self._plot_hawking_radiation_power(hawking, fig.add_subplot(gs[3, 0]))
        self._plot_schwarzschild(hawking, fig.add_subplot(gs[3, 1]))
        self._plot_evaporation(hawking, fig.add_subplot(gs[3, 2]))
        self._plot_purity(maxwell, fig.add_subplot(gs[3, 3]))

        plt.savefig(output_path, dpi=self.config.FIGURE_DPI, format=self.config.SAVE_FORMAT, bbox_inches='tight')
        plt.close()

    def _plot_hawking_summary(self, h: Dict, ax):
        """Hawking temperature and BH entropy bars."""
        hw = h.get('hawking', {})
        vals = [hw.get('T_H', 0), hw.get('S_BH', 0)]
        labels = ['T_Hawking', 'S_BH']
        finite_vals = [v if np.isfinite(v) else 0 for v in vals]
        ax.bar(labels, finite_vals, color=[self.config.VIZ_COLOR_DANGER, self.config.VIZ_COLOR_PRIMARY], alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Hawking Summary', fontweight='bold')

    def _plot_hawking_temperature(self, h: Dict, ax):
        """Temperature gauge."""
        T = h.get('hawking', {}).get('T_H', 0)
        T_disp = T if np.isfinite(T) else 0
        ax.barh(['T_Hawking'], [T_disp], color=self.config.VIZ_COLOR_DANGER, alpha=self.config.VIZ_BAR_ALPHA)
        regime = h.get('diagnostics', {}).get('temperature_regime', '?')
        ax.set_title(f'Hawking Temperature\nRegime: {regime}', fontweight='bold')

    def _plot_hawking_entropy(self, h: Dict, ax):
        """Bekenstein-Hawking entropy."""
        S = h.get('hawking', {}).get('S_BH', 0)
        S_disp = min(S, 1e10) if np.isfinite(S) else 0
        ax.bar(['S_BH'], [S_disp], color=self.config.VIZ_COLOR_PRIMARY, alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('BH Entropy', fontweight='bold')

    def _plot_hawking_constants(self, h: Dict, ax):
        """Effective constants summary."""
        c = h.get('constants', {})
        names = ['G_alg', 'hbar', 'k_B', 'c_eff']
        vals = [
            c.get('G_alg', {}).get('G_alg', 0),
            c.get('h_bar', {}).get('h_bar_unified', 0),
            c.get('k_B', {}).get('k_b_unified', 0),
            c.get('c_eff', {}).get('c_unified', 0)
        ]
        finite = [v if np.isfinite(v) and abs(v) < 1e15 else 0 for v in vals]
        ax.bar(names, finite, color=self.config.VIZ_COLOR_ACCENT, alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Effective Constants', fontweight='bold')
        ax.tick_params(axis='x', rotation=45)

    def _plot_potential_slice(self, m: Dict, ax):
        """Central slice of electrostatic potential."""
        ps = m.get('_potential_slice')
        if ps is not None:
            im = ax.imshow(ps, cmap='viridis', aspect='auto')
            plt.colorbar(im, ax=ax, fraction=0.046)
        ax.set_title('Poisson Potential (slice)', fontweight='bold')

    def _plot_scattering_slice(self, m: Dict, ax):
        """kx-ky scattering intensity."""
        ss = m.get('_scattering_slice')
        if ss is not None:
            im = ax.imshow(ss, cmap='hot', aspect='auto')
            plt.colorbar(im, ax=ax, fraction=0.046)
        ax.set_title('EM Scattering (Bragg)', fontweight='bold')
        ax.set_xlabel('kx')
        ax.set_ylabel('ky')

    def _plot_dielectric_anisotropy(self, m: Dict, ax):
        """Dielectric tensor eigenvalues."""
        d = m.get('dielectric', {})
        eigs = d.get('dielectric_eigenvalues', [0, 0, 0])
        ax.bar(['lambda_1', 'lambda_2', 'lambda_3'], eigs,
               color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY, self.config.VIZ_COLOR_ACCENT],
               alpha=self.config.VIZ_BAR_ALPHA)
        aniso = d.get('anisotropy_ratio', 0)
        ax.set_title(f'Dielectric Tensor\nAnisotropy: {aniso:.3f}', fontweight='bold')

    def _plot_photonic_entropy(self, m: Dict, ax):
        """Field and mode entropy bars."""
        pe = m.get('photonic_entropy', {})
        ax.bar(['Field S', 'Mode S', 'Total S'],
               [pe.get('field_entropy', 0), pe.get('mode_entropy', 0), pe.get('total_photonic_entropy', 0)],
               color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY, self.config.VIZ_COLOR_WARNING],
               alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Photonic Entropy', fontweight='bold')

    def _plot_bandgap(self, m: Dict, ax):
        """Radial Fourier profile and bandgap indicator."""
        bg = m.get('bandgap', {})
        profile = bg.get('radial_profile', [])
        if profile:
            ax.plot(profile[:len(profile) // 2], color=self.config.VIZ_COLOR_PRIMARY)
        has_gap = bg.get('has_bandgap', False)
        ax.set_title(f'Bandgap: {"YES" if has_gap else "NO"}\nDepth: {bg.get("gap_depth", 0):.4f}', fontweight='bold')
        ax.set_xlabel('Radial k')
        ax.set_ylabel('Intensity')

    def _plot_electric_field(self, m: Dict, ax):
        """Electric field magnitude statistics."""
        ef = m.get('electric_field', {})
        ax.bar(['Max |E|', 'Mean |E|'],
               [ef.get('max_E', 0), ef.get('mean_E', 0)],
               color=[self.config.VIZ_COLOR_DANGER, self.config.VIZ_COLOR_ACCENT], alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Electric Field', fontweight='bold')

    def _plot_em_classification(self, m: Dict, ax):
        """Phase classification text panel."""
        ax.axis('off')
        cl = m.get('classification', {})
        criteria = cl.get('criteria', {})
        text = (
            f"Phase: {cl.get('phase', '?')}\n"
            f"Confidence: {cl.get('confidence', 0):.2f}\n"
            f"Crystal: {cl.get('is_crystal', False)}\n\n"
            f"High Alpha: {criteria.get('high_alpha', False)}\n"
            f"High Aniso: {criteria.get('high_anisotropy', False)}\n"
            f"Bragg Peaks: {criteria.get('bragg_peaks', False)}\n"
            f"Low Entropy: {criteria.get('low_entropy', False)}"
        )
        ax.text(0.1, 0.5, text, transform=ax.transAxes, fontsize=9, verticalalignment='center',
                fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        ax.set_title('EM Phase Classification', fontweight='bold')

    def _plot_combined_summary(self, h: Dict, m: Dict, meta: Dict, ax):
        """Text summary combining both analyses."""
        ax.axis('off')
        hw = h.get('hawking', {})
        diag = h.get('diagnostics', {})
        pur = m.get('purity', {})
        cl = m.get('classification', {})
        text = (
            f"Epoch: {meta.get('epoch', '?')}\n"
            f"Delta: {pur.get('delta', 0):.6f}\n"
            f"Alpha: {pur.get('alpha', 0):.4f}\n"
            f"Crystal State: {diag.get('crystallization_state', '?')}\n"
            f"EM Phase: {cl.get('phase', '?')}\n"
            f"T_Hawking: {hw.get('T_H', 0):.4e}\n"
            f"S_BH: {hw.get('S_BH', 0):.4e}\n"
            f"P_rad: {hw.get('P_radiation', 0):.4e}\n"
            f"tau_evap: {hw.get('tau_evaporation', 0):.4e}"
        )
        ax.text(0.1, 0.5, text, transform=ax.transAxes, fontsize=9, verticalalignment='center',
                fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        ax.set_title('Combined Summary', fontweight='bold')

    def _plot_hawking_radiation_power(self, h: Dict, ax):
        """Radiation power bar."""
        P = h.get('hawking', {}).get('P_radiation', 0)
        P_disp = min(P, 1e10) if np.isfinite(P) else 0
        ax.bar(['P_radiation'], [P_disp], color=self.config.VIZ_COLOR_WARNING, alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Radiation Power', fontweight='bold')

    def _plot_schwarzschild(self, h: Dict, ax):
        """Schwarzschild radius and surface gravity."""
        hw = h.get('hawking', {})
        rs = hw.get('r_schwarzschild', 0)
        sg = hw.get('surface_gravity', 0)
        rs_d = min(rs, 1e10) if np.isfinite(rs) else 0
        sg_d = min(sg, 1e10) if np.isfinite(sg) else 0
        ax.bar(['r_s', 'kappa_s'], [rs_d, sg_d],
               color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY], alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Schwarzschild Metrics', fontweight='bold')

    def _plot_evaporation(self, h: Dict, ax):
        """Evaporation timescale bar."""
        tau = h.get('hawking', {}).get('tau_evaporation', 0)
        tau_d = min(tau, 1e10) if np.isfinite(tau) else 0
        ax.bar(['tau_evaporation'], [tau_d], color=self.config.VIZ_COLOR_ACCENT, alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Evaporation Time', fontweight='bold')

    def _plot_purity(self, m: Dict, ax):
        """Delta and alpha purity bars."""
        p = m.get('purity', {})
        ax.bar(['Delta', 'Alpha'], [p.get('delta', 0), p.get('alpha', 0)],
               color=[self.config.VIZ_COLOR_DANGER, self.config.VIZ_COLOR_ACCENT], alpha=self.config.VIZ_BAR_ALPHA)
        ax.set_title('Weight Purity', fontweight='bold')


class CombinedAnalyzer:
    """Orchestrator that runs both Hawking and Maxwell analyses on a single checkpoint."""

    def __init__(self, config: AnalysisConfig):
        """Instantiate sub-analyzers and visualizer."""
        self.config = config
        self.logger = LoggerFactory.create_logger("CombinedAnalyzer", config.LOG_LEVEL)
        self.hawking = HawkingRadiationCalculator(config)
        self.maxwell = MaxwellFieldAnalyzer(config)
        self.visualizer = CombinedVisualizer(config)

    def analyze_checkpoint(self, checkpoint_path: str, output_dir: str) -> Dict[str, Any]:
        """Load, analyze, visualize, and return aggregated results."""
        self.logger.info(f"Analyzing: {checkpoint_path}")
        os.makedirs(output_dir, exist_ok=True)
        checkpoint = load_checkpoint_robust(checkpoint_path, self.config.DEVICE)
        metadata = MetadataExtractor.extract(checkpoint)
        imaginary_ratio = self.config.DEFAULT_IMAGINARY_RATIO
        if isinstance(checkpoint, dict):
            cfg = checkpoint.get('config', {})
            if isinstance(cfg, dict):
                imaginary_ratio = cfg.get('imaginary_ratio', imaginary_ratio)
        model = MaxwellSpectralNetwork(self.config, imaginary_ratio=imaginary_ratio)
        if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'], strict=False)
        elif isinstance(checkpoint, dict):
            try:
                model.load_state_dict(checkpoint, strict=False)
            except Exception:
                pass
        model.eval()
        loss = metadata.get('loss', 1.0)
        loss_history = metadata.get('loss_history', [])
        delta = metadata.get('delta')

        self.logger.info("  Running Hawking radiation analysis...")
        hawking_results = self.hawking.calculate(model, loss, loss_history, delta)

        self.logger.info("  Running Maxwell / Poisson field analysis...")
        maxwell_results = self.maxwell.analyze(model)

        name = Path(checkpoint_path).stem
        viz_path = os.path.join(output_dir, f"{name}_analysis.{self.config.SAVE_FORMAT}")
        self.visualizer.render(hawking_results, maxwell_results, metadata, viz_path)

        combined = {
            'metadata': {
                'checkpoint_path': checkpoint_path,
                'epoch': metadata.get('epoch', '?'),
                'timestamp': datetime.now().isoformat()
            },
            'hawking': hawking_results,
            'maxwell': {k: v for k, v in maxwell_results.items() if not k.startswith('_')}
        }

        json_path = os.path.join(output_dir, f"{name}_results.json")
        with open(json_path, 'w') as f:
            json.dump(combined, f, indent=2, default=str)

        self.logger.info(f"  Results saved: {json_path}")
        self.logger.info(f"  Visualization: {viz_path}")
        return combined


class BatchAnalyzer:
    """Process all checkpoints in a directory."""

    def __init__(self, config: AnalysisConfig):
        """Instantiate the single-checkpoint analyzer."""
        self.config = config
        self.logger = LoggerFactory.create_logger("BatchAnalyzer", config.LOG_LEVEL)
        self.analyzer = CombinedAnalyzer(config)

    def process(self, input_path: str, output_dir: str):
        """Analyze one file or all .pth files in a directory."""
        self.logger.info("=" * 70)
        self.logger.info("MAXWELL FIELD + HAWKING RADIATION ANALYSIS SUITE")
        self.logger.info("=" * 70)
        os.makedirs(output_dir, exist_ok=True)
        p = Path(input_path)
        if p.is_file():
            files = [p]
        elif p.is_dir():
            files = sorted(list(p.glob('*.pth')) + list(p.glob('*.pt')))
        else:
            self.logger.error(f"Path not found: {input_path}")
            return
        if not files:
            self.logger.warning(f"No checkpoint files found in {input_path}")
            return
        self.logger.info(f"Found {len(files)} checkpoints")
        all_results = []
        for i, f in enumerate(files):
            self.logger.info(f"[{i + 1}/{len(files)}] {f}")
            try:
                result = self.analyzer.analyze_checkpoint(str(f), output_dir)
                all_results.append(result)
            except Exception as e:
                self.logger.error(f"Error processing {f}: {e}")
                import traceback
                self.logger.error(traceback.format_exc())
        if all_results:
            summary = self._build_summary(all_results)
            with open(os.path.join(output_dir, 'analysis_summary.json'), 'w') as f:
                json.dump(summary, f, indent=2, default=str)
            self._print_ranking(all_results)
        self.logger.info("=" * 70)
        self.logger.info("ANALYSIS COMPLETE")
        self.logger.info(f"Results in: {output_dir}")
        self.logger.info("=" * 70)

    def _build_summary(self, results: List[Dict]) -> Dict[str, Any]:
        """Aggregate statistics across checkpoints."""
        deltas = [r.get('maxwell', {}).get('purity', {}).get('delta', 1.0) for r in results]
        alphas = [r.get('maxwell', {}).get('purity', {}).get('alpha', 0.0) for r in results]
        T_H = [r.get('hawking', {}).get('hawking', {}).get('T_H', 0) for r in results]
        S_BH = [r.get('hawking', {}).get('hawking', {}).get('S_BH', 0) for r in results]
        phases = [r.get('maxwell', {}).get('classification', {}).get('phase', '?') for r in results]
        states = [r.get('hawking', {}).get('diagnostics', {}).get('crystallization_state', '?') for r in results]

        def _safe_stats(vals):
            arr = np.array([v for v in vals if np.isfinite(v)], dtype=float)
            if len(arr) == 0:
                return {'mean': 0, 'std': 0, 'min': 0, 'max': 0}
            return {'mean': float(np.mean(arr)), 'std': float(np.std(arr)),
                    'min': float(np.min(arr)), 'max': float(np.max(arr))}

        return {
            'total_checkpoints': len(results),
            'statistics': {
                'delta': _safe_stats(deltas), 'alpha': _safe_stats(alphas),
                'T_Hawking': _safe_stats(T_H), 'S_BH': _safe_stats(S_BH)
            },
            'phase_distribution': {k: phases.count(k) for k in set(phases)},
            'state_distribution': {k: states.count(k) for k in set(states)},
            'epochs': [r.get('metadata', {}).get('epoch', '?') for r in results]
        }

    def _print_ranking(self, results: List[Dict]):
        """Log the best checkpoint by delta and alpha."""
        deltas = [(i, r.get('maxwell', {}).get('purity', {}).get('delta', 1.0)) for i, r in enumerate(results)]
        alphas = [(i, r.get('maxwell', {}).get('purity', {}).get('alpha', 0.0)) for i, r in enumerate(results)]
        best_delta_idx = min(deltas, key=lambda x: x[1])[0]
        best_alpha_idx = max(alphas, key=lambda x: x[1])[0]

        def _info(idx):
            r = results[idx]
            ep = r.get('metadata', {}).get('epoch', '?')
            d = r.get('maxwell', {}).get('purity', {}).get('delta', 0)
            a = r.get('maxwell', {}).get('purity', {}).get('alpha', 0)
            ph = r.get('maxwell', {}).get('classification', {}).get('phase', '?')
            st = r.get('hawking', {}).get('diagnostics', {}).get('crystallization_state', '?')
            T = r.get('hawking', {}).get('hawking', {}).get('T_H', 0)
            return f"epoch={ep} delta={d:.6f} alpha={a:.4f} phase={ph} state={st} T_H={T:.4e}"

        self.logger.info("=" * 70)
        self.logger.info("BEST CHECKPOINT RANKING")
        self.logger.info(f"  Best by delta: {_info(best_delta_idx)}")
        self.logger.info(f"  Best by alpha: {_info(best_alpha_idx)}")
        self.logger.info("=" * 70)


def main():
    """Parse arguments and run the combined analysis suite."""
    parser = argparse.ArgumentParser(
        description='Maxwell Field + Hawking Radiation Analysis for Maxwell Spectral Network Checkpoints'
    )
    parser.add_argument('path', nargs='?', default='checkpoints_maxwell_phase3')
    parser.add_argument('--output', '-o', default='maxwell_hawking_analysis')
    parser.add_argument('--grid_size', type=int, default=16)
    parser.add_argument('--hidden_dim', type=int, default=32)
    parser.add_argument('--expansion_dim', type=int, default=64)
    parser.add_argument('--spectral_layers', type=int, default=2)
    parser.add_argument('--imaginary_ratio', type=float, default=0.3)
    parser.add_argument('--lattice_dim', type=int, default=16)
    parser.add_argument('--log_level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    args = parser.parse_args()

    config = AnalysisConfig(
        GRID_SIZE=args.grid_size, HIDDEN_DIM=args.hidden_dim,
        EXPANSION_DIM=args.expansion_dim, NUM_SPECTRAL_LAYERS=args.spectral_layers,
        DEFAULT_IMAGINARY_RATIO=args.imaginary_ratio,
        LATTICE_DIMENSION=args.lattice_dim, LOG_LEVEL=args.log_level
    )

    batch = BatchAnalyzer(config)
    batch.process(args.path, args.output)


if __name__ == "__main__":
    main()
