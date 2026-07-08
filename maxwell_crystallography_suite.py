#!/usr/bin/env python3
"""
maxwell_crystallography_suite.py

Comprehensive crystallographic and physical analysis suite for Maxwell equation
neural network checkpoints.  Integrates Berry phase, MBL analysis, Ricci flow,
control theory, Schrodinger analysis, thermodynamic metrics, and Chapter 10
GOE/GUE spectral universality diagnostics.

The GOE/GUE analysis measures the imaginary-to-real kernel ratio of each
SpectralLayer and evaluates nearest-neighbour spacing P(s), pair correlation
R_2(s), and the Dyson beta index to determine whether the operator sits in the
Gaussian Orthogonal (beta=1) or Gaussian Unitary (beta=2) universality class.

Author: Gris Iscomeback
Email: grisiscomeback@gmail.com
Date: 2026
License: AGPL v3
"""

import argparse
import copy
import glob
import json
import logging
import math
import os
import re
import time
import warnings
from abc import ABC, abstractmethod
from collections import deque
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Tuple, Optional, List, Any, Union, Protocol, runtime_checkable

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from scipy import stats, signal, linalg
from scipy.stats import entropy as scipy_entropy
from scipy.linalg import eigh, expm, eigvals
from scipy.optimize import fsolve
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import eigsh

warnings.filterwarnings('ignore')


@dataclass(frozen=True)
class CrystallographySuiteConfig:
    """Master configuration for the complete Maxwell crystallography suite."""

    GRID_SIZE: int = 16
    HIDDEN_DIM: int = 32
    NUM_SPECTRAL_LAYERS: int = 2
    EXPANSION_DIM: int = 64
    FIELD_COMPONENTS: int = 3

    MAXWELL_C: float = 1.0
    MAXWELL_PERMITTIVITY: float = 1.0
    MAXWELL_PERMEABILITY: float = 1.0
    MAXWELL_CONDUCTIVITY: float = 0.0
    POTENTIAL_DEPTH: float = 5.0
    POTENTIAL_WIDTH: float = 0.3
    NUM_EIGENSTATES: int = 8
    ENERGY_SCALE: float = 1.0
    FIELD_NORM_TARGET: float = 1.0
    HBAR: float = 1e-6
    HBAR_PHYSICAL: float = 1.054571817e-34

    BATCH_SIZE: int = 32
    LEARNING_RATE: float = 0.005
    WEIGHT_DECAY: float = 1e-4
    EPOCHS: int = 5000
    TIME_STEPS: int = 2
    DT: float = 0.01
    TRAIN_RATIO: float = 0.7
    NUM_SAMPLES: int = 200
    GRADIENT_CLIP_NORM: float = 1.0

    LEVEL_SPACING_WIGNER_DYSON: float = 0.5307
    LEVEL_SPACING_POISSON: float = 0.3863
    LEVEL_SPACING_TOLERANCE: float = 0.05
    BRODY_THERMAL: float = 1.0
    BRODY_MBL: float = 0.0
    BRODY_TOLERANCE: float = 0.1
    PR_LOCALIZATION_THRESHOLD: float = 0.8
    PR_DELIMITED_THRESHOLD: float = 0.1
    PR_RENYI_INDEX: int = 2

    ALPHA_CRYSTAL_THRESHOLD: float = 7.0
    ALPHA_PERFECT_CRYSTAL_THRESHOLD: float = 10.0
    DELTA_CRYSTAL_THRESHOLD: float = 0.1
    DELTA_OPTICAL_THRESHOLD: float = 0.01
    DELTA_GLASS_THRESHOLD: float = 0.4
    KAPPA_CRYSTAL_THRESHOLD: float = 1.5
    TEMPERATURE_CRYSTAL_THRESHOLD: float = 1e-9

    TORUS_GRID_SIZE: int = 16
    TOPO_ALIGNMENT_THRESHOLD: float = 0.7
    TOPO_HYSTERESIS_WIDTH: float = 0.1
    TOPO_COUPLING_STRENGTH: float = 0.5
    TOPO_LAMBDA_BASE: float = 1e20
    TOPO_LAMBDA_CRITICAL: float = 1e34
    TOPO_ALIGNMENT_HISTORY_LEN: int = 100
    TOPO_PHASE_SMOOTHING: float = 0.95
    TOPO_LOCALIZATION_LIQUID: float = 0.2
    TOPO_LOCALIZATION_CRYSTAL: float = 1.0
    TOPO_CRYSTALLIZATION_PRESSURE_DECAY: float = 0.999
    TOPO_ENABLED: bool = True

    RICCI_FLOW_TEMPORAL_STEPS: int = 50
    RICCI_FLOW_TIME_STEP_SIZE: float = 0.001
    RICCI_FLOW_REGULARIZATION_ALPHA: float = 0.1
    NECK_EIGENVALUE_RATIO_THRESHOLD: float = 100.0
    CURVATURE_COLLAPSE_ABSOLUTE_THRESHOLD: float = 1e-6
    ENTROPY_SINGULARITY_THRESHOLD: float = 0.05
    RICCI_SCALAR_DIVERGENCE_THRESHOLD: float = 1e6
    RICCI_CURVATURE_SAMPLES: int = 100
    RICCI_MAX_DIMENSION: int = 5000

    POLE_ZERO_TOLERANCE: float = 1e-6
    STABILITY_MARGIN: float = 0.01
    FREQUENCY_SAMPLES: int = 1000
    FREQUENCY_MIN: float = 1e-3
    FREQUENCY_MAX: float = 1e3
    TIME_SAMPLES: int = 500
    TIME_MAX: float = 10.0

    BERRY_PHASE_TOLERANCE: float = 0.1

    GIBBS_T0: float = 1e-3
    GIBBS_C: float = 0.5
    ENTROPY_BINS: int = 50
    PCA_COMPONENTS: int = 3
    ENTROPY_EPS: float = 1e-10
    MIN_VARIANCE_THRESHOLD: float = 1e-8
    EIGENVALUE_TOL: float = 1e-10
    KAPPA_MAX_DIM: int = 10000
    KAPPA_GRADIENT_BATCHES: int = 5

    SPECTRAL_PEAK_LIMIT: int = 20
    SPECTRAL_POWER_LIMIT: int = 100
    PARAM_FLATTEN_LIMIT: int = 2000
    GRADIENT_BUFFER_LIMIT: int = 500
    WEIGHT_METRIC_DIM_LIMIT: int = 256
    HEAT_KERNEL_SPECTRAL_CUTOFF: int = 100
    COMPRESSED_DIMENSION: int = 512
    NORMALIZATION_EPS: float = 1e-8

    CHECKPOINT_INTERVAL_MINUTES: int = 5
    MAX_CHECKPOINTS: int = 10
    CHECKPOINT_LATEST_PATH: str = 'latest.pth'

    KERNEL_IMAGINARY_RATIO_MIN: float = 0.1
    KERNEL_IMAGINARY_RATIO_MAX: float = 0.5
    KERNEL_IMAGINARY_RATIO_OPTIMAL_P_S: float = 0.18
    KERNEL_IMAGINARY_RATIO_OPTIMAL_R2: float = 0.30
    DEFAULT_IMAGINARY_RATIO: float = 0.3

    GOE_GUE_MATRIX_SIZE: int = 256
    GOE_GUE_NUM_MATRICES: int = 10
    GOE_GUE_SPACING_BINS: int = 40
    GOE_GUE_SPACING_RANGE_MAX: float = 4.0
    GOE_GUE_CORRELATION_NUM_POINTS: int = 50
    GOE_GUE_CORRELATION_DELTA: float = 0.2
    GOE_GUE_CORRELATION_S_MIN: float = -3.0
    GOE_GUE_CORRELATION_S_MAX: float = 3.0
    GOE_GUE_SMALL_SPACING_CUTOFF: float = 0.5
    GOE_GUE_SMALL_SPACING_MIN_SAMPLES: int = 5
    GOE_GUE_MIN_SPACINGS_FOR_LOSS: int = 10
    GOE_GUE_DYSON_MIN_SPACINGS: int = 20
    GOE_GUE_CORRELATION_VALID_THRESHOLD: float = 0.1
    GOE_GUE_BETA_CLAMP_MIN: float = 0.5
    GOE_GUE_BETA_CLAMP_MAX: float = 2.5
    GOE_GUE_BETA_DEFAULT: float = 1.5

    DEVICE: str = 'cuda' if torch.cuda.is_available() else 'cpu'
    RANDOM_SEED: int = 42
    LOG_LEVEL: str = 'INFO'
    FIGURE_DPI: int = 300
    SAVE_FORMAT: str = 'png'

    VIZ_COLOR_PRIMARY: str = '#2E86AB'
    VIZ_COLOR_SECONDARY: str = '#A23B72'
    VIZ_COLOR_ACCENT: str = '#06A77D'
    VIZ_COLOR_DANGER: str = '#D62828'
    VIZ_COLOR_WARNING: str = '#F18F01'
    VIZ_BAR_ALPHA: float = 0.7


class LoggerFactory:
    """Factory for creating configured logger instances."""

    @staticmethod
    def create_logger(name: str, level: str = None, config: CrystallographySuiteConfig = None) -> logging.Logger:
        """Create and return a configured logger."""
        logger = logging.getLogger(name)
        effective_level = level or (config.LOG_LEVEL if config else 'INFO')
        logger.setLevel(getattr(logging, effective_level.upper()))
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        return logger


