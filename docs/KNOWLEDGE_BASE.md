# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Total Files Parsed:** 8 | **Total Symbols Extracted:** 556 | **Total Imports:** 137

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray:5 5,color:#aaa;
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

**Classes:**
- `Config` (line 56) `class Config` - *Central configuration for all hyperparameters, architecture sizes, and protocol constants.*
- `IPhaseDetector` (line 257) `class IPhaseDetector(ABC)` - *Abstract interface for phase detection in neural network training.*
- `IMetricCalculator` (line 266) `class IMetricCalculator(ABC)` - *Abstract interface for metric calculation.*
- `SeedManager` (line 275) `class SeedManager` - *Deterministic seed management for reproducibility.*
- `LoggerFactory` (line 290) `class LoggerFactory` - *Factory for creating consistently formatted loggers.*
- `MaxwellOperator` (line 308) `class MaxwellOperator` - *Maxwell equations operator for 2D TM polarization (Ex, Ey, Bz).

Implements spectral (Fourier-space) derivatives for the curl operator on
a periodic square grid.  Time evolution uses an Euler forward step with
unitarity-preserving norm rescaling.

dBz/dt = -(dEy/dx - dEx/dy)
dEx/dt =  dBz/dy
dEy/dt = -dBz/dx*
- `SpectralStatisticsCalculator` (line 396) `class SpectralStatisticsCalculator` - *Spectral statistics engine for GOE/GUE analysis (Chapter 10).

Generates random matrix ensembles interpolating between the Gaussian
Orthogonal Ensemble (imaginary_ratio=0) and the Gaussian Unitary
Ensemble (imaginary_ratio=1), then evaluates nearest-neighbor spacing
P(s), pair correlation R_2(s), and the Dyson beta index.*
- `SpectralLayer` (line 610) `class SpectralLayer` - *Fourier-domain convolutional layer with tuneable imaginary ratio.

The imaginary_ratio parameter controls the transition between GOE-like
(real symmetric kernel) and GUE-like (complex Hermitian kernel)
spectral statistics of the operator.*
- `MaxwellSpectralNetwork` (line 688) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics on a 2D grid.

Input/output: 6 real channels encoding (Re, Im) of (Ex, Ey, Bz).
Architecture: 1x1 projection --> expansion --> spectral layers --> contraction --> 1x1.*
- `HamiltonianBackbone` (line 749) `class HamiltonianBackbone` - *Pre-trained backbone for single-channel Hamiltonian inference.*
- `HamiltonianInferenceEngine` (line 780) `class HamiltonianInferenceEngine` - *Dispatch layer that tries to load a pre-trained backbone and falls back
to the analytical Maxwell operator.*
- `MaxwellPotentialGenerator` (line 840) `class MaxwellPotentialGenerator` - *Generate source configurations and background media for the Maxwell system.

Potentials here represent spatially varying permittivity profiles and
external current sources that break translational symmetry.*
- `MaxwellDataset` (line 903) `class MaxwellDataset(Dataset)` - *Dataset of electromagnetic field evolution samples.

Each sample consists of an initial (Ex, Ey, Bz) configuration encoded
as 6 real channels (Re + Im interleaved) and the time-evolved target.*
- `FullFourierAnalyzer` (line 1033) `class FullFourierAnalyzer` - *Complete 2D Fourier analysis with radial profiles and Bragg peak detection.*
- `FourierMassCenterAnalyzer` (line 1183) `class FourierMassCenterAnalyzer` - *Centre-of-mass and inertia-tensor analysis in Fourier space.*
- `TopologicalPhaseDetector` (line 1247) `class TopologicalPhaseDetector(IPhaseDetector)` - *Hysteretic phase detector combining alignment, localisation, and resonance signals.*
- `SpectralFieldExtractor` (line 1312) `class SpectralFieldExtractor` - *Extract spectral weight tensors from spectral layers of a model.*
- `TopologicalCrystallizationLoss` (line 1333) `class TopologicalCrystallizationLoss` - *Loss function driving the system toward topological crystal order.*
- `CrystallizationPressureApplicator` (line 1365) `class CrystallizationPressureApplicator` - *Apply weight decay pressure proportional to phase crystallinity.*
- `TopologicalMetricsCalculator` (line 1384) `class TopologicalMetricsCalculator(IMetricCalculator)` - *Orchestrate topological phase detection, loss, and pressure application.*
- `LocalComplexityAnalyzer` (line 1453) `class LocalComplexityAnalyzer` - *Compute local complexity via cosine-similarity dispersion of weight vectors.*
- `SuperpositionAnalyzer` (line 1472) `class SuperpositionAnalyzer` - *Measure average off-diagonal correlation between weight rows.*
- `CrystallographyMetricsCalculator` (line 1495) `class CrystallographyMetricsCalculator(IMetricCalculator)` - *Compute the five primary observables from the paper:
kappa, delta, alpha, T_eff, hbar_eff, plus Poynting vector diagnostics.*
- `ThermodynamicMetricsCalculator` (line 1699) `class ThermodynamicMetricsCalculator(IMetricCalculator)` - *Effective temperature, specific heat, Gibbs free energy, and critical temperature.*
- `SpectralGeometryCalculator` (line 1773) `class SpectralGeometryCalculator(IMetricCalculator)` - *Spectral gap, effective dimension, participation ratio, and level-spacing ratio.*
- `RicciCurvatureCalculator` (line 1819) `class RicciCurvatureCalculator(IMetricCalculator)` - *Ricci scalar and mean sectional curvature of the weight manifold.*
- `PerelmanRicciFlow` (line 1865) `class PerelmanRicciFlow` - *Ricci flow with Perelman surgery for singularity resolution.*
- `SpectroscopyMetricsCalculator` (line 2061) `class SpectroscopyMetricsCalculator(IMetricCalculator)` - *Weight-space diffraction analysis: Bragg peaks, spectral entropy.*
- `LambdaPressureScheduler` (line 2101) `class LambdaPressureScheduler` - *Exponentially growing discretisation pressure lambda(t).*
- `AdaptiveLambdaScheduler` (line 2144) `class AdaptiveLambdaScheduler(LambdaPressureScheduler)` - *Lambda scheduler that accelerates growth when topological phase is detected.*
- `AnnealingScheduler` (line 2169) `class AnnealingScheduler` - *Simulated annealing with exponential cooling and Metropolis acceptance.*
- `TopologicalAnnealingScheduler` (line 2202) `class TopologicalAnnealingScheduler(AnnealingScheduler)` - *Annealing scheduler with adaptive cooling guided by topological signals.*
- `TrainingMetricsMonitor` (line 2222) `class TrainingMetricsMonitor` - *Accumulate, store, and format all training metrics across epochs.*
- `CheckpointManager` (line 2353) `class CheckpointManager` - *Periodic checkpoint saving with rotation and latest-link semantics.*
- `GlassStateDetector` (line 2407) `class GlassStateDetector` - *Detect whether the system is trapped in a glassy (non-crystalline) state.*
- `WeightIntegrityChecker` (line 2467) `class WeightIntegrityChecker` - *Detect NaN and Inf corruption in model parameters.*
- `TrainingEngine` (line 2498) `class TrainingEngine` - *Core training loop with metric collection, gradient injection, and Ricci regularisation.*
- `Phase0Orchestrator` (line 2665) `class Phase0Orchestrator` - *Phase 0: Spectral Kernel Ratio Optimization.

Sweeps imaginary_ratio to find the value that minimises the combined
P(s) + R_2(s) loss relative to the GUE target, following Chapter 10.*
- `BatchSizeProspector` (line 2727) `class BatchSizeProspector` - *Phase 1: Evaluate candidate batch sizes for delta and kappa performance.*
- `SeedMiner` (line 2786) `class SeedMiner` - *Phase 2: Mine for optimal random seed via short training probes.*
- `FullTrainingOrchestrator` (line 2881) `class FullTrainingOrchestrator` - *Phase 3: Full training with grokking detection and adaptive lambda pressure.*
- `RefinementOrchestrator` (line 3002) `class RefinementOrchestrator` - *Phase 4: Simulated annealing refinement toward perfect crystal.*

**Functions:**
- `main` (line 3112) `def main()` - *Entry point: parse arguments, run the five-phase protocol.*
- `detect` (line 261) `def detect(self, spectral_field)` - *Detect phase characteristics from spectral field data.*
- `compute` (line 270) `def compute(self, model)` - *Compute metrics for the given model and optional keyword arguments.*
- `set_seed` (line 279) `def set_seed(seed, device)` - *Set random seeds across all relevant libraries and backends.*
- `create_logger` (line 294) `def create_logger(name, level)` - *Create and return a configured logger instance.*
- `__init__` (line 321) `def __init__(self, config)` - *Precompute wavenumber grids and material constants.*
- `_precompute_operators` (line 331) `def _precompute_operators(self)` - *Build Fourier-space wavenumber grids.*
- `apply_maxwell_operator` (line 339) `def apply_maxwell_operator(self, fields)` - *Apply the Maxwell curl operator to a (batch, 3, H, W) real tensor.

