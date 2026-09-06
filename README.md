# Maxwell Equations Grokking via Hamiltonian Topological Crystallization

I study whether a neural network trained on Maxwell's equations undergoes a phase transition analogous to topological crystallization in condensed matter. The central claim is that the dynamics of weight discretization under spectral-domain training can be mapped onto a thermodynamic trajectory through a glass phase, a polycrystalline regime, and ideally toward a perfect crystal. I do not claim this happens reliably. The evidence suggests it does not.

DOI: [pending]

## The Question

A spectral neural network -- convolutional layers operating in Fourier space -- is trained to predict electromagnetic field evolution on a periodic grid. Simultaneously, a regularization pressure pushes the weights toward discrete integer values. Two forces compete: the data-fitting loss moves weights freely to minimize prediction error, while the lambda penalty drives quantization. The system should, in principle, trace a path from an amorphous phase through a glass into a crystal. I built protocols to test this. The results are mixed.

## What I Built

The architecture is a small spectral network:

- 6 input channels (3 field components in TM mode, encoded as complex)
- Two 1x1 convolutions (expansion to 64 hidden)
- Two SpectralLayer modules (rFFT2, complex kernel multiplication, irFFT2)
- Two 1x1 convolutions back to 6 channels

The grid is 16x16. The data is synthetic: analytical Maxwell evolution of random initial conditions. The network has approximately 2.4 million parameters.

## The Five-Phase Protocol

**Phase 0: Spectral Kernel Ratio Optimization.** I sweep the ratio of imaginary to real kernel norms across ensembles of random matrices, interpolating between the Gaussian Orthogonal Ensemble (GOE, beta=1) and the Gaussian Unitary Ensemble (GUE, beta=2). The optimal ratio minimizes the combined nearest-neighbor spacing loss against the Wigner surmise. The optimum is 0.311 (combined loss 0.1356).

**Phase 1: Batch Size Prospecting.** Short training runs at batch sizes 8, 16, 32, 64. I select the size that minimizes the discretization margin delta while keeping the gradient covariance condition number kappa low. Best: batch size 32 (delta=0.486, kappa=1.0).

**Phase 2: Seed Mining.** Two hundred random seeds are tested with short training runs. Seeds are ranked by delta velocity -- preference for decreasing delta ("cooling") with kappa near 1 ("crystalline"). Best seed: 186 (delta=0.458, dDelta/dt=-1.2e-5, kappa=1.0).

**Phase 3: Full Training with Grokking Detection.** The chosen seed and batch size are trained for up to 5000 epochs. Grokking is detected when training and validation accuracy exceed 0.99 and the delta slope is negative. Grokking occurs at epoch 50 (train_acc=1.0, val_acc=1.0, delta=0.458). Training continues to approximately epoch 3700.

**Phase 4: Simulated Annealing Refinement.** Exponential cooling, Metropolis acceptance, Perelman-style Ricci flow smoothing, and surgery on curvature singularities. This phase attempts to push the system below the crystal threshold (delta < 0.1). It does not succeed.

## The Glass Ceiling

Across all 11 analyzed checkpoints (epochs 314 through 496), the phase classification is uniformly "Cold Glass" or "EM_Glass." Delta stabilizes near 0.45. The alpha purity metric reaches approximately 0.79, an order of magnitude below the crystal threshold of 7.0. The system learns the field evolution perfectly by epoch 50 but the weights never crystallize.

This is the central negative result. Grokking occurs. Crystallization does not.

## Black Hole Thermodynamic Analogs

I map the weight state onto gravitational and thermodynamic constants via heuristics:

- G_eff from force of crystallization (gradient divided by distance-to-integer squared)
- hbar_eff from four estimates: Heisenberg uncertainty on weight deviations, action quantization, conductance (accuracy over loss), and configurational information
- k_B_eff from configurational entropy of the weight histogram
- c_eff from the Planck relation and spectral velocity of weight matrices

These feed into the Bekenstein-Hawking formulas:

