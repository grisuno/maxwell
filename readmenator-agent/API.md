# API

## maxwell_crystal.py

### main (method) `def main()`
- Defined: `maxwell_crystal.py:3112`
- Doc: Entry point: parse arguments, run the five-phase protocol.

### detect (method) `def detect(self, spectral_field)`
- Defined: `maxwell_crystal.py:261`
- Doc: Detect phase characteristics from spectral field data.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:270`
- Doc: Compute metrics for the given model and optional keyword arguments.

### set_seed (method) `def set_seed(seed, device)`
- Defined: `maxwell_crystal.py:279`
- Doc: Set random seeds across all relevant libraries and backends.

### create_logger (method) `def create_logger(name, level)`
- Defined: `maxwell_crystal.py:294`
- Doc: Create and return a configured logger instance.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:321`
- Doc: Precompute wavenumber grids and material constants.

### _precompute_operators (method) `def _precompute_operators(self)`
- Defined: `maxwell_crystal.py:331`
- Doc: Build Fourier-space wavenumber grids.

### apply_maxwell_operator (method) `def apply_maxwell_operator(self, fields)`
- Defined: `maxwell_crystal.py:339`
- Doc: Apply the Maxwell curl operator to a (batch, 3, H, W) real tensor.

### time_evolution (method) `def time_evolution(self, fields, dt)`
- Defined: `maxwell_crystal.py:371`
- Doc: Advance electromagnetic fields by one time step using Euler integration

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:406`
- Doc: Store reference to global configuration.

### generate_goe_matrix (method) `def generate_goe_matrix(size, device)`
- Defined: `maxwell_crystal.py:411`
- Doc: Return a sample from the Gaussian Orthogonal Ensemble.

### generate_gue_matrix (method) `def generate_gue_matrix(size, device)`
- Defined: `maxwell_crystal.py:417`
- Doc: Return a sample from the Gaussian Unitary Ensemble.

### generate_interpolated_matrix (method) `def generate_interpolated_matrix(self, size, imaginary_ratio, device)`
- Defined: `maxwell_crystal.py:425`
- Doc: Return a complex Hermitian matrix interpolating between GOE and GUE.

### compute_eigenvalue_spacing (method) `def compute_eigenvalue_spacing(self, eigenvalues)`
- Defined: `maxwell_crystal.py:443`
- Doc: Unfold eigenvalues via polynomial fit and return normalised spacings.

### compute_spacing_distribution_loss (method) `def compute_spacing_distribution_loss(self, spacings, target)`
- Defined: `maxwell_crystal.py:458`
- Doc: MSE between the empirical P(s) histogram and the Wigner surmise.

### compute_dyson_index (method) `def compute_dyson_index(self, eigenvalues, spacings)`
- Defined: `maxwell_crystal.py:481`
- Doc: Estimate Dyson beta from small-spacing power-law P(s) ~ s^beta.

### compute_pair_correlation (method) `def compute_pair_correlation(self, eigenvalues, s_range, num_points)`
- Defined: `maxwell_crystal.py:506`
- Doc: Two-level correlation function R_2(s).

### compute_correlation_loss (method) `def compute_correlation_loss(self, eigenvalues, target)`
- Defined: `maxwell_crystal.py:533`
- Doc: MSE between empirical R_2(s) and the analytical prediction.

### compute_spectral_stats_for_ratio (method) `def compute_spectral_stats_for_ratio(self, imaginary_ratio, matrix_size, num_matrices, device)`
- Defined: `maxwell_crystal.py:552`
- Doc: Ensemble-averaged spectral statistics at a given imaginary ratio.

### __init__ (method) `def __init__(self, channels, grid_size, imaginary_ratio)`
- Defined: `maxwell_crystal.py:619`
- Doc: Initialise real and imaginary kernel parameters.

### _apply_imaginary_ratio (method) `def _apply_imaginary_ratio(self)`
- Defined: `maxwell_crystal.py:638`
- Doc: Scale the imaginary kernel by the imaginary ratio at init time.

### set_imaginary_ratio (method) `def set_imaginary_ratio(self, ratio)`
- Defined: `maxwell_crystal.py:643`
- Doc: Rescale imaginary kernel to reflect a new imaginary ratio.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_crystal.py:651`
- Doc: Apply spectral convolution in Fourier space.

### get_spectral_operator (method) `def get_spectral_operator(self)`
- Defined: `maxwell_crystal.py:674`
- Doc: Extract a (channels x channels) complex matrix for eigenvalue analysis.

### __init__ (method) `def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, field_components, imaginary_ratio)`
- Defined: `maxwell_crystal.py:696`
- Doc: Build all sub-layers with the given architectural parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_crystal.py:721`
- Doc: Forward pass through the full spectral network.

### set_imaginary_ratio (method) `def set_imaginary_ratio(self, ratio)`
- Defined: `maxwell_crystal.py:732`
- Doc: Propagate imaginary ratio to all spectral layers.

### get_kernel_ratio (method) `def get_kernel_ratio(self)`
- Defined: `maxwell_crystal.py:738`
- Doc: Compute the effective imaginary-to-real kernel norm ratio.

### __init__ (method) `def __init__(self, grid_size, hidden_dim, num_spectral_layers)`
- Defined: `maxwell_crystal.py:752`
- Doc: Build the backbone with spectral layers.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_crystal.py:768`
- Doc: Single-channel forward pass.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:786`
- Doc: Attempt backbone load; fall back to analytical operator.

### _try_load_backbone (method) `def _try_load_backbone(self)`
- Defined: `maxwell_crystal.py:794`
- Doc: Load backbone weights from disk if available and enabled.

### apply_operator (method) `def apply_operator(self, fields)`
- Defined: `maxwell_crystal.py:829`
- Doc: Apply the Maxwell operator to the electromagnetic field tensor.

### time_evolve (method) `def time_evolve(self, fields, dt)`
- Defined: `maxwell_crystal.py:833`
- Doc: Advance fields by one time step.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:848`
- Doc: Store grid parameters from configuration.

### gaussian_source (method) `def gaussian_source(self)`
- Defined: `maxwell_crystal.py:853`
- Doc: Smooth Gaussian current-density envelope centred on the grid.

### dipole_source (method) `def dipole_source(self)`
- Defined: `maxwell_crystal.py:861`
- Doc: 1/r dipole-like source envelope.

### plane_wave_source (method) `def plane_wave_source(self)`
- Defined: `maxwell_crystal.py:870`
- Doc: Sinusoidal plane-wave seed for Ex, Ey components.

### periodic_medium (method) `def periodic_medium(self)`
- Defined: `maxwell_crystal.py:879`
- Doc: Periodic permittivity modulation (photonic-crystal-like).

### generate_mixed_source (method) `def generate_mixed_source(self, seed)`
- Defined: `maxwell_crystal.py:886`
- Doc: Dirichlet-weighted superposition of all source types.

### __init__ (method) `def __init__(self, config, hamiltonian_engine, seed)`
- Defined: `maxwell_crystal.py:911`
- Doc: Generate all samples at construction time.

### _generate_initial_fields (method) `def _generate_initial_fields(self, source, sample_seed)`
- Defined: `maxwell_crystal.py:954`
- Doc: Create a random initial electromagnetic field configuration.

### _time_evolve_fields (method) `def _time_evolve_fields(self, fields, source, energy)`
- Defined: `maxwell_crystal.py:983`
- Doc: Advance the EM field through multiple time steps under the Maxwell operator.

### _fields_to_real_imag (method) `def _fields_to_real_imag(self, fields)`
- Defined: `maxwell_crystal.py:1012`
- Doc: Convert (3, H, W) complex tensor to (6, H, W) real tensor.

### __len__ (method) `def __len__(self)`
- Defined: `maxwell_crystal.py:1020`
- Doc: Number of training samples.

### __getitem__ (method) `def __getitem__(self, idx)`
- Defined: `maxwell_crystal.py:1024`
- Doc: Return (input, target) pair for training.