class IMetricCalculator(Protocol):
    """Protocol for metric calculation strategies."""

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute metrics for the given model."""
        ...


class IPhaseDetector(Protocol):
    """Protocol for phase detection strategies."""

    def detect(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        """Detect phase from spectral field."""
        ...


class SpectralLayer(nn.Module):
    """Spectral convolution layer with tuneable imaginary ratio for GOE/GUE control."""

    def __init__(self, channels: int, grid_size: int, config: CrystallographySuiteConfig,
                 imaginary_ratio: float = 0.3):
        """Initialise real and imaginary kernel parameters."""
        super().__init__()
        self.channels = channels
        self.grid_size = grid_size
        self.config = config
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
        kernel_real_exp = kernel_real.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_imag_exp = kernel_imag.unsqueeze(0).unsqueeze(0).squeeze(0)
        kernel_real_interp = F.interpolate(
            kernel_real_exp, size=(freq_h, freq_w), mode='bilinear', align_corners=False
        )
        kernel_imag_interp = F.interpolate(
            kernel_imag_exp, size=(freq_h, freq_w), mode='bilinear', align_corners=False
        )
        real_part = x_fft.real * kernel_real_interp - x_fft.imag * kernel_imag_interp
        imag_part = x_fft.real * kernel_imag_interp + x_fft.imag * kernel_real_interp
        output_fft = torch.complex(real_part, imag_part)
        return torch.fft.irfft2(output_fft, s=(self.grid_size, self.grid_size))

    def get_spectral_operator(self) -> torch.Tensor:
        """Extract (channels x channels) complex Hermitian-like matrix for eigenvalue analysis."""
        kr = self.kernel_real[:, :, 0, 0]
        ki = self.kernel_imag[:, :, 0, 0]
        kr_sym = (kr + kr.T) / 2
        ki_asym = (ki - ki.T) / 2
        return torch.complex(kr_sym, ki_asym * self.imaginary_ratio)

    def get_kernel_ratio(self) -> float:
        """Return the imaginary-to-real kernel norm ratio."""
        real_norm = self.kernel_real.data.norm().item()
        imag_norm = self.kernel_imag.data.norm().item()
        if real_norm < 1e-10:
            return self.imaginary_ratio
        return imag_norm / real_norm


class MaxwellSpectralNetwork(nn.Module):
    """Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz)."""

    def __init__(self, config: CrystallographySuiteConfig, imaginary_ratio: float = 0.3):
        """Build all sub-layers with the given architectural parameters."""
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
            SpectralLayer(config.EXPANSION_DIM, config.GRID_SIZE, config, imaginary_ratio)
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
        for spectral_layer in self.spectral_layers:
            x = F.gelu(spectral_layer(x))
        x = F.gelu(self.contraction_proj(x))
        return self.output_proj(x)

    def get_kernel_ratio(self) -> float:
        """Compute effective imaginary-to-real kernel norm ratio across all layers."""
        real_norms = [layer.kernel_real.data.norm() for layer in self.spectral_layers]
        imag_norms = [layer.kernel_imag.data.norm() for layer in self.spectral_layers]
        total_real = sum(real_norms)
        total_imag = sum(imag_norms)
        if total_real < self.grid_size * 1e-8:
            return self.imaginary_ratio
        return (total_imag / total_real).item()


class GOEGUESpectralAnalyzer:
    """
    Chapter 10 spectral universality analyzer.

    Extracts the spectral operator from each SpectralLayer, computes its
    eigenvalue statistics, and determines proximity to GOE (beta=1) or
    GUE (beta=2) universality via P(s), R_2(s), and the Dyson index.
    """

    def __init__(self, config: CrystallographySuiteConfig):
        """Store configuration reference."""
        self.config = config

    def extract_spectral_operators(self, model: nn.Module) -> List[torch.Tensor]:
        """Return the complex spectral operator from every SpectralLayer in the model."""
        operators = []
        if hasattr(model, 'spectral_layers'):
            for layer in model.spectral_layers:
                if hasattr(layer, 'get_spectral_operator'):
                    operators.append(layer.get_spectral_operator())
        return operators

    def compute_eigenvalue_spacing(self, eigenvalues: np.ndarray) -> np.ndarray:
        """Unfold eigenvalues and return normalised nearest-neighbour spacings."""
        sorted_eigs = np.sort(eigenvalues.real)
        n = len(sorted_eigs)
        if n < 3:
            return np.array([1.0])
        unfolded = np.arange(1, n + 1, dtype=float)
        coeffs = np.polyfit(sorted_eigs, unfolded, 3)
        unfolded_eigs = np.polyval(coeffs, sorted_eigs)
        spacings = np.diff(unfolded_eigs)
        mean_spacing = np.mean(spacings) if len(spacings) > 0 else 1.0
        if mean_spacing > 1e-10:
            spacings = spacings / mean_spacing
        return spacings

    def compute_spacing_distribution_loss(self, spacings: np.ndarray, target: str = 'gue') -> float:
        """MSE between empirical P(s) and Wigner surmise for GOE or GUE."""
        if len(spacings) < self.config.GOE_GUE_MIN_SPACINGS_FOR_LOSS:
            return float('inf')
        empirical, bin_edges = np.histogram(
            spacings, bins=self.config.GOE_GUE_SPACING_BINS,
            range=(0, self.config.GOE_GUE_SPACING_RANGE_MAX), density=True
        )
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        if target == 'goe':
            theoretical = (np.pi / 2) * bin_centers * np.exp(-np.pi * bin_centers ** 2 / 4)
        elif target == 'gue':
            theoretical = (32 / np.pi ** 2) * bin_centers ** 2 * np.exp(-4 * bin_centers ** 2 / np.pi)
        else:
            theoretical = np.ones_like(bin_centers)
        return float(np.mean((empirical - theoretical) ** 2))

    def compute_dyson_index(self, spacings: np.ndarray) -> float:
        """Estimate the Dyson beta from small-spacing power-law P(s) ~ s^beta."""
        if len(spacings) < self.config.GOE_GUE_DYSON_MIN_SPACINGS:
            return self.config.GOE_GUE_BETA_DEFAULT
        small_spacings = spacings[spacings < self.config.GOE_GUE_SMALL_SPACING_CUTOFF]
        if len(small_spacings) < self.config.GOE_GUE_SMALL_SPACING_MIN_SAMPLES:
            return self.config.GOE_GUE_BETA_DEFAULT
        log_s = np.log(small_spacings + 1e-10)
        log_p = np.log(
            np.histogram(spacings, bins=50, range=(0, self.config.GOE_GUE_SMALL_SPACING_CUTOFF), density=True)[0] + 1e-10
        )
        min_len = min(len(log_s), len(log_p))
        if min_len < 2:
            return self.config.GOE_GUE_BETA_DEFAULT
        slope, _ = np.polyfit(log_s[:min_len], log_p[:min_len], 1)
        return max(self.config.GOE_GUE_BETA_CLAMP_MIN, min(self.config.GOE_GUE_BETA_CLAMP_MAX, slope))

    def compute_pair_correlation(self, eigenvalues: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Two-level correlation function R_2(s)."""
        sorted_eigs = np.sort(eigenvalues.real)
        n = len(sorted_eigs)
        num_points = self.config.GOE_GUE_CORRELATION_NUM_POINTS
        s_min = self.config.GOE_GUE_CORRELATION_S_MIN
        s_max = self.config.GOE_GUE_CORRELATION_S_MAX
        if n < 10:
            return np.linspace(s_min, s_max, num_points), np.ones(num_points)
        unfolded = np.arange(1, n + 1, dtype=float)
        coeffs = np.polyfit(sorted_eigs, unfolded, 3)
        unfolded_eigs = np.polyval(coeffs, sorted_eigs)
        s_values = np.linspace(s_min, s_max, num_points)
        R2_empirical = np.zeros(num_points)
        delta = self.config.GOE_GUE_CORRELATION_DELTA
        diffs = np.diff(unfolded_eigs)
        for idx, s in enumerate(s_values):
            count = np.sum(np.abs(diffs - s) < delta)
            R2_empirical[idx] = count / (n * 2 * delta)
        return s_values, R2_empirical

    def compute_correlation_loss(self, eigenvalues: np.ndarray, target: str = 'gue') -> float:
        """MSE between empirical R_2(s) and analytical prediction."""
        s_values, R2_empirical = self.compute_pair_correlation(eigenvalues)
        s_safe = np.where(np.abs(s_values) < 1e-8, 1e-8, s_values)
        if target == 'gue':
            R2_theoretical = 1 - (np.sin(np.pi * s_safe) / (np.pi * s_safe)) ** 2
        elif target == 'goe':
            R2_theoretical = 1 - (np.sin(np.pi * s_safe / 2) / (np.pi * s_safe / 2)) ** 2
        else:
            R2_theoretical = np.ones_like(s_values)
        valid_mask = np.abs(s_values) > self.config.GOE_GUE_CORRELATION_VALID_THRESHOLD
        if np.sum(valid_mask) > 0:
            return float(np.mean((R2_empirical[valid_mask] - R2_theoretical[valid_mask]) ** 2))
        return float(np.mean((R2_empirical - R2_theoretical) ** 2))

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Run full GOE/GUE spectral analysis on all spectral layers."""
        operators = self.extract_spectral_operators(model)
        if not operators:
            return self._empty_results()

        all_eigenvalues = []
        all_spacings = []
        per_layer_ratios = []

        for op in operators:
            try:
                eigs = torch.linalg.eigvals(op).cpu().numpy()
                all_eigenvalues.append(eigs)
                spacings = self.compute_eigenvalue_spacing(eigs)
                all_spacings.extend(spacings.tolist())
            except Exception:
                continue

        if hasattr(model, 'spectral_layers'):
            for layer in model.spectral_layers:
                if hasattr(layer, 'get_kernel_ratio'):
                    per_layer_ratios.append(layer.get_kernel_ratio())

        if not all_eigenvalues:
            return self._empty_results()

        all_spacings_arr = np.array(all_spacings)
        combined_eigs = np.concatenate([e.real for e in all_eigenvalues])

        p_s_loss_goe = self.compute_spacing_distribution_loss(all_spacings_arr, 'goe')
        p_s_loss_gue = self.compute_spacing_distribution_loss(all_spacings_arr, 'gue')
        r2_loss_goe = self.compute_correlation_loss(combined_eigs, 'goe')
        r2_loss_gue = self.compute_correlation_loss(combined_eigs, 'gue')
        beta_estimate = self.compute_dyson_index(all_spacings_arr)

        goe_total = p_s_loss_goe + r2_loss_goe
        gue_total = p_s_loss_gue + r2_loss_gue
        ensemble_ratio = gue_total / (goe_total + 1e-10)

        if gue_total < goe_total:
            dominant_ensemble = "GUE"
        elif goe_total < gue_total:
            dominant_ensemble = "GOE"
        else:
            dominant_ensemble = "Intermediate"

        global_kernel_ratio = model.get_kernel_ratio() if hasattr(model, 'get_kernel_ratio') else 0.0
        imaginary_ratio = model.imaginary_ratio if hasattr(model, 'imaginary_ratio') else self.config.DEFAULT_IMAGINARY_RATIO

        beta_distance_goe = abs(beta_estimate - 1.0)
        beta_distance_gue = abs(beta_estimate - 2.0)
        universality_interpolation = beta_distance_goe / (beta_distance_goe + beta_distance_gue + 1e-10)

        return {
            'p_s_loss_goe': p_s_loss_goe,
            'p_s_loss_gue': p_s_loss_gue,
            'r2_loss_goe': r2_loss_goe,
            'r2_loss_gue': r2_loss_gue,
            'beta_estimate': beta_estimate,
            'ensemble_ratio': ensemble_ratio,
            'dominant_ensemble': dominant_ensemble,
            'global_kernel_ratio': global_kernel_ratio,
            'imaginary_ratio': imaginary_ratio,
            'per_layer_kernel_ratios': per_layer_ratios,
            'universality_interpolation': universality_interpolation,
            'beta_distance_goe': beta_distance_goe,
            'beta_distance_gue': beta_distance_gue,
            'num_operators_analyzed': len(operators),
            'total_eigenvalues': len(combined_eigs),
            'total_spacings': len(all_spacings_arr)
        }

    @staticmethod
    def _empty_results() -> Dict[str, Any]:
        """Return zero-valued results when no spectral layers are found."""
        return {
            'p_s_loss_goe': float('inf'), 'p_s_loss_gue': float('inf'),
            'r2_loss_goe': float('inf'), 'r2_loss_gue': float('inf'),
            'beta_estimate': 1.5, 'ensemble_ratio': 1.0,
            'dominant_ensemble': 'Unknown',
            'global_kernel_ratio': 0.0, 'imaginary_ratio': 0.0,
            'per_layer_kernel_ratios': [],
            'universality_interpolation': 0.5,
            'beta_distance_goe': 0.5, 'beta_distance_gue': 0.5,
            'num_operators_analyzed': 0, 'total_eigenvalues': 0,
            'total_spacings': 0
        }


class WeightIntegrityCalculator:
    """Detect NaN and Inf corruption in model parameters."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Return integrity report."""
        has_nan = has_inf = False
        total_params = nan_count = inf_count = 0
        for param in model.parameters():
            data = param.data
            numel = data.numel()
            total_params += numel
            n_nan = torch.isnan(data).sum().item()
            n_inf = torch.isinf(data).sum().item()
            if n_nan > 0:
                has_nan = True
                nan_count += n_nan
            if n_inf > 0:
                has_inf = True
                inf_count += n_inf
        corruption_ratio = (nan_count + inf_count) / total_params if total_params > 0 else 0.0
        return {
            'is_valid': not (has_nan or has_inf), 'has_nan': has_nan, 'has_inf': has_inf,
            'total_params': total_params, 'nan_count': nan_count, 'inf_count': inf_count,
            'corruption_ratio': corruption_ratio
        }


