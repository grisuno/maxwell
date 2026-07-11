# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 8 | **Total Symbols Extracted:** 556 | **Total Imports:** 137

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    maxwell_crystallography_suite_py["maxwell_crystallography_suite.py (py)"]
    class maxwell_crystallography_suite_py mod;
    maxwell_crystallography_suite_py_CrystallographySuiteConfig["CrystallographySuiteConfig"]
    class maxwell_crystallography_suite_py_CrystallographySuiteConfig cls;
    maxwell_crystallography_suite_py --> maxwell_crystallography_suite_py_CrystallographySuiteConfig
    maxwell_crystallography_suite_py_LoggerFactory["LoggerFactory"]
    class maxwell_crystallography_suite_py_LoggerFactory cls;
    maxwell_crystallography_suite_py --> maxwell_crystallography_suite_py_LoggerFactory
    maxwell_crystallography_suite_py_IMetricCalculator["IMetricCalculator"]
    class maxwell_crystallography_suite_py_IMetricCalculator cls;
    maxwell_crystallography_suite_py --> maxwell_crystallography_suite_py_IMetricCalculator
    maxwell_crystallography_suite_py_IPhaseDetector["IPhaseDetector"]
    class maxwell_crystallography_suite_py_IPhaseDetector cls;
    maxwell_crystallography_suite_py --> maxwell_crystallography_suite_py_IPhaseDetector
    maxwell_crystallography_suite_py_SpectralLayer["SpectralLayer"]
    class maxwell_crystallography_suite_py_SpectralLayer cls;
    maxwell_crystallography_suite_py --> maxwell_crystallography_suite_py_SpectralLayer
    maxwell_field_hawking_suite_py["maxwell_field_hawking_suite.py (py)"]
    class maxwell_field_hawking_suite_py mod;
    maxwell_field_hawking_suite_py_AnalysisConfig["AnalysisConfig"]
    class maxwell_field_hawking_suite_py_AnalysisConfig cls;
    maxwell_field_hawking_suite_py --> maxwell_field_hawking_suite_py_AnalysisConfig
    maxwell_field_hawking_suite_py_LoggerFactory["LoggerFactory"]
    class maxwell_field_hawking_suite_py_LoggerFactory cls;
    maxwell_field_hawking_suite_py --> maxwell_field_hawking_suite_py_LoggerFactory
    maxwell_field_hawking_suite_py_CustomUnpickler["CustomUnpickler"]
    class maxwell_field_hawking_suite_py_CustomUnpickler cls;
    maxwell_field_hawking_suite_py --> maxwell_field_hawking_suite_py_CustomUnpickler
    maxwell_field_hawking_suite_py_load_checkpoint_robust["load_checkpoint_robust"]
    class maxwell_field_hawking_suite_py_load_checkpoint_robust fn;
    maxwell_field_hawking_suite_py --> maxwell_field_hawking_suite_py_load_checkpoint_robust
    maxwell_field_hawking_suite_py_SpectralLayer["SpectralLayer"]
    class maxwell_field_hawking_suite_py_SpectralLayer cls;
    maxwell_field_hawking_suite_py --> maxwell_field_hawking_suite_py_SpectralLayer
    maxwell_magnetic_orbitals_v2_py["maxwell_magnetic_orbitals_v2.py (py)"]
    class maxwell_magnetic_orbitals_v2_py mod;
    maxwell_magnetic_orbitals_v2_py_Config["Config"]
    class maxwell_magnetic_orbitals_v2_py_Config cls;
    maxwell_magnetic_orbitals_v2_py --> maxwell_magnetic_orbitals_v2_py_Config
    maxwell_magnetic_orbitals_v2_py_LoggerFactory["LoggerFactory"]
    class maxwell_magnetic_orbitals_v2_py_LoggerFactory cls;
    maxwell_magnetic_orbitals_v2_py --> maxwell_magnetic_orbitals_v2_py_LoggerFactory
    maxwell_magnetic_orbitals_v2_py_SpectralLayer["SpectralLayer"]
    class maxwell_magnetic_orbitals_v2_py_SpectralLayer cls;
    maxwell_magnetic_orbitals_v2_py --> maxwell_magnetic_orbitals_v2_py_SpectralLayer
    maxwell_magnetic_orbitals_v2_py_MaxwellSpectralNetwork["MaxwellSpectralNetwork"]
    class maxwell_magnetic_orbitals_v2_py_MaxwellSpectralNetwork cls;
    maxwell_magnetic_orbitals_v2_py --> maxwell_magnetic_orbitals_v2_py_MaxwellSpectralNetwork
    maxwell_magnetic_orbitals_v2_py_AnalyticalMultipoleSource["AnalyticalMultipoleSource"]
    class maxwell_magnetic_orbitals_v2_py_AnalyticalMultipoleSource cls;
    maxwell_magnetic_orbitals_v2_py --> maxwell_magnetic_orbitals_v2_py_AnalyticalMultipoleSource
    maxwell_magnetic_orbitals_py["maxwell_magnetic_orbitals.py (py)"]
    class maxwell_magnetic_orbitals_py mod;
    maxwell_magnetic_orbitals_py_IsomorphismConfig["IsomorphismConfig"]
    class maxwell_magnetic_orbitals_py_IsomorphismConfig cls;
    maxwell_magnetic_orbitals_py --> maxwell_magnetic_orbitals_py_IsomorphismConfig
    maxwell_magnetic_orbitals_py_LoggerFactory["LoggerFactory"]
    class maxwell_magnetic_orbitals_py_LoggerFactory cls;
    maxwell_magnetic_orbitals_py --> maxwell_magnetic_orbitals_py_LoggerFactory
    maxwell_magnetic_orbitals_py_SpectralLayer["SpectralLayer"]
    class maxwell_magnetic_orbitals_py_SpectralLayer cls;
    maxwell_magnetic_orbitals_py --> maxwell_magnetic_orbitals_py_SpectralLayer
    maxwell_magnetic_orbitals_py_MaxwellSpectralNetwork["MaxwellSpectralNetwork"]
    class maxwell_magnetic_orbitals_py_MaxwellSpectralNetwork cls;
    maxwell_magnetic_orbitals_py --> maxwell_magnetic_orbitals_py_MaxwellSpectralNetwork
    maxwell_magnetic_orbitals_py_ModelLoader["ModelLoader"]
    class maxwell_magnetic_orbitals_py_ModelLoader cls;
    maxwell_magnetic_orbitals_py --> maxwell_magnetic_orbitals_py_ModelLoader
    maxwell_crystal_py["maxwell_crystal.py (py)"]
    class maxwell_crystal_py mod;
    maxwell_crystal_py_Config["Config"]
    class maxwell_crystal_py_Config cls;
    maxwell_crystal_py --> maxwell_crystal_py_Config
    maxwell_crystal_py_IPhaseDetector["IPhaseDetector"]
    class maxwell_crystal_py_IPhaseDetector cls;
    maxwell_crystal_py --> maxwell_crystal_py_IPhaseDetector
    maxwell_crystal_py_IMetricCalculator["IMetricCalculator"]
    class maxwell_crystal_py_IMetricCalculator cls;
    maxwell_crystal_py --> maxwell_crystal_py_IMetricCalculator
    maxwell_crystal_py_SeedManager["SeedManager"]
    class maxwell_crystal_py_SeedManager cls;
    maxwell_crystal_py --> maxwell_crystal_py_SeedManager
    maxwell_crystal_py_LoggerFactory["LoggerFactory"]
    class maxwell_crystal_py_LoggerFactory cls;
    maxwell_crystal_py --> maxwell_crystal_py_LoggerFactory
    maxwell_orbital_diagnostic_py["maxwell_orbital_diagnostic.py (py)"]
    class maxwell_orbital_diagnostic_py mod;
    maxwell_orbital_diagnostic_py_DiagnosticConfig["DiagnosticConfig"]
    class maxwell_orbital_diagnostic_py_DiagnosticConfig cls;
    maxwell_orbital_diagnostic_py --> maxwell_orbital_diagnostic_py_DiagnosticConfig
    maxwell_orbital_diagnostic_py_LoggerFactory["LoggerFactory"]
    class maxwell_orbital_diagnostic_py_LoggerFactory cls;
    maxwell_orbital_diagnostic_py --> maxwell_orbital_diagnostic_py_LoggerFactory
    maxwell_orbital_diagnostic_py_SpectralLayer["SpectralLayer"]
    class maxwell_orbital_diagnostic_py_SpectralLayer cls;
    maxwell_orbital_diagnostic_py --> maxwell_orbital_diagnostic_py_SpectralLayer
    maxwell_orbital_diagnostic_py_MaxwellSpectralNetwork["MaxwellSpectralNetwork"]
    class maxwell_orbital_diagnostic_py_MaxwellSpectralNetwork cls;
    maxwell_orbital_diagnostic_py --> maxwell_orbital_diagnostic_py_MaxwellSpectralNetwork
    maxwell_orbital_diagnostic_py_AnalyticalMultipoleSource["AnalyticalMultipoleSource"]
    class maxwell_orbital_diagnostic_py_AnalyticalMultipoleSource cls;
    maxwell_orbital_diagnostic_py --> maxwell_orbital_diagnostic_py_AnalyticalMultipoleSource
    app_py["app.py (py)"]
    class app_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_argparse["argparse"]
    class ext_argparse ext;
    maxwell_crystal_py -.->|imports| ext_argparse
    ext_torch["torch"]
    class ext_torch ext;
    maxwell_crystal_py -.->|imports| ext_torch
    ext_torch_nn["torch.nn"]
    class ext_torch_nn ext;
    maxwell_crystal_py -.->|imports| ext_torch_nn
    ext_torch_nn_functional["torch.nn.functional"]
    class ext_torch_nn_functional ext;
    maxwell_crystal_py -.->|imports| ext_torch_nn_functional
    ext_torch_optim["torch.optim"]
    class ext_torch_optim ext;
    maxwell_crystal_py -.->|imports| ext_torch_optim
    ext_torch_utils_data["torch.utils.data"]
    class ext_torch_utils_data ext;
    maxwell_crystal_py -.->|imports| ext_torch_utils_data
    ext_numpy["numpy"]
    class ext_numpy ext;
    maxwell_crystal_py -.->|imports| ext_numpy
    ext_os["os"]
    class ext_os ext;
    maxwell_crystal_py -.->|imports| ext_os
    ext_time["time"]
    class ext_time ext;
    maxwell_crystal_py -.->|imports| ext_time
    ext_json["json"]
    class ext_json ext;
    maxwell_crystal_py -.->|imports| ext_json
    ext_datetime["datetime"]
    class ext_datetime ext;
    maxwell_crystal_py -.->|imports| ext_datetime
    ext_typing["typing"]
    class ext_typing ext;
    maxwell_crystal_py -.->|imports| ext_typing
    ext_abc["abc"]
    class ext_abc ext;
    maxwell_crystal_py -.->|imports| ext_abc
    ext_dataclasses["dataclasses"]
    class ext_dataclasses ext;
    maxwell_crystal_py -.->|imports| ext_dataclasses
    ext_collections["collections"]
    class ext_collections ext;
    maxwell_crystal_py -.->|imports| ext_collections
    ext_logging["logging"]
    class ext_logging ext;
    maxwell_crystal_py -.->|imports| ext_logging
    ext_math["math"]
    class ext_math ext;
    maxwell_crystal_py -.->|imports| ext_math
    ext_copy["copy"]
    class ext_copy ext;
    maxwell_crystal_py -.->|imports| ext_copy
    ext_warnings["warnings"]
    class ext_warnings ext;
    maxwell_crystal_py -.->|imports| ext_warnings
    maxwell_crystallography_suite_py -.->|imports| ext_argparse
    maxwell_crystallography_suite_py -.->|imports| ext_copy
    ext_glob["glob"]
    class ext_glob ext;
    maxwell_crystallography_suite_py -.->|imports| ext_glob
    maxwell_crystallography_suite_py -.->|imports| ext_json
    maxwell_crystallography_suite_py -.->|imports| ext_logging
    maxwell_crystallography_suite_py -.->|imports| ext_math
    maxwell_crystallography_suite_py -.->|imports| ext_os
    ext_re["re"]
    class ext_re ext;
    maxwell_crystallography_suite_py -.->|imports| ext_re
    maxwell_crystallography_suite_py -.->|imports| ext_time
    maxwell_crystallography_suite_py -.->|imports| ext_warnings
    maxwell_crystallography_suite_py -.->|imports| ext_abc
    maxwell_crystallography_suite_py -.->|imports| ext_collections
    maxwell_crystallography_suite_py -.->|imports| ext_dataclasses
    maxwell_crystallography_suite_py -.->|imports| ext_datetime
    ext_pathlib["pathlib"]
    class ext_pathlib ext;
    maxwell_crystallography_suite_py -.->|imports| ext_pathlib
    maxwell_crystallography_suite_py -.->|imports| ext_typing
    ext_matplotlib["matplotlib"]
    class ext_matplotlib ext;
    maxwell_crystallography_suite_py -.->|imports| ext_matplotlib
    ext_matplotlib_pyplot["matplotlib.pyplot"]
    class ext_matplotlib_pyplot ext;
    maxwell_crystallography_suite_py -.->|imports| ext_matplotlib_pyplot
    ext_matplotlib_gridspec["matplotlib.gridspec"]
    class ext_matplotlib_gridspec ext;
    maxwell_crystallography_suite_py -.->|imports| ext_matplotlib_gridspec
    maxwell_crystallography_suite_py -.->|imports| ext_numpy
    maxwell_crystallography_suite_py -.->|imports| ext_torch
    maxwell_crystallography_suite_py -.->|imports| ext_torch_nn
    maxwell_crystallography_suite_py -.->|imports| ext_torch_nn_functional
    maxwell_crystallography_suite_py -.->|imports| ext_torch_optim
    maxwell_crystallography_suite_py -.->|imports| ext_torch_utils_data
    ext_scipy["scipy"]
    class ext_scipy ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy
    ext_scipy_stats["scipy.stats"]
    class ext_scipy_stats ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy_stats
    ext_scipy_linalg["scipy.linalg"]
    class ext_scipy_linalg ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy_linalg
    ext_scipy_optimize["scipy.optimize"]
    class ext_scipy_optimize ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy_optimize
    ext_scipy_sparse["scipy.sparse"]
    class ext_scipy_sparse ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy_sparse
    ext_scipy_sparse_linalg["scipy.sparse.linalg"]
    class ext_scipy_sparse_linalg ext;
    maxwell_crystallography_suite_py -.->|imports| ext_scipy_sparse_linalg
    ext_traceback["traceback"]
    class ext_traceback ext;
    maxwell_crystallography_suite_py -.->|imports| ext_traceback
    maxwell_field_hawking_suite_py -.->|imports| ext_argparse
    maxwell_field_hawking_suite_py -.->|imports| ext_glob
    maxwell_field_hawking_suite_py -.->|imports| ext_json
    maxwell_field_hawking_suite_py -.->|imports| ext_logging
    maxwell_field_hawking_suite_py -.->|imports| ext_math
    maxwell_field_hawking_suite_py -.->|imports| ext_os
    ext_pickle["pickle"]
    class ext_pickle ext;
    maxwell_field_hawking_suite_py -.->|imports| ext_pickle
    ext_io["io"]
    class ext_io ext;
    maxwell_field_hawking_suite_py -.->|imports| ext_io
    maxwell_field_hawking_suite_py -.->|imports| ext_re
    maxwell_field_hawking_suite_py -.->|imports| ext_time
    maxwell_field_hawking_suite_py -.->|imports| ext_warnings
    maxwell_field_hawking_suite_py -.->|imports| ext_datetime
    maxwell_field_hawking_suite_py -.->|imports| ext_pathlib
    maxwell_field_hawking_suite_py -.->|imports| ext_typing
    maxwell_field_hawking_suite_py -.->|imports| ext_dataclasses
    maxwell_field_hawking_suite_py -.->|imports| ext_abc
    maxwell_field_hawking_suite_py -.->|imports| ext_numpy
    maxwell_field_hawking_suite_py -.->|imports| ext_torch
    maxwell_field_hawking_suite_py -.->|imports| ext_torch_nn
    maxwell_field_hawking_suite_py -.->|imports| ext_torch_nn_functional
    ext_scipy_fft["scipy.fft"]
    class ext_scipy_fft ext;
    maxwell_field_hawking_suite_py -.->|imports| ext_scipy_fft
    maxwell_field_hawking_suite_py -.->|imports| ext_scipy_stats
    maxwell_field_hawking_suite_py -.->|imports| ext_scipy_linalg
    maxwell_field_hawking_suite_py -.->|imports| ext_matplotlib
    maxwell_field_hawking_suite_py -.->|imports| ext_matplotlib_pyplot
    maxwell_field_hawking_suite_py -.->|imports| ext_matplotlib_gridspec
    maxwell_field_hawking_suite_py -.->|imports| ext_traceback
    maxwell_magnetic_orbitals_py -.->|imports| ext_argparse
    maxwell_magnetic_orbitals_py -.->|imports| ext_glob
    maxwell_magnetic_orbitals_py -.->|imports| ext_json
    maxwell_magnetic_orbitals_py -.->|imports| ext_logging
    maxwell_magnetic_orbitals_py -.->|imports| ext_math
    maxwell_magnetic_orbitals_py -.->|imports| ext_os
    maxwell_magnetic_orbitals_py -.->|imports| ext_warnings
    maxwell_magnetic_orbitals_py -.->|imports| ext_datetime
    maxwell_magnetic_orbitals_py -.->|imports| ext_pathlib
    maxwell_magnetic_orbitals_py -.->|imports| ext_typing
    maxwell_magnetic_orbitals_py -.->|imports| ext_dataclasses
    maxwell_magnetic_orbitals_py -.->|imports| ext_numpy
    ext_scipy_special["scipy.special"]
    class ext_scipy_special ext;
    maxwell_magnetic_orbitals_py -.->|imports| ext_scipy_special
    maxwell_magnetic_orbitals_py -.->|imports| ext_torch
    maxwell_magnetic_orbitals_py -.->|imports| ext_torch_nn
    maxwell_magnetic_orbitals_py -.->|imports| ext_torch_nn_functional
    maxwell_magnetic_orbitals_py -.->|imports| ext_matplotlib
    maxwell_magnetic_orbitals_py -.->|imports| ext_matplotlib_pyplot
    maxwell_magnetic_orbitals_py -.->|imports| ext_matplotlib_gridspec
    ext_scipy_ndimage["scipy.ndimage"]
    class ext_scipy_ndimage ext;
    maxwell_magnetic_orbitals_py -.->|imports| ext_scipy_ndimage
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_argparse
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_glob
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_json
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_logging
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_os
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_warnings
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_math
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_datetime
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_pathlib
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_typing
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_dataclasses
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_numpy
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_scipy_special
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_scipy_fft
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_torch
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_torch_nn
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_torch_nn_functional
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_matplotlib
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_matplotlib_pyplot
    maxwell_magnetic_orbitals_v2_py -.->|imports| ext_matplotlib_gridspec
    maxwell_orbital_diagnostic_py -.->|imports| ext_argparse
    maxwell_orbital_diagnostic_py -.->|imports| ext_glob
    maxwell_orbital_diagnostic_py -.->|imports| ext_json
    maxwell_orbital_diagnostic_py -.->|imports| ext_logging
    maxwell_orbital_diagnostic_py -.->|imports| ext_os
    maxwell_orbital_diagnostic_py -.->|imports| ext_warnings
    maxwell_orbital_diagnostic_py -.->|imports| ext_math
    maxwell_orbital_diagnostic_py -.->|imports| ext_datetime
    maxwell_orbital_diagnostic_py -.->|imports| ext_pathlib
    maxwell_orbital_diagnostic_py -.->|imports| ext_typing
    maxwell_orbital_diagnostic_py -.->|imports| ext_dataclasses
    maxwell_orbital_diagnostic_py -.->|imports| ext_numpy
    maxwell_orbital_diagnostic_py -.->|imports| ext_scipy_special
    maxwell_orbital_diagnostic_py -.->|imports| ext_torch
    maxwell_orbital_diagnostic_py -.->|imports| ext_torch_nn
    maxwell_orbital_diagnostic_py -.->|imports| ext_torch_nn_functional
    maxwell_orbital_diagnostic_py -.->|imports| ext_matplotlib
    maxwell_orbital_diagnostic_py -.->|imports| ext_matplotlib_pyplot
    maxwell_orbital_diagnostic_py -.->|imports| ext_matplotlib_gridspec