### get_validation_batch (method) `def get_validation_batch(self)`
- Defined: `maxwell_crystal.py:1028`
- Doc: Return the full validation set as a single batch.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1036`
- Doc: Precompute wavenumber magnitude grid.

### compute_full_spectrum (method) `def compute_full_spectrum(self, spectral_field)`
- Defined: `maxwell_crystal.py:1045`
- Doc: Return magnitude, phase, power, radial profile, and derived statistics.

### detect_bragg_peaks (method) `def detect_bragg_peaks(self, power_spectrum, threshold_sigma)`
- Defined: `maxwell_crystal.py:1098`
- Doc: Identify local maxima in the power spectrum exceeding a statistical threshold.

### compute_resonance_metrics (method) `def compute_resonance_metrics(self, spectral_field)`
- Defined: `maxwell_crystal.py:1146`
- Doc: Aggregate spectral concentration, phase coherence, and Bragg analysis.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1186`
- Doc: Initialise wavenumber grids and full Fourier sub-analyzer.

### compute_mass_center (method) `def compute_mass_center(self, spectral_field)`
- Defined: `maxwell_crystal.py:1195`
- Doc: Return centre of mass, inertia tensor, anisotropy, and resonance diagnostics.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1250`
- Doc: Initialise history buffers and state variables.

### detect (method) `def detect(self, spectral_field)`
- Defined: `maxwell_crystal.py:1258`
- Doc: Run full topological phase detection and return diagnostic dict.

### extract (method) `def extract(model, grid_size)`
- Defined: `maxwell_crystal.py:1316`
- Doc: Return the mean complex spectral kernel across all spectral layers.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1336`
- Doc: Initialise with base lambda pressure.

### forward (method) `def forward(self, phase_info, epoch)`
- Defined: `maxwell_crystal.py:1342`
- Doc: Compute quadrant, localisation, and resonance penalty terms.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1368`
- Doc: Store pressure decay rate from config.

### apply (method) `def apply(self, model, phase_info)`
- Defined: `maxwell_crystal.py:1373`
- Doc: Multiplicatively decay parameters when crystal phase is detected.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1387`
- Doc: Initialise all topological sub-components.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:1395`
- Doc: Extract spectral field, detect phase, compute loss, return full metrics dict.

### apply_crystallization_pressure (method) `def apply_crystallization_pressure(self, model, topo_metrics)`
- Defined: `maxwell_crystal.py:1429`
- Doc: Delegate pressure application to the sub-component.

### _empty_metrics (method) `def _empty_metrics()`
- Defined: `maxwell_crystal.py:1436`
- Doc: Return a zero-valued metrics dict when topological analysis is disabled.

### compute_local_complexity (method) `def compute_local_complexity(weights, epsilon)`
- Defined: `maxwell_crystal.py:1457`
- Doc: Return a scalar in [0, 1] measuring weight diversity.

### compute_superposition (method) `def compute_superposition(weights)`
- Defined: `maxwell_crystal.py:1476`
- Doc: Return the mean absolute off-diagonal Pearson correlation.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1501`
- Doc: Store config and create logger.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:1506`
- Doc: Facade that delegates to compute_all_metrics.

### compute_kappa (method) `def compute_kappa(self, model, val_x, val_y, num_batches)`
- Defined: `maxwell_crystal.py:1512`
- Doc: Gradient covariance condition number kappa = lambda_max / lambda_min.

### compute_discretization_margin (method) `def compute_discretization_margin(self, model)`
- Defined: `maxwell_crystal.py:1563`
- Doc: delta = max_i |theta_i - round(theta_i)|.

### compute_alpha_purity (method) `def compute_alpha_purity(self, model)`
- Defined: `maxwell_crystal.py:1572`
- Doc: alpha = -log(delta).

### compute_kappa_quantum (method) `def compute_kappa_quantum(self, model)`
- Defined: `maxwell_crystal.py:1579`
- Doc: Quantum-regularised condition number with hbar regularisation.

### compute_poynting_vector (method) `def compute_poynting_vector(self, model)`
- Defined: `maxwell_crystal.py:1601`
- Doc: Compute the electromagnetic Poynting-like energy flow through the network.

### compute_hbar_effective (method) `def compute_hbar_effective(self, model, lambda_pressure)`
- Defined: `maxwell_crystal.py:1651`
- Doc: hbar_eff = delta^2 * lambda / omega.

### compute_all_metrics (method) `def compute_all_metrics(self, model, val_x, val_y)`
- Defined: `maxwell_crystal.py:1661`
- Doc: Compute delta, alpha, kappa, kappa_q, poynting, purity, and is_crystal.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1702`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:1706`
- Doc: Return all thermodynamic observables.

### compute_effective_temperature (method) `def compute_effective_temperature(self, gradient_buffer, learning_rate)`
- Defined: `maxwell_crystal.py:1727`
- Doc: T_eff = (lr / 2) * Var(grad).

### compute_specific_heat (method) `def compute_specific_heat(self, loss_history, temp_history)`
- Defined: `maxwell_crystal.py:1750`
- Doc: C_v = Var(U) / T^2.

### compute_gibbs_free_energy (method) `def compute_gibbs_free_energy(self, delta, alpha, temperature)`
- Defined: `maxwell_crystal.py:1762`
- Doc: G = delta - T * (-alpha).

### compute_critical_temperature (method) `def compute_critical_temperature(self, alpha)`
- Defined: `maxwell_crystal.py:1768`
- Doc: T_c = T_0 * exp(-c * alpha).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1776`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:1780`
- Doc: Compute spectral geometry observables from weight outer product.

### _compute_level_spacing_ratio (method) `def _compute_level_spacing_ratio(self, spacings)`
- Defined: `maxwell_crystal.py:1806`
- Doc: Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}) over consecutive spacings.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1822`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:1826`
- Doc: Compute Ricci scalar and sectional curvatures from weight metric.

### _compute_ricci_scalar (method) `def _compute_ricci_scalar(self, metric)`
- Defined: `maxwell_crystal.py:1842`
- Doc: Ricci scalar via inverse eigenvalue sum.

### _estimate_sectional_curvatures (method) `def _estimate_sectional_curvatures(self, metric)`
- Defined: `maxwell_crystal.py:1851`
- Doc: Sample 2x2 sub-block determinants as sectional curvature proxies.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:1868`
- Doc: Initialise curvature history and surgery counter.

### compute_ricci_scalar_fast (method) `def compute_ricci_scalar_fast(self, model)`
- Defined: `maxwell_crystal.py:1877`
- Doc: Fast Ricci scalar estimate from normalised weight outer product.

### compute_local_curvature (method) `def compute_local_curvature(self, param)`
- Defined: `maxwell_crystal.py:1907`
- Doc: Second-difference curvature estimate along the flattened parameter.

### compute_anisotropy (method) `def compute_anisotropy(self, model)`
- Defined: `maxwell_crystal.py:1916`
- Doc: Ratio of smallest to largest covariance eigenvalue of the weight vector.

### compute_ricci_regularization_loss (method) `def compute_ricci_regularization_loss(self, model)`
- Defined: `maxwell_crystal.py:1941`
- Doc: Smoothness penalty proportional to second-difference curvature.

### apply_ricci_flow_step (method) `def apply_ricci_flow_step(self, model, lr)`
- Defined: `maxwell_crystal.py:1959`
- Doc: One step of diffusive Ricci flow smoothing on all parameters.

### perform_perelman_surgery (method) `def perform_perelman_surgery(self, model, ricci_scalar)`
- Defined: `maxwell_crystal.py:1989`
- Doc: Cut singularities (outlier weights) when curvature exceeds the surgery threshold.

### compute_adaptive_lr_factor (method) `def compute_adaptive_lr_factor(self, model)`
- Defined: `maxwell_crystal.py:2031`
- Doc: Reduce learning rate when curvature spikes above recent average.

### get_flow_metrics (method) `def get_flow_metrics(self, model)`
- Defined: `maxwell_crystal.py:2047`
- Doc: Return summary Ricci-flow diagnostics.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2064`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystal.py:2068`
- Doc: Compute weight diffraction pattern and spectral entropy.