Channel ordering: 0=Ex, 1=Ey, 2=Bz.
Returns dF/dt of the same shape.*
- `time_evolution` (line 371) `def time_evolution(self, fields, dt)` - *Advance electromagnetic fields by one time step using Euler integration
with norm-preserving rescaling.*
- `__init__` (line 406) `def __init__(self, config)` - *Store reference to global configuration.*
- `generate_goe_matrix` (line 411) `def generate_goe_matrix(size, device)` - *Return a sample from the Gaussian Orthogonal Ensemble.*
- `generate_gue_matrix` (line 417) `def generate_gue_matrix(size, device)` - *Return a sample from the Gaussian Unitary Ensemble.*
- `generate_interpolated_matrix` (line 425) `def generate_interpolated_matrix(self, size, imaginary_ratio, device)` - *Return a complex Hermitian matrix interpolating between GOE and GUE.

imaginary_ratio = 0  -->  real symmetric  (GOE)
imaginary_ratio = 1  -->  complex Hermitian (GUE)*
- `compute_eigenvalue_spacing` (line 443) `def compute_eigenvalue_spacing(self, eigenvalues)` - *Unfold eigenvalues via polynomial fit and return normalised spacings.*
- `compute_spacing_distribution_loss` (line 458) `def compute_spacing_distribution_loss(self, spacings, target)` - *MSE between the empirical P(s) histogram and the Wigner surmise.

GOE: P(s) = (pi/2) s exp(-pi s^2 / 4)
GUE: P(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)*
- `compute_dyson_index` (line 481) `def compute_dyson_index(self, eigenvalues, spacings)` - *Estimate Dyson beta from small-spacing power-law P(s) ~ s^beta.

beta = 1 for GOE, beta = 2 for GUE.*
- `compute_pair_correlation` (line 506) `def compute_pair_correlation(self, eigenvalues, s_range, num_points)` - *Two-level correlation function R_2(s).

For GUE the theoretical form is R_2(s) = 1 - (sin(pi s)/(pi s))^2.*
- `compute_correlation_loss` (line 533) `def compute_correlation_loss(self, eigenvalues, target)` - *MSE between empirical R_2(s) and the analytical prediction.*
- `compute_spectral_stats_for_ratio` (line 552) `def compute_spectral_stats_for_ratio(self, imaginary_ratio, matrix_size, num_matrices, device)` - *Ensemble-averaged spectral statistics at a given imaginary ratio.

Returns P(s) loss, R_2 loss, Dyson beta, and combined losses for both
GOE and GUE targets.*
- `__init__` (line 619) `def __init__(self, channels, grid_size, imaginary_ratio)` - *Initialise real and imaginary kernel parameters.*
- `_apply_imaginary_ratio` (line 638) `def _apply_imaginary_ratio(self)` - *Scale the imaginary kernel by the imaginary ratio at init time.*
- `set_imaginary_ratio` (line 643) `def set_imaginary_ratio(self, ratio)` - *Rescale imaginary kernel to reflect a new imaginary ratio.*
- `forward` (line 651) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `get_spectral_operator` (line 674) `def get_spectral_operator(self)` - *Extract a (channels x channels) complex matrix for eigenvalue analysis.

