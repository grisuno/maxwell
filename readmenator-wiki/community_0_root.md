# root

*Community 0 | 8 files | cohesion 1.00*

## Definition

This community groups 8 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `AdaptiveLambdaScheduler`, `AnalysisConfig`, `AnalyticalMultipoleSource`, `AnnealingScheduler`, `BandgapAnalyzer`, `BatchAnalyzer`, `BatchProcessor`, `BatchSizeProspector`. Core file: `maxwell_crystal.py` (188 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 0 | yes |
| `install.sh` | sh | utility | 0 | no |
| `maxwell_crystal.py` | py | utility | 188 | yes |
| `maxwell_crystallography_suite.py` | py | utility | 123 | yes |
| `maxwell_field_hawking_suite.py` | py | utility | 99 | yes |
| `maxwell_magnetic_orbitals.py` | py | utility | 47 | yes |
| `maxwell_magnetic_orbitals_v2.py` | py | utility | 50 | yes |
| `maxwell_orbital_diagnostic.py` | py | utility | 49 | yes |

## Key Symbols

- `Config` (class, `maxwell_crystal.py:56`) `class Config` - Central configuration for all hyperparameters, architecture sizes, and protocol constants.
- `IPhaseDetector` (class, `maxwell_crystal.py:257`) `class IPhaseDetector(ABC)` - Abstract interface for phase detection in neural network training.
- `detect` (method, `maxwell_crystal.py:261`) `def detect(self, spectral_field)` - Detect phase characteristics from spectral field data.
- `IMetricCalculator` (class, `maxwell_crystal.py:266`) `class IMetricCalculator(ABC)` - Abstract interface for metric calculation.
- `compute` (method, `maxwell_crystal.py:270`) `def compute(self, model)` - Compute metrics for the given model and optional keyword arguments.
- `SeedManager` (class, `maxwell_crystal.py:275`) `class SeedManager` - Deterministic seed management for reproducibility.
- `set_seed` (method, `maxwell_crystal.py:279`) `def set_seed(seed, device)` - Set random seeds across all relevant libraries and backends.
- `LoggerFactory` (class, `maxwell_crystal.py:290`) `class LoggerFactory` - Factory for creating consistently formatted loggers.
- `create_logger` (method, `maxwell_crystal.py:294`) `def create_logger(name, level)` - Create and return a configured logger instance.
- `MaxwellOperator` (class, `maxwell_crystal.py:308`) `class MaxwellOperator` - Maxwell equations operator for 2D TM polarization (Ex, Ey, Bz).
- `__init__` (method, `maxwell_crystal.py:321`) `def __init__(self, config)` - Precompute wavenumber grids and material constants.
- `_precompute_operators` (method, `maxwell_crystal.py:331`) `def _precompute_operators(self)` - Build Fourier-space wavenumber grids.
- `apply_maxwell_operator` (method, `maxwell_crystal.py:339`) `def apply_maxwell_operator(self, fields)` - Apply the Maxwell curl operator to a (batch, 3, H, W) real tensor.
- `time_evolution` (method, `maxwell_crystal.py:371`) `def time_evolution(self, fields, dt)` - Advance electromagnetic fields by one time step using Euler integration
- `SpectralStatisticsCalculator` (class, `maxwell_crystal.py:396`) `class SpectralStatisticsCalculator` - Spectral statistics engine for GOE/GUE analysis (Chapter 10).
- `__init__` (method, `maxwell_crystal.py:406`) `def __init__(self, config)` - Store reference to global configuration.
- `generate_goe_matrix` (method, `maxwell_crystal.py:411`) `def generate_goe_matrix(size, device)` - Return a sample from the Gaussian Orthogonal Ensemble.
- `generate_gue_matrix` (method, `maxwell_crystal.py:417`) `def generate_gue_matrix(size, device)` - Return a sample from the Gaussian Unitary Ensemble.
- `generate_interpolated_matrix` (method, `maxwell_crystal.py:425`) `def generate_interpolated_matrix(self, size, imaginary_ratio, device)` - Return a complex Hermitian matrix interpolating between GOE and GUE.
- `compute_eigenvalue_spacing` (method, `maxwell_crystal.py:443`) `def compute_eigenvalue_spacing(self, eigenvalues)` - Unfold eigenvalues via polynomial fit and return normalised spacings.
- `compute_spacing_distribution_loss` (method, `maxwell_crystal.py:458`) `def compute_spacing_distribution_loss(self, spacings, target)` - MSE between the empirical P(s) histogram and the Wigner surmise.
- `compute_dyson_index` (method, `maxwell_crystal.py:481`) `def compute_dyson_index(self, eigenvalues, spacings)` - Estimate Dyson beta from small-spacing power-law P(s) ~ s^beta.
- `compute_pair_correlation` (method, `maxwell_crystal.py:506`) `def compute_pair_correlation(self, eigenvalues, s_range, num_points)` - Two-level correlation function R_2(s).
- `compute_correlation_loss` (method, `maxwell_crystal.py:533`) `def compute_correlation_loss(self, eigenvalues, target)` - MSE between empirical R_2(s) and the analytical prediction.
- `compute_spectral_stats_for_ratio` (method, `maxwell_crystal.py:552`) `def compute_spectral_stats_for_ratio(self, imaginary_ratio, matrix_size, num_mat` - Ensemble-averaged spectral statistics at a given imaginary ratio.
- `SpectralLayer` (class, `maxwell_crystal.py:610`) `class SpectralLayer(Module)` - Fourier-domain convolutional layer with tuneable imaginary ratio.
- `__init__` (method, `maxwell_crystal.py:619`) `def __init__(self, channels, grid_size, imaginary_ratio)` - Initialise real and imaginary kernel parameters.
- `_apply_imaginary_ratio` (method, `maxwell_crystal.py:638`) `def _apply_imaginary_ratio(self)` - Scale the imaginary kernel by the imaginary ratio at init time.
- `set_imaginary_ratio` (method, `maxwell_crystal.py:643`) `def set_imaginary_ratio(self, ratio)` - Rescale imaginary kernel to reflect a new imaginary ratio.
- `forward` (method, `maxwell_crystal.py:651`) `def forward(self, x)` - Apply spectral convolution in Fourier space.

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 1 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `app.py`
- `install.sh`
- `maxwell_crystal.py`
- `maxwell_crystallography_suite.py`
- `maxwell_field_hawking_suite.py`
- `maxwell_magnetic_orbitals.py`
- `maxwell_magnetic_orbitals_v2.py`
- `maxwell_orbital_diagnostic.py`