### compute_weight_diffraction (method) `def compute_weight_diffraction(self, coeffs)`
- Defined: `maxwell_crystal.py:2073`
- Doc: FFT of concatenated weights with peak detection.

### _compute_spectral_entropy (method) `def _compute_spectral_entropy(power_spectrum)`
- Defined: `maxwell_crystal.py:2092`
- Doc: Shannon entropy of the normalised power spectrum.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2104`
- Doc: Initialise lambda in float64 precision.

### current_lambda (method) `def current_lambda(self)`
- Defined: `maxwell_crystal.py:2114`
- Doc: Current pressure value.

### step (method) `def step(self, epoch)`
- Defined: `maxwell_crystal.py:2118`
- Doc: Increase lambda at fixed epoch intervals.

### compute_regularization_loss (method) `def compute_regularization_loss(self, model)`
- Defined: `maxwell_crystal.py:2126`
- Doc: L2 penalty on distance from nearest integer for each parameter.

### set_lambda (method) `def set_lambda(self, value)`
- Defined: `maxwell_crystal.py:2139`
- Doc: Directly set the lambda value.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2147`
- Doc: Initialise base and accelerated growth factors.

### step_adaptive (method) `def step_adaptive(self, epoch, topo_phase_state)`
- Defined: `maxwell_crystal.py:2153`
- Doc: Grow lambda faster when topological order is emerging.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2172`
- Doc: Initialise temperature schedule.

### temperature (method) `def temperature(self)`
- Defined: `maxwell_crystal.py:2180`
- Doc: Current annealing temperature.

### step (method) `def step(self)`
- Defined: `maxwell_crystal.py:2184`
- Doc: Cool by one step.

### accept_perturbation (method) `def accept_perturbation(self, delta_loss)`
- Defined: `maxwell_crystal.py:2188`
- Doc: Metropolis acceptance criterion.

### should_restart (method) `def should_restart(self, current_delta, best_delta)`
- Defined: `maxwell_crystal.py:2197`
- Doc: Whether the current state has drifted too far from best.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2205`
- Doc: Initialise with base cooling rate.

### step_adaptive (method) `def step_adaptive(self, alignment_trend, resonance_score)`
- Defined: `maxwell_crystal.py:2210`
- Doc: Slow cooling when alignment is growing, speed up when it recedes.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2225`
- Doc: Initialise metric history buffers.

### update_metrics (method) `def update_metrics(self)`
- Defined: `maxwell_crystal.py:2257`
- Doc: Append each provided metric to its history list.

### compute_delta_slope (method) `def compute_delta_slope(self)`
- Defined: `maxwell_crystal.py:2269`
- Doc: Linear regression slope of recent delta values.

### format_progress_bar (method) `def format_progress_bar(self, epoch, total_epochs, phase)`
- Defined: `maxwell_crystal.py:2282`
- Doc: Format all metrics into a multi-line progress string.

### __init__ (method) `def __init__(self, config, checkpoint_dir)`
- Defined: `maxwell_crystal.py:2356`
- Doc: Create checkpoint directory and initialise timer.

### should_save_checkpoint (method) `def should_save_checkpoint(self)`
- Defined: `maxwell_crystal.py:2366`
- Doc: True when at least CHECKPOINT_INTERVAL_MINUTES have elapsed.

### save_checkpoint (method) `def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)`
- Defined: `maxwell_crystal.py:2370`
- Doc: Save model, optimiser, metrics, and config to a timestamped file and latest link.

### load_latest_checkpoint (method) `def load_latest_checkpoint(self)`
- Defined: `maxwell_crystal.py:2399`
- Doc: Load the latest checkpoint if it exists.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2410`
- Doc: Initialise patience buffer.

### should_stop (method) `def should_stop(self, epoch, lc, sp, kappa, delta, temp, cv)`
- Defined: `maxwell_crystal.py:2416`
- Doc: Return True if recent metrics indicate glass formation.

### is_crystal_formed (method) `def is_crystal_formed(self, lc, sp, kappa, delta, temp, cv)`
- Defined: `maxwell_crystal.py:2452`
- Doc: Return True if all metrics are below crystal thresholds.

### check (method) `def check(model)`
- Defined: `maxwell_crystal.py:2471`
- Doc: Return integrity report with counts and corruption ratio.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2501`
- Doc: Instantiate all metric calculators.

### compute_weight_metrics (method) `def compute_weight_metrics(self, model)`
- Defined: `maxwell_crystal.py:2515`
- Doc: Local complexity and superposition averaged over all weight matrices.

### compute_norm_conservation_error (method) `def compute_norm_conservation_error(self, model, val_x)`
- Defined: `maxwell_crystal.py:2530`
- Doc: Relative norm difference between input and output.

### train_single_epoch (method) `def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler, ricci_flow)`
- Defined: `maxwell_crystal.py:2540`
- Doc: Run one epoch of gradient descent with optional regularisation.

### validate (method) `def validate(self, model, val_x, val_y)`
- Defined: `maxwell_crystal.py:2578`
- Doc: Compute validation loss and accuracy.

### collect_all_metrics (method) `def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)`
- Defined: `maxwell_crystal.py:2590`
- Doc: Compute every metric from the paper and return as a flat dict.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystal.py:2673`
- Doc: Initialise spectral statistics calculator.

### optimize_kernel_ratio (method) `def optimize_kernel_ratio(self)`
- Defined: `maxwell_crystal.py:2679`
- Doc: Sweep imaginary ratios and return the one with lowest combined GUE loss.

### __init__ (method) `def __init__(self, config, hamiltonian_engine, imaginary_ratio)`
- Defined: `maxwell_crystal.py:2730`
- Doc: Store engine reference and optimal imaginary ratio.

### prospect (method) `def prospect(self)`
- Defined: `maxwell_crystal.py:2737`
- Doc: Train briefly at each candidate batch size and return the best.

### __init__ (method) `def __init__(self, config, hamiltonian_engine, batch_size, imaginary_ratio)`
- Defined: `maxwell_crystal.py:2789`
- Doc: Store references for dataset and model creation.

### mine (method) `def mine(self)`
- Defined: `maxwell_crystal.py:2798`
- Doc: Evaluate seeds and return the one with best delta velocity and kappa.

### __init__ (method) `def __init__(self, config, hamiltonian_engine, seed, batch_size, imaginary_ratio)`
- Defined: `maxwell_crystal.py:2884`
- Doc: Store all training configuration.

### run_phase3_training (method) `def run_phase3_training(self, start_epoch, model)`
- Defined: `maxwell_crystal.py:2894`
- Doc: Execute Phase 3 and return (model, optimiser, monitor).

### __init__ (method) `def __init__(self, config, hamiltonian_engine, model, optimizer, monitor, seed, batch_size, imaginary_ratio)`
- Defined: `maxwell_crystal.py:3005`
- Doc: Store all refinement parameters.

### run_phase4_refinement (method) `def run_phase4_refinement(self, start_epoch)`
- Defined: `maxwell_crystal.py:3021`
- Doc: Run Phase 4 refinement and return the best model.

### load_latest_checkpoint (method) `def load_latest_checkpoint(mdl, checkpoint_paths)`
- Defined: `maxwell_crystal.py:3193`

### safe_compute (method) `def safe_compute(func)`
- Defined: `maxwell_crystal.py:1672`

### safe_get (method) `def safe_get(key)`
- Defined: `maxwell_crystal.py:2286`

## maxwell_crystallography_suite.py

### main (method) `def main()`
- Defined: `maxwell_crystallography_suite.py:1850`
- Doc: Parse arguments and run the Maxwell crystallography suite.

### create_logger (method) `def create_logger(name, level, config)`
- Defined: `maxwell_crystallography_suite.py:205`
- Doc: Create and return a configured logger.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:221`
- Doc: Compute metrics for the given model.

### detect (method) `def detect(self, spectral_field)`
- Defined: `maxwell_crystallography_suite.py:229`
- Doc: Detect phase from spectral field.

### __init__ (method) `def __init__(self, channels, grid_size, config, imaginary_ratio)`
- Defined: `maxwell_crystallography_suite.py:237`
- Doc: Initialise real and imaginary kernel parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_crystallography_suite.py:252`
- Doc: Apply spectral convolution in Fourier space.