```

---

## Architecture Reference

### PY (7 files)

#### `app.py`
**Path:** `app.py`

*No symbols extracted*

#### `maxwell_crystal.py`
**Path:** `maxwell_crystal.py`

**Classs:**
- `Config` (line 56) - *Central configuration for all hyperparameters, architecture sizes, and protocol constants.*
- `IPhaseDetector` (line 257) - *Abstract interface for phase detection in neural network training.*
- `IMetricCalculator` (line 266) - *Abstract interface for metric calculation.*
- `SeedManager` (line 275) - *Deterministic seed management for reproducibility.*
- `LoggerFactory` (line 290) - *Factory for creating consistently formatted loggers.*
- `MaxwellOperator` (line 308) - *Maxwell equations operator for 2D TM polarization (Ex, Ey, Bz).

Implements spectral (Fourier-space) derivatives for the curl operator on
a periodic square grid.  Time evolution uses an Euler forward step with
unitarity-preserving norm rescaling.

dBz/dt = -(dEy/dx - dEx/dy)
dEx/dt =  dBz/dy
dEy/dt = -dBz/dx*
- `SpectralStatisticsCalculator` (line 396) - *Spectral statistics engine for GOE/GUE analysis (Chapter 10).

Generates random matrix ensembles interpolating between the Gaussian
Orthogonal Ensemble (imaginary_ratio=0) and the Gaussian Unitary
Ensemble (imaginary_ratio=1), then evaluates nearest-neighbor spacing
P(s), pair correlation R_2(s), and the Dyson beta index.*
- `SpectralLayer` (line 610) - *Fourier-domain convolutional layer with tuneable imaginary ratio.

The imaginary_ratio parameter controls the transition between GOE-like
(real symmetric kernel) and GUE-like (complex Hermitian kernel)
spectral statistics of the operator.*
- `MaxwellSpectralNetwork` (line 688) - *Neural network for learning Maxwell equation dynamics on a 2D grid.

Input/output: 6 real channels encoding (Re, Im) of (Ex, Ey, Bz).
Architecture: 1x1 projection --> expansion --> spectral layers --> contraction --> 1x1.*
- `HamiltonianBackbone` (line 749) - *Pre-trained backbone for single-channel Hamiltonian inference.*
- `HamiltonianInferenceEngine` (line 780) - *Dispatch layer that tries to load a pre-trained backbone and falls back
to the analytical Maxwell operator.*
- `MaxwellPotentialGenerator` (line 840) - *Generate source configurations and background media for the Maxwell system.

Potentials here represent spatially varying permittivity profiles and
external current sources that break translational symmetry.*
- `MaxwellDataset` (line 903) - *Dataset of electromagnetic field evolution samples.

Each sample consists of an initial (Ex, Ey, Bz) configuration encoded
as 6 real channels (Re + Im interleaved) and the time-evolved target.*
- `FullFourierAnalyzer` (line 1033) - *Complete 2D Fourier analysis with radial profiles and Bragg peak detection.*
- `FourierMassCenterAnalyzer` (line 1183) - *Centre-of-mass and inertia-tensor analysis in Fourier space.*
- `TopologicalPhaseDetector` (line 1247) - *Hysteretic phase detector combining alignment, localisation, and resonance signals.*
- `SpectralFieldExtractor` (line 1312) - *Extract spectral weight tensors from spectral layers of a model.*
- `TopologicalCrystallizationLoss` (line 1333) - *Loss function driving the system toward topological crystal order.*
- `CrystallizationPressureApplicator` (line 1365) - *Apply weight decay pressure proportional to phase crystallinity.*
- `TopologicalMetricsCalculator` (line 1384) - *Orchestrate topological phase detection, loss, and pressure application.*
- `LocalComplexityAnalyzer` (line 1453) - *Compute local complexity via cosine-similarity dispersion of weight vectors.*
- `SuperpositionAnalyzer` (line 1472) - *Measure average off-diagonal correlation between weight rows.*
- `CrystallographyMetricsCalculator` (line 1495) - *Compute the five primary observables from the paper:
kappa, delta, alpha, T_eff, hbar_eff, plus Poynting vector diagnostics.*
- `ThermodynamicMetricsCalculator` (line 1699) - *Effective temperature, specific heat, Gibbs free energy, and critical temperature.*
- `SpectralGeometryCalculator` (line 1773) - *Spectral gap, effective dimension, participation ratio, and level-spacing ratio.*
- `RicciCurvatureCalculator` (line 1819) - *Ricci scalar and mean sectional curvature of the weight manifold.*
- `PerelmanRicciFlow` (line 1865) - *Ricci flow with Perelman surgery for singularity resolution.*
- `SpectroscopyMetricsCalculator` (line 2061) - *Weight-space diffraction analysis: Bragg peaks, spectral entropy.*
- `LambdaPressureScheduler` (line 2101) - *Exponentially growing discretisation pressure lambda(t).*
- `AdaptiveLambdaScheduler` (line 2144) - *Lambda scheduler that accelerates growth when topological phase is detected.*
- `AnnealingScheduler` (line 2169) - *Simulated annealing with exponential cooling and Metropolis acceptance.*
- `TopologicalAnnealingScheduler` (line 2202) - *Annealing scheduler with adaptive cooling guided by topological signals.*
- `TrainingMetricsMonitor` (line 2222) - *Accumulate, store, and format all training metrics across epochs.*
- `CheckpointManager` (line 2353) - *Periodic checkpoint saving with rotation and latest-link semantics.*
- `GlassStateDetector` (line 2407) - *Detect whether the system is trapped in a glassy (non-crystalline) state.*
- `WeightIntegrityChecker` (line 2467) - *Detect NaN and Inf corruption in model parameters.*
- `TrainingEngine` (line 2498) - *Core training loop with metric collection, gradient injection, and Ricci regularisation.*
- `Phase0Orchestrator` (line 2665) - *Phase 0: Spectral Kernel Ratio Optimization.

Sweeps imaginary_ratio to find the value that minimises the combined
P(s) + R_2(s) loss relative to the GUE target, following Chapter 10.*
- `BatchSizeProspector` (line 2727) - *Phase 1: Evaluate candidate batch sizes for delta and kappa performance.*
- `SeedMiner` (line 2786) - *Phase 2: Mine for optimal random seed via short training probes.*
- `FullTrainingOrchestrator` (line 2881) - *Phase 3: Full training with grokking detection and adaptive lambda pressure.*
- `RefinementOrchestrator` (line 3002) - *Phase 4: Simulated annealing refinement toward perfect crystal.*

**Functions:**
- `main` (line 3112) - *Entry point: parse arguments, run the five-phase protocol.*
- `detect` (line 261) - *Detect phase characteristics from spectral field data.*
- `compute` (line 270) - *Compute metrics for the given model and optional keyword arguments.*
- `set_seed` (line 279) - *Set random seeds across all relevant libraries and backends.*
- `create_logger` (line 294) - *Create and return a configured logger instance.*
- `__init__` (line 321) - *Precompute wavenumber grids and material constants.*
- `_precompute_operators` (line 331) - *Build Fourier-space wavenumber grids.*
- `apply_maxwell_operator` (line 339) - *Apply the Maxwell curl operator to a (batch, 3, H, W) real tensor.

Channel ordering: 0=Ex, 1=Ey, 2=Bz.
Returns dF/dt of the same shape.*
- `time_evolution` (line 371) - *Advance electromagnetic fields by one time step using Euler integration
with norm-preserving rescaling.*
- `__init__` (line 406) - *Store reference to global configuration.*
- `generate_goe_matrix` (line 411) - *Return a sample from the Gaussian Orthogonal Ensemble.*
- `generate_gue_matrix` (line 417) - *Return a sample from the Gaussian Unitary Ensemble.*
- `generate_interpolated_matrix` (line 425) - *Return a complex Hermitian matrix interpolating between GOE and GUE.

imaginary_ratio = 0  -->  real symmetric  (GOE)
imaginary_ratio = 1  -->  complex Hermitian (GUE)*
- `compute_eigenvalue_spacing` (line 443) - *Unfold eigenvalues via polynomial fit and return normalised spacings.*
- `compute_spacing_distribution_loss` (line 458) - *MSE between the empirical P(s) histogram and the Wigner surmise.

GOE: P(s) = (pi/2) s exp(-pi s^2 / 4)
GUE: P(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)*
- `compute_dyson_index` (line 481) - *Estimate Dyson beta from small-spacing power-law P(s) ~ s^beta.

beta = 1 for GOE, beta = 2 for GUE.*
- `compute_pair_correlation` (line 506) - *Two-level correlation function R_2(s).

For GUE the theoretical form is R_2(s) = 1 - (sin(pi s)/(pi s))^2.*
- `compute_correlation_loss` (line 533) - *MSE between empirical R_2(s) and the analytical prediction.*
- `compute_spectral_stats_for_ratio` (line 552) - *Ensemble-averaged spectral statistics at a given imaginary ratio.

Returns P(s) loss, R_2 loss, Dyson beta, and combined losses for both
GOE and GUE targets.*
- `__init__` (line 619) - *Initialise real and imaginary kernel parameters.*
- `_apply_imaginary_ratio` (line 638) - *Scale the imaginary kernel by the imaginary ratio at init time.*
- `set_imaginary_ratio` (line 643) - *Rescale imaginary kernel to reflect a new imaginary ratio.*
- `forward` (line 651) - *Apply spectral convolution in Fourier space.*
- `get_spectral_operator` (line 674) - *Extract a (channels x channels) complex matrix for eigenvalue analysis.

The real part is symmetrised, the imaginary part anti-symmetrised,
yielding a Hermitian-like operator suitable for GOE/GUE diagnostics.*
- `__init__` (line 696) - *Build all sub-layers with the given architectural parameters.*
- `forward` (line 721) - *Forward pass through the full spectral network.*
- `set_imaginary_ratio` (line 732) - *Propagate imaginary ratio to all spectral layers.*
- `get_kernel_ratio` (line 738) - *Compute the effective imaginary-to-real kernel norm ratio.*
- `__init__` (line 752) - *Build the backbone with spectral layers.*
- `forward` (line 768) - *Single-channel forward pass.*
- `__init__` (line 786) - *Attempt backbone load; fall back to analytical operator.*
- `_try_load_backbone` (line 794) - *Load backbone weights from disk if available and enabled.*
- `apply_operator` (line 829) - *Apply the Maxwell operator to the electromagnetic field tensor.*
- `time_evolve` (line 833) - *Advance fields by one time step.*
- `__init__` (line 848) - *Store grid parameters from configuration.*
- `gaussian_source` (line 853) - *Smooth Gaussian current-density envelope centred on the grid.*
- `dipole_source` (line 861) - *1/r dipole-like source envelope.*
- `plane_wave_source` (line 870) - *Sinusoidal plane-wave seed for Ex, Ey components.*
- `periodic_medium` (line 879) - *Periodic permittivity modulation (photonic-crystal-like).*
- `generate_mixed_source` (line 886) - *Dirichlet-weighted superposition of all source types.*
- `__init__` (line 911) - *Generate all samples at construction time.*
- `_generate_initial_fields` (line 954) - *Create a random initial electromagnetic field configuration.

Returns a (3, H, W) complex tensor [Ex, Ey, Bz] and a scalar energy.*
- `_time_evolve_fields` (line 983) - *Advance the EM field through multiple time steps under the Maxwell operator.*
- `_fields_to_real_imag` (line 1012) - *Convert (3, H, W) complex tensor to (6, H, W) real tensor.*
- `__len__` (line 1020) - *Number of training samples.*
- `__getitem__` (line 1024) - *Return (input, target) pair for training.*
- `get_validation_batch` (line 1028) - *Return the full validation set as a single batch.*
- `__init__` (line 1036) - *Precompute wavenumber magnitude grid.*
- `compute_full_spectrum` (line 1045) - *Return magnitude, phase, power, radial profile, and derived statistics.*
- `detect_bragg_peaks` (line 1098) - *Identify local maxima in the power spectrum exceeding a statistical threshold.*
- `compute_resonance_metrics` (line 1146) - *Aggregate spectral concentration, phase coherence, and Bragg analysis.*
- `__init__` (line 1186) - *Initialise wavenumber grids and full Fourier sub-analyzer.*
- `compute_mass_center` (line 1195) - *Return centre of mass, inertia tensor, anisotropy, and resonance diagnostics.*
- `__init__` (line 1250) - *Initialise history buffers and state variables.*
- `detect` (line 1258) - *Run full topological phase detection and return diagnostic dict.*
- `extract` (line 1316) - *Return the mean complex spectral kernel across all spectral layers.*
- `__init__` (line 1336) - *Initialise with base lambda pressure.*
- `forward` (line 1342) - *Compute quadrant, localisation, and resonance penalty terms.*
- `__init__` (line 1368) - *Store pressure decay rate from config.*
- `apply` (line 1373) - *Multiplicatively decay parameters when crystal phase is detected.*
- `__init__` (line 1387) - *Initialise all topological sub-components.*
- `compute` (line 1395) - *Extract spectral field, detect phase, compute loss, return full metrics dict.*
- `apply_crystallization_pressure` (line 1429) - *Delegate pressure application to the sub-component.*
- `_empty_metrics` (line 1436) - *Return a zero-valued metrics dict when topological analysis is disabled.*
- `compute_local_complexity` (line 1457) - *Return a scalar in [0, 1] measuring weight diversity.*
- `compute_superposition` (line 1476) - *Return the mean absolute off-diagonal Pearson correlation.*
- `__init__` (line 1501) - *Store config and create logger.*
- `compute` (line 1506) - *Facade that delegates to compute_all_metrics.*
- `compute_kappa` (line 1512) - *Gradient covariance condition number kappa = lambda_max / lambda_min.*
- `compute_discretization_margin` (line 1563) - *delta = max_i |theta_i - round(theta_i)|.*
- `compute_alpha_purity` (line 1572) - *alpha = -log(delta).*
- `compute_kappa_quantum` (line 1579) - *Quantum-regularised condition number with hbar regularisation.*
- `compute_poynting_vector` (line 1601) - *Compute the electromagnetic Poynting-like energy flow through the network.*
- `compute_hbar_effective` (line 1651) - *hbar_eff = delta^2 * lambda / omega.*
- `compute_all_metrics` (line 1661) - *Compute delta, alpha, kappa, kappa_q, poynting, purity, and is_crystal.*
- `__init__` (line 1702) - *Store config reference.*
- `compute` (line 1706) - *Return all thermodynamic observables.*
- `compute_effective_temperature` (line 1727) - *T_eff = (lr / 2) * Var(grad).*
- `compute_specific_heat` (line 1750) - *C_v = Var(U) / T^2.*
- `compute_gibbs_free_energy` (line 1762) - *G = delta - T * (-alpha).*
- `compute_critical_temperature` (line 1768) - *T_c = T_0 * exp(-c * alpha).*
- `__init__` (line 1776) - *Store config reference.*
- `compute` (line 1780) - *Compute spectral geometry observables from weight outer product.*
- `_compute_level_spacing_ratio` (line 1806) - *Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}) over consecutive spacings.*
- `__init__` (line 1822) - *Store config reference.*
- `compute` (line 1826) - *Compute Ricci scalar and sectional curvatures from weight metric.*
- `_compute_ricci_scalar` (line 1842) - *Ricci scalar via inverse eigenvalue sum.*
- `_estimate_sectional_curvatures` (line 1851) - *Sample 2x2 sub-block determinants as sectional curvature proxies.*
- `__init__` (line 1868) - *Initialise curvature history and surgery counter.*
- `compute_ricci_scalar_fast` (line 1877) - *Fast Ricci scalar estimate from normalised weight outer product.*
- `compute_local_curvature` (line 1907) - *Second-difference curvature estimate along the flattened parameter.*
- `compute_anisotropy` (line 1916) - *Ratio of smallest to largest covariance eigenvalue of the weight vector.*
- `compute_ricci_regularization_loss` (line 1941) - *Smoothness penalty proportional to second-difference curvature.*
- `apply_ricci_flow_step` (line 1959) - *One step of diffusive Ricci flow smoothing on all parameters.*
- `perform_perelman_surgery` (line 1989) - *Cut singularities (outlier weights) when curvature exceeds the surgery threshold.*
- `compute_adaptive_lr_factor` (line 2031) - *Reduce learning rate when curvature spikes above recent average.*
- `get_flow_metrics` (line 2047) - *Return summary Ricci-flow diagnostics.*
- `__init__` (line 2064) - *Store config reference.*
- `compute` (line 2068) - *Compute weight diffraction pattern and spectral entropy.*
- `compute_weight_diffraction` (line 2073) - *FFT of concatenated weights with peak detection.*
- `_compute_spectral_entropy` (line 2092) - *Shannon entropy of the normalised power spectrum.*
- `__init__` (line 2104) - *Initialise lambda in float64 precision.*
- `current_lambda` (line 2114) - *Current pressure value.*
- `step` (line 2118) - *Increase lambda at fixed epoch intervals.*
- `compute_regularization_loss` (line 2126) - *L2 penalty on distance from nearest integer for each parameter.*
- `set_lambda` (line 2139) - *Directly set the lambda value.*
- `__init__` (line 2147) - *Initialise base and accelerated growth factors.*
- `step_adaptive` (line 2153) - *Grow lambda faster when topological order is emerging.*
- `__init__` (line 2172) - *Initialise temperature schedule.*
- `temperature` (line 2180) - *Current annealing temperature.*
- `step` (line 2184) - *Cool by one step.*
- `accept_perturbation` (line 2188) - *Metropolis acceptance criterion.*
- `should_restart` (line 2197) - *Whether the current state has drifted too far from best.*
- `__init__` (line 2205) - *Initialise with base cooling rate.*
- `step_adaptive` (line 2210) - *Slow cooling when alignment is growing, speed up when it recedes.*
- `__init__` (line 2225) - *Initialise metric history buffers.*
- `update_metrics` (line 2257) - *Append each provided metric to its history list.*
- `compute_delta_slope` (line 2269) - *Linear regression slope of recent delta values.*
- `format_progress_bar` (line 2282) - *Format all metrics into a multi-line progress string.*
- `__init__` (line 2356) - *Create checkpoint directory and initialise timer.*
- `should_save_checkpoint` (line 2366) - *True when at least CHECKPOINT_INTERVAL_MINUTES have elapsed.*
- `save_checkpoint` (line 2370) - *Save model, optimiser, metrics, and config to a timestamped file and latest link.*
- `load_latest_checkpoint` (line 2399) - *Load the latest checkpoint if it exists.*
- `__init__` (line 2410) - *Initialise patience buffer.*
- `should_stop` (line 2416) - *Return True if recent metrics indicate glass formation.*
- `is_crystal_formed` (line 2452) - *Return True if all metrics are below crystal thresholds.*
- `check` (line 2471) - *Return integrity report with counts and corruption ratio.*
- `__init__` (line 2501) - *Instantiate all metric calculators.*
- `compute_weight_metrics` (line 2515) - *Local complexity and superposition averaged over all weight matrices.*
- `compute_norm_conservation_error` (line 2530) - *Relative norm difference between input and output.*
- `train_single_epoch` (line 2540) - *Run one epoch of gradient descent with optional regularisation.*
- `validate` (line 2578) - *Compute validation loss and accuracy.*
- `collect_all_metrics` (line 2590) - *Compute every metric from the paper and return as a flat dict.*
- `__init__` (line 2673) - *Initialise spectral statistics calculator.*
- `optimize_kernel_ratio` (line 2679) - *Sweep imaginary ratios and return the one with lowest combined GUE loss.*
- `__init__` (line 2730) - *Store engine reference and optimal imaginary ratio.*
- `prospect` (line 2737) - *Train briefly at each candidate batch size and return the best.*
- `__init__` (line 2789) - *Store references for dataset and model creation.*
- `mine` (line 2798) - *Evaluate seeds and return the one with best delta velocity and kappa.*
- `__init__` (line 2884) - *Store all training configuration.*
- `run_phase3_training` (line 2894) - *Execute Phase 3 and return (model, optimiser, monitor).*
- `__init__` (line 3005) - *Store all refinement parameters.*
- `run_phase4_refinement` (line 3021) - *Run Phase 4 refinement and return the best model.*
- `load_latest_checkpoint` (line 3193)
- `safe_compute` (line 1672)
- `safe_get` (line 2286)

#### `maxwell_crystallography_suite.py`
**Path:** `maxwell_crystallography_suite.py`

**Classs:**
- `CrystallographySuiteConfig` (line 59) - *Master configuration for the complete Maxwell crystallography suite.*
- `LoggerFactory` (line 201) - *Factory for creating configured logger instances.*
- `IMetricCalculator` (line 218) - *Protocol for metric calculation strategies.*
- `IPhaseDetector` (line 226) - *Protocol for phase detection strategies.*
- `SpectralLayer` (line 234) - *Spectral convolution layer with tuneable imaginary ratio for GOE/GUE control.*
- `MaxwellSpectralNetwork` (line 288) - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `GOEGUESpectralAnalyzer` (line 331) - *Chapter 10 spectral universality analyzer.

Extracts the spectral operator from each SpectralLayer, computes its
eigenvalue statistics, and determines proximity to GOE (beta=1) or
GUE (beta=2) universality via P(s), R_2(s), and the Dyson index.*
- `WeightIntegrityCalculator` (line 528) - *Detect NaN and Inf corruption in model parameters.*
- `DiscretizationCalculator` (line 559) - *Delta, alpha purity, and spectral entropy of the weight distribution.*
- `SpectralGeometryCalculator` (line 602) - *Spectral gap, effective dimension, participation ratio, and level-spacing ratio.*
- `RicciCurvatureCalculator` (line 650) - *Ricci scalar and mean sectional curvature of the weight manifold.*
- `BerryPhaseCalculator` (line 695) - *Berry phase from training checkpoint trajectory.*
- `ControlSystemAnalyzer` (line 784) - *Control theory stability analysis for neural network dynamics.*
- `ThermodynamicCalculator` (line 842) - *Gibbs free energy, critical temperature, and phase classification.*
- `FullFourierAnalyzer` (line 881) - *Complete 2D Fourier analysis with spectral concentration and resonance metrics.*
- `FourierMassCenterAnalyzer` (line 924) - *Centre-of-mass in Fourier space for topological phase detection.*
- `TopologicalPhaseDetector` (line 962) - *Hysteretic phase detector combining alignment and resonance signals.*
- `SpectralFieldExtractor` (line 996) - *Extract spectral weight tensors from SpectralLayer modules.*
- `TopologicalMetricsCalculator` (line 1015) - *Topological metrics from model spectral fields.*
- `GradientDynamicsCalculator` (line 1051) - *Gradient covariance kappa and effective temperature.*
- `SchrodingerAnalyzer` (line 1110) - *Quantum mechanical analysis via Johnson-Lindenstrauss compressed wavefunction.*
- `ComprehensiveVisualizer` (line 1156) - *Generate multi-panel analysis figures for each checkpoint.*
- `CheckpointAnalyzer` (line 1451) - *Main analyzer orchestrating all metric calculations on a single checkpoint.*
- `BatchProcessor` (line 1575) - *Process all checkpoints in a directory, generating per-checkpoint and summary outputs.*
- `MaxwellCrystallographySuite` (line 1775) - *Main entry point for the Maxwell crystallography analysis suite.*

**Functions:**
- `main` (line 1850) - *Parse arguments and run the Maxwell crystallography suite.*
- `create_logger` (line 205) - *Create and return a configured logger.*
- `compute` (line 221) - *Compute metrics for the given model.*
- `detect` (line 229) - *Detect phase from spectral field.*
- `__init__` (line 237) - *Initialise real and imaginary kernel parameters.*
- `forward` (line 252) - *Apply spectral convolution in Fourier space.*
- `get_spectral_operator` (line 271) - *Extract (channels x channels) complex Hermitian-like matrix for eigenvalue analysis.*
- `get_kernel_ratio` (line 279) - *Return the imaginary-to-real kernel norm ratio.*
- `__init__` (line 291) - *Build all sub-layers with the given architectural parameters.*
- `forward` (line 309) - *Forward pass through the full spectral network.*
- `get_kernel_ratio` (line 320) - *Compute effective imaginary-to-real kernel norm ratio across all layers.*
- `__init__` (line 340) - *Store configuration reference.*
- `extract_spectral_operators` (line 344) - *Return the complex spectral operator from every SpectralLayer in the model.*
- `compute_eigenvalue_spacing` (line 353) - *Unfold eigenvalues and return normalised nearest-neighbour spacings.*
- `compute_spacing_distribution_loss` (line 368) - *MSE between empirical P(s) and Wigner surmise for GOE or GUE.*
- `compute_dyson_index` (line 385) - *Estimate the Dyson beta from small-spacing power-law P(s) ~ s^beta.*
- `compute_pair_correlation` (line 402) - *Two-level correlation function R_2(s).*
- `compute_correlation_loss` (line 423) - *MSE between empirical R_2(s) and analytical prediction.*
- `compute` (line 438) - *Run full GOE/GUE spectral analysis on all spectral layers.*
- `_empty_results` (line 512) - *Return zero-valued results when no spectral layers are found.*
- `__init__` (line 531) - *Store config reference.*
- `compute` (line 535) - *Return integrity report.*
- `__init__` (line 562) - *Store config reference.*
- `compute` (line 566) - *Compute delta, alpha, spectral entropy, and per-layer deltas.*
- `_compute_spectral_entropy` (line 588) - *Shannon entropy of the normalised power spectrum of concatenated weights.*
- `__init__` (line 605) - *Store config reference.*
- `compute` (line 609) - *Compute spectral geometry observables from weight outer product.*
- `_compute_level_spacing_ratio` (line 638) - *Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}).*
- `__init__` (line 653) - *Store config reference.*
- `compute` (line 657) - *Compute Ricci scalar and sectional curvatures from weight metric.*
- `_compute_ricci_scalar` (line 672) - *Ricci scalar via inverse eigenvalue sum.*
- `_estimate_sectional_curvatures` (line 681) - *Sample 2x2 sub-block determinants as sectional curvature proxies.*
- `__init__` (line 698) - *Initialise logger.*
- `load_checkpoints` (line 703) - *Load all .pth files sorted by epoch.*
- `_extract_epoch` (line 720) - *Parse epoch number from filename.*
- `flatten_kernel_params` (line 725) - *Concatenate all spectral layer kernels into a single complex vector.*
- `compute_berry_connection_discrete` (line 744) - *Discrete Berry connection between consecutive parameter snapshots.*
- `calculate_berry_phase` (line 755) - *Compute total Berry phase, winding number, and cumulative trajectory.*
- `__init__` (line 787) - *Store config reference.*
- `extract_state_space` (line 791) - *Extract a composite state-space (A, B, C, D) from weight matrices.*
- `analyze_stability` (line 821) - *Eigenvalue stability analysis of the state matrix.*
- `compute` (line 836) - *Run full control-theory analysis.*
- `__init__` (line 845) - *Store config reference.*
- `compute` (line 849) - *Compute thermodynamic potentials from crystallographic observables.*
- `_classify_phase` (line 866) - *Classify the thermodynamic phase of the model.*
- `__init__` (line 884) - *Precompute wavenumber grids.*
- `compute_full_spectrum` (line 893) - *Return magnitude, phase, power, and derived statistics.*
- `compute_resonance_metrics` (line 913) - *Aggregate spectral concentration into a resonance score.*
- `__init__` (line 927) - *Initialise wavenumber grids and sub-analyzers.*
- `compute_mass_center` (line 936) - *Return centre-of-mass coordinates and resonance diagnostics.*
- `__init__` (line 965) - *Initialise history buffers.*
- `detect` (line 973) - *Full topological phase detection returning diagnostic dict.*
- `extract` (line 1000) - *Return the mean complex spectral kernel across all spectral layers.*
- `__init__` (line 1018) - *Initialise sub-components.*
- `compute` (line 1024) - *Run topological detection and return metrics dict.*
- `_empty_metrics` (line 1042) - *Zero-valued metrics when analysis is disabled or unavailable.*
- `__init__` (line 1054) - *Store config reference.*
- `compute` (line 1058) - *Compute kappa, T_eff, and gradient variance from validation data.*
- `__init__` (line 1113) - *Initialise projection parameters.*
- `extract_compressed_wavefunction` (line 1119) - *Project the full parameter vector to a fixed-dimension wavefunction.*
- `_compress_johnson_lindenstrauss` (line 1134) - *Random projection preserving pairwise distances.*
- `compute` (line 1142) - *Compute wavefunction entropy, participation ratio, and quantum coherence.*
- `__init__` (line 1159) - *Store config reference.*
- `visualize_checkpoint_analysis` (line 1163) - *Render the full 5x4 analysis dashboard to a file.*
- `_plot_weight_distribution` (line 1194) - *Pie chart of valid / NaN / Inf parameter counts.*
- `_plot_spectral_analysis` (line 1206) - *Bar chart of spectral geometry observables.*
- `_plot_phase_diagram` (line 1217) - *Alpha vs T_eff phase diagram with crystal/glass boundaries.*
- `_plot_curvature_distribution` (line 1232) - *Bar chart of Ricci curvature summary statistics.*
- `_plot_level_spacing` (line 1243) - *Level spacing ratio with Wigner-Dyson and Poisson reference lines.*
- `_plot_eigenvalue_spectrum` (line 1253) - *Largest and smallest eigenvalue on log scale.*
- `_plot_thermodynamic_potentials` (line 1267) - *Gibbs free energy, entropy proxy, and critical temperature.*
- `_plot_topological_metrics` (line 1278) - *Phase state, alignment, and resonance scores.*
- `_plot_berry_phase` (line 1289) - *Berry phase arrow on the unit circle.*
- `_plot_control_stability` (line 1304) - *Stability margin and binary stability flag.*
- `_plot_quantum_metrics` (line 1314) - *Wavefunction entropy, participation ratio, and coherence.*
- `_plot_summary_table` (line 1325) - *Text summary of key observables and phase classification.*
- `_plot_layer_deltas` (line 1352) - *Horizontal bar chart of per-layer discretization margins.*
- `_plot_resonance_metrics` (line 1364) - *Spectral concentration and resonance score bars.*
- `_plot_spectral_concentration` (line 1374) - *Scatter of spectral gap vs participation ratio.*
- `_plot_health_score` (line 1384) - *Single-bar health score with traffic-light colouring.*
- `_plot_goe_gue_losses` (line 1393) - *Grouped bar chart comparing P(s) and R_2(s) losses for GOE and GUE.*
- `_plot_dyson_beta` (line 1410) - *Dyson beta index gauge with GOE and GUE reference markers.*
- `_plot_kernel_ratios` (line 1421) - *Per-layer imaginary-to-real kernel norm ratios.*
- `_plot_universality_gauge` (line 1438) - *Horizontal gauge showing interpolation between GOE and GUE.*
- `__init__` (line 1454) - *Instantiate all sub-calculators.*
- `analyze_checkpoint` (line 1471) - *Load a checkpoint, run every analyzer, and return the aggregated results dict.*
- `_compute_health_score` (line 1553) - *Weighted average of integrity, purity, MBL, and topological scores.*
- `__init__` (line 1578) - *Initialise analyzer and visualizer.*
- `process_directory` (line 1585) - *Iterate over all .pth files, analyze each, and save results.*
- `_generate_summary` (line 1616) - *Aggregate statistics and rank checkpoints by delta, alpha, accuracy, and health score.*
- `_generate_evolution_plots` (line 1735) - *Time-series plots of key metrics across training.*
- `__init__` (line 1778) - *Initialise the suite with all sub-components.*
- `run_analysis` (line 1785) - *Execute full analysis: batch processing, Berry phase, and summary.*
- `_generate_berry_phase_visualization` (line 1804) - *Dedicated Berry phase figure with phasor diagram and summary text.*
- `_extract` (line 1621)
- `_stats` (line 1624)
- `_checkpoint_id` (line 1630)
- `_best_entry` (line 1662)

#### `maxwell_field_hawking_suite.py`
**Path:** `maxwell_field_hawking_suite.py`

**Classs:**
- `AnalysisConfig` (line 67) - *Immutable master configuration for the combined analysis suite.*
- `LoggerFactory` (line 142) - *Factory for creating configured logger instances.*
- `CustomUnpickler` (line 158) - *Unpickler that handles unknown classes by creating dummy dict-like objects.*
- `SpectralLayer` (line 207) - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 242) - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `MetadataExtractor` (line 283) - *Extract metadata (epoch, loss, delta) from checkpoint dicts.*
- `GravitationalConstantCalculator` (line 331) - *G_eff from weight distance to discrete attractor and gradient magnitude.*
- `PlanckConstantCalculator` (line 366) - *hbar_eff from uncertainty, action quantisation, conductance, and information entropy.*
- `BoltzmannConstantCalculator` (line 412) - *k_B_eff from configuration entropy and thermal fluctuations.*
- `SpeedOfLightCalculator` (line 440) - *c_eff from Planck relation and spectral velocity of weight matrices.*
- `InformationalMassCalculator` (line 466) - *M_eff from Planck mass formula, active parameter count, and energy-mass relation.*
- `HorizonAreaCalculator` (line 500) - *A_eff from active parameter counts and entropy proxy.*
- `HawkingRadiationCalculator` (line 520) - *Full Hawking radiation thermodynamic analysis.*
- `WeightLatticeMapper` (line 596) - *Map neural network weights to a 3D dielectric lattice.*
- `PoissonSolver` (line 626) - *Spectral Poisson solver: nabla^2 phi = -rho / eps_0.*
- `ScatteringSolver` (line 652) - *EM scattering from dielectric contrast: S(k) ~ |FT(delta_eps)|^2.*
- `DielectricTensorAnalyzer` (line 683) - *Anisotropy analysis of the dielectric medium via the structure tensor.*
- `PhotonicEntropyCalculator` (line 714) - *Shannon entropy of the EM field energy distribution and density of modes.*
- `BandgapAnalyzer` (line 741) - *Photonic bandgap estimation from radial Fourier profile.*
- `ElectromagneticPhaseClassifier` (line 773) - *Crystal vs Glass classification from EM observables.*
- `MaxwellFieldAnalyzer` (line 807) - *Full Maxwell / Poisson electromagnetic field analysis pipeline.*
- `CombinedVisualizer` (line 863) - *Generate multi-panel dashboard combining Hawking and Maxwell analyses.*
- `CombinedAnalyzer` (line 1065) - *Orchestrator that runs both Hawking and Maxwell analyses on a single checkpoint.*
- `BatchAnalyzer` (line 1129) - *Process all checkpoints in a directory.*
- `DummyClass` (line 170)

**Functions:**
- `load_checkpoint_robust` (line 185) - *Load a checkpoint with multiple fallback strategies.*
- `main` (line 1227) - *Parse arguments and run the combined analysis suite.*
- `create_logger` (line 146) - *Create and return a configured logger.*
- `find_class` (line 161) - *Override to handle missing classes gracefully.*
- `_create_dummy_class` (line 168) - *Return a dummy class that acts like a dictionary.*
- `__init__` (line 210) - *Initialise real and imaginary kernel parameters.*
- `forward` (line 223) - *Apply spectral convolution in Fourier space.*
- `__init__` (line 245) - *Build all sub-layers.*
- `forward` (line 263) - *Forward pass through the full spectral network.*
- `get_flat_parameters` (line 274) - *Return all parameters as a single flat tensor.*
- `get_weight_dict` (line 278) - *Return all named parameter tensors as numpy arrays.*
- `extract` (line 287) - *Return a standardised metadata dict from any checkpoint format.*
- `_find_delta` (line 312) - *Recursively search for a delta value.*
- `__init__` (line 334) - *Store config reference.*
- `calculate` (line 338) - *Return G_alg, force, and crystallisation pressure.*
- `__init__` (line 369) - *Store config reference.*
- `calculate` (line 373) - *Return four estimates of hbar and their weighted unification.*
- `__init__` (line 415) - *Store config reference.*
- `calculate` (line 419) - *Return entropy-based and thermal k_B estimates.*
- `__init__` (line 443) - *Store config reference.*
- `calculate` (line 447) - *Return multiple c estimates.*
- `__init__` (line 469) - *Store config reference.*
- `calculate` (line 473) - *Return multiple mass estimates.*
- `__init__` (line 503) - *Store config reference.*
- `calculate` (line 507) - *Return effective area from active parameters and weight entropy.*
- `__init__` (line 523) - *Instantiate all sub-calculators.*
- `calculate` (line 533) - *Run the full Hawking radiation pipeline and return all results.*
- `__init__` (line 599) - *Store config reference.*
- `map` (line 603) - *Return (charge_density, permittivity) as 3D arrays.

Weights are flattened and embedded into a cubic grid.
Permittivity = 1 + scale * w_i.
Charge density = w_i.*
- `__init__` (line 629) - *Store config reference.*
- `solve` (line 633) - *Return the electrostatic potential phi on the 3D grid.*
- `compute_electric_field` (line 647) - *Return E = -grad(phi).*
- `__init__` (line 655) - *Store config reference.*
- `compute` (line 659) - *Return scattering intensity map, central slice, and peak analysis.*
- `__init__` (line 686) - *Store config reference.*
- `analyze` (line 690) - *Return eigenvalues of the gradient structure tensor and anisotropy ratio.*
- `__init__` (line 717) - *Store config reference.*
- `calculate` (line 721) - *Return field entropy, mode entropy, and their sum.*
- `__init__` (line 744) - *Store config reference.*
- `analyze` (line 748) - *Return radial profile, gap depth, and boolean bandgap detection.*
- `__init__` (line 776) - *Store config reference.*
- `classify` (line 780) - *Return phase name, crystal/glass flags, and confidence score.*
- `__init__` (line 810) - *Instantiate all sub-components.*
- `analyze` (line 821) - *Run the full EM pipeline on the model weights.*
- `__init__` (line 866) - *Store config reference.*
- `render` (line 870) - *Save a comprehensive 4x4 figure to disk.*
- `_plot_hawking_summary` (line 897) - *Hawking temperature and BH entropy bars.*
- `_plot_hawking_temperature` (line 906) - *Temperature gauge.*
- `_plot_hawking_entropy` (line 914) - *Bekenstein-Hawking entropy.*
- `_plot_hawking_constants` (line 921) - *Effective constants summary.*
- `_plot_potential_slice` (line 936) - *Central slice of electrostatic potential.*
- `_plot_scattering_slice` (line 944) - *kx-ky scattering intensity.*
- `_plot_dielectric_anisotropy` (line 954) - *Dielectric tensor eigenvalues.*
- `_plot_photonic_entropy` (line 964) - *Field and mode entropy bars.*
- `_plot_bandgap` (line 973) - *Radial Fourier profile and bandgap indicator.*
- `_plot_electric_field` (line 984) - *Electric field magnitude statistics.*
- `_plot_em_classification` (line 992) - *Phase classification text panel.*
- `_plot_combined_summary` (line 1010) - *Text summary combining both analyses.*
- `_plot_hawking_radiation_power` (line 1032) - *Radiation power bar.*
- `_plot_schwarzschild` (line 1039) - *Schwarzschild radius and surface gravity.*
- `_plot_evaporation` (line 1050) - *Evaporation timescale bar.*
- `_plot_purity` (line 1057) - *Delta and alpha purity bars.*
- `__init__` (line 1068) - *Instantiate sub-analyzers and visualizer.*
- `analyze_checkpoint` (line 1076) - *Load, analyze, visualize, and return aggregated results.*
- `__init__` (line 1132) - *Instantiate the single-checkpoint analyzer.*
- `process` (line 1138) - *Analyze one file or all .pth files in a directory.*
- `_build_summary` (line 1176) - *Aggregate statistics across checkpoints.*
- `_print_ranking` (line 1203) - *Log the best checkpoint by delta and alpha.*
- `_safe_stats` (line 1185)
- `_info` (line 1210)
- `__init__` (line 171)
- `get` (line 176)
- `keys` (line 178)
- `items` (line 180)

#### `maxwell_magnetic_orbitals.py`
**Path:** `maxwell_magnetic_orbitals.py`

**Classs:**
- `IsomorphismConfig` (line 40) - *Configuration for the magnetic orbital isomorphism experiment.*
- `LoggerFactory` (line 82) - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 96) - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 117) - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `ModelLoader` (line 141) - *Load the best Maxwell checkpoint.*
- `AnalyticalMultipoleSource` (line 184) - *Analytical electromagnetic multipole sources.

Fix 2: Real dipole B-field from B = (mu0/4pi)(3(m.r_hat)r_hat - m)/r^3.
Fix 1: theta = pi/2 (equatorial) for all 2D projections.
Fix 4: Proper multipole hierarchy -- l=1 dipole, l=2 quadrupole, etc.*
- `HallProjectionCalculator` (line 267) - *Fix 3: Multi-angle averaged Hall projection at equatorial theta = pi/2.

At theta=pi/2: nx=cos(phi), ny=sin(phi), nz=0.
We average over HALL_SENSOR_NUM_ANGLES phi values and add |Bz|^2.*
- `TomographicScanner` (line 292) - *Generate tomographic slices at different effective distances.*
- `HydrogenOrbitalCalculator` (line 310) - *Analytical hydrogen orbital wavefunctions.*
- `IsomorphismMetricsCalculator` (line 376) - *Quantify structural similarity between EM field patterns and hydrogen orbitals.*
- `OrbitalVisualizer` (line 404) - *Side-by-side EM field vs hydrogen orbital visualisation.*
- `MagneticOrbitalExperiment` (line 480) - *Main experiment: analytical control + network response for each orbital.

Fix 4: Only l=1 (p orbitals) use true dipole sources.
l=0 uses monopole proxy, l>=2 uses multipole scalar potential.*

**Functions:**
- `main` (line 585) - *Parse arguments and run the experiment.*
- `create_logger` (line 85) - *Create and return a configured logger.*
- `__init__` (line 98)
- `forward` (line 106) - *Apply spectral convolution in Fourier space.*
- `__init__` (line 119)
- `forward` (line 132)
- `__init__` (line 143)
- `load` (line 147) - *Return (model, info_dict) from the best available checkpoint.*
- `_fallback` (line 179)
- `__init__` (line 192) - *Precompute coordinate grids in the equatorial plane.*
- `generate` (line 205) - *Return a (6,H,W) source tensor for the l-th multipole.*
- `_dipole` (line 211) - *Analytical magnetic dipole B-field in equatorial plane.*
- `_multipole` (line 229) - *Higher-order multipole from scalar potential gradient.*
- `_monopole_proxy` (line 243) - *Isotropic l=0 proxy (current loop).*
- `_normalise_and_pack` (line 250) - *Sanitise, normalise, and pack into 6-channel tensor.*
- `get_analytical_density` (line 260) - *Return normalised |B|^2 for analytical control (no network).*
- `__init__` (line 274)
- `project` (line 277) - *Multi-angle averaged Hall projection.*
- `__init__` (line 294)
- `scan` (line 297) - *Return a list of 2D Hall projection slices.*
- `__init__` (line 312)
- `radial_wavefunction` (line 315) - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 323) - *Real spherical harmonic Y_l^m.*
- `probability_density_2d` (line 330) - *Fix 1: |psi(r, theta=pi/2, phi)|^2 in equatorial plane.*
- `sample_orbital_3d` (line 345) - *Monte Carlo rejection sampling of |psi|^2.*
- `__init__` (line 378)
- `compute` (line 381) - *Return spatial correlation, node overlap, symmetry correlation, KL divergence.*
- `__init__` (line 406)
- `visualize_comparison` (line 409) - *Render comparison figure with analytical control row.*
- `__init__` (line 487)
- `run` (line 498) - *Execute the full protocol.*
- `_analyze` (line 528) - *Full protocol for one orbital.*
- `_summary` (line 544) - *Aggregate.*
- `_interp` (line 562) - *Narrative interpretation.*
- `_print` (line 573) - *Log summary.*

#### `maxwell_magnetic_orbitals_v2.py`
**Path:** `maxwell_magnetic_orbitals_v2.py`

**Classs:**
- `Config` (line 55) - *Configuration for the v2 isomorphism experiment.*
- `LoggerFactory` (line 91) - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 105) - *Spectral convolution layer.*
- `MaxwellSpectralNetwork` (line 129) - *Neural network for learning Maxwell equation dynamics.*
- `AnalyticalMultipoleSource` (line 163) - *Analytical EM multipole sources.*
- `PoissonEvolver` (line 234) - *Strategy A: Evolve the dipole source using the Poisson equation.

Solves nabla^2 phi = -rho in Fourier space, computes E = -grad(phi),
and returns the field energy density.  This is pure Maxwell physics
with no neural network.*
- `ChannelAwareProjection` (line 270) - *Strategy B: Physically-informed input projection.

Instead of a single Conv2d(6, 32, 1) that scrambles channels,
this processes each field component (Ex, Ey, Bz) separately with
its own 2->hidden/3 projection, then concatenates.*
- `HallProjector` (line 296) - *Multi-angle averaged Hall projection.*
- `HydrogenOrbitalCalculator` (line 323) - *Analytical hydrogen orbital wavefunctions.*
- `Visualizer` (line 419) - *Comprehensive multi-strategy comparison visualisation.*
- `IsomorphismExperimentV2` (line 479) - *Multi-strategy isomorphism experiment.

For each orbital, runs:
  A) Analytical control (no network)
  B) Poisson evolution (pure physics)
  C) Full network (standard forward pass)
  D) Direct spectral (bypass input_proj, feed spectral layers directly)*

**Functions:**
- `spatial_corr` (line 387) - *Cosine similarity between two flattened maps.*
- `node_overlap` (line 393) - *Jaccard index of nodal regions.*
- `symmetry_corr` (line 402) - *Correlation of angular Fourier power spectra.*
- `full_metrics` (line 410) - *Compute all isomorphism metrics.*
- `main` (line 658) - *Parse arguments and run the v2 experiment.*
- `create_logger` (line 94) - *Create and return a configured logger.*
- `__init__` (line 107) - *Initialise real and imaginary kernel parameters.*
- `forward` (line 116) - *Apply spectral convolution in Fourier space.*
- `__init__` (line 131) - *Build all sub-layers.*
- `forward` (line 147) - *Standard forward pass.*
- `forward_spectral_only` (line 156) - *Apply only the spectral layers (bypass input/expansion projections).*
- `__init__` (line 165) - *Precompute coordinate grids.*
- `generate` (line 177) - *Return a (6,H,W) source tensor.*
- `_dipole` (line 183) - *Analytical magnetic dipole in equatorial plane.*
- `_multipole` (line 201) - *Higher-order multipole from scalar potential gradient.*
- `_monopole` (line 212) - *Isotropic l=0 proxy.*
- `_pack` (line 218) - *Normalise and pack into 6-channel tensor.*
- `get_density` (line 227) - *Return normalised |B|^2 for analytical control.*
- `__init__` (line 242) - *Store config reference.*
- `evolve` (line 246) - *Treat the Bz channel as charge density, solve Poisson, return |E|^2.

This mimics what the network should ideally learn: the electrostatic
response to a given source configuration.*
- `__init__` (line 278) - *Build per-component projections.*
- `forward` (line 288) - *Process each (Re, Im) pair separately then concatenate.*
- `__init__` (line 298) - *Store config reference.*
- `project_6ch` (line 302) - *Project a 6-channel field tensor to scalar density.*
- `project_energy` (line 316) - *Project an arbitrary multi-channel tensor to scalar energy density.*
- `__init__` (line 325) - *Store config reference.*
- `radial_wavefunction` (line 329) - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 337) - *Real spherical harmonic.*
- `density_2d` (line 344) - *2D |psi|^2 in equatorial plane.*
- `sample_3d` (line 357) - *Monte Carlo rejection sampling.*
- `__init__` (line 421) - *Store config reference.*
- `render` (line 425) - *Render comparison of all strategies for one orbital.*
- `__init__` (line 489) - *Initialise all sub-components.*
- `_load_model` (line 499) - *Load trained checkpoint.*
- `run` (line 527) - *Execute the full multi-strategy experiment.*
- `_analyze` (line 557) - *Run all strategies for one orbital.*
- `_summary` (line 591) - *Aggregate results across orbitals and strategies.*
- `_interpret` (line 624) - *Narrative interpretation.*
- `_print_summary` (line 646) - *Log the summary.*

#### `maxwell_orbital_diagnostic.py`
**Path:** `maxwell_orbital_diagnostic.py`

**Classs:**
- `DiagnosticConfig` (line 47) - *Configuration for the diagnostic suite.*
- `LoggerFactory` (line 80) - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 94) - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 128) - *Neural network for learning Maxwell equation dynamics.*
- `AnalyticalMultipoleSource` (line 182) - *Analytical EM multipole sources (same as corrected main script).*
- `HallProjectionCalculator` (line 254) - *Multi-angle averaged Hall projection at equatorial theta = pi/2.*
- `HydrogenOrbitalCalculator` (line 281) - *Analytical hydrogen orbital wavefunctions.*
- `PassthroughTest` (line 324) - *Mode 1: Identity-initialised network.

If isomorphism survives passthrough, the projection pipeline is correct.*
- `LayerTraceTest` (line 385) - *Mode 2: Layer-by-layer trace through a trained network.

Measures spatial correlation after every sub-layer to find where
the angular structure collapses.*
- `SymmetryTrainingTest` (line 499) - *Mode 3: Short training with rotational symmetry preservation loss.

Loss = MSE(output, target) + weight * SymmetryLoss
where SymmetryLoss penalises changes in the angular power spectrum
between input and output.*
- `DiagnosticSuite` (line 596) - *Orchestrate all three diagnostic modes.*

**Functions:**
- `compute_spatial_correlation` (line 316) - *Cosine similarity between two flattened density maps.*
- `main` (line 625) - *Parse arguments and run the diagnostic suite.*
- `create_logger` (line 83) - *Create and return a configured logger.*
- `__init__` (line 96) - *Initialise real and imaginary kernel parameters.*
- `forward` (line 105) - *Apply spectral convolution in Fourier space.*
- `init_identity` (line 117) - *Initialise kernels near identity: real=small, imag=0.*
- `__init__` (line 130) - *Build all sub-layers.*
- `forward` (line 146) - *Forward pass.*
- `forward_with_intermediates` (line 155) - *Forward pass returning the output after every sub-layer.*
- `init_identity` (line 167) - *Initialise all layers near identity / passthrough.*
- `__init__` (line 184) - *Precompute coordinate grids in the equatorial plane.*
- `generate` (line 196) - *Return a (6,H,W) source tensor for the l-th multipole.*
- `_dipole` (line 202) - *Analytical magnetic dipole B-field in equatorial plane.*
- `_multipole` (line 220) - *Higher-order multipole from scalar potential gradient.*
- `_monopole_proxy` (line 232) - *Isotropic l=0 proxy.*
- `_pack` (line 238) - *Sanitise, normalise, pack into 6 channels.*
- `get_analytical_density` (line 247) - *Return normalised |B|^2.*
- `__init__` (line 256) - *Store config reference.*
- `project` (line 260) - *Multi-angle averaged Hall projection.*
- `project_intermediate` (line 273) - *Project an intermediate activation to a scalar energy density.*
- `__init__` (line 283) - *Store config reference.*
- `radial_wavefunction` (line 287) - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 295) - *Real spherical harmonic Y_l^m.*
- `probability_density_2d` (line 302) - *2D |psi|^2 in equatorial plane (theta=pi/2).*
- `__init__` (line 330) - *Initialise sub-components.*
- `run` (line 338) - *Test all orbitals with an identity-initialised network.*
- `__init__` (line 392) - *Initialise sub-components.*
- `run` (line 400) - *Trace a trained model layer by layer.*
- `_find_collapse` (line 436) - *Find the layer where correlation drops most sharply.*
- `_plot_traces` (line 448) - *Plot correlation vs layer index for all orbitals.*
- `_load_model` (line 472) - *Load the trained model.*
- `__init__` (line 507) - *Initialise sub-components.*
- `compute_angular_power` (line 515) - *Compute the angular power spectrum of a 2D field via azimuthal FFT.*
- `symmetry_loss` (line 522) - *Penalise angular power spectrum distortion.*
- `run` (line 528) - *Train a fresh model with symmetry loss and track isomorphism.*
- `_plot_history` (line 572) - *Plot training loss and correlation over epochs.*
- `__init__` (line 598) - *Initialise all test modes.*
- `run_all` (line 606) - *Execute all three diagnostic modes and save results.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