class DiscretizationCalculator:
    """Delta, alpha purity, and spectral entropy of the weight distribution."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute delta, alpha, spectral entropy, and per-layer deltas."""
        margins = []
        all_params = []
        layer_deltas = {}
        for name, param in model.named_parameters():
            if param.numel() > 0:
                p_data = param.data.detach()
                all_params.append(p_data.flatten())
                margin = (p_data - p_data.round()).abs().max().item()
                margins.append(margin)
                layer_deltas[name] = margin
        delta = max(margins) if margins else 0.0
        alpha = -np.log(delta + self.config.ENTROPY_EPS) if delta > 0 else 20.0
        flat_params = torch.cat(all_params)[:self.config.PARAM_FLATTEN_LIMIT]
        spectral_entropy = self._compute_spectral_entropy(flat_params)
        return {
            'delta': delta, 'alpha': alpha, 'spectral_entropy': spectral_entropy,
            'is_discrete': delta < self.config.DELTA_CRYSTAL_THRESHOLD,
            'layer_deltas': layer_deltas
        }

    def _compute_spectral_entropy(self, weights: torch.Tensor) -> float:
        """Shannon entropy of the normalised power spectrum of concatenated weights."""
        if weights.numel() == 0:
            return 0.0
        w = weights.detach().cpu()
        fft_spectrum = torch.fft.fft(w)
        power_spectrum = torch.abs(fft_spectrum) ** 2
        ps_normalized = power_spectrum / (torch.sum(power_spectrum) + 1e-10)
        ps_normalized = ps_normalized[ps_normalized > 1e-10]
        if len(ps_normalized) == 0:
            return 0.0
        return float(-torch.sum(ps_normalized * torch.log(ps_normalized + 1e-10)).item())


class SpectralGeometryCalculator:
    """Spectral gap, effective dimension, participation ratio, and level-spacing ratio."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute spectral geometry observables from weight outer product."""
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        all_weights = all_weights[:self.config.PARAM_FLATTEN_LIMIT].cpu().numpy()
        n = len(all_weights)
        outer_product = np.outer(all_weights, all_weights) / n
        outer_product += np.eye(n) * self.config.EIGENVALUE_TOL
        try:
            eigenvalues = eigh(outer_product, eigvals_only=True)
            eigenvalues = np.sort(eigenvalues)[::-1]
            effective_dim = np.sum(eigenvalues > self.config.EIGENVALUE_TOL)
            spectral_gap = eigenvalues[0] - eigenvalues[1] if len(eigenvalues) > 1 else 0.0
            participation_ratio = (np.sum(eigenvalues) ** 2) / (np.sum(eigenvalues ** 2) + 1e-10)
            level_spacing = np.diff(eigenvalues)
            level_spacing_ratio = self._compute_level_spacing_ratio(level_spacing)
            return {
                'spectral_gap': float(spectral_gap), 'effective_dimension': int(effective_dim),
                'participation_ratio': float(participation_ratio),
                'level_spacing_ratio': float(level_spacing_ratio),
                'largest_eigenvalue': float(eigenvalues[0]),
                'smallest_eigenvalue': float(eigenvalues[-1])
            }
        except Exception as e:
            return {
                'spectral_gap': 0.0, 'effective_dimension': 0, 'participation_ratio': 0.0,
                'level_spacing_ratio': 0.0, 'largest_eigenvalue': 0.0,
                'smallest_eigenvalue': 0.0, 'error': str(e)
            }

    def _compute_level_spacing_ratio(self, spacings: np.ndarray) -> float:
        """Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1})."""
        if len(spacings) < 2:
            return 0.0
        ratios = []
        for i in range(len(spacings) - 1):
            s1, s2 = abs(spacings[i]), abs(spacings[i + 1])
            if s1 > 1e-15 and s2 > 1e-15:
                ratios.append(min(s1, s2) / max(s1, s2))
        return float(np.mean(ratios)) if ratios else 0.0