### get_spectral_operator (method) `def get_spectral_operator(self)`
- Defined: `maxwell_crystallography_suite.py:271`
- Doc: Extract (channels x channels) complex Hermitian-like matrix for eigenvalue analysis.

### get_kernel_ratio (method) `def get_kernel_ratio(self)`
- Defined: `maxwell_crystallography_suite.py:279`
- Doc: Return the imaginary-to-real kernel norm ratio.

### __init__ (method) `def __init__(self, config, imaginary_ratio)`
- Defined: `maxwell_crystallography_suite.py:291`
- Doc: Build all sub-layers with the given architectural parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_crystallography_suite.py:309`
- Doc: Forward pass through the full spectral network.

### get_kernel_ratio (method) `def get_kernel_ratio(self)`
- Defined: `maxwell_crystallography_suite.py:320`
- Doc: Compute effective imaginary-to-real kernel norm ratio across all layers.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:340`
- Doc: Store configuration reference.

### extract_spectral_operators (method) `def extract_spectral_operators(self, model)`
- Defined: `maxwell_crystallography_suite.py:344`
- Doc: Return the complex spectral operator from every SpectralLayer in the model.

### compute_eigenvalue_spacing (method) `def compute_eigenvalue_spacing(self, eigenvalues)`
- Defined: `maxwell_crystallography_suite.py:353`
- Doc: Unfold eigenvalues and return normalised nearest-neighbour spacings.

### compute_spacing_distribution_loss (method) `def compute_spacing_distribution_loss(self, spacings, target)`
- Defined: `maxwell_crystallography_suite.py:368`
- Doc: MSE between empirical P(s) and Wigner surmise for GOE or GUE.

### compute_dyson_index (method) `def compute_dyson_index(self, spacings)`
- Defined: `maxwell_crystallography_suite.py:385`
- Doc: Estimate the Dyson beta from small-spacing power-law P(s) ~ s^beta.

### compute_pair_correlation (method) `def compute_pair_correlation(self, eigenvalues)`
- Defined: `maxwell_crystallography_suite.py:402`
- Doc: Two-level correlation function R_2(s).

### compute_correlation_loss (method) `def compute_correlation_loss(self, eigenvalues, target)`
- Defined: `maxwell_crystallography_suite.py:423`
- Doc: MSE between empirical R_2(s) and analytical prediction.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:438`
- Doc: Run full GOE/GUE spectral analysis on all spectral layers.

### _empty_results (method) `def _empty_results()`
- Defined: `maxwell_crystallography_suite.py:512`
- Doc: Return zero-valued results when no spectral layers are found.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:531`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:535`
- Doc: Return integrity report.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:562`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:566`
- Doc: Compute delta, alpha, spectral entropy, and per-layer deltas.

### _compute_spectral_entropy (method) `def _compute_spectral_entropy(self, weights)`
- Defined: `maxwell_crystallography_suite.py:588`
- Doc: Shannon entropy of the normalised power spectrum of concatenated weights.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:605`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:609`
- Doc: Compute spectral geometry observables from weight outer product.

### _compute_level_spacing_ratio (method) `def _compute_level_spacing_ratio(self, spacings)`
- Defined: `maxwell_crystallography_suite.py:638`
- Doc: Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:653`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:657`
- Doc: Compute Ricci scalar and sectional curvatures from weight metric.

### _compute_ricci_scalar (method) `def _compute_ricci_scalar(self, metric)`
- Defined: `maxwell_crystallography_suite.py:672`
- Doc: Ricci scalar via inverse eigenvalue sum.

### _estimate_sectional_curvatures (method) `def _estimate_sectional_curvatures(self, metric)`
- Defined: `maxwell_crystallography_suite.py:681`
- Doc: Sample 2x2 sub-block determinants as sectional curvature proxies.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:698`
- Doc: Initialise logger.

### load_checkpoints (method) `def load_checkpoints(self, checkpoint_dir)`
- Defined: `maxwell_crystallography_suite.py:703`
- Doc: Load all .pth files sorted by epoch.

### _extract_epoch (method) `def _extract_epoch(self, filepath)`
- Defined: `maxwell_crystallography_suite.py:720`
- Doc: Parse epoch number from filename.

### flatten_kernel_params (method) `def flatten_kernel_params(self, state_dict)`
- Defined: `maxwell_crystallography_suite.py:725`
- Doc: Concatenate all spectral layer kernels into a single complex vector.

### compute_berry_connection_discrete (method) `def compute_berry_connection_discrete(self, theta_prev, theta_curr)`
- Defined: `maxwell_crystallography_suite.py:744`
- Doc: Discrete Berry connection between consecutive parameter snapshots.

### calculate_berry_phase (method) `def calculate_berry_phase(self, checkpoint_dir)`
- Defined: `maxwell_crystallography_suite.py:755`
- Doc: Compute total Berry phase, winding number, and cumulative trajectory.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:787`
- Doc: Store config reference.

### extract_state_space (method) `def extract_state_space(self, model)`
- Defined: `maxwell_crystallography_suite.py:791`
- Doc: Extract a composite state-space (A, B, C, D) from weight matrices.

### analyze_stability (method) `def analyze_stability(self, A)`
- Defined: `maxwell_crystallography_suite.py:821`
- Doc: Eigenvalue stability analysis of the state matrix.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:836`
- Doc: Run full control-theory analysis.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:845`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:849`
- Doc: Compute thermodynamic potentials from crystallographic observables.

### _classify_phase (method) `def _classify_phase(self, delta, kappa, temp, alpha)`
- Defined: `maxwell_crystallography_suite.py:866`
- Doc: Classify the thermodynamic phase of the model.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:884`
- Doc: Precompute wavenumber grids.

### compute_full_spectrum (method) `def compute_full_spectrum(self, spectral_field)`
- Defined: `maxwell_crystallography_suite.py:893`
- Doc: Return magnitude, phase, power, and derived statistics.

### compute_resonance_metrics (method) `def compute_resonance_metrics(self, spectral_field)`
- Defined: `maxwell_crystallography_suite.py:913`
- Doc: Aggregate spectral concentration into a resonance score.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:927`
- Doc: Initialise wavenumber grids and sub-analyzers.

### compute_mass_center (method) `def compute_mass_center(self, spectral_field)`
- Defined: `maxwell_crystallography_suite.py:936`
- Doc: Return centre-of-mass coordinates and resonance diagnostics.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:965`
- Doc: Initialise history buffers.

### detect (method) `def detect(self, spectral_field)`
- Defined: `maxwell_crystallography_suite.py:973`
- Doc: Full topological phase detection returning diagnostic dict.

### extract (method) `def extract(model, grid_size)`
- Defined: `maxwell_crystallography_suite.py:1000`
- Doc: Return the mean complex spectral kernel across all spectral layers.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1018`
- Doc: Initialise sub-components.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:1024`
- Doc: Run topological detection and return metrics dict.

### _empty_metrics (method) `def _empty_metrics()`
- Defined: `maxwell_crystallography_suite.py:1042`
- Doc: Zero-valued metrics when analysis is disabled or unavailable.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1054`
- Doc: Store config reference.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:1058`
- Doc: Compute kappa, T_eff, and gradient variance from validation data.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1113`
- Doc: Initialise projection parameters.

### extract_compressed_wavefunction (method) `def extract_compressed_wavefunction(self, model)`
- Defined: `maxwell_crystallography_suite.py:1119`
- Doc: Project the full parameter vector to a fixed-dimension wavefunction.

### _compress_johnson_lindenstrauss (method) `def _compress_johnson_lindenstrauss(self, vector)`
- Defined: `maxwell_crystallography_suite.py:1134`
- Doc: Random projection preserving pairwise distances.