The real part is symmetrised, the imaginary part anti-symmetrised,
yielding a Hermitian-like operator suitable for GOE/GUE diagnostics.*
- `__init__` (line 696) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, field_components, imaginary_ratio)` - *Build all sub-layers with the given architectural parameters.*
- `forward` (line 721) `def forward(self, x)` - *Forward pass through the full spectral network.*
- `set_imaginary_ratio` (line 732) `def set_imaginary_ratio(self, ratio)` - *Propagate imaginary ratio to all spectral layers.*
- `get_kernel_ratio` (line 738) `def get_kernel_ratio(self)` - *Compute the effective imaginary-to-real kernel norm ratio.*
- `__init__` (line 752) `def __init__(self, grid_size, hidden_dim, num_spectral_layers)` - *Build the backbone with spectral layers.*
- `forward` (line 768) `def forward(self, x)` - *Single-channel forward pass.*
- `__init__` (line 786) `def __init__(self, config)` - *Attempt backbone load; fall back to analytical operator.*
- `_try_load_backbone` (line 794) `def _try_load_backbone(self)` - *Load backbone weights from disk if available and enabled.*
- `apply_operator` (line 829) `def apply_operator(self, fields)` - *Apply the Maxwell operator to the electromagnetic field tensor.*
- `time_evolve` (line 833) `def time_evolve(self, fields, dt)` - *Advance fields by one time step.*
- `__init__` (line 848) `def __init__(self, config)` - *Store grid parameters from configuration.*
- `gaussian_source` (line 853) `def gaussian_source(self)` - *Smooth Gaussian current-density envelope centred on the grid.*
- `dipole_source` (line 861) `def dipole_source(self)` - *1/r dipole-like source envelope.*
- `plane_wave_source` (line 870) `def plane_wave_source(self)` - *Sinusoidal plane-wave seed for Ex, Ey components.*
- `periodic_medium` (line 879) `def periodic_medium(self)` - *Periodic permittivity modulation (photonic-crystal-like).*
- `generate_mixed_source` (line 886) `def generate_mixed_source(self, seed)` - *Dirichlet-weighted superposition of all source types.*
- `__init__` (line 911) `def __init__(self, config, hamiltonian_engine, seed)` - *Generate all samples at construction time.*
- `_generate_initial_fields` (line 954) `def _generate_initial_fields(self, source, sample_seed)` - *Create a random initial electromagnetic field configuration.

Returns a (3, H, W) complex tensor [Ex, Ey, Bz] and a scalar energy.*
- `_time_evolve_fields` (line 983) `def _time_evolve_fields(self, fields, source, energy)` - *Advance the EM field through multiple time steps under the Maxwell operator.*
- `_fields_to_real_imag` (line 1012) `def _fields_to_real_imag(self, fields)` - *Convert (3, H, W) complex tensor to (6, H, W) real tensor.*
- `__len__` (line 1020) `def __len__(self)` - *Number of training samples.*
- `__getitem__` (line 1024) `def __getitem__(self, idx)` - *Return (input, target) pair for training.*
- `get_validation_batch` (line 1028) `def get_validation_batch(self)` - *Return the full validation set as a single batch.*
- `__init__` (line 1036) `def __init__(self, config)` - *Precompute wavenumber magnitude grid.*
- `compute_full_spectrum` (line 1045) `def compute_full_spectrum(self, spectral_field)` - *Return magnitude, phase, power, radial profile, and derived statistics.*
- `detect_bragg_peaks` (line 1098) `def detect_bragg_peaks(self, power_spectrum, threshold_sigma)` - *Identify local maxima in the power spectrum exceeding a statistical threshold.*
- `compute_resonance_metrics` (line 1146) `def compute_resonance_metrics(self, spectral_field)` - *Aggregate spectral concentration, phase coherence, and Bragg analysis.*
- `__init__` (line 1186) `def __init__(self, config)` - *Initialise wavenumber grids and full Fourier sub-analyzer.*
- `compute_mass_center` (line 1195) `def compute_mass_center(self, spectral_field)` - *Return centre of mass, inertia tensor, anisotropy, and resonance diagnostics.*
- `__init__` (line 1250) `def __init__(self, config)` - *Initialise history buffers and state variables.*
- `detect` (line 1258) `def detect(self, spectral_field)` - *Run full topological phase detection and return diagnostic dict.*
- `extract` (line 1316) `def extract(model, grid_size)` - *Return the mean complex spectral kernel across all spectral layers.*
- `__init__` (line 1336) `def __init__(self, config)` - *Initialise with base lambda pressure.*
- `forward` (line 1342) `def forward(self, phase_info, epoch)` - *Compute quadrant, localisation, and resonance penalty terms.*
- `__init__` (line 1368) `def __init__(self, config)` - *Store pressure decay rate from config.*
- `apply` (line 1373) `def apply(self, model, phase_info)` - *Multiplicatively decay parameters when crystal phase is detected.*
- `__init__` (line 1387) `def __init__(self, config)` - *Initialise all topological sub-components.*
- `compute` (line 1395) `def compute(self, model)` - *Extract spectral field, detect phase, compute loss, return full metrics dict.*
- `apply_crystallization_pressure` (line 1429) `def apply_crystallization_pressure(self, model, topo_metrics)` - *Delegate pressure application to the sub-component.*
- `_empty_metrics` (line 1436) `def _empty_metrics()` - *Return a zero-valued metrics dict when topological analysis is disabled.*
- `compute_local_complexity` (line 1457) `def compute_local_complexity(weights, epsilon)` - *Return a scalar in [0, 1] measuring weight diversity.*
- `compute_superposition` (line 1476) `def compute_superposition(weights)` - *Return the mean absolute off-diagonal Pearson correlation.*
- `__init__` (line 1501) `def __init__(self, config)` - *Store config and create logger.*
- `compute` (line 1506) `def compute(self, model)` - *Facade that delegates to compute_all_metrics.*
- `compute_kappa` (line 1512) `def compute_kappa(self, model, val_x, val_y, num_batches)` - *Gradient covariance condition number kappa = lambda_max / lambda_min.*
- `compute_discretization_margin` (line 1563) `def compute_discretization_margin(self, model)` - *delta = max_i |theta_i - round(theta_i)|.*
- `compute_alpha_purity` (line 1572) `def compute_alpha_purity(self, model)` - *alpha = -log(delta).*
- `compute_kappa_quantum` (line 1579) `def compute_kappa_quantum(self, model)` - *Quantum-regularised condition number with hbar regularisation.*
- `compute_poynting_vector` (line 1601) `def compute_poynting_vector(self, model)` - *Compute the electromagnetic Poynting-like energy flow through the network.*
- `compute_hbar_effective` (line 1651) `def compute_hbar_effective(self, model, lambda_pressure)` - *hbar_eff = delta^2 * lambda / omega.*
- `compute_all_metrics` (line 1661) `def compute_all_metrics(self, model, val_x, val_y)` - *Compute delta, alpha, kappa, kappa_q, poynting, purity, and is_crystal.*
- `__init__` (line 1702) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 1706) `def compute(self, model)` - *Return all thermodynamic observables.*
- `compute_effective_temperature` (line 1727) `def compute_effective_temperature(self, gradient_buffer, learning_rate)` - *T_eff = (lr / 2) * Var(grad).*
- `compute_specific_heat` (line 1750) `def compute_specific_heat(self, loss_history, temp_history)` - *C_v = Var(U) / T^2.*
- `compute_gibbs_free_energy` (line 1762) `def compute_gibbs_free_energy(self, delta, alpha, temperature)` - *G = delta - T * (-alpha).*
- `compute_critical_temperature` (line 1768) `def compute_critical_temperature(self, alpha)` - *T_c = T_0 * exp(-c * alpha).*
- `__init__` (line 1776) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 1780) `def compute(self, model)` - *Compute spectral geometry observables from weight outer product.*
- `_compute_level_spacing_ratio` (line 1806) `def _compute_level_spacing_ratio(self, spacings)` - *Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}) over consecutive spacings.*
- `__init__` (line 1822) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 1826) `def compute(self, model)` - *Compute Ricci scalar and sectional curvatures from weight metric.*
- `_compute_ricci_scalar` (line 1842) `def _compute_ricci_scalar(self, metric)` - *Ricci scalar via inverse eigenvalue sum.*
- `_estimate_sectional_curvatures` (line 1851) `def _estimate_sectional_curvatures(self, metric)` - *Sample 2x2 sub-block determinants as sectional curvature proxies.*
- `__init__` (line 1868) `def __init__(self, config)` - *Initialise curvature history and surgery counter.*
- `compute_ricci_scalar_fast` (line 1877) `def compute_ricci_scalar_fast(self, model)` - *Fast Ricci scalar estimate from normalised weight outer product.*
- `compute_local_curvature` (line 1907) `def compute_local_curvature(self, param)` - *Second-difference curvature estimate along the flattened parameter.*
- `compute_anisotropy` (line 1916) `def compute_anisotropy(self, model)` - *Ratio of smallest to largest covariance eigenvalue of the weight vector.*
- `compute_ricci_regularization_loss` (line 1941) `def compute_ricci_regularization_loss(self, model)` - *Smoothness penalty proportional to second-difference curvature.*
- `apply_ricci_flow_step` (line 1959) `def apply_ricci_flow_step(self, model, lr)` - *One step of diffusive Ricci flow smoothing on all parameters.*
- `perform_perelman_surgery` (line 1989) `def perform_perelman_surgery(self, model, ricci_scalar)` - *Cut singularities (outlier weights) when curvature exceeds the surgery threshold.*
- `compute_adaptive_lr_factor` (line 2031) `def compute_adaptive_lr_factor(self, model)` - *Reduce learning rate when curvature spikes above recent average.*
- `get_flow_metrics` (line 2047) `def get_flow_metrics(self, model)` - *Return summary Ricci-flow diagnostics.*
- `__init__` (line 2064) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 2068) `def compute(self, model)` - *Compute weight diffraction pattern and spectral entropy.*
- `compute_weight_diffraction` (line 2073) `def compute_weight_diffraction(self, coeffs)` - *FFT of concatenated weights with peak detection.*
- `_compute_spectral_entropy` (line 2092) `def _compute_spectral_entropy(power_spectrum)` - *Shannon entropy of the normalised power spectrum.*
- `__init__` (line 2104) `def __init__(self, config)` - *Initialise lambda in float64 precision.*
- `current_lambda` (line 2114) `def current_lambda(self)` - *Current pressure value.*
- `step` (line 2118) `def step(self, epoch)` - *Increase lambda at fixed epoch intervals.*
- `compute_regularization_loss` (line 2126) `def compute_regularization_loss(self, model)` - *L2 penalty on distance from nearest integer for each parameter.*
- `set_lambda` (line 2139) `def set_lambda(self, value)` - *Directly set the lambda value.*
- `__init__` (line 2147) `def __init__(self, config)` - *Initialise base and accelerated growth factors.*
- `step_adaptive` (line 2153) `def step_adaptive(self, epoch, topo_phase_state)` - *Grow lambda faster when topological order is emerging.*
- `__init__` (line 2172) `def __init__(self, config)` - *Initialise temperature schedule.*
- `temperature` (line 2180) `def temperature(self)` - *Current annealing temperature.*
- `step` (line 2184) `def step(self)` - *Cool by one step.*
- `accept_perturbation` (line 2188) `def accept_perturbation(self, delta_loss)` - *Metropolis acceptance criterion.*
- `should_restart` (line 2197) `def should_restart(self, current_delta, best_delta)` - *Whether the current state has drifted too far from best.*
- `__init__` (line 2205) `def __init__(self, config)` - *Initialise with base cooling rate.*
- `step_adaptive` (line 2210) `def step_adaptive(self, alignment_trend, resonance_score)` - *Slow cooling when alignment is growing, speed up when it recedes.*
- `__init__` (line 2225) `def __init__(self, config)` - *Initialise metric history buffers.*
- `update_metrics` (line 2257) `def update_metrics(self)` - *Append each provided metric to its history list.*
- `compute_delta_slope` (line 2269) `def compute_delta_slope(self)` - *Linear regression slope of recent delta values.*
- `format_progress_bar` (line 2282) `def format_progress_bar(self, epoch, total_epochs, phase)` - *Format all metrics into a multi-line progress string.*
- `__init__` (line 2356) `def __init__(self, config, checkpoint_dir)` - *Create checkpoint directory and initialise timer.*
- `should_save_checkpoint` (line 2366) `def should_save_checkpoint(self)` - *True when at least CHECKPOINT_INTERVAL_MINUTES have elapsed.*
- `save_checkpoint` (line 2370) `def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)` - *Save model, optimiser, metrics, and config to a timestamped file and latest link.*
- `load_latest_checkpoint` (line 2399) `def load_latest_checkpoint(self)` - *Load the latest checkpoint if it exists.*
- `__init__` (line 2410) `def __init__(self, config)` - *Initialise patience buffer.*
- `should_stop` (line 2416) `def should_stop(self, epoch, lc, sp, kappa, delta, temp, cv)` - *Return True if recent metrics indicate glass formation.*
- `is_crystal_formed` (line 2452) `def is_crystal_formed(self, lc, sp, kappa, delta, temp, cv)` - *Return True if all metrics are below crystal thresholds.*
- `check` (line 2471) `def check(model)` - *Return integrity report with counts and corruption ratio.*
- `__init__` (line 2501) `def __init__(self, config)` - *Instantiate all metric calculators.*
- `compute_weight_metrics` (line 2515) `def compute_weight_metrics(self, model)` - *Local complexity and superposition averaged over all weight matrices.*
- `compute_norm_conservation_error` (line 2530) `def compute_norm_conservation_error(self, model, val_x)` - *Relative norm difference between input and output.*
- `train_single_epoch` (line 2540) `def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler, ricci_flow)` - *Run one epoch of gradient descent with optional regularisation.*
- `validate` (line 2578) `def validate(self, model, val_x, val_y)` - *Compute validation loss and accuracy.*
- `collect_all_metrics` (line 2590) `def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)` - *Compute every metric from the paper and return as a flat dict.*
- `__init__` (line 2673) `def __init__(self, config)` - *Initialise spectral statistics calculator.*
- `optimize_kernel_ratio` (line 2679) `def optimize_kernel_ratio(self)` - *Sweep imaginary ratios and return the one with lowest combined GUE loss.*
- `__init__` (line 2730) `def __init__(self, config, hamiltonian_engine, imaginary_ratio)` - *Store engine reference and optimal imaginary ratio.*
- `prospect` (line 2737) `def prospect(self)` - *Train briefly at each candidate batch size and return the best.*
- `__init__` (line 2789) `def __init__(self, config, hamiltonian_engine, batch_size, imaginary_ratio)` - *Store references for dataset and model creation.*
- `mine` (line 2798) `def mine(self)` - *Evaluate seeds and return the one with best delta velocity and kappa.*
- `__init__` (line 2884) `def __init__(self, config, hamiltonian_engine, seed, batch_size, imaginary_ratio)` - *Store all training configuration.*
- `run_phase3_training` (line 2894) `def run_phase3_training(self, start_epoch, model)` - *Execute Phase 3 and return (model, optimiser, monitor).*
- `__init__` (line 3005) `def __init__(self, config, hamiltonian_engine, model, optimizer, monitor, seed, batch_size, imaginary_ratio)` - *Store all refinement parameters.*
- `run_phase4_refinement` (line 3021) `def run_phase4_refinement(self, start_epoch)` - *Run Phase 4 refinement and return the best model.*
- `load_latest_checkpoint` (line 3193) `def load_latest_checkpoint(mdl, checkpoint_paths)`
- `safe_compute` (line 1672) `def safe_compute(func)`
- `safe_get` (line 2286) `def safe_get(key)`

#### `maxwell_crystallography_suite.py`
**Path:** `maxwell_crystallography_suite.py`

**Classes:**
- `CrystallographySuiteConfig` (line 59) `class CrystallographySuiteConfig` - *Master configuration for the complete Maxwell crystallography suite.*
- `LoggerFactory` (line 201) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `IMetricCalculator` (line 218) `class IMetricCalculator(Protocol)` - *Protocol for metric calculation strategies.*
- `IPhaseDetector` (line 226) `class IPhaseDetector(Protocol)` - *Protocol for phase detection strategies.*
- `SpectralLayer` (line 234) `class SpectralLayer` - *Spectral convolution layer with tuneable imaginary ratio for GOE/GUE control.*
- `MaxwellSpectralNetwork` (line 288) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `GOEGUESpectralAnalyzer` (line 331) `class GOEGUESpectralAnalyzer` - *Chapter 10 spectral universality analyzer.

Extracts the spectral operator from each SpectralLayer, computes its
eigenvalue statistics, and determines proximity to GOE (beta=1) or
GUE (beta=2) universality via P(s), R_2(s), and the Dyson index.*
- `WeightIntegrityCalculator` (line 528) `class WeightIntegrityCalculator` - *Detect NaN and Inf corruption in model parameters.*
- `DiscretizationCalculator` (line 559) `class DiscretizationCalculator` - *Delta, alpha purity, and spectral entropy of the weight distribution.*
- `SpectralGeometryCalculator` (line 602) `class SpectralGeometryCalculator` - *Spectral gap, effective dimension, participation ratio, and level-spacing ratio.*
- `RicciCurvatureCalculator` (line 650) `class RicciCurvatureCalculator` - *Ricci scalar and mean sectional curvature of the weight manifold.*
- `BerryPhaseCalculator` (line 695) `class BerryPhaseCalculator` - *Berry phase from training checkpoint trajectory.*
- `ControlSystemAnalyzer` (line 784) `class ControlSystemAnalyzer` - *Control theory stability analysis for neural network dynamics.*
- `ThermodynamicCalculator` (line 842) `class ThermodynamicCalculator` - *Gibbs free energy, critical temperature, and phase classification.*
- `FullFourierAnalyzer` (line 881) `class FullFourierAnalyzer` - *Complete 2D Fourier analysis with spectral concentration and resonance metrics.*
- `FourierMassCenterAnalyzer` (line 924) `class FourierMassCenterAnalyzer` - *Centre-of-mass in Fourier space for topological phase detection.*
- `TopologicalPhaseDetector` (line 962) `class TopologicalPhaseDetector` - *Hysteretic phase detector combining alignment and resonance signals.*
- `SpectralFieldExtractor` (line 996) `class SpectralFieldExtractor` - *Extract spectral weight tensors from SpectralLayer modules.*
- `TopologicalMetricsCalculator` (line 1015) `class TopologicalMetricsCalculator` - *Topological metrics from model spectral fields.*
- `GradientDynamicsCalculator` (line 1051) `class GradientDynamicsCalculator` - *Gradient covariance kappa and effective temperature.*
- `SchrodingerAnalyzer` (line 1110) `class SchrodingerAnalyzer` - *Quantum mechanical analysis via Johnson-Lindenstrauss compressed wavefunction.*
- `ComprehensiveVisualizer` (line 1156) `class ComprehensiveVisualizer` - *Generate multi-panel analysis figures for each checkpoint.*
- `CheckpointAnalyzer` (line 1451) `class CheckpointAnalyzer` - *Main analyzer orchestrating all metric calculations on a single checkpoint.*
- `BatchProcessor` (line 1575) `class BatchProcessor` - *Process all checkpoints in a directory, generating per-checkpoint and summary outputs.*
- `MaxwellCrystallographySuite` (line 1775) `class MaxwellCrystallographySuite` - *Main entry point for the Maxwell crystallography analysis suite.*

**Functions:**
- `main` (line 1850) `def main()` - *Parse arguments and run the Maxwell crystallography suite.*
- `create_logger` (line 205) `def create_logger(name, level, config)` - *Create and return a configured logger.*
- `compute` (line 221) `def compute(self, model)` - *Compute metrics for the given model.*
- `detect` (line 229) `def detect(self, spectral_field)` - *Detect phase from spectral field.*
- `__init__` (line 237) `def __init__(self, channels, grid_size, config, imaginary_ratio)` - *Initialise real and imaginary kernel parameters.*
- `forward` (line 252) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `get_spectral_operator` (line 271) `def get_spectral_operator(self)` - *Extract (channels x channels) complex Hermitian-like matrix for eigenvalue analysis.*
- `get_kernel_ratio` (line 279) `def get_kernel_ratio(self)` - *Return the imaginary-to-real kernel norm ratio.*
- `__init__` (line 291) `def __init__(self, config, imaginary_ratio)` - *Build all sub-layers with the given architectural parameters.*
- `forward` (line 309) `def forward(self, x)` - *Forward pass through the full spectral network.*
- `get_kernel_ratio` (line 320) `def get_kernel_ratio(self)` - *Compute effective imaginary-to-real kernel norm ratio across all layers.*
- `__init__` (line 340) `def __init__(self, config)` - *Store configuration reference.*
- `extract_spectral_operators` (line 344) `def extract_spectral_operators(self, model)` - *Return the complex spectral operator from every SpectralLayer in the model.*
- `compute_eigenvalue_spacing` (line 353) `def compute_eigenvalue_spacing(self, eigenvalues)` - *Unfold eigenvalues and return normalised nearest-neighbour spacings.*
- `compute_spacing_distribution_loss` (line 368) `def compute_spacing_distribution_loss(self, spacings, target)` - *MSE between empirical P(s) and Wigner surmise for GOE or GUE.*
- `compute_dyson_index` (line 385) `def compute_dyson_index(self, spacings)` - *Estimate the Dyson beta from small-spacing power-law P(s) ~ s^beta.*
- `compute_pair_correlation` (line 402) `def compute_pair_correlation(self, eigenvalues)` - *Two-level correlation function R_2(s).*
- `compute_correlation_loss` (line 423) `def compute_correlation_loss(self, eigenvalues, target)` - *MSE between empirical R_2(s) and analytical prediction.*
- `compute` (line 438) `def compute(self, model)` - *Run full GOE/GUE spectral analysis on all spectral layers.*
- `_empty_results` (line 512) `def _empty_results()` - *Return zero-valued results when no spectral layers are found.*
- `__init__` (line 531) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 535) `def compute(self, model)` - *Return integrity report.*
- `__init__` (line 562) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 566) `def compute(self, model)` - *Compute delta, alpha, spectral entropy, and per-layer deltas.*
- `_compute_spectral_entropy` (line 588) `def _compute_spectral_entropy(self, weights)` - *Shannon entropy of the normalised power spectrum of concatenated weights.*
- `__init__` (line 605) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 609) `def compute(self, model)` - *Compute spectral geometry observables from weight outer product.*
- `_compute_level_spacing_ratio` (line 638) `def _compute_level_spacing_ratio(self, spacings)` - *Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}).*
- `__init__` (line 653) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 657) `def compute(self, model)` - *Compute Ricci scalar and sectional curvatures from weight metric.*
- `_compute_ricci_scalar` (line 672) `def _compute_ricci_scalar(self, metric)` - *Ricci scalar via inverse eigenvalue sum.*
- `_estimate_sectional_curvatures` (line 681) `def _estimate_sectional_curvatures(self, metric)` - *Sample 2x2 sub-block determinants as sectional curvature proxies.*
- `__init__` (line 698) `def __init__(self, config)` - *Initialise logger.*
- `load_checkpoints` (line 703) `def load_checkpoints(self, checkpoint_dir)` - *Load all .pth files sorted by epoch.*
- `_extract_epoch` (line 720) `def _extract_epoch(self, filepath)` - *Parse epoch number from filename.*
- `flatten_kernel_params` (line 725) `def flatten_kernel_params(self, state_dict)` - *Concatenate all spectral layer kernels into a single complex vector.*
- `compute_berry_connection_discrete` (line 744) `def compute_berry_connection_discrete(self, theta_prev, theta_curr)` - *Discrete Berry connection between consecutive parameter snapshots.*
- `calculate_berry_phase` (line 755) `def calculate_berry_phase(self, checkpoint_dir)` - *Compute total Berry phase, winding number, and cumulative trajectory.*
- `__init__` (line 787) `def __init__(self, config)` - *Store config reference.*
- `extract_state_space` (line 791) `def extract_state_space(self, model)` - *Extract a composite state-space (A, B, C, D) from weight matrices.*
- `analyze_stability` (line 821) `def analyze_stability(self, A)` - *Eigenvalue stability analysis of the state matrix.*
- `compute` (line 836) `def compute(self, model)` - *Run full control-theory analysis.*
- `__init__` (line 845) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 849) `def compute(self, model)` - *Compute thermodynamic potentials from crystallographic observables.*
- `_classify_phase` (line 866) `def _classify_phase(self, delta, kappa, temp, alpha)` - *Classify the thermodynamic phase of the model.*
- `__init__` (line 884) `def __init__(self, config)` - *Precompute wavenumber grids.*
- `compute_full_spectrum` (line 893) `def compute_full_spectrum(self, spectral_field)` - *Return magnitude, phase, power, and derived statistics.*
- `compute_resonance_metrics` (line 913) `def compute_resonance_metrics(self, spectral_field)` - *Aggregate spectral concentration into a resonance score.*
- `__init__` (line 927) `def __init__(self, config)` - *Initialise wavenumber grids and sub-analyzers.*
- `compute_mass_center` (line 936) `def compute_mass_center(self, spectral_field)` - *Return centre-of-mass coordinates and resonance diagnostics.*
- `__init__` (line 965) `def __init__(self, config)` - *Initialise history buffers.*
- `detect` (line 973) `def detect(self, spectral_field)` - *Full topological phase detection returning diagnostic dict.*
- `extract` (line 1000) `def extract(model, grid_size)` - *Return the mean complex spectral kernel across all spectral layers.*
- `__init__` (line 1018) `def __init__(self, config)` - *Initialise sub-components.*
- `compute` (line 1024) `def compute(self, model)` - *Run topological detection and return metrics dict.*
- `_empty_metrics` (line 1042) `def _empty_metrics()` - *Zero-valued metrics when analysis is disabled or unavailable.*
- `__init__` (line 1054) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 1058) `def compute(self, model)` - *Compute kappa, T_eff, and gradient variance from validation data.*
- `__init__` (line 1113) `def __init__(self, config)` - *Initialise projection parameters.*
- `extract_compressed_wavefunction` (line 1119) `def extract_compressed_wavefunction(self, model)` - *Project the full parameter vector to a fixed-dimension wavefunction.*
- `_compress_johnson_lindenstrauss` (line 1134) `def _compress_johnson_lindenstrauss(self, vector)` - *Random projection preserving pairwise distances.*
- `compute` (line 1142) `def compute(self, model)` - *Compute wavefunction entropy, participation ratio, and quantum coherence.*
- `__init__` (line 1159) `def __init__(self, config)` - *Store config reference.*
- `visualize_checkpoint_analysis` (line 1163) `def visualize_checkpoint_analysis(self, results, output_path)` - *Render the full 5x4 analysis dashboard to a file.*
- `_plot_weight_distribution` (line 1194) `def _plot_weight_distribution(self, results, ax)` - *Pie chart of valid / NaN / Inf parameter counts.*
- `_plot_spectral_analysis` (line 1206) `def _plot_spectral_analysis(self, results, ax)` - *Bar chart of spectral geometry observables.*
- `_plot_phase_diagram` (line 1217) `def _plot_phase_diagram(self, results, ax)` - *Alpha vs T_eff phase diagram with crystal/glass boundaries.*
- `_plot_curvature_distribution` (line 1232) `def _plot_curvature_distribution(self, results, ax)` - *Bar chart of Ricci curvature summary statistics.*
- `_plot_level_spacing` (line 1243) `def _plot_level_spacing(self, results, ax)` - *Level spacing ratio with Wigner-Dyson and Poisson reference lines.*
- `_plot_eigenvalue_spectrum` (line 1253) `def _plot_eigenvalue_spectrum(self, results, ax)` - *Largest and smallest eigenvalue on log scale.*
- `_plot_thermodynamic_potentials` (line 1267) `def _plot_thermodynamic_potentials(self, results, ax)` - *Gibbs free energy, entropy proxy, and critical temperature.*
- `_plot_topological_metrics` (line 1278) `def _plot_topological_metrics(self, results, ax)` - *Phase state, alignment, and resonance scores.*
- `_plot_berry_phase` (line 1289) `def _plot_berry_phase(self, results, ax)` - *Berry phase arrow on the unit circle.*
- `_plot_control_stability` (line 1304) `def _plot_control_stability(self, results, ax)` - *Stability margin and binary stability flag.*
- `_plot_quantum_metrics` (line 1314) `def _plot_quantum_metrics(self, results, ax)` - *Wavefunction entropy, participation ratio, and coherence.*
- `_plot_summary_table` (line 1325) `def _plot_summary_table(self, results, ax)` - *Text summary of key observables and phase classification.*
- `_plot_layer_deltas` (line 1352) `def _plot_layer_deltas(self, results, ax)` - *Horizontal bar chart of per-layer discretization margins.*
- `_plot_resonance_metrics` (line 1364) `def _plot_resonance_metrics(self, results, ax)` - *Spectral concentration and resonance score bars.*
- `_plot_spectral_concentration` (line 1374) `def _plot_spectral_concentration(self, results, ax)` - *Scatter of spectral gap vs participation ratio.*
- `_plot_health_score` (line 1384) `def _plot_health_score(self, results, ax)` - *Single-bar health score with traffic-light colouring.*
- `_plot_goe_gue_losses` (line 1393) `def _plot_goe_gue_losses(self, results, ax)` - *Grouped bar chart comparing P(s) and R_2(s) losses for GOE and GUE.*
- `_plot_dyson_beta` (line 1410) `def _plot_dyson_beta(self, results, ax)` - *Dyson beta index gauge with GOE and GUE reference markers.*
- `_plot_kernel_ratios` (line 1421) `def _plot_kernel_ratios(self, results, ax)` - *Per-layer imaginary-to-real kernel norm ratios.*
- `_plot_universality_gauge` (line 1438) `def _plot_universality_gauge(self, results, ax)` - *Horizontal gauge showing interpolation between GOE and GUE.*
- `__init__` (line 1454) `def __init__(self, config)` - *Instantiate all sub-calculators.*
- `analyze_checkpoint` (line 1471) `def analyze_checkpoint(self, checkpoint_path, val_data)` - *Load a checkpoint, run every analyzer, and return the aggregated results dict.*
- `_compute_health_score` (line 1553) `def _compute_health_score(self, results)` - *Weighted average of integrity, purity, MBL, and topological scores.*
- `__init__` (line 1578) `def __init__(self, config)` - *Initialise analyzer and visualizer.*
- `process_directory` (line 1585) `def process_directory(self, checkpoint_dir, output_dir, val_data)` - *Iterate over all .pth files, analyze each, and save results.*
- `_generate_summary` (line 1616) `def _generate_summary(self, all_results)` - *Aggregate statistics and rank checkpoints by delta, alpha, accuracy, and health score.*
- `_generate_evolution_plots` (line 1735) `def _generate_evolution_plots(self, all_results, output_dir)` - *Time-series plots of key metrics across training.*
- `__init__` (line 1778) `def __init__(self, config)` - *Initialise the suite with all sub-components.*
- `run_analysis` (line 1785) `def run_analysis(self, checkpoint_dir, output_dir)` - *Execute full analysis: batch processing, Berry phase, and summary.*
- `_generate_berry_phase_visualization` (line 1804) `def _generate_berry_phase_visualization(self, berry_results, output_dir)` - *Dedicated Berry phase figure with phasor diagram and summary text.*
- `_extract` (line 1621) `def _extract(cat, key, default)`
- `_stats` (line 1624) `def _stats(vals)`
- `_checkpoint_id` (line 1630) `def _checkpoint_id(r)`
- `_best_entry` (line 1662) `def _best_entry(idx)`

#### `maxwell_field_hawking_suite.py`
**Path:** `maxwell_field_hawking_suite.py`

**Classes:**
- `AnalysisConfig` (line 67) `class AnalysisConfig` - *Immutable master configuration for the combined analysis suite.*
- `LoggerFactory` (line 142) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `CustomUnpickler` (line 158) `class CustomUnpickler` - *Unpickler that handles unknown classes by creating dummy dict-like objects.*
- `SpectralLayer` (line 207) `class SpectralLayer` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 242) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `MetadataExtractor` (line 283) `class MetadataExtractor` - *Extract metadata (epoch, loss, delta) from checkpoint dicts.*
- `GravitationalConstantCalculator` (line 331) `class GravitationalConstantCalculator` - *G_eff from weight distance to discrete attractor and gradient magnitude.*
- `PlanckConstantCalculator` (line 366) `class PlanckConstantCalculator` - *hbar_eff from uncertainty, action quantisation, conductance, and information entropy.*
- `BoltzmannConstantCalculator` (line 412) `class BoltzmannConstantCalculator` - *k_B_eff from configuration entropy and thermal fluctuations.*
- `SpeedOfLightCalculator` (line 440) `class SpeedOfLightCalculator` - *c_eff from Planck relation and spectral velocity of weight matrices.*
- `InformationalMassCalculator` (line 466) `class InformationalMassCalculator` - *M_eff from Planck mass formula, active parameter count, and energy-mass relation.*
- `HorizonAreaCalculator` (line 500) `class HorizonAreaCalculator` - *A_eff from active parameter counts and entropy proxy.*
- `HawkingRadiationCalculator` (line 520) `class HawkingRadiationCalculator` - *Full Hawking radiation thermodynamic analysis.*
- `WeightLatticeMapper` (line 596) `class WeightLatticeMapper` - *Map neural network weights to a 3D dielectric lattice.*
- `PoissonSolver` (line 626) `class PoissonSolver` - *Spectral Poisson solver: nabla^2 phi = -rho / eps_0.*
- `ScatteringSolver` (line 652) `class ScatteringSolver` - *EM scattering from dielectric contrast: S(k) ~ |FT(delta_eps)|^2.*
- `DielectricTensorAnalyzer` (line 683) `class DielectricTensorAnalyzer` - *Anisotropy analysis of the dielectric medium via the structure tensor.*
- `PhotonicEntropyCalculator` (line 714) `class PhotonicEntropyCalculator` - *Shannon entropy of the EM field energy distribution and density of modes.*
- `BandgapAnalyzer` (line 741) `class BandgapAnalyzer` - *Photonic bandgap estimation from radial Fourier profile.*
- `ElectromagneticPhaseClassifier` (line 773) `class ElectromagneticPhaseClassifier` - *Crystal vs Glass classification from EM observables.*
- `MaxwellFieldAnalyzer` (line 807) `class MaxwellFieldAnalyzer` - *Full Maxwell / Poisson electromagnetic field analysis pipeline.*
- `CombinedVisualizer` (line 863) `class CombinedVisualizer` - *Generate multi-panel dashboard combining Hawking and Maxwell analyses.*
- `CombinedAnalyzer` (line 1065) `class CombinedAnalyzer` - *Orchestrator that runs both Hawking and Maxwell analyses on a single checkpoint.*
- `BatchAnalyzer` (line 1129) `class BatchAnalyzer` - *Process all checkpoints in a directory.*
- `DummyClass` (line 170) `class DummyClass`

**Functions:**
- `load_checkpoint_robust` (line 185) `def load_checkpoint_robust(path, device)` - *Load a checkpoint with multiple fallback strategies.*
- `main` (line 1227) `def main()` - *Parse arguments and run the combined analysis suite.*
- `create_logger` (line 146) `def create_logger(name, level)` - *Create and return a configured logger.*
- `find_class` (line 161) `def find_class(self, module, name)` - *Override to handle missing classes gracefully.*
- `_create_dummy_class` (line 168) `def _create_dummy_class(self, name)` - *Return a dummy class that acts like a dictionary.*
- `__init__` (line 210) `def __init__(self, channels, grid_size, imaginary_ratio)` - *Initialise real and imaginary kernel parameters.*
- `forward` (line 223) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `__init__` (line 245) `def __init__(self, config, imaginary_ratio)` - *Build all sub-layers.*
- `forward` (line 263) `def forward(self, x)` - *Forward pass through the full spectral network.*
- `get_flat_parameters` (line 274) `def get_flat_parameters(self)` - *Return all parameters as a single flat tensor.*
- `get_weight_dict` (line 278) `def get_weight_dict(self)` - *Return all named parameter tensors as numpy arrays.*
- `extract` (line 287) `def extract(checkpoint)` - *Return a standardised metadata dict from any checkpoint format.*
- `_find_delta` (line 312) `def _find_delta(data, depth)` - *Recursively search for a delta value.*
- `__init__` (line 334) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 338) `def calculate(self, all_weights, delta)` - *Return G_alg, force, and crystallisation pressure.*
- `__init__` (line 369) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 373) `def calculate(self, all_weights, delta, loss)` - *Return four estimates of hbar and their weighted unification.*
- `__init__` (line 415) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 419) `def calculate(self, all_weights_np, loss, loss_history)` - *Return entropy-based and thermal k_B estimates.*
- `__init__` (line 443) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 447) `def calculate(self, all_weights_np, h_bar, G_alg)` - *Return multiple c estimates.*
- `__init__` (line 469) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 473) `def calculate(self, all_weights, G_alg, c_eff, h_bar)` - *Return multiple mass estimates.*
- `__init__` (line 503) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 507) `def calculate(self, all_weights)` - *Return effective area from active parameters and weight entropy.*
- `__init__` (line 523) `def __init__(self, config)` - *Instantiate all sub-calculators.*
- `calculate` (line 533) `def calculate(self, model, loss, loss_history, precomputed_delta)` - *Run the full Hawking radiation pipeline and return all results.*
- `__init__` (line 599) `def __init__(self, config)` - *Store config reference.*
- `map` (line 603) `def map(self, weight_dict)` - *Return (charge_density, permittivity) as 3D arrays.

Weights are flattened and embedded into a cubic grid.
Permittivity = 1 + scale * w_i.
Charge density = w_i.*
- `__init__` (line 629) `def __init__(self, config)` - *Store config reference.*
- `solve` (line 633) `def solve(self, charge_density, permittivity)` - *Return the electrostatic potential phi on the 3D grid.*
- `compute_electric_field` (line 647) `def compute_electric_field(self, potential)` - *Return E = -grad(phi).*
- `__init__` (line 655) `def __init__(self, config)` - *Store config reference.*
- `compute` (line 659) `def compute(self, permittivity)` - *Return scattering intensity map, central slice, and peak analysis.*
- `__init__` (line 686) `def __init__(self, config)` - *Store config reference.*
- `analyze` (line 690) `def analyze(self, permittivity)` - *Return eigenvalues of the gradient structure tensor and anisotropy ratio.*
- `__init__` (line 717) `def __init__(self, config)` - *Store config reference.*
- `calculate` (line 721) `def calculate(self, potential, intensity_3d)` - *Return field entropy, mode entropy, and their sum.*
- `__init__` (line 744) `def __init__(self, config)` - *Store config reference.*
- `analyze` (line 748) `def analyze(self, fourier_coeffs)` - *Return radial profile, gap depth, and boolean bandgap detection.*
- `__init__` (line 776) `def __init__(self, config)` - *Store config reference.*
- `classify` (line 780) `def classify(self, anisotropy, scattering, photonic_entropy, delta, alpha)` - *Return phase name, crystal/glass flags, and confidence score.*
- `__init__` (line 810) `def __init__(self, config)` - *Instantiate all sub-components.*
- `analyze` (line 821) `def analyze(self, model)` - *Run the full EM pipeline on the model weights.*
- `__init__` (line 866) `def __init__(self, config)` - *Store config reference.*
- `render` (line 870) `def render(self, hawking, maxwell, metadata, output_path)` - *Save a comprehensive 4x4 figure to disk.*
- `_plot_hawking_summary` (line 897) `def _plot_hawking_summary(self, h, ax)` - *Hawking temperature and BH entropy bars.*
- `_plot_hawking_temperature` (line 906) `def _plot_hawking_temperature(self, h, ax)` - *Temperature gauge.*
- `_plot_hawking_entropy` (line 914) `def _plot_hawking_entropy(self, h, ax)` - *Bekenstein-Hawking entropy.*
- `_plot_hawking_constants` (line 921) `def _plot_hawking_constants(self, h, ax)` - *Effective constants summary.*
- `_plot_potential_slice` (line 936) `def _plot_potential_slice(self, m, ax)` - *Central slice of electrostatic potential.*
- `_plot_scattering_slice` (line 944) `def _plot_scattering_slice(self, m, ax)` - *kx-ky scattering intensity.*
- `_plot_dielectric_anisotropy` (line 954) `def _plot_dielectric_anisotropy(self, m, ax)` - *Dielectric tensor eigenvalues.*
- `_plot_photonic_entropy` (line 964) `def _plot_photonic_entropy(self, m, ax)` - *Field and mode entropy bars.*
- `_plot_bandgap` (line 973) `def _plot_bandgap(self, m, ax)` - *Radial Fourier profile and bandgap indicator.*
- `_plot_electric_field` (line 984) `def _plot_electric_field(self, m, ax)` - *Electric field magnitude statistics.*
- `_plot_em_classification` (line 992) `def _plot_em_classification(self, m, ax)` - *Phase classification text panel.*
- `_plot_combined_summary` (line 1010) `def _plot_combined_summary(self, h, m, meta, ax)` - *Text summary combining both analyses.*
- `_plot_hawking_radiation_power` (line 1032) `def _plot_hawking_radiation_power(self, h, ax)` - *Radiation power bar.*
- `_plot_schwarzschild` (line 1039) `def _plot_schwarzschild(self, h, ax)` - *Schwarzschild radius and surface gravity.*
- `_plot_evaporation` (line 1050) `def _plot_evaporation(self, h, ax)` - *Evaporation timescale bar.*
- `_plot_purity` (line 1057) `def _plot_purity(self, m, ax)` - *Delta and alpha purity bars.*
- `__init__` (line 1068) `def __init__(self, config)` - *Instantiate sub-analyzers and visualizer.*
- `analyze_checkpoint` (line 1076) `def analyze_checkpoint(self, checkpoint_path, output_dir)` - *Load, analyze, visualize, and return aggregated results.*
- `__init__` (line 1132) `def __init__(self, config)` - *Instantiate the single-checkpoint analyzer.*
- `process` (line 1138) `def process(self, input_path, output_dir)` - *Analyze one file or all .pth files in a directory.*
- `_build_summary` (line 1176) `def _build_summary(self, results)` - *Aggregate statistics across checkpoints.*
- `_print_ranking` (line 1203) `def _print_ranking(self, results)` - *Log the best checkpoint by delta and alpha.*
- `_safe_stats` (line 1185) `def _safe_stats(vals)`
- `_info` (line 1210) `def _info(idx)`
- `__init__` (line 171) `def __init__(self)`
- `get` (line 176) `def get(self, key, default)`
- `keys` (line 178) `def keys(self)`
- `items` (line 180) `def items(self)`

#### `maxwell_magnetic_orbitals.py`
**Path:** `maxwell_magnetic_orbitals.py`

**Classes:**
- `IsomorphismConfig` (line 40) `class IsomorphismConfig` - *Configuration for the magnetic orbital isomorphism experiment.*
- `LoggerFactory` (line 82) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 96) `class SpectralLayer` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 117) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
- `ModelLoader` (line 141) `class ModelLoader` - *Load the best Maxwell checkpoint.*
- `AnalyticalMultipoleSource` (line 184) `class AnalyticalMultipoleSource` - *Analytical electromagnetic multipole sources.

Fix 2: Real dipole B-field from B = (mu0/4pi)(3(m.r_hat)r_hat - m)/r^3.
Fix 1: theta = pi/2 (equatorial) for all 2D projections.
Fix 4: Proper multipole hierarchy -- l=1 dipole, l=2 quadrupole, etc.*
- `HallProjectionCalculator` (line 267) `class HallProjectionCalculator` - *Fix 3: Multi-angle averaged Hall projection at equatorial theta = pi/2.

At theta=pi/2: nx=cos(phi), ny=sin(phi), nz=0.
We average over HALL_SENSOR_NUM_ANGLES phi values and add |Bz|^2.*
- `TomographicScanner` (line 292) `class TomographicScanner` - *Generate tomographic slices at different effective distances.*
- `HydrogenOrbitalCalculator` (line 310) `class HydrogenOrbitalCalculator` - *Analytical hydrogen orbital wavefunctions.*
- `IsomorphismMetricsCalculator` (line 376) `class IsomorphismMetricsCalculator` - *Quantify structural similarity between EM field patterns and hydrogen orbitals.*
- `OrbitalVisualizer` (line 404) `class OrbitalVisualizer` - *Side-by-side EM field vs hydrogen orbital visualisation.*
- `MagneticOrbitalExperiment` (line 480) `class MagneticOrbitalExperiment` - *Main experiment: analytical control + network response for each orbital.

Fix 4: Only l=1 (p orbitals) use true dipole sources.
l=0 uses monopole proxy, l>=2 uses multipole scalar potential.*

**Functions:**
- `main` (line 585) `def main()` - *Parse arguments and run the experiment.*
- `create_logger` (line 85) `def create_logger(name, level)` - *Create and return a configured logger.*
- `__init__` (line 98) `def __init__(self, channels, grid_size, imaginary_ratio)`
- `forward` (line 106) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `__init__` (line 119) `def __init__(self, config, imaginary_ratio)`
- `forward` (line 132) `def forward(self, x)`
- `__init__` (line 143) `def __init__(self, config)`
- `load` (line 147) `def load(self, checkpoint_dir)` - *Return (model, info_dict) from the best available checkpoint.*
- `_fallback` (line 179) `def _fallback(self)`
- `__init__` (line 192) `def __init__(self, config)` - *Precompute coordinate grids in the equatorial plane.*
- `generate` (line 205) `def generate(self, l, m)` - *Return a (6,H,W) source tensor for the l-th multipole.*
- `_dipole` (line 211) `def _dipole(self, m)` - *Analytical magnetic dipole B-field in equatorial plane.*
- `_multipole` (line 229) `def _multipole(self, l, m)` - *Higher-order multipole from scalar potential gradient.*
- `_monopole_proxy` (line 243) `def _monopole_proxy(self)` - *Isotropic l=0 proxy (current loop).*
- `_normalise_and_pack` (line 250) `def _normalise_and_pack(self, Bx, By, Bz, scale)` - *Sanitise, normalise, and pack into 6-channel tensor.*
- `get_analytical_density` (line 260) `def get_analytical_density(self, l, m)` - *Return normalised |B|^2 for analytical control (no network).*
- `__init__` (line 274) `def __init__(self, config)`
- `project` (line 277) `def project(self, model_output)` - *Multi-angle averaged Hall projection.*
- `__init__` (line 294) `def __init__(self, config)`
- `scan` (line 297) `def scan(self, model, source, n_slices)` - *Return a list of 2D Hall projection slices.*
- `__init__` (line 312) `def __init__(self, config)`
- `radial_wavefunction` (line 315) `def radial_wavefunction(self, n, l, r)` - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 323) `def spherical_harmonic_real(self, l, m, theta, phi)` - *Real spherical harmonic Y_l^m.*
- `probability_density_2d` (line 330) `def probability_density_2d(self, n, l, m, grid_size)` - *Fix 1: |psi(r, theta=pi/2, phi)|^2 in equatorial plane.*
- `sample_orbital_3d` (line 345) `def sample_orbital_3d(self, n, l, m, num_samples)` - *Monte Carlo rejection sampling of |psi|^2.*
- `__init__` (line 378) `def __init__(self, config)`
- `compute` (line 381) `def compute(self, em_density, quantum_density)` - *Return spatial correlation, node overlap, symmetry correlation, KL divergence.*
- `__init__` (line 406) `def __init__(self, config)`
- `visualize_comparison` (line 409) `def visualize_comparison(self, em_density, quantum_density, metrics, label, tomo_slices, orbital_3d, save_path, analytical_density)` - *Render comparison figure with analytical control row.*
- `__init__` (line 487) `def __init__(self, config)`
- `run` (line 498) `def run(self, output_dir, checkpoint_dir)` - *Execute the full protocol.*
- `_analyze` (line 528) `def _analyze(self, model, n, l, m, label, out)` - *Full protocol for one orbital.*
- `_summary` (line 544) `def _summary(self, results, info)` - *Aggregate.*
- `_interp` (line 562) `def _interp(self, ma, mn, mp)` - *Narrative interpretation.*
- `_print` (line 573) `def _print(self, s)` - *Log summary.*

#### `maxwell_magnetic_orbitals_v2.py`
**Path:** `maxwell_magnetic_orbitals_v2.py`

**Classes:**
- `Config` (line 55) `class Config` - *Configuration for the v2 isomorphism experiment.*
- `LoggerFactory` (line 91) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 105) `class SpectralLayer` - *Spectral convolution layer.*
- `MaxwellSpectralNetwork` (line 129) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics.*
- `AnalyticalMultipoleSource` (line 163) `class AnalyticalMultipoleSource` - *Analytical EM multipole sources.*
- `PoissonEvolver` (line 234) `class PoissonEvolver` - *Strategy A: Evolve the dipole source using the Poisson equation.

Solves nabla^2 phi = -rho in Fourier space, computes E = -grad(phi),
and returns the field energy density.  This is pure Maxwell physics
with no neural network.*
- `ChannelAwareProjection` (line 270) `class ChannelAwareProjection` - *Strategy B: Physically-informed input projection.

Instead of a single Conv2d(6, 32, 1) that scrambles channels,
this processes each field component (Ex, Ey, Bz) separately with
its own 2->hidden/3 projection, then concatenates.*
- `HallProjector` (line 296) `class HallProjector` - *Multi-angle averaged Hall projection.*
- `HydrogenOrbitalCalculator` (line 323) `class HydrogenOrbitalCalculator` - *Analytical hydrogen orbital wavefunctions.*
- `Visualizer` (line 419) `class Visualizer` - *Comprehensive multi-strategy comparison visualisation.*
- `IsomorphismExperimentV2` (line 479) `class IsomorphismExperimentV2` - *Multi-strategy isomorphism experiment.

For each orbital, runs:
  A) Analytical control (no network)
  B) Poisson evolution (pure physics)
  C) Full network (standard forward pass)
  D) Direct spectral (bypass input_proj, feed spectral layers directly)*

**Functions:**
- `spatial_corr` (line 387) `def spatial_corr(a, b, eps)` - *Cosine similarity between two flattened maps.*
- `node_overlap` (line 393) `def node_overlap(a, b, thr)` - *Jaccard index of nodal regions.*
- `symmetry_corr` (line 402) `def symmetry_corr(a, b)` - *Correlation of angular Fourier power spectra.*
- `full_metrics` (line 410) `def full_metrics(em, qd, config)` - *Compute all isomorphism metrics.*
- `main` (line 658) `def main()` - *Parse arguments and run the v2 experiment.*
- `create_logger` (line 94) `def create_logger(name, level)` - *Create and return a configured logger.*
- `__init__` (line 107) `def __init__(self, channels, grid_size, imaginary_ratio)` - *Initialise real and imaginary kernel parameters.*
- `forward` (line 116) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `__init__` (line 131) `def __init__(self, config, imaginary_ratio)` - *Build all sub-layers.*
- `forward` (line 147) `def forward(self, x)` - *Standard forward pass.*
- `forward_spectral_only` (line 156) `def forward_spectral_only(self, x_expanded)` - *Apply only the spectral layers (bypass input/expansion projections).*
- `__init__` (line 165) `def __init__(self, config)` - *Precompute coordinate grids.*
- `generate` (line 177) `def generate(self, l, m)` - *Return a (6,H,W) source tensor.*
- `_dipole` (line 183) `def _dipole(self, m)` - *Analytical magnetic dipole in equatorial plane.*
- `_multipole` (line 201) `def _multipole(self, l, m)` - *Higher-order multipole from scalar potential gradient.*
- `_monopole` (line 212) `def _monopole(self)` - *Isotropic l=0 proxy.*
- `_pack` (line 218) `def _pack(self, Bx, By, Bz, scale)` - *Normalise and pack into 6-channel tensor.*
- `get_density` (line 227) `def get_density(self, l, m)` - *Return normalised |B|^2 for analytical control.*
- `__init__` (line 242) `def __init__(self, config)` - *Store config reference.*
- `evolve` (line 246) `def evolve(self, source_6ch)` - *Treat the Bz channel as charge density, solve Poisson, return |E|^2.

This mimics what the network should ideally learn: the electrostatic
response to a given source configuration.*
- `__init__` (line 278) `def __init__(self, config)` - *Build per-component projections.*
- `forward` (line 288) `def forward(self, x)` - *Process each (Re, Im) pair separately then concatenate.*
- `__init__` (line 298) `def __init__(self, config)` - *Store config reference.*
- `project_6ch` (line 302) `def project_6ch(self, tensor)` - *Project a 6-channel field tensor to scalar density.*
- `project_energy` (line 316) `def project_energy(self, tensor)` - *Project an arbitrary multi-channel tensor to scalar energy density.*
- `__init__` (line 325) `def __init__(self, config)` - *Store config reference.*
- `radial_wavefunction` (line 329) `def radial_wavefunction(self, n, l, r)` - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 337) `def spherical_harmonic_real(self, l, m, theta, phi)` - *Real spherical harmonic.*
- `density_2d` (line 344) `def density_2d(self, n, l, m, grid_size)` - *2D |psi|^2 in equatorial plane.*
- `sample_3d` (line 357) `def sample_3d(self, n, l, m, num)` - *Monte Carlo rejection sampling.*
- `__init__` (line 421) `def __init__(self, config)` - *Store config reference.*
- `render` (line 425) `def render(self, label, strategies, qd, orbital_3d, save_path)` - *Render comparison of all strategies for one orbital.*
- `__init__` (line 489) `def __init__(self, config)` - *Initialise all sub-components.*
- `_load_model` (line 499) `def _load_model(self, checkpoint_dir)` - *Load trained checkpoint.*
- `run` (line 527) `def run(self, output_dir, checkpoint_dir)` - *Execute the full multi-strategy experiment.*
- `_analyze` (line 557) `def _analyze(self, model, n, l, m, label, output_dir)` - *Run all strategies for one orbital.*
- `_summary` (line 591) `def _summary(self, results, info)` - *Aggregate results across orbitals and strategies.*
- `_interpret` (line 624) `def _interpret(self, agg, p_agg)` - *Narrative interpretation.*
- `_print_summary` (line 646) `def _print_summary(self, s)` - *Log the summary.*

#### `maxwell_orbital_diagnostic.py`
**Path:** `maxwell_orbital_diagnostic.py`

**Classes:**
- `DiagnosticConfig` (line 47) `class DiagnosticConfig` - *Configuration for the diagnostic suite.*
- `LoggerFactory` (line 80) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 94) `class SpectralLayer` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 128) `class MaxwellSpectralNetwork` - *Neural network for learning Maxwell equation dynamics.*
- `AnalyticalMultipoleSource` (line 182) `class AnalyticalMultipoleSource` - *Analytical EM multipole sources (same as corrected main script).*
- `HallProjectionCalculator` (line 254) `class HallProjectionCalculator` - *Multi-angle averaged Hall projection at equatorial theta = pi/2.*
- `HydrogenOrbitalCalculator` (line 281) `class HydrogenOrbitalCalculator` - *Analytical hydrogen orbital wavefunctions.*
- `PassthroughTest` (line 324) `class PassthroughTest` - *Mode 1: Identity-initialised network.

If isomorphism survives passthrough, the projection pipeline is correct.*
- `LayerTraceTest` (line 385) `class LayerTraceTest` - *Mode 2: Layer-by-layer trace through a trained network.

Measures spatial correlation after every sub-layer to find where
the angular structure collapses.*
- `SymmetryTrainingTest` (line 499) `class SymmetryTrainingTest` - *Mode 3: Short training with rotational symmetry preservation loss.

Loss = MSE(output, target) + weight * SymmetryLoss
where SymmetryLoss penalises changes in the angular power spectrum
between input and output.*
- `DiagnosticSuite` (line 596) `class DiagnosticSuite` - *Orchestrate all three diagnostic modes.*

**Functions:**
- `compute_spatial_correlation` (line 316) `def compute_spatial_correlation(a, b, eps)` - *Cosine similarity between two flattened density maps.*
- `main` (line 625) `def main()` - *Parse arguments and run the diagnostic suite.*
- `create_logger` (line 83) `def create_logger(name, level)` - *Create and return a configured logger.*
- `__init__` (line 96) `def __init__(self, channels, grid_size, imaginary_ratio)` - *Initialise real and imaginary kernel parameters.*
- `forward` (line 105) `def forward(self, x)` - *Apply spectral convolution in Fourier space.*
- `init_identity` (line 117) `def init_identity(self, scale)` - *Initialise kernels near identity: real=small, imag=0.*
- `__init__` (line 130) `def __init__(self, config, imaginary_ratio)` - *Build all sub-layers.*
- `forward` (line 146) `def forward(self, x)` - *Forward pass.*
- `forward_with_intermediates` (line 155) `def forward_with_intermediates(self, x)` - *Forward pass returning the output after every sub-layer.*
- `init_identity` (line 167) `def init_identity(self)` - *Initialise all layers near identity / passthrough.*
- `__init__` (line 184) `def __init__(self, config)` - *Precompute coordinate grids in the equatorial plane.*
- `generate` (line 196) `def generate(self, l, m)` - *Return a (6,H,W) source tensor for the l-th multipole.*
- `_dipole` (line 202) `def _dipole(self, m)` - *Analytical magnetic dipole B-field in equatorial plane.*
- `_multipole` (line 220) `def _multipole(self, l, m)` - *Higher-order multipole from scalar potential gradient.*
- `_monopole_proxy` (line 232) `def _monopole_proxy(self)` - *Isotropic l=0 proxy.*
- `_pack` (line 238) `def _pack(self, Bx, By, Bz, scale)` - *Sanitise, normalise, pack into 6 channels.*
- `get_analytical_density` (line 247) `def get_analytical_density(self, l, m)` - *Return normalised |B|^2.*
- `__init__` (line 256) `def __init__(self, config)` - *Store config reference.*
- `project` (line 260) `def project(self, tensor)` - *Multi-angle averaged Hall projection.*
- `project_intermediate` (line 273) `def project_intermediate(self, tensor)` - *Project an intermediate activation to a scalar energy density.*
- `__init__` (line 283) `def __init__(self, config)` - *Store config reference.*
- `radial_wavefunction` (line 287) `def radial_wavefunction(self, n, l, r)` - *Non-relativistic radial wavefunction R_nl(r).*
- `spherical_harmonic_real` (line 295) `def spherical_harmonic_real(self, l, m, theta, phi)` - *Real spherical harmonic Y_l^m.*
- `probability_density_2d` (line 302) `def probability_density_2d(self, n, l, m, grid_size)` - *2D |psi|^2 in equatorial plane (theta=pi/2).*
- `__init__` (line 330) `def __init__(self, config)` - *Initialise sub-components.*
- `run` (line 338) `def run(self, output_dir)` - *Test all orbitals with an identity-initialised network.*
- `__init__` (line 392) `def __init__(self, config)` - *Initialise sub-components.*
- `run` (line 400) `def run(self, checkpoint_dir, output_dir)` - *Trace a trained model layer by layer.*
- `_find_collapse` (line 436) `def _find_collapse(self, trace)` - *Find the layer where correlation drops most sharply.*
- `_plot_traces` (line 448) `def _plot_traces(self, all_traces, output_dir)` - *Plot correlation vs layer index for all orbitals.*
- `_load_model` (line 472) `def _load_model(self, checkpoint_dir)` - *Load the trained model.*
- `__init__` (line 507) `def __init__(self, config)` - *Initialise sub-components.*
- `compute_angular_power` (line 515) `def compute_angular_power(self, tensor)` - *Compute the angular power spectrum of a 2D field via azimuthal FFT.*
- `symmetry_loss` (line 522) `def symmetry_loss(self, input_tensor, output_tensor)` - *Penalise angular power spectrum distortion.*
- `run` (line 528) `def run(self, output_dir)` - *Train a fresh model with symmetry loss and track isomorphism.*
- `_plot_history` (line 572) `def _plot_history(self, history, output_dir)` - *Plot training loss and correlation over epochs.*
- `__init__` (line 598) `def __init__(self, config)` - *Initialise all test modes.*
- `run_all` (line 606) `def run_all(self, output_dir, checkpoint_dir)` - *Execute all three diagnostic modes and save results.*

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