- S_BH = 1.95e136 (entropy)
- T_H = 4.80e110 K (Hawking temperature)
- r_Schwarzschild = 1.18e-65 m

The temperature is extraordinarily high. The entropy is astronomically large. Whether these numbers are physically meaningful is an open question. They are analogies, not derivations.

## Magnetic Orbital Isomorphism

I test whether the electromagnetic field patterns produced by the network are isomorphic to hydrogen orbital probability densities. Magnetic multipole sources (dipole for l=1, quadrupole for l=2) are fed through the network, and the output is compared to hydrogen |psi|^2 for (n,l,m) states in the equatorial plane.

The analytical control achieves spatial correlation of approximately 0.97 with hydrogen orbitals. The trained network achieves approximately 0.14.

The collapse occurs at the first layer: a generic 1x1 convolution (input_proj from 6 to 32 channels) destroys the physical semantics of the field components. The angular structure never recovers. This is an architectural limitation, not a fundamental one. Version 2 of the experiment introduces channel-aware projections and bypass strategies that partially mitigate the collapse (Poisson strategy: mean correlation 0.317), but the full network remains degraded.

## Limitations

I state these explicitly.

1. The system does not reach a perfect crystal. The glass phase appears stable over thousands of epochs. Phase 4 refinement does not break the barrier. This may reflect a fundamental limitation of 1x1 convolution layers for weight discretization, or a flaw in the lambda scheduling protocol.

2. The black hole thermodynamic mapping is heuristic. The effective constants are derived from plausible but non-unique formulas. The claim is not that a delta~0.45 network is a black hole. The claim is that the formal structure of thermodynamics provides a useful language for describing the weight ensemble.

3. The random matrix theory interpolation (Phase 0) operates on synthetic Gaussian matrices, not on the learned kernels. The assumption that the spectral layer operators will resemble the interpolated ensembles is untested.

4. The data is synthetic. The network learns an analytical Maxwell operator, not measured electromagnetic fields. The grokking phenomenon demonstrates that the network can discover the known solution, but says nothing about discovery from physical data.

5. The architecture is small (16x16 grid, 2 spectral layers, approximately 2.4M parameters). Results may not generalize to larger scales.

## The Code

- **maxwell_crystal.py**: main training pipeline (approximately 3300 lines). Orchestrates all five phases.
- **maxwell_crystallography_suite.py**: post-hoc analysis of any checkpoint. Computes GOE/GUE diagnostics, weight integrity, discretization metrics, spectral geometry, Ricci curvature, Berry phase, thermodynamics, Schrodinger analysis, and topological phase detection.
- **maxwell_field_hawking_suite.py**: black hole thermodynamic analogs. HawkingRadiationCalculator and WeightLatticeMapper.
- **maxwell_magnetic_orbitals.py** and **maxwell_magnetic_orbitals_v2.py**: hydrogen orbital isomorphism experiments with multiple reconstruction strategies.
- **maxwell_orbital_diagnostic.py**: layer tracing, passthrough tests, and symmetry training modes.
- **app.py**: Flask web interface for interactive exploration.
- **RESULTS.md**: full training log from the March 14, 2026 run.
- **analysis_output/**, **maxwell_analysis/**, **orbital_results/**: per-checkpoint metrics, visualizations, and analysis summaries.

## License

AGPL v3. See LICENSE.

---

grisun0


---
### Related Physics and Mathematics Projects
Exploring fundamental patterns and equations:
- [schrodinger](https://github.com/grisuno/schrodinger): Quantum mechanics and waves.
- [dirac](https://github.com/grisuno/dirac): Relativistic electromagnetism.
- [algebra-de-grok](https://github.com/grisuno/algebra-de-grok): Algebra applied to physical equations.

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Analysis outputs are available:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings
  - `SECURITY.md` -- Findings by severity

AI agents: Read `readmenator-agent/INDEX.md` for fast project context.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference.
<!-- /readmenator-kb-link -->