class RicciCurvatureCalculator:
    """Ricci scalar and mean sectional curvature of the weight manifold."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute Ricci scalar and sectional curvatures from weight metric."""
        all_weights = torch.cat([p.detach().flatten() for p in model.parameters()])
        n = min(len(all_weights), self.config.PARAM_FLATTEN_LIMIT)
        w = all_weights[:n].cpu().numpy()
        metric_tensor = np.outer(w, w) / n
        metric_tensor += np.eye(n) * self.config.EIGENVALUE_TOL
        ricci_scalar = self._compute_ricci_scalar(metric_tensor)
        sectional_curvatures = self._estimate_sectional_curvatures(metric_tensor)
        return {
            'ricci_scalar': float(ricci_scalar),
            'mean_sectional_curvature': float(np.mean(sectional_curvatures)),
            'curvature_variance': float(np.var(sectional_curvatures))
        }

    def _compute_ricci_scalar(self, metric: np.ndarray) -> float:
        """Ricci scalar via inverse eigenvalue sum."""
        eigenvalues = eigh(metric, eigvals_only=True)
        eigenvalues = eigenvalues[eigenvalues > self.config.EIGENVALUE_TOL]
        n = len(eigenvalues)
        if n < 2:
            return 0.0
        return float(n * np.sum(1.0 / eigenvalues))

    def _estimate_sectional_curvatures(self, metric: np.ndarray) -> np.ndarray:
        """Sample 2x2 sub-block determinants as sectional curvature proxies."""
        curvatures = []
        n = metric.shape[0]
        samples = min(self.config.RICCI_CURVATURE_SAMPLES, n * (n - 1) // 2)
        for _ in range(samples):
            i, j = np.random.choice(n, 2, replace=False)
            block = metric[np.ix_([i, j], [i, j])]
            det = np.linalg.det(block)
            if det > self.config.EIGENVALUE_TOL:
                curvatures.append(1.0 / det)
        return np.array(curvatures) if curvatures else np.array([0.0])


class BerryPhaseCalculator:
    """Berry phase from training checkpoint trajectory."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise logger."""
        self.config = config
        self.logger = LoggerFactory.create_logger("BerryPhaseCalculator", config=config)

    def load_checkpoints(self, checkpoint_dir: str) -> List[Dict[str, Any]]:
        """Load all .pth files sorted by epoch."""
        pattern = os.path.join(checkpoint_dir, "*.pth")
        files = sorted(glob.glob(pattern), key=self._extract_epoch)
        checkpoints = []
        for f in files:
            try:
                ckpt = torch.load(f, map_location='cpu', weights_only=False)
                checkpoints.append({
                    'path': f, 'epoch': self._extract_epoch(f),
                    'state_dict': ckpt.get('model_state_dict', ckpt),
                    'metrics': ckpt.get('metrics', {})
                })
            except Exception as e:
                self.logger.warning(f"Could not load {f}: {e}")
        return checkpoints

    def _extract_epoch(self, filepath: str) -> int:
        """Parse epoch number from filename."""
        match = re.search(r'epoch[_]?(\d+)', filepath)
        return int(match.group(1)) if match else 0

    def flatten_kernel_params(self, state_dict: Dict) -> Optional[torch.Tensor]:
        """Concatenate all spectral layer kernels into a single complex vector."""
        kernels = []
        layer_indices = set()
        for key in state_dict.keys():
            if 'spectral_layers' in key:
                parts = key.split('.')
                if len(parts) >= 2:
                    try:
                        layer_indices.add(int(parts[1]))
                    except ValueError:
                        pass
        for idx in sorted(layer_indices):
            real_key = f'spectral_layers.{idx}.kernel_real'
            imag_key = f'spectral_layers.{idx}.kernel_imag'
            if real_key in state_dict and imag_key in state_dict:
                kernels.append(torch.complex(state_dict[real_key], state_dict[imag_key]).flatten())
        return torch.cat(kernels) if kernels else None

    def compute_berry_connection_discrete(self, theta_prev: torch.Tensor, theta_curr: torch.Tensor) -> float:
        """Discrete Berry connection between consecutive parameter snapshots."""
        if theta_prev is None or theta_curr is None:
            return 0.0
        theta_prev_norm = theta_prev / (torch.norm(theta_prev) + 1e-10)
        theta_curr_norm = theta_curr / (torch.norm(theta_curr) + 1e-10)
        overlap = torch.sum(torch.conj(theta_prev_norm) * theta_curr_norm)
        if torch.abs(overlap) < 1e-10:
            return 0.0
        return torch.angle(overlap).item()

    def calculate_berry_phase(self, checkpoint_dir: str) -> Dict[str, Any]:
        """Compute total Berry phase, winding number, and cumulative trajectory."""
        checkpoints = self.load_checkpoints(checkpoint_dir)
        if len(checkpoints) < 2:
            return {'error': f'Need at least 2 checkpoints, found {len(checkpoints)}'}
        kernels = []
        epochs = []
        for ckpt in checkpoints:
            kernels.append(self.flatten_kernel_params(ckpt['state_dict']))
            epochs.append(ckpt['epoch'])
        berry_phases = []
        for i in range(1, len(kernels)):
            if kernels[i - 1] is not None and kernels[i] is not None:
                berry_phases.append(self.compute_berry_connection_discrete(kernels[i - 1], kernels[i]))
            else:
                berry_phases.append(0.0)
        cumulative_phase = np.cumsum(berry_phases)
        total_phase = cumulative_phase[-1] if len(cumulative_phase) > 0 else 0.0
        phase_mod_2pi = total_phase % (2 * np.pi)
        if phase_mod_2pi > np.pi:
            phase_mod_2pi -= 2 * np.pi
        winding_number = int(round(total_phase / (2 * np.pi)))
        return {
            'total_berry_phase': total_phase, 'berry_phase_mod_2pi': phase_mod_2pi,
            'winding_number': winding_number, 'num_checkpoints': len(checkpoints),
            'epochs': epochs
        }


class ControlSystemAnalyzer:
    """Control theory stability analysis for neural network dynamics."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def extract_state_space(self, model: nn.Module) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Extract a composite state-space (A, B, C, D) from weight matrices."""
        all_weights = []
        for name, param in model.named_parameters():
            if 'weight' in name and param.dim() >= 2:
                all_weights.append(param.data.cpu().numpy())
        if not all_weights:
            n = 10
            return np.eye(n), np.random.randn(n, 1), np.random.randn(1, n), np.zeros((1, 1))
        A_blocks = []
        for w in all_weights:
            if w.ndim > 2:
                w = w.reshape(w.shape[0], -1)
            n = min(w.shape[0], w.shape[1])
            if n > 0:
                A_blocks.append(w[:n, :n])
        if not A_blocks:
            n = 10
            return np.eye(n), np.random.randn(n, 1), np.random.randn(1, n), np.zeros((1, 1))
        sizes = [min(b.shape[0], b.shape[1]) for b in A_blocks]
        target_dim = max(int(np.median(sizes)), 2)
        A_composite = np.zeros((target_dim, target_dim))
        for b in A_blocks:
            n = min(b.shape[0], b.shape[1], target_dim)
            if n > 0:
                A_composite[:n, :n] += b[:n, :n]
        A = A_composite / len(A_blocks) + np.eye(target_dim) * 0.01
        n_states = A.shape[0]
        return A, np.random.randn(n_states, 1) * 0.01, np.random.randn(1, n_states) * 0.01, np.zeros((1, 1))

    def analyze_stability(self, A: np.ndarray) -> Dict[str, Any]:
        """Eigenvalue stability analysis of the state matrix."""
        try:
            eigenvalues = np.linalg.eigvals(A)
            real_parts = np.real(eigenvalues)
            is_stable = bool(np.all(real_parts < -self.config.STABILITY_MARGIN))
            stability_margin = float(-np.max(real_parts)) if len(real_parts) > 0 else float('inf')
            return {
                'is_stable': is_stable, 'stability_margin': stability_margin,
                'eigenvalues': [complex(e) for e in eigenvalues[:10]],
                'dominant_pole': complex(eigenvalues[np.argmax(real_parts)]) if len(eigenvalues) > 0 else None
            }
        except Exception as e:
            return {'is_stable': False, 'error': str(e)}

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Run full control-theory analysis."""
        A, B, C, D = self.extract_state_space(model)
        return {'system_dimension': A.shape[0], 'stability_analysis': self.analyze_stability(A)}


class ThermodynamicCalculator:
    """Gibbs free energy, critical temperature, and phase classification."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute thermodynamic potentials from crystallographic observables."""
        delta = kwargs.get('delta', 1.0)
        alpha = kwargs.get('alpha', 0.0)
        kappa = kwargs.get('kappa', 1.0)
        t_eff = kwargs.get('effective_temperature', 1.0)
        gibbs = delta - (t_eff * (-alpha)) if t_eff > 0 else delta
        T_critical = self.config.GIBBS_T0 * np.exp(-self.config.GIBBS_C * alpha)
        phase_stability = "stable" if t_eff < T_critical else "unstable"
        return {
            'gibbs_free_energy': float(gibbs), 'entropy_proxy': float(-alpha),
            'critical_temperature_estimate': float(T_critical),
            'effective_temperature': float(t_eff),
            'phase_stability': phase_stability,
            'phase_type': self._classify_phase(delta, kappa, t_eff, alpha)
        }

    def _classify_phase(self, delta: float, kappa: float, temp: float, alpha: float) -> str:
        """Classify the thermodynamic phase of the model."""
        if delta < self.config.DELTA_CRYSTAL_THRESHOLD and kappa < self.config.KAPPA_CRYSTAL_THRESHOLD and temp < self.config.TEMPERATURE_CRYSTAL_THRESHOLD:
            return "Perfect Crystal"
        if delta < self.config.DELTA_CRYSTAL_THRESHOLD and kappa >= self.config.KAPPA_CRYSTAL_THRESHOLD:
            return "Polycrystalline"
        if delta >= self.config.DELTA_GLASS_THRESHOLD and temp < self.config.TEMPERATURE_CRYSTAL_THRESHOLD:
            return "Cold Glass"
        if kappa > 1e6:
            return "Amorphous Glass"
        if alpha > self.config.ALPHA_CRYSTAL_THRESHOLD:
            return "Topological Insulator"
        return "Functional Glass"


class FullFourierAnalyzer:
    """Complete 2D Fourier analysis with spectral concentration and resonance metrics."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Precompute wavenumber grids."""
        self.config = config
        self.grid_size = config.TORUS_GRID_SIZE
        kx = torch.fft.fftfreq(self.grid_size) * 2 * np.pi
        ky = torch.fft.fftfreq(self.grid_size) * 2 * np.pi
        self.KX, self.KY = torch.meshgrid(kx, ky, indexing='ij')
        self.K_MAG = torch.sqrt(self.KX ** 2 + self.KY ** 2)

    def compute_full_spectrum(self, spectral_field: torch.Tensor) -> Dict[str, torch.Tensor]:
        """Return magnitude, phase, power, and derived statistics."""
        if spectral_field.dim() == 3:
            spectral_field = spectral_field.unsqueeze(0)
        fft_2d = torch.fft.fft2(spectral_field, dim=(-2, -1))
        fft_shifted = torch.fft.fftshift(fft_2d, dim=(-2, -1))
        magnitude = torch.abs(fft_shifted)
        phase = torch.angle(fft_shifted)
        power_spectrum = magnitude ** 2
        power_spectrum_sum = power_spectrum.sum(dim=(-2, -1), keepdim=True) + 1e-10
        total_power = power_spectrum.sum(dim=(-2, -1))
        spectral_concentration = (power_spectrum.max(dim=-1)[0].max(dim=-1)[0]) / (total_power + 1e-10)
        return {
            'fft_2d': fft_shifted, 'magnitude': magnitude, 'phase': phase,
            'power_spectrum': power_spectrum,
            'power_normalized': power_spectrum / power_spectrum_sum,
            'spectral_concentration': spectral_concentration,
            'total_power': total_power
        }

    def compute_resonance_metrics(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        """Aggregate spectral concentration into a resonance score."""
        spectrum = self.compute_full_spectrum(spectral_field)
        spectral_conc = spectrum['spectral_concentration'].mean().item()
        return {
            'spectral_concentration': spectral_conc,
            'resonance_score': float(spectral_conc),
            'total_power': float(spectrum['total_power'].mean().item())
        }


class FourierMassCenterAnalyzer:
    """Centre-of-mass in Fourier space for topological phase detection."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise wavenumber grids and sub-analyzers."""
        self.config = config
        self.grid_size = config.TORUS_GRID_SIZE
        self.full_fourier = FullFourierAnalyzer(config)
        kx = torch.fft.fftfreq(config.TORUS_GRID_SIZE) * 2 * np.pi
        ky = torch.fft.fftfreq(config.TORUS_GRID_SIZE) * 2 * np.pi
        self.KX, self.KY = torch.meshgrid(kx, ky, indexing='ij')

    def compute_mass_center(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        """Return centre-of-mass coordinates and resonance diagnostics."""
        if spectral_field.dim() == 3:
            spectral_field = spectral_field.unsqueeze(0)
        B, C, H, W = spectral_field.shape
        device = spectral_field.device
        kx = self.KX.to(device)
        ky = self.KY.to(device)
        if H != self.grid_size or W != self.grid_size:
            kx = F.interpolate(kx.unsqueeze(0).unsqueeze(0).float(), size=(H, W), mode='bilinear', align_corners=False).squeeze(0).squeeze(0)
            ky = F.interpolate(ky.unsqueeze(0).unsqueeze(0).float(), size=(H, W), mode='bilinear', align_corners=False).squeeze(0).squeeze(0)
        density = torch.abs(spectral_field) ** 2
        density = density.mean(dim=1)
        total_mass = density.sum(dim=(-2, -1), keepdim=True) + 1e-10
        R_x = (kx * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        R_y = (ky * density).sum(dim=(-2, -1)) / total_mass.squeeze(-1).squeeze(-1)
        resonance = self.full_fourier.compute_resonance_metrics(spectral_field)
        return {
            'R_cm': torch.stack([R_x, R_y], dim=-1),
            'R_cm_x': float(R_x.mean().item()), 'R_cm_y': float(R_y.mean().item()),
            'total_mass': total_mass.squeeze(),
            'resonance_score': resonance['resonance_score'],
            'spectral_concentration': resonance['spectral_concentration']
        }


class TopologicalPhaseDetector:
    """Hysteretic phase detector combining alignment and resonance signals."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise history buffers."""
        self.config = config
        self.mass_analyzer = FourierMassCenterAnalyzer(config)
        self.phase_state = 0.0
        self.alignment_history = np.zeros(config.TOPO_ALIGNMENT_HISTORY_LEN)
        self.history_ptr = 0

    def detect(self, spectral_field: torch.Tensor) -> Dict[str, Any]:
        """Full topological phase detection returning diagnostic dict."""
        mass_analysis = self.mass_analyzer.compute_mass_center(spectral_field)
        R_cm = mass_analysis['R_cm']
        alignment = R_cm[..., 0] < -0.5
        resonance_score = mass_analysis['resonance_score']
        alignment_val = alignment.float().mean().item() if alignment.dim() > 0 else alignment.float().item()
        self.alignment_history[self.history_ptr] = alignment_val
        self.history_ptr = (self.history_ptr + 1) % len(self.alignment_history)
        is_aligned = float(alignment_val > self.config.TOPO_ALIGNMENT_THRESHOLD)
        alpha = self.config.TOPO_PHASE_SMOOTHING
        self.phase_state = alpha * self.phase_state + (1 - alpha) * is_aligned
        return {
            'R_cm': R_cm.detach(),
            'R_cm_x': mass_analysis['R_cm_x'], 'R_cm_y': mass_analysis['R_cm_y'],
            'alignment_score': float(alignment_val),
            'phase_state': float(self.phase_state),
            'is_crystalline': float(self.phase_state > 0.7),
            'resonance_score': float(resonance_score),
            'spectral_concentration': mass_analysis['spectral_concentration']
        }


class SpectralFieldExtractor:
    """Extract spectral weight tensors from SpectralLayer modules."""

    @staticmethod
    def extract(model: nn.Module, grid_size: int = 16) -> Optional[torch.Tensor]:
        """Return the mean complex spectral kernel across all spectral layers."""
        if not hasattr(model, 'spectral_layers'):
            return None
        spectral_weights = []
        for layer in model.spectral_layers:
            if hasattr(layer, 'kernel_real') and hasattr(layer, 'kernel_imag'):
                kr_avg = layer.kernel_real.data.mean(dim=0)
                ki_avg = layer.kernel_imag.data.mean(dim=0)
                spectral_weights.append(torch.complex(kr_avg, ki_avg))
        if not spectral_weights:
            return None
        return torch.stack(spectral_weights).mean(dim=0)


class TopologicalMetricsCalculator:
    """Topological metrics from model spectral fields."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise sub-components."""
        self.config = config
        self.phase_detector = TopologicalPhaseDetector(config)
        self.field_extractor = SpectralFieldExtractor()

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Run topological detection and return metrics dict."""
        if not self.config.TOPO_ENABLED:
            return self._empty_metrics()
        spectral_field = self.field_extractor.extract(model, self.config.GRID_SIZE)
        if spectral_field is None:
            return self._empty_metrics()
        phase_info = self.phase_detector.detect(spectral_field)
        return {
            'topo_R_cm_x': phase_info['R_cm_x'], 'topo_R_cm_y': phase_info['R_cm_y'],
            'topo_phase_state': phase_info['phase_state'],
            'topo_is_crystalline': phase_info['is_crystalline'],
            'topo_alignment_score': phase_info['alignment_score'],
            'topo_resonance_score': phase_info['resonance_score'],
            'topo_spectral_concentration': phase_info['spectral_concentration']
        }

    @staticmethod
    def _empty_metrics() -> Dict[str, Any]:
        """Zero-valued metrics when analysis is disabled or unavailable."""
        return {
            'topo_R_cm_x': 0.0, 'topo_R_cm_y': 0.0, 'topo_phase_state': 0.0,
            'topo_is_crystalline': 0.0, 'topo_alignment_score': 0.0,
            'topo_resonance_score': 0.0, 'topo_spectral_concentration': 0.0
        }


class GradientDynamicsCalculator:
    """Gradient covariance kappa and effective temperature."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute kappa, T_eff, and gradient variance from validation data."""
        val_x = kwargs.get('val_x')
        val_y = kwargs.get('val_y')
        if val_x is None or val_y is None:
            return {'kappa': float('inf'), 'effective_temperature': 0.0, 'gradient_variance': 0.0}
        model.train()
        grads = []
        for i in range(self.config.KAPPA_GRADIENT_BATCHES):
            try:
                model.zero_grad()
                outputs = model(val_x)
                loss = F.mse_loss(outputs, val_y)
                loss.backward()
                grad_list = []
                for p in model.parameters():
                    if p.grad is not None and p.grad.numel() > 0:
                        grad_list.append(p.grad.flatten())
                if grad_list:
                    grad_vector = torch.cat(grad_list)
                    if torch.isfinite(grad_vector).all():
                        grads.append(grad_vector.detach().clone())
            except Exception:
                continue
        model.eval()
        if len(grads) < 2:
            return {'kappa': float('inf'), 'effective_temperature': 0.0, 'gradient_variance': 0.0}
        grads_tensor = torch.stack(grads)
        n_samples, n_dims = grads_tensor.shape
        if n_dims > self.config.KAPPA_MAX_DIM:
            indices = torch.randperm(n_dims, device=grads_tensor.device)[:self.config.KAPPA_MAX_DIM]
            grads_tensor = grads_tensor[:, indices]
        try:
            if n_samples < grads_tensor.shape[1]:
                gram = torch.mm(grads_tensor, grads_tensor.t()) / max(n_samples - 1, 1)
                eigenvals = torch.linalg.eigvalsh(gram)
            else:
                cov = torch.cov(grads_tensor.t())
                eigenvals = torch.linalg.eigvalsh(cov).real
            eigenvals = eigenvals[eigenvals > self.config.EIGENVALUE_TOL]
            if len(eigenvals) == 0:
                return {'kappa': float('inf'), 'effective_temperature': 0.0, 'gradient_variance': 0.0}
            kappa = (eigenvals.max() / eigenvals.min()).item()
            second_moment = torch.mean(torch.norm(grads_tensor, dim=1) ** 2)
            first_moment_sq = torch.norm(torch.mean(grads_tensor, dim=0)) ** 2
            variance = second_moment - first_moment_sq
            temperature = float(variance / (2.0 * grads_tensor.shape[1]))
            return {'kappa': kappa, 'effective_temperature': temperature, 'gradient_variance': float(variance)}
        except Exception:
            return {'kappa': float('inf'), 'effective_temperature': 0.0, 'gradient_variance': 0.0}


class SchrodingerAnalyzer:
    """Quantum mechanical analysis via Johnson-Lindenstrauss compressed wavefunction."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise projection parameters."""
        self.config = config
        self.target_dim = config.COMPRESSED_DIMENSION
        self.projection_matrix = None

    def extract_compressed_wavefunction(self, model: nn.Module) -> torch.Tensor:
        """Project the full parameter vector to a fixed-dimension wavefunction."""
        all_params = []
        for name, param in model.named_parameters():
            if param.numel() > 0:
                all_params.append(param.data.flatten())
        full_vector = torch.cat(all_params)
        total_params = full_vector.numel()
        if total_params <= self.target_dim:
            if len(full_vector) < self.target_dim:
                padding = torch.zeros(self.target_dim - len(full_vector), dtype=full_vector.dtype, device=full_vector.device)
                full_vector = torch.cat([full_vector, padding])
            return full_vector[:self.target_dim]
        return self._compress_johnson_lindenstrauss(full_vector)

    def _compress_johnson_lindenstrauss(self, vector: torch.Tensor) -> torch.Tensor:
        """Random projection preserving pairwise distances."""
        if self.projection_matrix is None or self.projection_matrix.shape[1] != len(vector):
            self.projection_matrix = torch.randn(
                self.target_dim, len(vector), device=vector.device, dtype=torch.float32
            ) / np.sqrt(self.target_dim)
        return torch.matmul(self.projection_matrix, vector.float())

    def compute(self, model: nn.Module, **kwargs) -> Dict[str, Any]:
        """Compute wavefunction entropy, participation ratio, and quantum coherence."""
        wf = self.extract_compressed_wavefunction(model)
        prob = torch.abs(wf) ** 2
        prob = prob / (torch.sum(prob) + 1e-10)
        entropy = -torch.sum(prob * torch.log(prob + 1e-10)).item()
        pr = 1.0 / torch.sum(prob ** 2).item()
        coherence = torch.sum(torch.abs(torch.outer(wf, wf.conj()))).item() - torch.sum(torch.abs(wf) ** 2).item()
        return {
            'wavefunction_entropy': entropy, 'participation_ratio': pr,
            'quantum_coherence': coherence, 'compressed_dimension': len(wf)
        }


class ComprehensiveVisualizer:
    """Generate multi-panel analysis figures for each checkpoint."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Store config reference."""
        self.config = config

    def visualize_checkpoint_analysis(self, results: Dict[str, Any], output_path: str):
        """Render the full 5x4 analysis dashboard to a file."""
        fig = plt.figure(figsize=(24, 20), dpi=self.config.FIGURE_DPI)
        gs = GridSpec(5, 4, figure=fig, hspace=0.35, wspace=0.35)
        epoch = results.get('metadata', {}).get('epoch', 'unknown')
        fig.suptitle(f'Maxwell Crystallographic Analysis -- Epoch {epoch}', fontsize=16, fontweight='bold')

        self._plot_weight_distribution(results, fig.add_subplot(gs[0, 0]))
        self._plot_spectral_analysis(results, fig.add_subplot(gs[0, 1]))
        self._plot_phase_diagram(results, fig.add_subplot(gs[0, 2]))
        self._plot_curvature_distribution(results, fig.add_subplot(gs[0, 3]))
        self._plot_level_spacing(results, fig.add_subplot(gs[1, 0]))
        self._plot_eigenvalue_spectrum(results, fig.add_subplot(gs[1, 1]))
        self._plot_thermodynamic_potentials(results, fig.add_subplot(gs[1, 2]))
        self._plot_topological_metrics(results, fig.add_subplot(gs[1, 3]))
        self._plot_berry_phase(results, fig.add_subplot(gs[2, 0]))
        self._plot_control_stability(results, fig.add_subplot(gs[2, 1]))
        self._plot_quantum_metrics(results, fig.add_subplot(gs[2, 2]))
        self._plot_summary_table(results, fig.add_subplot(gs[2, 3]))
        self._plot_layer_deltas(results, fig.add_subplot(gs[3, 0]))
        self._plot_resonance_metrics(results, fig.add_subplot(gs[3, 1]))
        self._plot_spectral_concentration(results, fig.add_subplot(gs[3, 2]))
        self._plot_health_score(results, fig.add_subplot(gs[3, 3]))
        self._plot_goe_gue_losses(results, fig.add_subplot(gs[4, 0]))
        self._plot_dyson_beta(results, fig.add_subplot(gs[4, 1]))
        self._plot_kernel_ratios(results, fig.add_subplot(gs[4, 2]))
        self._plot_universality_gauge(results, fig.add_subplot(gs[4, 3]))

        plt.savefig(output_path, dpi=self.config.FIGURE_DPI, format=self.config.SAVE_FORMAT, bbox_inches='tight')
        plt.close()

    def _plot_weight_distribution(self, results: Dict, ax):
        """Pie chart of valid / NaN / Inf parameter counts."""
        if 'weight_integrity' in results:
            wi = results['weight_integrity']
            total = wi.get('total_params', 1)
            valid = total - wi.get('nan_count', 0) - wi.get('inf_count', 0)
            ax.pie([valid, wi.get('nan_count', 0), wi.get('inf_count', 0)],
                   labels=['Valid', 'NaN', 'Inf'],
                   colors=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_DANGER, self.config.VIZ_COLOR_WARNING],
                   autopct='%1.1f%%', startangle=90)
            ax.set_title('Weight Integrity', fontweight='bold')

    def _plot_spectral_analysis(self, results: Dict, ax):
        """Bar chart of spectral geometry observables."""
        if 'spectral_geometry' in results:
            sg = results['spectral_geometry']
            ax.bar(['Spectral Gap', 'Part. Ratio', 'Eff. Dim/100'],
                   [sg.get('spectral_gap', 0), sg.get('participation_ratio', 0), sg.get('effective_dimension', 0) / 100],
                   color=[self.config.VIZ_COLOR_ACCENT, self.config.VIZ_COLOR_SECONDARY, self.config.VIZ_COLOR_PRIMARY],
                   alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Spectral Geometry', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_phase_diagram(self, results: Dict, ax):
        """Alpha vs T_eff phase diagram with crystal/glass boundaries."""
        if 'thermodynamics' in results and 'discretization' in results:
            alpha_val = results['discretization'].get('alpha', 0)
            temp = results['thermodynamics'].get('effective_temperature', 1)
            ax.scatter([alpha_val], [max(temp, 1e-18)], s=200, c=self.config.VIZ_COLOR_DANGER, marker='*', zorder=5)
            ax.axhline(y=self.config.TEMPERATURE_CRYSTAL_THRESHOLD, color='gray', linestyle='--', alpha=0.5)
            ax.axvline(x=self.config.ALPHA_CRYSTAL_THRESHOLD, color='gray', linestyle='--', alpha=0.5)
            ax.set_xlabel('Alpha (Purity)')
            ax.set_ylabel('Temperature')
            ax.set_title('Phase Diagram', fontweight='bold')
            ax.set_xlim(0, max(15, alpha_val * 1.2))
            ax.set_ylim(1e-18, max(1e-3, temp * 10))
            ax.set_yscale('log')

    def _plot_curvature_distribution(self, results: Dict, ax):
        """Bar chart of Ricci curvature summary statistics."""
        if 'ricci_curvature' in results:
            rc = results['ricci_curvature']
            ax.bar(['Ricci Scalar', 'Mean Sectional', 'Variance'],
                   [rc.get('ricci_scalar', 0), rc.get('mean_sectional_curvature', 0), rc.get('curvature_variance', 0)],
                   color=[self.config.VIZ_COLOR_WARNING, self.config.VIZ_COLOR_ACCENT, self.config.VIZ_COLOR_SECONDARY],
                   alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Ricci Curvature', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_level_spacing(self, results: Dict, ax):
        """Level spacing ratio with Wigner-Dyson and Poisson reference lines."""
        if 'spectral_geometry' in results:
            lsr = results['spectral_geometry'].get('level_spacing_ratio', 0)
            ax.bar(['Level Spacing Ratio'], [lsr], color=self.config.VIZ_COLOR_PRIMARY, alpha=self.config.VIZ_BAR_ALPHA)
            ax.axhline(y=self.config.LEVEL_SPACING_WIGNER_DYSON, color='red', linestyle='--', label=f'WD: {self.config.LEVEL_SPACING_WIGNER_DYSON}')
            ax.axhline(y=self.config.LEVEL_SPACING_POISSON, color='green', linestyle='--', label=f'Poisson: {self.config.LEVEL_SPACING_POISSON}')
            ax.set_title('MBL Level Spacing', fontweight='bold')
            ax.legend(fontsize=8)

    def _plot_eigenvalue_spectrum(self, results: Dict, ax):
        """Largest and smallest eigenvalue on log scale."""
        if 'spectral_geometry' in results:
            sg = results['spectral_geometry']
            largest = sg.get('largest_eigenvalue', 0)
            smallest = sg.get('smallest_eigenvalue', 0)
            if largest > 0 and smallest > 0:
                ax.bar(['Largest', 'Smallest'], [np.log10(largest + 1e-10), np.log10(smallest + 1e-10)],
                       color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY], alpha=self.config.VIZ_BAR_ALPHA)
                ax.set_ylabel('log10(Eigenvalue)')
            else:
                ax.text(0.5, 0.5, 'N/A', ha='center', va='center')
            ax.set_title('Eigenvalue Spectrum', fontweight='bold')

    def _plot_thermodynamic_potentials(self, results: Dict, ax):
        """Gibbs free energy, entropy proxy, and critical temperature."""
        if 'thermodynamics' in results:
            thermo = results['thermodynamics']
            ax.bar(['Gibbs', 'Entropy', 'T_crit'],
                   [thermo.get('gibbs_free_energy', 0), thermo.get('entropy_proxy', 0), thermo.get('critical_temperature_estimate', 0)],
                   color=[self.config.VIZ_COLOR_ACCENT, self.config.VIZ_COLOR_DANGER, self.config.VIZ_COLOR_WARNING],
                   alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Thermodynamics', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_topological_metrics(self, results: Dict, ax):
        """Phase state, alignment, and resonance scores."""
        if 'topological' in results:
            topo = results['topological']
            ax.bar(['Phase State', 'Alignment', 'Resonance'],
                   [topo.get('topo_phase_state', 0), topo.get('topo_alignment_score', 0), topo.get('topo_resonance_score', 0)],
                   color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY, self.config.VIZ_COLOR_ACCENT],
                   alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Topological Metrics', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_berry_phase(self, results: Dict, ax):
        """Berry phase arrow on the unit circle."""
        if 'berry_phase' in results:
            bp = results['berry_phase']
            mod = bp.get('berry_phase_mod_2pi', 0)
            winding = bp.get('winding_number', 0)
            theta = np.linspace(0, 2 * np.pi, 100)
            ax.plot(np.cos(theta), np.sin(theta), 'gray', linestyle='--', alpha=0.5)
            ax.arrow(0, 0, 0.9 * np.cos(mod), 0.9 * np.sin(mod), head_width=0.1, head_length=0.05, fc='blue', ec='blue')
            ax.plot(np.cos(mod), np.sin(mod), 'ro', markersize=10)
            ax.set_xlim(-1.3, 1.3)
            ax.set_ylim(-1.3, 1.3)
            ax.set_aspect('equal')
            ax.set_title(f'Berry Phase: {mod:.3f} rad\nWinding: {winding}', fontweight='bold')

    def _plot_control_stability(self, results: Dict, ax):
        """Stability margin and binary stability flag."""
        if 'control_theory' in results:
            stab = results['control_theory'].get('stability_analysis', {})
            is_stable = stab.get('is_stable', False)
            margin = stab.get('stability_margin', 0)
            color = self.config.VIZ_COLOR_ACCENT if is_stable else self.config.VIZ_COLOR_DANGER
            ax.bar(['Stability Margin', 'Is Stable'], [margin, float(is_stable)], color=[color, color], alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title(f'Control Theory\n{"Stable" if is_stable else "Unstable"}', fontweight='bold')

    def _plot_quantum_metrics(self, results: Dict, ax):
        """Wavefunction entropy, participation ratio, and coherence."""
        if 'schrodinger' in results:
            sch = results['schrodinger']
            ax.bar(['Entropy', 'Part. Ratio/10', 'Coherence'],
                   [sch.get('wavefunction_entropy', 0), sch.get('participation_ratio', 0) / 10, sch.get('quantum_coherence', 0)],
                   color=[self.config.VIZ_COLOR_PRIMARY, self.config.VIZ_COLOR_SECONDARY, self.config.VIZ_COLOR_WARNING],
                   alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Quantum Metrics', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_summary_table(self, results: Dict, ax):
        """Text summary of key observables and phase classification."""
        ax.axis('off')
        summary = "Summary\n" + "=" * 30 + "\n"
        if 'discretization' in results:
            disc = results['discretization']
            summary += f"Alpha: {disc.get('alpha', 0):.4f}\n"
            summary += f"Delta: {disc.get('delta', 0):.6f}\n"
            summary += f"Phase: {results.get('thermodynamics', {}).get('phase_type', 'Unknown')}\n"
        if 'checkpoint_metrics' in results:
            cm = results['checkpoint_metrics']
            summary += f"Val Acc: {cm.get('val_acc', 0):.4f}\n"
            summary += f"Train Acc: {cm.get('train_acc', 0):.4f}\n"
            summary += f"Val Loss: {cm.get('val_loss', 0):.6f}\n"
        if 'topological' in results:
            summary += f"Crystalline: {'Yes' if results['topological'].get('topo_is_crystalline', 0) > 0.5 else 'No'}\n"
        if 'goe_gue' in results:
            gg = results['goe_gue']
            summary += f"Ensemble: {gg.get('dominant_ensemble', '?')}\n"
            summary += f"Beta: {gg.get('beta_estimate', 0):.2f}\n"
            summary += f"Kernel Ratio: {gg.get('global_kernel_ratio', 0):.4f}\n"
        if 'health_score' in results:
            summary += f"Health: {results['health_score']:.2f}\n"
        ax.text(0.1, 0.5, summary, transform=ax.transAxes, fontsize=9, verticalalignment='center',
                fontfamily='monospace', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        ax.set_title('Summary', fontweight='bold')

    def _plot_layer_deltas(self, results: Dict, ax):
        """Horizontal bar chart of per-layer discretization margins."""
        if 'discretization' in results and 'layer_deltas' in results['discretization']:
            layer_deltas = results['discretization']['layer_deltas']
            names = list(layer_deltas.keys())[:10]
            values = [layer_deltas[n] for n in names]
            ax.barh(range(len(names)), values, color=self.config.VIZ_COLOR_PRIMARY, alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_yticks(range(len(names)))
            ax.set_yticklabels([n[:20] for n in names], fontsize=8)
            ax.set_xlabel('Delta')
            ax.set_title('Layer Discretization', fontweight='bold')

    def _plot_resonance_metrics(self, results: Dict, ax):
        """Spectral concentration and resonance score bars."""
        if 'topological' in results:
            topo = results['topological']
            ax.bar(['Spectral Conc.', 'Resonance'],
                   [topo.get('topo_spectral_concentration', 0), topo.get('topo_resonance_score', 0)],
                   color=[self.config.VIZ_COLOR_WARNING, self.config.VIZ_COLOR_ACCENT], alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_title('Resonance', fontweight='bold')
            ax.tick_params(axis='x', rotation=45)

    def _plot_spectral_concentration(self, results: Dict, ax):
        """Scatter of spectral gap vs participation ratio."""
        if 'spectral_geometry' in results:
            sg = results['spectral_geometry']
            ax.scatter([sg.get('spectral_gap', 0)], [sg.get('participation_ratio', 0)],
                       s=200, c=self.config.VIZ_COLOR_DANGER, marker='*', zorder=5)
            ax.set_xlabel('Spectral Gap')
            ax.set_ylabel('Participation Ratio')
            ax.set_title('Spectral Metrics', fontweight='bold')

    def _plot_health_score(self, results: Dict, ax):
        """Single-bar health score with traffic-light colouring."""
        if 'health_score' in results:
            score = results['health_score']
            color = self.config.VIZ_COLOR_DANGER if score < 0.33 else self.config.VIZ_COLOR_WARNING if score < 0.67 else self.config.VIZ_COLOR_ACCENT
            ax.bar(['Health Score'], [score], color=color, alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_ylim(0, 1)
            ax.set_title(f'Health: {score:.2f}', fontweight='bold')

    def _plot_goe_gue_losses(self, results: Dict, ax):
        """Grouped bar chart comparing P(s) and R_2(s) losses for GOE and GUE."""
        if 'goe_gue' in results:
            gg = results['goe_gue']
            x = np.arange(2)
            width = 0.35
            goe_vals = [gg.get('p_s_loss_goe', 0), gg.get('r2_loss_goe', 0)]
            gue_vals = [gg.get('p_s_loss_gue', 0), gg.get('r2_loss_gue', 0)]
            goe_vals = [v if np.isfinite(v) else 0 for v in goe_vals]
            gue_vals = [v if np.isfinite(v) else 0 for v in gue_vals]
            ax.bar(x - width / 2, goe_vals, width, label='GOE', color=self.config.VIZ_COLOR_PRIMARY, alpha=self.config.VIZ_BAR_ALPHA)
            ax.bar(x + width / 2, gue_vals, width, label='GUE', color=self.config.VIZ_COLOR_SECONDARY, alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_xticks(x)
            ax.set_xticklabels(['P(s) Loss', 'R2 Loss'])
            ax.legend(fontsize=8)
            ax.set_title(f'GOE vs GUE Losses\nDominant: {gg.get("dominant_ensemble", "?")}', fontweight='bold')

    def _plot_dyson_beta(self, results: Dict, ax):
        """Dyson beta index gauge with GOE and GUE reference markers."""
        if 'goe_gue' in results:
            beta = results['goe_gue'].get('beta_estimate', 1.5)
            ax.barh(['Dyson Beta'], [beta], color=self.config.VIZ_COLOR_ACCENT, alpha=self.config.VIZ_BAR_ALPHA)
            ax.axvline(x=1.0, color='blue', linestyle='--', label='GOE (beta=1)')
            ax.axvline(x=2.0, color='red', linestyle='--', label='GUE (beta=2)')
            ax.set_xlim(0, 3)
            ax.legend(fontsize=8)
            ax.set_title(f'Dyson Index: beta={beta:.2f}', fontweight='bold')

    def _plot_kernel_ratios(self, results: Dict, ax):
        """Per-layer imaginary-to-real kernel norm ratios."""
        if 'goe_gue' in results:
            gg = results['goe_gue']
            ratios = gg.get('per_layer_kernel_ratios', [])
            global_ratio = gg.get('global_kernel_ratio', 0)
            if ratios:
                ax.bar(range(len(ratios)), ratios, color=self.config.VIZ_COLOR_PRIMARY, alpha=self.config.VIZ_BAR_ALPHA)
                ax.axhline(y=global_ratio, color=self.config.VIZ_COLOR_DANGER, linestyle='--', label=f'Global: {global_ratio:.3f}')
                ax.axhline(y=self.config.KERNEL_IMAGINARY_RATIO_OPTIMAL_R2, color='green', linestyle=':', label=f'R2 opt: {self.config.KERNEL_IMAGINARY_RATIO_OPTIMAL_R2}')
                ax.set_xlabel('Layer')
                ax.set_ylabel('Imag/Real Ratio')
                ax.legend(fontsize=7)
            else:
                ax.text(0.5, 0.5, 'No spectral layers', ha='center', va='center')
            ax.set_title('Kernel Ratios', fontweight='bold')

    def _plot_universality_gauge(self, results: Dict, ax):
        """Horizontal gauge showing interpolation between GOE and GUE."""
        if 'goe_gue' in results:
            gg = results['goe_gue']
            interp = gg.get('universality_interpolation', 0.5)
            ax.barh(['GOE <-> GUE'], [interp], color=self.config.VIZ_COLOR_WARNING, alpha=self.config.VIZ_BAR_ALPHA)
            ax.set_xlim(0, 1)
            ax.axvline(x=0.5, color='gray', linestyle='--', alpha=0.5)
            ax.text(0.0, -0.3, 'GOE', transform=ax.transAxes, fontsize=9, ha='left')
            ax.text(1.0, -0.3, 'GUE', transform=ax.transAxes, fontsize=9, ha='right')
            ax.set_title(f'Universality: {interp:.2f}', fontweight='bold')


class CheckpointAnalyzer:
    """Main analyzer orchestrating all metric calculations on a single checkpoint."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Instantiate all sub-calculators."""
        self.config = config
        self.logger = LoggerFactory.create_logger("CheckpointAnalyzer", config=config)
        self.weight_integrity_calc = WeightIntegrityCalculator(config)
        self.discretization_calc = DiscretizationCalculator(config)
        self.spectral_geometry_calc = SpectralGeometryCalculator(config)
        self.ricci_curvature_calc = RicciCurvatureCalculator(config)
        self.berry_phase_calc = BerryPhaseCalculator(config)
        self.control_analyzer = ControlSystemAnalyzer(config)
        self.thermodynamic_calc = ThermodynamicCalculator(config)
        self.topological_calc = TopologicalMetricsCalculator(config)
        self.gradient_dynamics_calc = GradientDynamicsCalculator(config)
        self.schrodinger_analyzer = SchrodingerAnalyzer(config)
        self.goe_gue_analyzer = GOEGUESpectralAnalyzer(config)
        self.visualizer = ComprehensiveVisualizer(config)

    def analyze_checkpoint(self, checkpoint_path: str, val_data: Optional[Tuple] = None) -> Dict[str, Any]:
        """Load a checkpoint, run every analyzer, and return the aggregated results dict."""
        self.logger.info(f"Analyzing checkpoint: {checkpoint_path}")
        start_time = time.time()
        try:
            checkpoint = torch.load(checkpoint_path, map_location='cpu', weights_only=False)
        except Exception as e:
            self.logger.error(f"Failed to load checkpoint: {e}")
            return {'error': str(e), 'checkpoint_path': checkpoint_path}

        imaginary_ratio = self.config.DEFAULT_IMAGINARY_RATIO
        if isinstance(checkpoint, dict):
            cfg = checkpoint.get('config', {})
            if isinstance(cfg, dict):
                imaginary_ratio = cfg.get('imaginary_ratio', imaginary_ratio)

        model = MaxwellSpectralNetwork(self.config, imaginary_ratio=imaginary_ratio)
        if isinstance(checkpoint, dict) and 'model_state_dict' in checkpoint:
            model.load_state_dict(checkpoint['model_state_dict'], strict=False)
        elif isinstance(checkpoint, dict):
            model.load_state_dict(checkpoint, strict=False)
        model.eval()

        epoch = checkpoint.get('epoch', 'unknown') if isinstance(checkpoint, dict) else 'unknown'
        saved_metrics = checkpoint.get('metrics', {}) if isinstance(checkpoint, dict) else {}
        results = {
            'metadata': {
                'checkpoint_path': checkpoint_path, 'epoch': epoch,
                'timestamp': datetime.now().isoformat(), 'analysis_duration_seconds': 0
            },
            'checkpoint_metrics': {
                'val_acc': saved_metrics.get('val_acc', 0.0),
                'train_acc': saved_metrics.get('train_acc', 0.0),
                'val_loss': saved_metrics.get('val_loss', float('inf')),
                'train_loss': saved_metrics.get('train_loss', float('inf')),
                'lambda_pressure': saved_metrics.get('lambda_pressure', 0.0)
            }
        }
        val_x, val_y = val_data if val_data else (None, None)

        self.logger.info("Computing weight integrity...")
        results['weight_integrity'] = self.weight_integrity_calc.compute(model)

        self.logger.info("Computing discretization metrics...")
        results['discretization'] = self.discretization_calc.compute(model)

        self.logger.info("Computing spectral geometry...")
        results['spectral_geometry'] = self.spectral_geometry_calc.compute(model)

        self.logger.info("Computing Ricci curvature...")
        results['ricci_curvature'] = self.ricci_curvature_calc.compute(model)

        self.logger.info("Computing control theory analysis...")
        results['control_theory'] = self.control_analyzer.compute(model)

        self.logger.info("Computing topological metrics...")
        results['topological'] = self.topological_calc.compute(model)

        self.logger.info("Computing Schrodinger analysis...")
        results['schrodinger'] = self.schrodinger_analyzer.compute(model)

        self.logger.info("Computing GOE/GUE spectral analysis (Chapter 10)...")
        results['goe_gue'] = self.goe_gue_analyzer.compute(model)

        self.logger.info("Computing gradient dynamics...")
        grad_results = self.gradient_dynamics_calc.compute(model, val_x=val_x, val_y=val_y)
        results['gradient_dynamics'] = grad_results

        self.logger.info("Computing thermodynamic metrics...")
        results['thermodynamics'] = self.thermodynamic_calc.compute(
            model,
            delta=results['discretization'].get('delta', 1.0),
            alpha=results['discretization'].get('alpha', 0.0),
            kappa=grad_results.get('kappa', 1.0),
            effective_temperature=grad_results.get('effective_temperature', 1.0)
        )

        results['health_score'] = self._compute_health_score(results)
        results['metadata']['analysis_duration_seconds'] = time.time() - start_time
        self.logger.info(f"Analysis completed in {results['metadata']['analysis_duration_seconds']:.2f}s")
        return results

    def _compute_health_score(self, results: Dict[str, Any]) -> float:
        """Weighted average of integrity, purity, MBL, and topological scores."""
        score = 0.0
        count = 0
        if 'weight_integrity' in results:
            score += float(results['weight_integrity'].get('is_valid', False))
            count += 1
        if 'discretization' in results:
            alpha = results['discretization'].get('alpha', 0)
            score += min(alpha / self.config.ALPHA_CRYSTAL_THRESHOLD, 1.0)
            count += 1
        if 'spectral_geometry' in results:
            lsr = results['spectral_geometry'].get('level_spacing_ratio', 0)
            mbl_score = 1.0 - abs(lsr - self.config.LEVEL_SPACING_POISSON) / self.config.LEVEL_SPACING_TOLERANCE
            score += max(0, min(1, mbl_score))
            count += 1
        if 'topological' in results:
            score += results['topological'].get('topo_phase_state', 0)
            count += 1
        return score / count if count > 0 else 0.0


class BatchProcessor:
    """Process all checkpoints in a directory, generating per-checkpoint and summary outputs."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise analyzer and visualizer."""
        self.config = config
        self.logger = LoggerFactory.create_logger("BatchProcessor", config=config)
        self.analyzer = CheckpointAnalyzer(config)
        self.visualizer = ComprehensiveVisualizer(config)

    def process_directory(self, checkpoint_dir: str, output_dir: str, val_data: Optional[Tuple] = None):
        """Iterate over all .pth files, analyze each, and save results."""
        self.logger.info(f"Processing directory: {checkpoint_dir}")
        os.makedirs(output_dir, exist_ok=True)
        checkpoint_files = sorted(glob.glob(os.path.join(checkpoint_dir, "*.pth")))
        if not checkpoint_files:
            self.logger.warning(f"No checkpoint files found in {checkpoint_dir}")
            return
        self.logger.info(f"Found {len(checkpoint_files)} checkpoints")
        all_results = []
        for i, checkpoint_path in enumerate(checkpoint_files):
            self.logger.info(f"Processing checkpoint {i + 1}/{len(checkpoint_files)}: {checkpoint_path}")
            try:
                results = self.analyzer.analyze_checkpoint(checkpoint_path, val_data)
                all_results.append(results)
                name = Path(checkpoint_path).stem
                viz_path = os.path.join(output_dir, f"{name}_analysis.{self.config.SAVE_FORMAT}")
                self.visualizer.visualize_checkpoint_analysis(results, viz_path)
                json_path = os.path.join(output_dir, f"{name}_metrics.json")
                with open(json_path, 'w') as f:
                    json.dump(results, f, indent=2, default=str)
            except Exception as e:
                self.logger.error(f"Error processing {checkpoint_path}: {e}")
                import traceback
                self.logger.error(traceback.format_exc())
        summary = self._generate_summary(all_results)
        with open(os.path.join(output_dir, "analysis_summary.json"), 'w') as f:
            json.dump(summary, f, indent=2, default=str)
        self._generate_evolution_plots(all_results, output_dir)
        self.logger.info(f"Batch processing complete. Results saved to {output_dir}")

    def _generate_summary(self, all_results: List[Dict]) -> Dict[str, Any]:
        """Aggregate statistics and rank checkpoints by delta, alpha, accuracy, and health score."""
        if not all_results:
            return {}

        def _extract(cat, key, default=0):
            return [r.get(cat, {}).get(key, default) for r in all_results]

        def _stats(vals):
            arr = np.array([v for v in vals if np.isfinite(v)], dtype=float)
            if len(arr) == 0:
                return {'mean': 0.0, 'std': 0.0, 'min': 0.0, 'max': 0.0}
            return {'mean': float(np.mean(arr)), 'std': float(np.std(arr)), 'min': float(np.min(arr)), 'max': float(np.max(arr))}

        def _checkpoint_id(r):
            return {
                'epoch': r.get('metadata', {}).get('epoch', '?'),
                'path': r.get('metadata', {}).get('checkpoint_path', '?')
            }

        alphas = _extract('discretization', 'alpha')
        deltas = _extract('discretization', 'delta')
        betas = _extract('goe_gue', 'beta_estimate')
        kernel_ratios = _extract('goe_gue', 'global_kernel_ratio')
        val_accs = _extract('checkpoint_metrics', 'val_acc')
        train_accs = _extract('checkpoint_metrics', 'train_acc')
        val_losses = _extract('checkpoint_metrics', 'val_loss', default=float('inf'))
        ensembles = [r.get('goe_gue', {}).get('dominant_ensemble', 'Unknown') for r in all_results]
        phases = [r.get('thermodynamics', {}).get('phase_type', 'Unknown') for r in all_results]
        healths = [r.get('health_score', 0) for r in all_results]

        best_by_delta = int(np.argmin(deltas))
        best_by_alpha = int(np.argmax(alphas))
        best_by_val_acc = int(np.argmax(val_accs))
        best_by_health = int(np.argmax(healths))

        composite_scores = []
        for i in range(len(all_results)):
            delta_rank = 1.0 - (deltas[i] / (max(deltas) + 1e-10))
            alpha_rank = alphas[i] / (max(alphas) + 1e-10)
            acc_rank = val_accs[i] / (max(val_accs) + 1e-10) if max(val_accs) > 0 else 0.0
            health_rank = healths[i] / (max(healths) + 1e-10) if max(healths) > 0 else 0.0
            composite = 0.3 * delta_rank + 0.25 * alpha_rank + 0.25 * acc_rank + 0.2 * health_rank
            composite_scores.append(composite)
        best_composite = int(np.argmax(composite_scores))

        def _best_entry(idx):
            r = all_results[idx]
            return {
                'epoch': r.get('metadata', {}).get('epoch', '?'),
                'checkpoint_path': r.get('metadata', {}).get('checkpoint_path', '?'),
                'delta': deltas[idx],
                'alpha': alphas[idx],
                'val_acc': val_accs[idx],
                'train_acc': train_accs[idx],
                'val_loss': val_losses[idx],
                'health_score': healths[idx],
                'beta_estimate': betas[idx],
                'kernel_ratio': kernel_ratios[idx],
                'dominant_ensemble': ensembles[idx],
                'phase_type': phases[idx],
                'composite_score': composite_scores[idx]
            }

        ranking = {
            'best_by_delta': _best_entry(best_by_delta),
            'best_by_alpha_purity': _best_entry(best_by_alpha),
            'best_by_val_accuracy': _best_entry(best_by_val_acc),
            'best_by_health_score': _best_entry(best_by_health),
            'best_composite': _best_entry(best_composite),
            'composite_weights': {
                'delta_weight': 0.3,
                'alpha_weight': 0.25,
                'accuracy_weight': 0.25,
                'health_weight': 0.2
            }
        }

        self.logger.info("=" * 70)
        self.logger.info("BEST CHECKPOINT RANKING")
        self.logger.info("=" * 70)
        for criterion, entry in ranking.items():
            if criterion == 'composite_weights':
                continue
            self.logger.info(
                f"  {criterion}: epoch={entry['epoch']} "
                f"delta={entry['delta']:.6f} alpha={entry['alpha']:.4f} "
                f"val_acc={entry['val_acc']:.4f} health={entry['health_score']:.4f} "
                f"beta={entry['beta_estimate']:.2f} ensemble={entry['dominant_ensemble']} "
                f"phase={entry['phase_type']}"
            )
        self.logger.info(
            f"  RECOMMENDED: epoch={ranking['best_composite']['epoch']} "
            f"(composite={ranking['best_composite']['composite_score']:.4f})"
        )
        self.logger.info("=" * 70)

        full_ranking = sorted(
            [{'index': i, **_best_entry(i)} for i in range(len(all_results))],
            key=lambda x: x['composite_score'],
            reverse=True
        )

        return {
            'total_checkpoints': len(all_results),
            'timestamp': datetime.now().isoformat(),
            'best_checkpoints': ranking,
            'full_ranking': full_ranking,
            'statistics': {
                'alpha': _stats(alphas), 'delta': _stats(deltas),
                'val_acc': _stats(val_accs), 'train_acc': _stats(train_accs),
                'health_score': _stats(healths),
                'beta_estimate': _stats(betas), 'kernel_ratio': _stats(kernel_ratios),
                'phase_distribution': {k: phases.count(k) for k in set(phases)},
                'ensemble_distribution': {k: ensembles.count(k) for k in set(ensembles)}
            },
            'epochs': [r.get('metadata', {}).get('epoch', i) for i, r in enumerate(all_results)]
        }

    def _generate_evolution_plots(self, all_results: List[Dict], output_dir: str):
        """Time-series plots of key metrics across training."""
        if not all_results or len(all_results) < 2:
            return
        epochs = [r.get('metadata', {}).get('epoch', i) for i, r in enumerate(all_results)]
        fig, axes = plt.subplots(5, 3, figsize=(18, 20), dpi=self.config.FIGURE_DPI)
        fig.suptitle('Metric Evolution Across Checkpoints', fontsize=14, fontweight='bold')
        metrics_to_plot = [
            ('discretization', 'alpha', 'Alpha (Purity)', axes[0, 0]),
            ('discretization', 'delta', 'Delta (Discretization)', axes[0, 1]),
            ('health_score', None, 'Health Score', axes[0, 2]),
            ('checkpoint_metrics', 'val_acc', 'Validation Accuracy', axes[1, 0]),
            ('checkpoint_metrics', 'train_acc', 'Training Accuracy', axes[1, 1]),
            ('checkpoint_metrics', 'val_loss', 'Validation Loss', axes[1, 2]),
            ('ricci_curvature', 'ricci_scalar', 'Ricci Scalar', axes[2, 0]),
            ('spectral_geometry', 'level_spacing_ratio', 'Level Spacing Ratio', axes[2, 1]),
            ('spectral_geometry', 'spectral_gap', 'Spectral Gap', axes[2, 2]),
            ('topological', 'topo_phase_state', 'Phase State', axes[3, 0]),
            ('schrodinger', 'wavefunction_entropy', 'Wavefunction Entropy', axes[3, 1]),
            ('gradient_dynamics', 'effective_temperature', 'Effective Temperature', axes[3, 2]),
            ('goe_gue', 'beta_estimate', 'Dyson Beta', axes[4, 0]),
            ('goe_gue', 'global_kernel_ratio', 'Kernel Ratio', axes[4, 1]),
            ('goe_gue', 'universality_interpolation', 'GOE<->GUE Interpolation', axes[4, 2]),
        ]
        for category, key, label, ax in metrics_to_plot:
            if category == 'health_score':
                values = [r.get('health_score', 0) for r in all_results]
            else:
                values = [r.get(category, {}).get(key, 0) for r in all_results]
            ax.plot(epochs, values, 'o-', color=self.config.VIZ_COLOR_PRIMARY, linewidth=2, markersize=6)
            ax.set_xlabel('Epoch')
            ax.set_ylabel(label)
            ax.set_title(label, fontweight='bold')
            ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"metric_evolution.{self.config.SAVE_FORMAT}"),
                    dpi=self.config.FIGURE_DPI, format=self.config.SAVE_FORMAT)
        plt.close()


class MaxwellCrystallographySuite:
    """Main entry point for the Maxwell crystallography analysis suite."""

    def __init__(self, config: CrystallographySuiteConfig):
        """Initialise the suite with all sub-components."""
        self.config = config
        self.logger = LoggerFactory.create_logger("MaxwellCrystallographySuite", config=config)
        self.batch_processor = BatchProcessor(config)
        self.berry_phase_calc = BerryPhaseCalculator(config)

    def run_analysis(self, checkpoint_dir: str, output_dir: str):
        """Execute full analysis: batch processing, Berry phase, and summary."""
        self.logger.info("=" * 70)
        self.logger.info("MAXWELL CRYSTALLOGRAPHY ANALYSIS SUITE")
        self.logger.info("With Chapter 10 GOE/GUE Spectral Universality Diagnostics")
        self.logger.info("=" * 70)
        start_time = time.time()
        self.batch_processor.process_directory(checkpoint_dir, output_dir)
        berry_results = self.berry_phase_calc.calculate_berry_phase(checkpoint_dir)
        with open(os.path.join(output_dir, "berry_phase_analysis.json"), 'w') as f:
            json.dump(berry_results, f, indent=2, default=str)
        self._generate_berry_phase_visualization(berry_results, output_dir)
        total_time = time.time() - start_time
        self.logger.info("=" * 70)
        self.logger.info("ANALYSIS COMPLETE")
        self.logger.info(f"Total duration: {total_time:.2f} seconds")
        self.logger.info(f"Results saved to: {output_dir}")
        self.logger.info("=" * 70)

    def _generate_berry_phase_visualization(self, berry_results: Dict, output_dir: str):
        """Dedicated Berry phase figure with phasor diagram and summary text."""
        if 'error' in berry_results:
            return
        fig, axes = plt.subplots(1, 2, figsize=(12, 5), dpi=self.config.FIGURE_DPI)
        total_phase = berry_results.get('total_berry_phase', 0)
        mod_2pi = berry_results.get('berry_phase_mod_2pi', 0)
        winding = berry_results.get('winding_number', 0)
        theta = np.linspace(0, 2 * np.pi, 100)
        axes[0].plot(np.cos(theta), np.sin(theta), 'gray', linestyle='--', alpha=0.5)
        axes[0].arrow(0, 0, 0.9 * np.cos(mod_2pi), 0.9 * np.sin(mod_2pi),
                      head_width=0.1, head_length=0.05, fc='blue', ec='blue')
        axes[0].plot(np.cos(mod_2pi), np.sin(mod_2pi), 'ro', markersize=15)
        axes[0].set_xlim(-1.5, 1.5)
        axes[0].set_ylim(-1.5, 1.5)
        axes[0].set_aspect('equal')
        axes[0].set_title(f'Berry Phase: {mod_2pi:.4f} rad ({np.degrees(mod_2pi):.1f} deg)', fontweight='bold')
        axes[0].set_xlabel('Re(exp(i*gamma))')
        axes[0].set_ylabel('Im(exp(i*gamma))')
        axes[0].grid(True, alpha=0.3)
        if abs(mod_2pi) < 0.1:
            interpretation = "Trivial (gamma ~ 0)"
        elif abs(abs(mod_2pi) - np.pi) < 0.3:
            interpretation = "Non-trivial Z2 (gamma ~ pi)"
        else:
            interpretation = "Generic topological"
        info_text = (
            f"Berry Phase Analysis\n"
            f"--------------------\n"
            f"Total Phase: {total_phase:.6f} rad\n"
            f"Phase (mod 2pi): {mod_2pi:.6f} rad\n"
            f"Winding Number: {winding}\n\n"
            f"Interpretation:\n{interpretation}\n\n"
            f"Checkpoints analyzed: {berry_results.get('num_checkpoints', 0)}"
        )
        axes[1].text(0.1, 0.5, info_text, transform=axes[1].transAxes, fontsize=10,
                     verticalalignment='center', fontfamily='monospace',
                     bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
        axes[1].axis('off')
        axes[1].set_title('Berry Phase Summary', fontweight='bold')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"berry_phase_visualization.{self.config.SAVE_FORMAT}"),
                    dpi=self.config.FIGURE_DPI, format=self.config.SAVE_FORMAT)
        plt.close()


def main():
    """Parse arguments and run the Maxwell crystallography suite."""
    parser = argparse.ArgumentParser(
        description='Maxwell Equation Crystallography Analysis Suite with GOE/GUE Spectral Diagnostics'
    )
    parser.add_argument('--checkpoint_dir', '-c', type=str, default='checkpoints_maxwell_phase3')
    parser.add_argument('--output_dir', '-o', type=str, default='maxwell_crystallography_analysis')
    parser.add_argument('--grid_size', '-g', type=int, default=16)
    parser.add_argument('--hidden_dim', '-hd', type=int, default=32)
    parser.add_argument('--expansion_dim', '-ed', type=int, default=64)
    parser.add_argument('--spectral_layers', '-sl', type=int, default=2)
    parser.add_argument('--imaginary_ratio', '-ir', type=float, default=0.3)
    parser.add_argument('--log_level', type=str, default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'])
    args = parser.parse_args()

    config = CrystallographySuiteConfig(
        GRID_SIZE=args.grid_size,
        HIDDEN_DIM=args.hidden_dim,
        EXPANSION_DIM=args.expansion_dim,
        NUM_SPECTRAL_LAYERS=args.spectral_layers,
        DEFAULT_IMAGINARY_RATIO=args.imaginary_ratio,
        LOG_LEVEL=args.log_level
    )

    suite = MaxwellCrystallographySuite(config)
    suite.run_analysis(args.checkpoint_dir, args.output_dir)


if __name__ == "__main__":
    main()