### compute (method) `def compute(self, model)`
- Defined: `maxwell_crystallography_suite.py:1142`
- Doc: Compute wavefunction entropy, participation ratio, and quantum coherence.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1159`
- Doc: Store config reference.

### visualize_checkpoint_analysis (method) `def visualize_checkpoint_analysis(self, results, output_path)`
- Defined: `maxwell_crystallography_suite.py:1163`
- Doc: Render the full 5x4 analysis dashboard to a file.

### _plot_weight_distribution (method) `def _plot_weight_distribution(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1194`
- Doc: Pie chart of valid / NaN / Inf parameter counts.

### _plot_spectral_analysis (method) `def _plot_spectral_analysis(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1206`
- Doc: Bar chart of spectral geometry observables.

### _plot_phase_diagram (method) `def _plot_phase_diagram(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1217`
- Doc: Alpha vs T_eff phase diagram with crystal/glass boundaries.

### _plot_curvature_distribution (method) `def _plot_curvature_distribution(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1232`
- Doc: Bar chart of Ricci curvature summary statistics.

### _plot_level_spacing (method) `def _plot_level_spacing(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1243`
- Doc: Level spacing ratio with Wigner-Dyson and Poisson reference lines.

### _plot_eigenvalue_spectrum (method) `def _plot_eigenvalue_spectrum(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1253`
- Doc: Largest and smallest eigenvalue on log scale.

### _plot_thermodynamic_potentials (method) `def _plot_thermodynamic_potentials(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1267`
- Doc: Gibbs free energy, entropy proxy, and critical temperature.

### _plot_topological_metrics (method) `def _plot_topological_metrics(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1278`
- Doc: Phase state, alignment, and resonance scores.

### _plot_berry_phase (method) `def _plot_berry_phase(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1289`
- Doc: Berry phase arrow on the unit circle.

### _plot_control_stability (method) `def _plot_control_stability(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1304`
- Doc: Stability margin and binary stability flag.

### _plot_quantum_metrics (method) `def _plot_quantum_metrics(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1314`
- Doc: Wavefunction entropy, participation ratio, and coherence.

### _plot_summary_table (method) `def _plot_summary_table(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1325`
- Doc: Text summary of key observables and phase classification.

### _plot_layer_deltas (method) `def _plot_layer_deltas(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1352`
- Doc: Horizontal bar chart of per-layer discretization margins.

### _plot_resonance_metrics (method) `def _plot_resonance_metrics(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1364`
- Doc: Spectral concentration and resonance score bars.

### _plot_spectral_concentration (method) `def _plot_spectral_concentration(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1374`
- Doc: Scatter of spectral gap vs participation ratio.

### _plot_health_score (method) `def _plot_health_score(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1384`
- Doc: Single-bar health score with traffic-light colouring.

### _plot_goe_gue_losses (method) `def _plot_goe_gue_losses(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1393`
- Doc: Grouped bar chart comparing P(s) and R_2(s) losses for GOE and GUE.

### _plot_dyson_beta (method) `def _plot_dyson_beta(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1410`
- Doc: Dyson beta index gauge with GOE and GUE reference markers.

### _plot_kernel_ratios (method) `def _plot_kernel_ratios(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1421`
- Doc: Per-layer imaginary-to-real kernel norm ratios.

### _plot_universality_gauge (method) `def _plot_universality_gauge(self, results, ax)`
- Defined: `maxwell_crystallography_suite.py:1438`
- Doc: Horizontal gauge showing interpolation between GOE and GUE.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1454`
- Doc: Instantiate all sub-calculators.

### analyze_checkpoint (method) `def analyze_checkpoint(self, checkpoint_path, val_data)`
- Defined: `maxwell_crystallography_suite.py:1471`
- Doc: Load a checkpoint, run every analyzer, and return the aggregated results dict.

### _compute_health_score (method) `def _compute_health_score(self, results)`
- Defined: `maxwell_crystallography_suite.py:1553`
- Doc: Weighted average of integrity, purity, MBL, and topological scores.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1578`
- Doc: Initialise analyzer and visualizer.

### process_directory (method) `def process_directory(self, checkpoint_dir, output_dir, val_data)`
- Defined: `maxwell_crystallography_suite.py:1585`
- Doc: Iterate over all .pth files, analyze each, and save results.

### _generate_summary (method) `def _generate_summary(self, all_results)`
- Defined: `maxwell_crystallography_suite.py:1616`
- Doc: Aggregate statistics and rank checkpoints by delta, alpha, accuracy, and health score.

### _generate_evolution_plots (method) `def _generate_evolution_plots(self, all_results, output_dir)`
- Defined: `maxwell_crystallography_suite.py:1735`
- Doc: Time-series plots of key metrics across training.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_crystallography_suite.py:1778`
- Doc: Initialise the suite with all sub-components.

### run_analysis (method) `def run_analysis(self, checkpoint_dir, output_dir)`
- Defined: `maxwell_crystallography_suite.py:1785`
- Doc: Execute full analysis: batch processing, Berry phase, and summary.

### _generate_berry_phase_visualization (method) `def _generate_berry_phase_visualization(self, berry_results, output_dir)`
- Defined: `maxwell_crystallography_suite.py:1804`
- Doc: Dedicated Berry phase figure with phasor diagram and summary text.

### _extract (method) `def _extract(cat, key, default)`
- Defined: `maxwell_crystallography_suite.py:1621`

### _stats (method) `def _stats(vals)`
- Defined: `maxwell_crystallography_suite.py:1624`

### _checkpoint_id (method) `def _checkpoint_id(r)`
- Defined: `maxwell_crystallography_suite.py:1630`

### _best_entry (method) `def _best_entry(idx)`
- Defined: `maxwell_crystallography_suite.py:1662`

## maxwell_field_hawking_suite.py

### load_checkpoint_robust (method) `def load_checkpoint_robust(path, device)`
- Defined: `maxwell_field_hawking_suite.py:185`
- Doc: Load a checkpoint with multiple fallback strategies.

### main (method) `def main()`
- Defined: `maxwell_field_hawking_suite.py:1227`
- Doc: Parse arguments and run the combined analysis suite.

### create_logger (method) `def create_logger(name, level)`
- Defined: `maxwell_field_hawking_suite.py:146`
- Doc: Create and return a configured logger.

### find_class (method) `def find_class(self, module, name)`
- Defined: `maxwell_field_hawking_suite.py:161`
- Doc: Override to handle missing classes gracefully.

### _create_dummy_class (method) `def _create_dummy_class(self, name)`
- Defined: `maxwell_field_hawking_suite.py:168`
- Doc: Return a dummy class that acts like a dictionary.

### __init__ (method) `def __init__(self, channels, grid_size, imaginary_ratio)`
- Defined: `maxwell_field_hawking_suite.py:210`
- Doc: Initialise real and imaginary kernel parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_field_hawking_suite.py:223`
- Doc: Apply spectral convolution in Fourier space.

### __init__ (method) `def __init__(self, config, imaginary_ratio)`
- Defined: `maxwell_field_hawking_suite.py:245`
- Doc: Build all sub-layers.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_field_hawking_suite.py:263`
- Doc: Forward pass through the full spectral network.

### get_flat_parameters (method) `def get_flat_parameters(self)`
- Defined: `maxwell_field_hawking_suite.py:274`
- Doc: Return all parameters as a single flat tensor.

### get_weight_dict (method) `def get_weight_dict(self)`
- Defined: `maxwell_field_hawking_suite.py:278`
- Doc: Return all named parameter tensors as numpy arrays.

### extract (method) `def extract(checkpoint)`
- Defined: `maxwell_field_hawking_suite.py:287`
- Doc: Return a standardised metadata dict from any checkpoint format.

### _find_delta (method) `def _find_delta(data, depth)`
- Defined: `maxwell_field_hawking_suite.py:312`
- Doc: Recursively search for a delta value.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:334`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights, delta)`
- Defined: `maxwell_field_hawking_suite.py:338`
- Doc: Return G_alg, force, and crystallisation pressure.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:369`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights, delta, loss)`
- Defined: `maxwell_field_hawking_suite.py:373`
- Doc: Return four estimates of hbar and their weighted unification.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:415`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights_np, loss, loss_history)`
- Defined: `maxwell_field_hawking_suite.py:419`
- Doc: Return entropy-based and thermal k_B estimates.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:443`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights_np, h_bar, G_alg)`
- Defined: `maxwell_field_hawking_suite.py:447`
- Doc: Return multiple c estimates.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:469`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights, G_alg, c_eff, h_bar)`
- Defined: `maxwell_field_hawking_suite.py:473`
- Doc: Return multiple mass estimates.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:503`
- Doc: Store config reference.

### calculate (method) `def calculate(self, all_weights)`
- Defined: `maxwell_field_hawking_suite.py:507`
- Doc: Return effective area from active parameters and weight entropy.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:523`
- Doc: Instantiate all sub-calculators.

### calculate (method) `def calculate(self, model, loss, loss_history, precomputed_delta)`
- Defined: `maxwell_field_hawking_suite.py:533`
- Doc: Run the full Hawking radiation pipeline and return all results.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:599`
- Doc: Store config reference.

### map (method) `def map(self, weight_dict)`
- Defined: `maxwell_field_hawking_suite.py:603`
- Doc: Return (charge_density, permittivity) as 3D arrays.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:629`
- Doc: Store config reference.

### solve (method) `def solve(self, charge_density, permittivity)`
- Defined: `maxwell_field_hawking_suite.py:633`
- Doc: Return the electrostatic potential phi on the 3D grid.

### compute_electric_field (method) `def compute_electric_field(self, potential)`
- Defined: `maxwell_field_hawking_suite.py:647`
- Doc: Return E = -grad(phi).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:655`
- Doc: Store config reference.

### compute (method) `def compute(self, permittivity)`
- Defined: `maxwell_field_hawking_suite.py:659`
- Doc: Return scattering intensity map, central slice, and peak analysis.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:686`
- Doc: Store config reference.

### analyze (method) `def analyze(self, permittivity)`
- Defined: `maxwell_field_hawking_suite.py:690`
- Doc: Return eigenvalues of the gradient structure tensor and anisotropy ratio.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:717`
- Doc: Store config reference.

### calculate (method) `def calculate(self, potential, intensity_3d)`
- Defined: `maxwell_field_hawking_suite.py:721`
- Doc: Return field entropy, mode entropy, and their sum.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:744`
- Doc: Store config reference.

### analyze (method) `def analyze(self, fourier_coeffs)`
- Defined: `maxwell_field_hawking_suite.py:748`
- Doc: Return radial profile, gap depth, and boolean bandgap detection.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:776`
- Doc: Store config reference.

### classify (method) `def classify(self, anisotropy, scattering, photonic_entropy, delta, alpha)`
- Defined: `maxwell_field_hawking_suite.py:780`
- Doc: Return phase name, crystal/glass flags, and confidence score.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:810`
- Doc: Instantiate all sub-components.

### analyze (method) `def analyze(self, model)`
- Defined: `maxwell_field_hawking_suite.py:821`
- Doc: Run the full EM pipeline on the model weights.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:866`
- Doc: Store config reference.

### render (method) `def render(self, hawking, maxwell, metadata, output_path)`
- Defined: `maxwell_field_hawking_suite.py:870`
- Doc: Save a comprehensive 4x4 figure to disk.

### _plot_hawking_summary (method) `def _plot_hawking_summary(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:897`
- Doc: Hawking temperature and BH entropy bars.

### _plot_hawking_temperature (method) `def _plot_hawking_temperature(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:906`
- Doc: Temperature gauge.

### _plot_hawking_entropy (method) `def _plot_hawking_entropy(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:914`
- Doc: Bekenstein-Hawking entropy.

### _plot_hawking_constants (method) `def _plot_hawking_constants(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:921`
- Doc: Effective constants summary.

### _plot_potential_slice (method) `def _plot_potential_slice(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:936`
- Doc: Central slice of electrostatic potential.

### _plot_scattering_slice (method) `def _plot_scattering_slice(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:944`
- Doc: kx-ky scattering intensity.

### _plot_dielectric_anisotropy (method) `def _plot_dielectric_anisotropy(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:954`
- Doc: Dielectric tensor eigenvalues.

### _plot_photonic_entropy (method) `def _plot_photonic_entropy(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:964`
- Doc: Field and mode entropy bars.

### _plot_bandgap (method) `def _plot_bandgap(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:973`
- Doc: Radial Fourier profile and bandgap indicator.

### _plot_electric_field (method) `def _plot_electric_field(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:984`
- Doc: Electric field magnitude statistics.

### _plot_em_classification (method) `def _plot_em_classification(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:992`
- Doc: Phase classification text panel.

### _plot_combined_summary (method) `def _plot_combined_summary(self, h, m, meta, ax)`
- Defined: `maxwell_field_hawking_suite.py:1010`
- Doc: Text summary combining both analyses.

### _plot_hawking_radiation_power (method) `def _plot_hawking_radiation_power(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:1032`
- Doc: Radiation power bar.

### _plot_schwarzschild (method) `def _plot_schwarzschild(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:1039`
- Doc: Schwarzschild radius and surface gravity.

### _plot_evaporation (method) `def _plot_evaporation(self, h, ax)`
- Defined: `maxwell_field_hawking_suite.py:1050`
- Doc: Evaporation timescale bar.

### _plot_purity (method) `def _plot_purity(self, m, ax)`
- Defined: `maxwell_field_hawking_suite.py:1057`
- Doc: Delta and alpha purity bars.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:1068`
- Doc: Instantiate sub-analyzers and visualizer.

### analyze_checkpoint (method) `def analyze_checkpoint(self, checkpoint_path, output_dir)`
- Defined: `maxwell_field_hawking_suite.py:1076`
- Doc: Load, analyze, visualize, and return aggregated results.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_field_hawking_suite.py:1132`
- Doc: Instantiate the single-checkpoint analyzer.

### process (method) `def process(self, input_path, output_dir)`
- Defined: `maxwell_field_hawking_suite.py:1138`
- Doc: Analyze one file or all .pth files in a directory.

### _build_summary (method) `def _build_summary(self, results)`
- Defined: `maxwell_field_hawking_suite.py:1176`
- Doc: Aggregate statistics across checkpoints.

### _print_ranking (method) `def _print_ranking(self, results)`
- Defined: `maxwell_field_hawking_suite.py:1203`
- Doc: Log the best checkpoint by delta and alpha.

### _safe_stats (method) `def _safe_stats(vals)`
- Defined: `maxwell_field_hawking_suite.py:1185`

### _info (method) `def _info(idx)`
- Defined: `maxwell_field_hawking_suite.py:1210`

### __init__ (method) `def __init__(self)`
- Defined: `maxwell_field_hawking_suite.py:171`

### get (method) `def get(self, key, default)`
- Defined: `maxwell_field_hawking_suite.py:176`

### keys (method) `def keys(self)`
- Defined: `maxwell_field_hawking_suite.py:178`

### items (method) `def items(self)`
- Defined: `maxwell_field_hawking_suite.py:180`

## maxwell_magnetic_orbitals.py

### main (method) `def main()`
- Defined: `maxwell_magnetic_orbitals.py:585`
- Doc: Parse arguments and run the experiment.

### create_logger (method) `def create_logger(name, level)`
- Defined: `maxwell_magnetic_orbitals.py:85`
- Doc: Create and return a configured logger.

### __init__ (method) `def __init__(self, channels, grid_size, imaginary_ratio)`
- Defined: `maxwell_magnetic_orbitals.py:98`

### forward (method) `def forward(self, x)`
- Defined: `maxwell_magnetic_orbitals.py:106`
- Doc: Apply spectral convolution in Fourier space.

### __init__ (method) `def __init__(self, config, imaginary_ratio)`
- Defined: `maxwell_magnetic_orbitals.py:119`

### forward (method) `def forward(self, x)`
- Defined: `maxwell_magnetic_orbitals.py:132`

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:143`

### load (method) `def load(self, checkpoint_dir)`
- Defined: `maxwell_magnetic_orbitals.py:147`
- Doc: Return (model, info_dict) from the best available checkpoint.

### _fallback (method) `def _fallback(self)`
- Defined: `maxwell_magnetic_orbitals.py:179`

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:192`
- Doc: Precompute coordinate grids in the equatorial plane.

### generate (method) `def generate(self, l, m)`
- Defined: `maxwell_magnetic_orbitals.py:205`
- Doc: Return a (6,H,W) source tensor for the l-th multipole.

### _dipole (method) `def _dipole(self, m)`
- Defined: `maxwell_magnetic_orbitals.py:211`
- Doc: Analytical magnetic dipole B-field in equatorial plane.

### _multipole (method) `def _multipole(self, l, m)`
- Defined: `maxwell_magnetic_orbitals.py:229`
- Doc: Higher-order multipole from scalar potential gradient.

### _monopole_proxy (method) `def _monopole_proxy(self)`
- Defined: `maxwell_magnetic_orbitals.py:243`
- Doc: Isotropic l=0 proxy (current loop).

### _normalise_and_pack (method) `def _normalise_and_pack(self, Bx, By, Bz, scale)`
- Defined: `maxwell_magnetic_orbitals.py:250`
- Doc: Sanitise, normalise, and pack into 6-channel tensor.

### get_analytical_density (method) `def get_analytical_density(self, l, m)`
- Defined: `maxwell_magnetic_orbitals.py:260`
- Doc: Return normalised |B|^2 for analytical control (no network).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:274`

### project (method) `def project(self, model_output)`
- Defined: `maxwell_magnetic_orbitals.py:277`
- Doc: Multi-angle averaged Hall projection.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:294`

### scan (method) `def scan(self, model, source, n_slices)`
- Defined: `maxwell_magnetic_orbitals.py:297`
- Doc: Return a list of 2D Hall projection slices.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:312`

### radial_wavefunction (method) `def radial_wavefunction(self, n, l, r)`
- Defined: `maxwell_magnetic_orbitals.py:315`
- Doc: Non-relativistic radial wavefunction R_nl(r).

### spherical_harmonic_real (method) `def spherical_harmonic_real(self, l, m, theta, phi)`
- Defined: `maxwell_magnetic_orbitals.py:323`
- Doc: Real spherical harmonic Y_l^m.

### probability_density_2d (method) `def probability_density_2d(self, n, l, m, grid_size)`
- Defined: `maxwell_magnetic_orbitals.py:330`
- Doc: Fix 1: |psi(r, theta=pi/2, phi)|^2 in equatorial plane.

### sample_orbital_3d (method) `def sample_orbital_3d(self, n, l, m, num_samples)`
- Defined: `maxwell_magnetic_orbitals.py:345`
- Doc: Monte Carlo rejection sampling of |psi|^2.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:378`

### compute (method) `def compute(self, em_density, quantum_density)`
- Defined: `maxwell_magnetic_orbitals.py:381`
- Doc: Return spatial correlation, node overlap, symmetry correlation, KL divergence.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:406`

### visualize_comparison (method) `def visualize_comparison(self, em_density, quantum_density, metrics, label, tomo_slices, orbital_3d, save_path, analytical_density)`
- Defined: `maxwell_magnetic_orbitals.py:409`
- Doc: Render comparison figure with analytical control row.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals.py:487`

### run (method) `def run(self, output_dir, checkpoint_dir)`
- Defined: `maxwell_magnetic_orbitals.py:498`
- Doc: Execute the full protocol.

### _analyze (method) `def _analyze(self, model, n, l, m, label, out)`
- Defined: `maxwell_magnetic_orbitals.py:528`
- Doc: Full protocol for one orbital.

### _summary (method) `def _summary(self, results, info)`
- Defined: `maxwell_magnetic_orbitals.py:544`
- Doc: Aggregate.

### _interp (method) `def _interp(self, ma, mn, mp)`
- Defined: `maxwell_magnetic_orbitals.py:562`
- Doc: Narrative interpretation.

### _print (method) `def _print(self, s)`
- Defined: `maxwell_magnetic_orbitals.py:573`
- Doc: Log summary.

## maxwell_magnetic_orbitals_v2.py

### spatial_corr (method) `def spatial_corr(a, b, eps)`
- Defined: `maxwell_magnetic_orbitals_v2.py:387`
- Doc: Cosine similarity between two flattened maps.

### node_overlap (method) `def node_overlap(a, b, thr)`
- Defined: `maxwell_magnetic_orbitals_v2.py:393`
- Doc: Jaccard index of nodal regions.

### symmetry_corr (method) `def symmetry_corr(a, b)`
- Defined: `maxwell_magnetic_orbitals_v2.py:402`
- Doc: Correlation of angular Fourier power spectra.

### full_metrics (method) `def full_metrics(em, qd, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:410`
- Doc: Compute all isomorphism metrics.

### main (method) `def main()`
- Defined: `maxwell_magnetic_orbitals_v2.py:658`
- Doc: Parse arguments and run the v2 experiment.

### create_logger (method) `def create_logger(name, level)`
- Defined: `maxwell_magnetic_orbitals_v2.py:94`
- Doc: Create and return a configured logger.

### __init__ (method) `def __init__(self, channels, grid_size, imaginary_ratio)`
- Defined: `maxwell_magnetic_orbitals_v2.py:107`
- Doc: Initialise real and imaginary kernel parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_magnetic_orbitals_v2.py:116`
- Doc: Apply spectral convolution in Fourier space.

### __init__ (method) `def __init__(self, config, imaginary_ratio)`
- Defined: `maxwell_magnetic_orbitals_v2.py:131`
- Doc: Build all sub-layers.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_magnetic_orbitals_v2.py:147`
- Doc: Standard forward pass.

### forward_spectral_only (method) `def forward_spectral_only(self, x_expanded)`
- Defined: `maxwell_magnetic_orbitals_v2.py:156`
- Doc: Apply only the spectral layers (bypass input/expansion projections).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:165`
- Doc: Precompute coordinate grids.

### generate (method) `def generate(self, l, m)`
- Defined: `maxwell_magnetic_orbitals_v2.py:177`
- Doc: Return a (6,H,W) source tensor.

### _dipole (method) `def _dipole(self, m)`
- Defined: `maxwell_magnetic_orbitals_v2.py:183`
- Doc: Analytical magnetic dipole in equatorial plane.

### _multipole (method) `def _multipole(self, l, m)`
- Defined: `maxwell_magnetic_orbitals_v2.py:201`
- Doc: Higher-order multipole from scalar potential gradient.

### _monopole (method) `def _monopole(self)`
- Defined: `maxwell_magnetic_orbitals_v2.py:212`
- Doc: Isotropic l=0 proxy.

### _pack (method) `def _pack(self, Bx, By, Bz, scale)`
- Defined: `maxwell_magnetic_orbitals_v2.py:218`
- Doc: Normalise and pack into 6-channel tensor.

### get_density (method) `def get_density(self, l, m)`
- Defined: `maxwell_magnetic_orbitals_v2.py:227`
- Doc: Return normalised |B|^2 for analytical control.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:242`
- Doc: Store config reference.

### evolve (method) `def evolve(self, source_6ch)`
- Defined: `maxwell_magnetic_orbitals_v2.py:246`
- Doc: Treat the Bz channel as charge density, solve Poisson, return |E|^2.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:278`
- Doc: Build per-component projections.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_magnetic_orbitals_v2.py:288`
- Doc: Process each (Re, Im) pair separately then concatenate.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:298`
- Doc: Store config reference.

### project_6ch (method) `def project_6ch(self, tensor)`
- Defined: `maxwell_magnetic_orbitals_v2.py:302`
- Doc: Project a 6-channel field tensor to scalar density.

### project_energy (method) `def project_energy(self, tensor)`
- Defined: `maxwell_magnetic_orbitals_v2.py:316`
- Doc: Project an arbitrary multi-channel tensor to scalar energy density.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:325`
- Doc: Store config reference.

### radial_wavefunction (method) `def radial_wavefunction(self, n, l, r)`
- Defined: `maxwell_magnetic_orbitals_v2.py:329`
- Doc: Non-relativistic radial wavefunction R_nl(r).

### spherical_harmonic_real (method) `def spherical_harmonic_real(self, l, m, theta, phi)`
- Defined: `maxwell_magnetic_orbitals_v2.py:337`
- Doc: Real spherical harmonic.

### density_2d (method) `def density_2d(self, n, l, m, grid_size)`
- Defined: `maxwell_magnetic_orbitals_v2.py:344`
- Doc: 2D |psi|^2 in equatorial plane.

### sample_3d (method) `def sample_3d(self, n, l, m, num)`
- Defined: `maxwell_magnetic_orbitals_v2.py:357`
- Doc: Monte Carlo rejection sampling.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:421`
- Doc: Store config reference.

### render (method) `def render(self, label, strategies, qd, orbital_3d, save_path)`
- Defined: `maxwell_magnetic_orbitals_v2.py:425`
- Doc: Render comparison of all strategies for one orbital.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_magnetic_orbitals_v2.py:489`
- Doc: Initialise all sub-components.

### _load_model (method) `def _load_model(self, checkpoint_dir)`
- Defined: `maxwell_magnetic_orbitals_v2.py:499`
- Doc: Load trained checkpoint.

### run (method) `def run(self, output_dir, checkpoint_dir)`
- Defined: `maxwell_magnetic_orbitals_v2.py:527`
- Doc: Execute the full multi-strategy experiment.

### _analyze (method) `def _analyze(self, model, n, l, m, label, output_dir)`
- Defined: `maxwell_magnetic_orbitals_v2.py:557`
- Doc: Run all strategies for one orbital.

### _summary (method) `def _summary(self, results, info)`
- Defined: `maxwell_magnetic_orbitals_v2.py:591`
- Doc: Aggregate results across orbitals and strategies.

### _interpret (method) `def _interpret(self, agg, p_agg)`
- Defined: `maxwell_magnetic_orbitals_v2.py:624`
- Doc: Narrative interpretation.

### _print_summary (method) `def _print_summary(self, s)`
- Defined: `maxwell_magnetic_orbitals_v2.py:646`
- Doc: Log the summary.

## maxwell_orbital_diagnostic.py

### compute_spatial_correlation (method) `def compute_spatial_correlation(a, b, eps)`
- Defined: `maxwell_orbital_diagnostic.py:316`
- Doc: Cosine similarity between two flattened density maps.

### main (method) `def main()`
- Defined: `maxwell_orbital_diagnostic.py:625`
- Doc: Parse arguments and run the diagnostic suite.

### create_logger (method) `def create_logger(name, level)`
- Defined: `maxwell_orbital_diagnostic.py:83`
- Doc: Create and return a configured logger.

### __init__ (method) `def __init__(self, channels, grid_size, imaginary_ratio)`
- Defined: `maxwell_orbital_diagnostic.py:96`
- Doc: Initialise real and imaginary kernel parameters.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_orbital_diagnostic.py:105`
- Doc: Apply spectral convolution in Fourier space.

### init_identity (method) `def init_identity(self, scale)`
- Defined: `maxwell_orbital_diagnostic.py:117`
- Doc: Initialise kernels near identity: real=small, imag=0.

### __init__ (method) `def __init__(self, config, imaginary_ratio)`
- Defined: `maxwell_orbital_diagnostic.py:130`
- Doc: Build all sub-layers.

### forward (method) `def forward(self, x)`
- Defined: `maxwell_orbital_diagnostic.py:146`
- Doc: Forward pass.

### forward_with_intermediates (method) `def forward_with_intermediates(self, x)`
- Defined: `maxwell_orbital_diagnostic.py:155`
- Doc: Forward pass returning the output after every sub-layer.

### init_identity (method) `def init_identity(self)`
- Defined: `maxwell_orbital_diagnostic.py:167`
- Doc: Initialise all layers near identity / passthrough.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:184`
- Doc: Precompute coordinate grids in the equatorial plane.

### generate (method) `def generate(self, l, m)`
- Defined: `maxwell_orbital_diagnostic.py:196`
- Doc: Return a (6,H,W) source tensor for the l-th multipole.

### _dipole (method) `def _dipole(self, m)`
- Defined: `maxwell_orbital_diagnostic.py:202`
- Doc: Analytical magnetic dipole B-field in equatorial plane.

### _multipole (method) `def _multipole(self, l, m)`
- Defined: `maxwell_orbital_diagnostic.py:220`
- Doc: Higher-order multipole from scalar potential gradient.

### _monopole_proxy (method) `def _monopole_proxy(self)`
- Defined: `maxwell_orbital_diagnostic.py:232`
- Doc: Isotropic l=0 proxy.

### _pack (method) `def _pack(self, Bx, By, Bz, scale)`
- Defined: `maxwell_orbital_diagnostic.py:238`
- Doc: Sanitise, normalise, pack into 6 channels.

### get_analytical_density (method) `def get_analytical_density(self, l, m)`
- Defined: `maxwell_orbital_diagnostic.py:247`
- Doc: Return normalised |B|^2.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:256`
- Doc: Store config reference.

### project (method) `def project(self, tensor)`
- Defined: `maxwell_orbital_diagnostic.py:260`
- Doc: Multi-angle averaged Hall projection.

### project_intermediate (method) `def project_intermediate(self, tensor)`
- Defined: `maxwell_orbital_diagnostic.py:273`
- Doc: Project an intermediate activation to a scalar energy density.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:283`
- Doc: Store config reference.

### radial_wavefunction (method) `def radial_wavefunction(self, n, l, r)`
- Defined: `maxwell_orbital_diagnostic.py:287`
- Doc: Non-relativistic radial wavefunction R_nl(r).

### spherical_harmonic_real (method) `def spherical_harmonic_real(self, l, m, theta, phi)`
- Defined: `maxwell_orbital_diagnostic.py:295`
- Doc: Real spherical harmonic Y_l^m.

### probability_density_2d (method) `def probability_density_2d(self, n, l, m, grid_size)`
- Defined: `maxwell_orbital_diagnostic.py:302`
- Doc: 2D |psi|^2 in equatorial plane (theta=pi/2).

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:330`
- Doc: Initialise sub-components.

### run (method) `def run(self, output_dir)`
- Defined: `maxwell_orbital_diagnostic.py:338`
- Doc: Test all orbitals with an identity-initialised network.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:392`
- Doc: Initialise sub-components.

### run (method) `def run(self, checkpoint_dir, output_dir)`
- Defined: `maxwell_orbital_diagnostic.py:400`
- Doc: Trace a trained model layer by layer.

### _find_collapse (method) `def _find_collapse(self, trace)`
- Defined: `maxwell_orbital_diagnostic.py:436`
- Doc: Find the layer where correlation drops most sharply.

### _plot_traces (method) `def _plot_traces(self, all_traces, output_dir)`
- Defined: `maxwell_orbital_diagnostic.py:448`
- Doc: Plot correlation vs layer index for all orbitals.

### _load_model (method) `def _load_model(self, checkpoint_dir)`
- Defined: `maxwell_orbital_diagnostic.py:472`
- Doc: Load the trained model.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:507`
- Doc: Initialise sub-components.

### compute_angular_power (method) `def compute_angular_power(self, tensor)`
- Defined: `maxwell_orbital_diagnostic.py:515`
- Doc: Compute the angular power spectrum of a 2D field via azimuthal FFT.

### symmetry_loss (method) `def symmetry_loss(self, input_tensor, output_tensor)`
- Defined: `maxwell_orbital_diagnostic.py:522`
- Doc: Penalise angular power spectrum distortion.

### run (method) `def run(self, output_dir)`
- Defined: `maxwell_orbital_diagnostic.py:528`
- Doc: Train a fresh model with symmetry loss and track isomorphism.

### _plot_history (method) `def _plot_history(self, history, output_dir)`
- Defined: `maxwell_orbital_diagnostic.py:572`
- Doc: Plot training loss and correlation over epochs.

### __init__ (method) `def __init__(self, config)`
- Defined: `maxwell_orbital_diagnostic.py:598`
- Doc: Initialise all test modes.

### run_all (method) `def run_all(self, output_dir, checkpoint_dir)`
- Defined: `maxwell_orbital_diagnostic.py:606`
- Doc: Execute all three diagnostic modes and save results.
