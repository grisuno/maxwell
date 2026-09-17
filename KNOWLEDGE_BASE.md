# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. 8 files, 556 symbols, 137 imports. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM, Ruby, Swift, Kotlin, Scala, Lua, Elixir.
> No LLMs. No tokens. Pure static analysis. See more [here](https://github.com/grisuno/ReadMenator)

**Start here:** Statistics Dashboard for scope, God Nodes for blast radius, Architecture Reference for per-file API. Agents: prefer `readmenator-agent/INDEX.md` + `SYMBOLS.md`.

**Wiki:** prefer `readmenator-wiki/index.md` for progressive disclosure: one synthesis page per community, `connections.json` with EXTRACTED vs INFERRED confidence, `queries.md` log, `REPORT.md` audit.

**Confidence:** EXTRACTED = parsed from source, INFERRED = heuristic bridge, AMBIGUOUS = reported, never hidden. See `readmenator-wiki/REPORT.md`.

**Total Files Parsed:** 8 | **Total Symbols Extracted:** 556 | **Total Imports:** 137

<!-- ranking_model: v1.0 | weights: {ppr:0.45,auth:0.2,test:0.15,doc:0.1,fresh:0.1} | alpha:0.85 | commit:b3ca3bb | date:2026-07-18 -->


## Table of Contents

1. [Statistics Dashboard](#statistics-dashboard)
2. [Architectural Layers](#architectural-layers)
3. [Ranked Context](#ranked-context)
4. [God Nodes](#god-nodes)
5. [Suggested Questions](#suggested-questions)
6. [Hotspot Analysis](#hotspot-analysis)
7. [Change Impact Analysis](#change-impact-analysis)
8. [Suggested Linting Rules](#suggested-linting-rules)
9. [Orphans](#orphans)
10. [Query Recipes](#query-recipes)
11. [Structural Knowledge Map](#structural-knowledge-map)
12. [UML Class Diagram](#uml-class-diagram)
13. [Code Property Graph](#code-property-graph)
14. [Architecture Reference](#architecture-reference)
    - [PY (7 files)](#py-7-files)
    - [SH (1 files)](#sh-1-files)

---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Total Files | 8 |
| Total Symbols | 556 |
| Total Imports | 137 |
| Call Edges | 4388 |
| Inheritance Edges | 30 |
| Languages | 2 |
| Avg Symbols/File | 69.5 |
| Avg Imports/File | 17.1 |

### Top Files by Import Count (Fan-Out)

| File | Imports | Symbols | Language |
|------|---------|---------|----------|
| `maxwell_crystallography_suite.py` | 32 | 123 | py |
| `maxwell_field_hawking_suite.py` | 27 | 99 | py |
| `maxwell_magnetic_orbitals.py` | 20 | 47 | py |
| `maxwell_magnetic_orbitals_v2.py` | 20 | 50 | py |
| `maxwell_crystal.py` | 19 | 188 | py |
| `maxwell_orbital_diagnostic.py` | 19 | 49 | py |

---

## Architectural Layers

Auto-detected from path patterns, naming conventions, and imported frameworks.

| Layer | Files |
|-------|-------|
| utility | 5 |
| presentation | 2 |
| infrastructure | 1 |

### utility

- `app.py` (py, 0 symbols)
- `install.sh` (sh, 0 symbols)
- `maxwell_crystal.py` (py, 188 symbols)
- `maxwell_magnetic_orbitals.py` (py, 47 symbols)
- `maxwell_magnetic_orbitals_v2.py` (py, 50 symbols)

### presentation

- `maxwell_crystallography_suite.py` (py, 123 symbols)
- `maxwell_field_hawking_suite.py` (py, 99 symbols)

### infrastructure

- `maxwell_orbital_diagnostic.py` (py, 49 symbols)

---

## Ranked Context

Files ranked by composite score for the current query context. The ranking combines Personalized PageRank (query relevance), global authority, test coverage, documentation coverage, and code freshness. Model: v1.0.

| Rank | File | Composite | PPR | Authority | Test | Doc |
|------|------|-----------|-----|-----------|------|-----|
| 1 | `maxwell_orbital_diagnostic.py` | 0.1020 | 0.0000 | 0.0000 | 0.00 | 1.02 |
| 2 | `maxwell_magnetic_orbitals_v2.py` | 0.1020 | 0.0000 | 0.0000 | 0.00 | 1.02 |
| 3 | `app.py` | 0.1000 | 0.0000 | 0.0000 | 0.00 | 1.00 |
| 4 | `maxwell_crystal.py` | 0.0989 | 0.0000 | 0.0000 | 0.00 | 0.99 |
| 5 | `maxwell_crystallography_suite.py` | 0.0976 | 0.0000 | 0.0000 | 0.00 | 0.98 |
| 6 | `maxwell_field_hawking_suite.py` | 0.0939 | 0.0000 | 0.0000 | 0.00 | 0.94 |
| 7 | `maxwell_magnetic_orbitals.py` | 0.0787 | 0.0000 | 0.0000 | 0.00 | 0.79 |
| 8 | `install.sh` | 0.0000 | 0.0000 | 0.0000 | 0.00 | 0.00 |

---

## God Nodes

Most architecturally central files ranked by combined import/export degree and symbol richness.

| File | Score | Connections | PageRank |
|------|-------|-------------|----------|
| `maxwell_crystal.py` | 18.8 | | 0.0000 |
| `maxwell_crystallography_suite.py` | 12.3 | | 0.0000 |
| `maxwell_field_hawking_suite.py` | 9.9 | | 0.0000 |
| `maxwell_magnetic_orbitals_v2.py` | 5.0 | | 0.0000 |
| `maxwell_orbital_diagnostic.py` | 4.9 | | 0.0000 |
| `maxwell_magnetic_orbitals.py` | 4.7 | | 0.0000 |
| `app.py` | 0.0 | | 0.0000 |
| `install.sh` | 0.0 | | 0.0000 |

---

## Suggested Questions

Auto-generated exploration prompts based on graph structure:

- What does maxwell_crystal.py depend on, and what depends on it? (0 connections)
- What does maxwell_crystallography_suite.py depend on, and what depends on it? (0 connections)
- What does maxwell_field_hawking_suite.py depend on, and what depends on it? (0 connections)
- What is Config in maxwell_crystal.py and how is it used?
- What is CrystallographySuiteConfig in maxwell_crystallography_suite.py and how is it used?

---

## Hotspot Analysis

Files ranked by combined complexity (symbol count) and centrality (connection count). High-scoring files are architecturally critical and may need refactoring attention.

| File | Complexity | Centrality | Combined | Symbols | Connections |
|------|-----------|------------|----------|---------|-------------|
| `maxwell_orbital_diagnostic.py` | 0.261 | 0.594 | 0.461 | 49 | 19 |
| `maxwell_magnetic_orbitals_v2.py` | 0.266 | 0.625 | 0.481 | 50 | 20 |
| `app.py` | 0.000 | 0.000 | 0.000 | 0 | 0 |
| `maxwell_crystal.py` | 1.000 | 0.594 | 0.756 | 188 | 19 |
| `maxwell_crystallography_suite.py` | 0.654 | 1.000 | 0.862 | 123 | 32 |
| `maxwell_field_hawking_suite.py` | 0.527 | 0.844 | 0.717 | 99 | 27 |
| `maxwell_magnetic_orbitals.py` | 0.250 | 0.625 | 0.475 | 47 | 20 |
| `install.sh` | 0.000 | 0.000 | 0.000 | 0 | 0 |

---

## Change Impact Analysis

Files sorted by how many other files would be affected if they changed. High-impact files should be changed with caution.

| File | Direct Dependents | Transitive Dependents | Total Impact |
|------|------------------|----------------------|--------------|
| `app.py` | 0 | 0 | 0 |
| `install.sh` | 0 | 0 | 0 |
| `maxwell_crystal.py` | 0 | 0 | 0 |
| `maxwell_crystallography_suite.py` | 0 | 0 | 0 |
| `maxwell_field_hawking_suite.py` | 0 | 0 | 0 |
| `maxwell_magnetic_orbitals.py` | 0 | 0 | 0 |
| `maxwell_magnetic_orbitals_v2.py` | 0 | 0 | 0 |
| `maxwell_orbital_diagnostic.py` | 0 | 0 | 0 |

---

## Suggested Linting Rules

Automatically suggested linting and security rules based on patterns detected in the codebase. These can be exported as Semgrep rules using the `--export-rules` flag.

| Rule ID | Severity | Description | Language | Matches |
|---------|----------|-------------|----------|---------|
| `RM002` | warning | Bare except clause catches all exceptions including SystemExit | python | 3 |
| `RM001` | info | Large number of functions in py: 430 total | py | 430 |

---

## Orphans

Files with no documentation or low connectivity. These are candidates for documentation investment or cleanup.

- `install.sh` (0 symbols, no doc)

---

## Query Recipes

Example queries you can run against this knowledge base using the ranking engine:

```
# Find files most relevant to a concept
readmenator query "Where is the import resolver implemented?"

# Rank files by relevance to a topic
readmenator query "How does documentation generation work?"

# Explain why a file ranks highly
readmenator query "explain readmenator/_documentation.py"

# Trace dependency paths with ranked context
readmenator query "path from CLI to exporter"
```

The ranking model uses the following signals:

- **Personalized PageRank** (45% weight): query-specific relevance via seed propagation
- **Global Authority** (20% weight): structural importance via standard PageRank
- **Test Coverage** (15% weight): fraction of symbols referenced in test files
- **Doc Coverage** (10% weight): presence of docstrings and file-level docs
- **Freshness** (10% weight): recent modification activity

Results include score decomposition and justification paths for each ranked item.

---

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
    maxwell_magnetic_orbitals_v2_py["maxwell_magnetic_orbitals_v2.py (py)"]
    class maxwell_magnetic_orbitals_v2_py mod;
    maxwell_magnetic_orbitals_py["maxwell_magnetic_orbitals.py (py)"]
    class maxwell_magnetic_orbitals_py mod;
    maxwell_crystal_py["maxwell_crystal.py (py)"]
    class maxwell_crystal_py mod;
    maxwell_orbital_diagnostic_py["maxwell_orbital_diagnostic.py (py)"]
    class maxwell_orbital_diagnostic_py mod;
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

## UML Class Diagram

Auto-generated Mermaid class diagram from parsed class-level symbols. Shows classes, structs, interfaces, traits, and their methods with inheritance and dependency relationships.

```mermaid
classDiagram
  class maxwell_crystal_py_Config {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_IPhaseDetector {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_IMetricCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SeedManager {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_LoggerFactory {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_MaxwellOperator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SpectralStatisticsCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SpectralLayer {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_MaxwellSpectralNetwork {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_HamiltonianBackbone {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_HamiltonianInferenceEngine {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_MaxwellPotentialGenerator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_MaxwellDataset {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_FullFourierAnalyzer {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_FourierMassCenterAnalyzer {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TopologicalPhaseDetector {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SpectralFieldExtractor {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TopologicalCrystallizationLoss {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_CrystallizationPressureApplicator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TopologicalMetricsCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_LocalComplexityAnalyzer {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SuperpositionAnalyzer {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_CrystallographyMetricsCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_ThermodynamicMetricsCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SpectralGeometryCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_RicciCurvatureCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_PerelmanRicciFlow {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SpectroscopyMetricsCalculator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_LambdaPressureScheduler {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_AdaptiveLambdaScheduler {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_AnnealingScheduler {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TopologicalAnnealingScheduler {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TrainingMetricsMonitor {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_CheckpointManager {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_GlassStateDetector {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_WeightIntegrityChecker {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_TrainingEngine {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_Phase0Orchestrator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_BatchSizeProspector {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_SeedMiner {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_FullTrainingOrchestrator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystal_py_RefinementOrchestrator {
    <<class>>
    +main()
    +detect(self, spectral_field)
    +compute(self, model)
    +set_seed(seed, device)
    +create_logger(name, level)
    +__init__(self, config)
    +_precompute_operators(self)
    +apply_maxwell_operator(self, fields)
    +time_evolution(self, fields, dt)
    +__init__(self, config)
  }
  class maxwell_crystallography_suite_py_CrystallographySuiteConfig {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_LoggerFactory {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_IMetricCalculator {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_IPhaseDetector {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_SpectralLayer {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_MaxwellSpectralNetwork {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_GOEGUESpectralAnalyzer {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
  class maxwell_crystallography_suite_py_WeightIntegrityCalculator {
    <<class>>
    +main()
    +create_logger(name, level, config)
    +compute(self, model)
    +detect(self, spectral_field)
    +__init__(self, channels, grid_size, config, imaginary_ratio)
    +forward(self, x)
    +get_spectral_operator(self)
    +get_kernel_ratio(self)
    +__init__(self, config, imaginary_ratio)
    +forward(self, x)
  }
```

---

## Code Property Graph

Machine-readable Code Property Graph (CPG) in JSON-LD format. This block allows AI agents to parse the full structural graph without additional file reads. Compatible with GraphRAG pipelines.

```json
{"@context": "https://schema.org", "analysis": {"communities": [], "god_nodes": [{"node_id": "maxwell_crystal.py", "score": 18.8}, {"node_id": "maxwell_crystallography_suite.py", "score": 12.3}, {"node_id": "maxwell_field_hawking_suite.py", "score": 9.9}, {"node_id": "maxwell_magnetic_orbitals_v2.py", "score": 5.0}, {"node_id": "maxwell_orbital_diagnostic.py", "score": 4.9}, {"node_id": "maxwell_magnetic_orbitals.py", "score": 4.7}, {"node_id": "app.py", "score": 0.0}, {"node_id": "install.sh", "score": 0.0}], "surprising_connections": []}, "edges": [{"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "torch.utils.data"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystal.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "copy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "collections"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "torch.optim"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "torch.utils.data"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy.stats"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy.linalg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy.optimize"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy.sparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "scipy.sparse.linalg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_crystallography_suite.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "pickle"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "io"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "re"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "time"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "abc"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "scipy.fft"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "scipy.stats"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "scipy.linalg"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_field_hawking_suite.py", "target": "traceback"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "scipy.special"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals.py", "target": "scipy.ndimage"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "scipy.special"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "scipy.fft"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_magnetic_orbitals_v2.py", "target": "matplotlib.gridspec"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "argparse"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "glob"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "json"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "logging"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "os"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "warnings"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "math"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "datetime"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "pathlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "typing"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "dataclasses"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "numpy"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "scipy.special"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "torch"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "torch.nn"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "torch.nn.functional"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "matplotlib"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "matplotlib.pyplot"}, {"confidence": "EXTRACTED", "relation": "imports", "source": "maxwell_orbital_diagnostic.py", "target": "matplotlib.gridspec"}], "generator": "readmenator", "metadata": {"edge_count": 4555, "file_count": 8, "language_count": 2, "symbol_count": 556}, "nodes": [{"doc": "app.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:", "id": "app.py", "kind": "module", "label": "app.py", "language": "py", "sha256": "57b21bdb023585b8", "symbol_count": 0, "symbols": []}, {"id": "install.sh", "kind": "module", "label": "install.sh", "language": "sh", "sha256": "c907d80fd6734993", "symbol_count": 0, "symbols": []}, {"doc": "maxwell_crystal.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date of creation: 2026 License: AGPL v3  Description: Maxwell Equations Grokking via Hamiltonian Topological Crystallization.  Maxwell equations in vacuum (CGS-Gauss units, c=1): curl E = -dB/dt curl B =  dE/dt div  E = 0 div  B = 0  2D TM polarization on a periodic grid (Ex, Ey, Bz): dBz/dt = -(dEy/dx - dEx/dy) dEx/dt =  dBz/dy dEy/dt = -dBz/dx  Five-phase protocol: Phase 0 - Spectral Kernel Ratio Optimization (Chapter 10: GOE-GUE transition) Phase 1 - Batch size prospecting with delta/dt velocity Phase 2 - Seed mining with decreasing delta criterion Phase 3 - Full training of best seed + batch size until grokking Phase 4 - Refinement via simulated annealing toward crystal state", "id": "maxwell_crystal.py", "kind": "module", "label": "maxwell_crystal.py", "language": "py", "sha256": "93d681c605e54825", "symbol_count": 188, "symbols": [{"doc": "Central configuration for all hyperparameters, architecture sizes, and protocol constants.", "kind": "class", "line": 56, "name": "Config", "signature": "class Config"}, {"doc": "Abstract interface for phase detection in neural network training.", "kind": "class", "line": 257, "name": "IPhaseDetector", "signature": "class IPhaseDetector(ABC)"}, {"doc": "Abstract interface for metric calculation.", "kind": "class", "line": 266, "name": "IMetricCalculator", "signature": "class IMetricCalculator(ABC)"}, {"doc": "Deterministic seed management for reproducibility.", "kind": "class", "line": 275, "name": "SeedManager", "signature": "class SeedManager"}, {"doc": "Factory for creating consistently formatted loggers.", "kind": "class", "line": 290, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Maxwell equations operator for 2D TM polarization (Ex, Ey, Bz).\n\nImplements spectral (Fourier-space) derivatives for the curl operator on\na periodic square grid.  Time evolution uses an Euler forward step with\nunitarity-preserving norm rescaling.\n\ndBz/dt = -(dEy/dx - dEx/dy)\ndEx/dt =  dBz/dy\ndEy/dt = -dBz/dx", "kind": "class", "line": 308, "name": "MaxwellOperator", "signature": "class MaxwellOperator"}, {"doc": "Spectral statistics engine for GOE/GUE analysis (Chapter 10).\n\nGenerates random matrix ensembles interpolating between the Gaussian\nOrthogonal Ensemble (imaginary_ratio=0) and the Gaussian Unitary\nEnsemble (imaginary_ratio=1), then evaluates nearest-neighbor spacing\nP(s), pair correlation R_2(s), and the Dyson beta index.", "kind": "class", "line": 396, "name": "SpectralStatisticsCalculator", "signature": "class SpectralStatisticsCalculator"}, {"doc": "Fourier-domain convolutional layer with tuneable imaginary ratio.\n\nThe imaginary_ratio parameter controls the transition between GOE-like\n(real symmetric kernel) and GUE-like (complex Hermitian kernel)\nspectral statistics of the operator.", "kind": "class", "line": 610, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics on a 2D grid.\n\nInput/output: 6 real channels encoding (Re, Im) of (Ex, Ey, Bz).\nArchitecture: 1x1 projection --> expansion --> spectral layers --> contraction --> 1x1.", "kind": "class", "line": 688, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Pre-trained backbone for single-channel Hamiltonian inference.", "kind": "class", "line": 749, "name": "HamiltonianBackbone", "signature": "class HamiltonianBackbone(Module)"}, {"doc": "Dispatch layer that tries to load a pre-trained backbone and falls back\nto the analytical Maxwell operator.", "kind": "class", "line": 780, "name": "HamiltonianInferenceEngine", "signature": "class HamiltonianInferenceEngine"}, {"doc": "Generate source configurations and background media for the Maxwell system.\n\nPotentials here represent spatially varying permittivity profiles and\nexternal current sources that break translational symmetry.", "kind": "class", "line": 840, "name": "MaxwellPotentialGenerator", "signature": "class MaxwellPotentialGenerator"}, {"doc": "Dataset of electromagnetic field evolution samples.\n\nEach sample consists of an initial (Ex, Ey, Bz) configuration encoded\nas 6 real channels (Re + Im interleaved) and the time-evolved target.", "kind": "class", "line": 903, "name": "MaxwellDataset", "signature": "class MaxwellDataset(Dataset)"}, {"doc": "Complete 2D Fourier analysis with radial profiles and Bragg peak detection.", "kind": "class", "line": 1033, "name": "FullFourierAnalyzer", "signature": "class FullFourierAnalyzer"}, {"doc": "Centre-of-mass and inertia-tensor analysis in Fourier space.", "kind": "class", "line": 1183, "name": "FourierMassCenterAnalyzer", "signature": "class FourierMassCenterAnalyzer"}, {"doc": "Hysteretic phase detector combining alignment, localisation, and resonance signals.", "kind": "class", "line": 1247, "name": "TopologicalPhaseDetector", "signature": "class TopologicalPhaseDetector(IPhaseDetector)"}, {"doc": "Extract spectral weight tensors from spectral layers of a model.", "kind": "class", "line": 1312, "name": "SpectralFieldExtractor", "signature": "class SpectralFieldExtractor"}, {"doc": "Loss function driving the system toward topological crystal order.", "kind": "class", "line": 1333, "name": "TopologicalCrystallizationLoss", "signature": "class TopologicalCrystallizationLoss(Module)"}, {"doc": "Apply weight decay pressure proportional to phase crystallinity.", "kind": "class", "line": 1365, "name": "CrystallizationPressureApplicator", "signature": "class CrystallizationPressureApplicator"}, {"doc": "Orchestrate topological phase detection, loss, and pressure application.", "kind": "class", "line": 1384, "name": "TopologicalMetricsCalculator", "signature": "class TopologicalMetricsCalculator(IMetricCalculator)"}, {"doc": "Compute local complexity via cosine-similarity dispersion of weight vectors.", "kind": "class", "line": 1453, "name": "LocalComplexityAnalyzer", "signature": "class LocalComplexityAnalyzer"}, {"doc": "Measure average off-diagonal correlation between weight rows.", "kind": "class", "line": 1472, "name": "SuperpositionAnalyzer", "signature": "class SuperpositionAnalyzer"}, {"doc": "Compute the five primary observables from the paper:\nkappa, delta, alpha, T_eff, hbar_eff, plus Poynting vector diagnostics.", "kind": "class", "line": 1495, "name": "CrystallographyMetricsCalculator", "signature": "class CrystallographyMetricsCalculator(IMetricCalculator)"}, {"doc": "Effective temperature, specific heat, Gibbs free energy, and critical temperature.", "kind": "class", "line": 1699, "name": "ThermodynamicMetricsCalculator", "signature": "class ThermodynamicMetricsCalculator(IMetricCalculator)"}, {"doc": "Spectral gap, effective dimension, participation ratio, and level-spacing ratio.", "kind": "class", "line": 1773, "name": "SpectralGeometryCalculator", "signature": "class SpectralGeometryCalculator(IMetricCalculator)"}, {"doc": "Ricci scalar and mean sectional curvature of the weight manifold.", "kind": "class", "line": 1819, "name": "RicciCurvatureCalculator", "signature": "class RicciCurvatureCalculator(IMetricCalculator)"}, {"doc": "Ricci flow with Perelman surgery for singularity resolution.", "kind": "class", "line": 1865, "name": "PerelmanRicciFlow", "signature": "class PerelmanRicciFlow"}, {"doc": "Weight-space diffraction analysis: Bragg peaks, spectral entropy.", "kind": "class", "line": 2061, "name": "SpectroscopyMetricsCalculator", "signature": "class SpectroscopyMetricsCalculator(IMetricCalculator)"}, {"doc": "Exponentially growing discretisation pressure lambda(t).", "kind": "class", "line": 2101, "name": "LambdaPressureScheduler", "signature": "class LambdaPressureScheduler"}, {"doc": "Lambda scheduler that accelerates growth when topological phase is detected.", "kind": "class", "line": 2144, "name": "AdaptiveLambdaScheduler", "signature": "class AdaptiveLambdaScheduler(LambdaPressureScheduler)"}, {"doc": "Simulated annealing with exponential cooling and Metropolis acceptance.", "kind": "class", "line": 2169, "name": "AnnealingScheduler", "signature": "class AnnealingScheduler"}, {"doc": "Annealing scheduler with adaptive cooling guided by topological signals.", "kind": "class", "line": 2202, "name": "TopologicalAnnealingScheduler", "signature": "class TopologicalAnnealingScheduler(AnnealingScheduler)"}, {"doc": "Accumulate, store, and format all training metrics across epochs.", "kind": "class", "line": 2222, "name": "TrainingMetricsMonitor", "signature": "class TrainingMetricsMonitor"}, {"doc": "Periodic checkpoint saving with rotation and latest-link semantics.", "kind": "class", "line": 2353, "name": "CheckpointManager", "signature": "class CheckpointManager"}, {"doc": "Detect whether the system is trapped in a glassy (non-crystalline) state.", "kind": "class", "line": 2407, "name": "GlassStateDetector", "signature": "class GlassStateDetector"}, {"doc": "Detect NaN and Inf corruption in model parameters.", "kind": "class", "line": 2467, "name": "WeightIntegrityChecker", "signature": "class WeightIntegrityChecker"}, {"doc": "Core training loop with metric collection, gradient injection, and Ricci regularisation.", "kind": "class", "line": 2498, "name": "TrainingEngine", "signature": "class TrainingEngine"}, {"doc": "Phase 0: Spectral Kernel Ratio Optimization.\n\nSweeps imaginary_ratio to find the value that minimises the combined\nP(s) + R_2(s) loss relative to the GUE target, following Chapter 10.", "kind": "class", "line": 2665, "name": "Phase0Orchestrator", "signature": "class Phase0Orchestrator"}, {"doc": "Phase 1: Evaluate candidate batch sizes for delta and kappa performance.", "kind": "class", "line": 2727, "name": "BatchSizeProspector", "signature": "class BatchSizeProspector"}, {"doc": "Phase 2: Mine for optimal random seed via short training probes.", "kind": "class", "line": 2786, "name": "SeedMiner", "signature": "class SeedMiner"}, {"doc": "Phase 3: Full training with grokking detection and adaptive lambda pressure.", "kind": "class", "line": 2881, "name": "FullTrainingOrchestrator", "signature": "class FullTrainingOrchestrator"}, {"doc": "Phase 4: Simulated annealing refinement toward perfect crystal.", "kind": "class", "line": 3002, "name": "RefinementOrchestrator", "signature": "class RefinementOrchestrator"}, {"doc": "Entry point: parse arguments, run the five-phase protocol.", "kind": "method", "line": 3112, "name": "main", "signature": "def main()"}, {"doc": "Detect phase characteristics from spectral field data.", "kind": "method", "line": 261, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"doc": "Compute metrics for the given model and optional keyword arguments.", "kind": "method", "line": 270, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Set random seeds across all relevant libraries and backends.", "kind": "method", "line": 279, "name": "set_seed", "signature": "def set_seed(seed, device)"}, {"doc": "Create and return a configured logger instance.", "kind": "method", "line": 294, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"doc": "Precompute wavenumber grids and material constants.", "kind": "method", "line": 321, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Build Fourier-space wavenumber grids.", "kind": "method", "line": 331, "name": "_precompute_operators", "signature": "def _precompute_operators(self)"}, {"doc": "Apply the Maxwell curl operator to a (batch, 3, H, W) real tensor.\n\nChannel ordering: 0=Ex, 1=Ey, 2=Bz.\nReturns dF/dt of the same shape.", "kind": "method", "line": 339, "name": "apply_maxwell_operator", "signature": "def apply_maxwell_operator(self, fields)"}, {"doc": "Advance electromagnetic fields by one time step using Euler integration\nwith norm-preserving rescaling.", "kind": "method", "line": 371, "name": "time_evolution", "signature": "def time_evolution(self, fields, dt)"}, {"doc": "Store reference to global configuration.", "kind": "method", "line": 406, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return a sample from the Gaussian Orthogonal Ensemble.", "kind": "method", "line": 411, "name": "generate_goe_matrix", "signature": "def generate_goe_matrix(size, device)"}, {"doc": "Return a sample from the Gaussian Unitary Ensemble.", "kind": "method", "line": 417, "name": "generate_gue_matrix", "signature": "def generate_gue_matrix(size, device)"}, {"doc": "Return a complex Hermitian matrix interpolating between GOE and GUE.\n\nimaginary_ratio = 0  -->  real symmetric  (GOE)\nimaginary_ratio = 1  -->  complex Hermitian (GUE)", "kind": "method", "line": 425, "name": "generate_interpolated_matrix", "signature": "def generate_interpolated_matrix(self, size, imaginary_ratio, device)"}, {"doc": "Unfold eigenvalues via polynomial fit and return normalised spacings.", "kind": "method", "line": 443, "name": "compute_eigenvalue_spacing", "signature": "def compute_eigenvalue_spacing(self, eigenvalues)"}, {"doc": "MSE between the empirical P(s) histogram and the Wigner surmise.\n\nGOE: P(s) = (pi/2) s exp(-pi s^2 / 4)\nGUE: P(s) = (32/pi^2) s^2 exp(-4 s^2 / pi)", "kind": "method", "line": 458, "name": "compute_spacing_distribution_loss", "signature": "def compute_spacing_distribution_loss(self, spacings, target)"}, {"doc": "Estimate Dyson beta from small-spacing power-law P(s) ~ s^beta.\n\nbeta = 1 for GOE, beta = 2 for GUE.", "kind": "method", "line": 481, "name": "compute_dyson_index", "signature": "def compute_dyson_index(self, eigenvalues, spacings)"}, {"doc": "Two-level correlation function R_2(s).\n\nFor GUE the theoretical form is R_2(s) = 1 - (sin(pi s)/(pi s))^2.", "kind": "method", "line": 506, "name": "compute_pair_correlation", "signature": "def compute_pair_correlation(self, eigenvalues, s_range, num_points)"}, {"doc": "MSE between empirical R_2(s) and the analytical prediction.", "kind": "method", "line": 533, "name": "compute_correlation_loss", "signature": "def compute_correlation_loss(self, eigenvalues, target)"}, {"doc": "Ensemble-averaged spectral statistics at a given imaginary ratio.\n\nReturns P(s) loss, R_2 loss, Dyson beta, and combined losses for both\nGOE and GUE targets.", "kind": "method", "line": 552, "name": "compute_spectral_stats_for_ratio", "signature": "def compute_spectral_stats_for_ratio(self, imaginary_ratio, matrix_size, num_matrices, device)"}, {"doc": "Initialise real and imaginary kernel parameters.", "kind": "method", "line": 619, "name": "__init__", "signature": "def __init__(self, channels, grid_size, imaginary_ratio)"}, {"doc": "Scale the imaginary kernel by the imaginary ratio at init time.", "kind": "method", "line": 638, "name": "_apply_imaginary_ratio", "signature": "def _apply_imaginary_ratio(self)"}, {"doc": "Rescale imaginary kernel to reflect a new imaginary ratio.", "kind": "method", "line": 643, "name": "set_imaginary_ratio", "signature": "def set_imaginary_ratio(self, ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 651, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Extract a (channels x channels) complex matrix for eigenvalue analysis.\n\nThe real part is symmetrised, the imaginary part anti-symmetrised,\nyielding a Hermitian-like operator suitable for GOE/GUE diagnostics.", "kind": "method", "line": 674, "name": "get_spectral_operator", "signature": "def get_spectral_operator(self)"}, {"doc": "Build all sub-layers with the given architectural parameters.", "kind": "method", "line": 696, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, expansion_dim, num_spectral_layers, field_components, imaginary_ratio)"}, {"doc": "Forward pass through the full spectral network.", "kind": "method", "line": 721, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Propagate imaginary ratio to all spectral layers.", "kind": "method", "line": 732, "name": "set_imaginary_ratio", "signature": "def set_imaginary_ratio(self, ratio)"}, {"doc": "Compute the effective imaginary-to-real kernel norm ratio.", "kind": "method", "line": 738, "name": "get_kernel_ratio", "signature": "def get_kernel_ratio(self)"}, {"doc": "Build the backbone with spectral layers.", "kind": "method", "line": 752, "name": "__init__", "signature": "def __init__(self, grid_size, hidden_dim, num_spectral_layers)"}, {"doc": "Single-channel forward pass.", "kind": "method", "line": 768, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Attempt backbone load; fall back to analytical operator.", "kind": "method", "line": 786, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load backbone weights from disk if available and enabled.", "kind": "method", "line": 794, "name": "_try_load_backbone", "signature": "def _try_load_backbone(self)"}, {"doc": "Apply the Maxwell operator to the electromagnetic field tensor.", "kind": "method", "line": 829, "name": "apply_operator", "signature": "def apply_operator(self, fields)"}, {"doc": "Advance fields by one time step.", "kind": "method", "line": 833, "name": "time_evolve", "signature": "def time_evolve(self, fields, dt)"}, {"doc": "Store grid parameters from configuration.", "kind": "method", "line": 848, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Smooth Gaussian current-density envelope centred on the grid.", "kind": "method", "line": 853, "name": "gaussian_source", "signature": "def gaussian_source(self)"}, {"doc": "1/r dipole-like source envelope.", "kind": "method", "line": 861, "name": "dipole_source", "signature": "def dipole_source(self)"}, {"doc": "Sinusoidal plane-wave seed for Ex, Ey components.", "kind": "method", "line": 870, "name": "plane_wave_source", "signature": "def plane_wave_source(self)"}, {"doc": "Periodic permittivity modulation (photonic-crystal-like).", "kind": "method", "line": 879, "name": "periodic_medium", "signature": "def periodic_medium(self)"}, {"doc": "Dirichlet-weighted superposition of all source types.", "kind": "method", "line": 886, "name": "generate_mixed_source", "signature": "def generate_mixed_source(self, seed)"}, {"doc": "Generate all samples at construction time.", "kind": "method", "line": 911, "name": "__init__", "signature": "def __init__(self, config, hamiltonian_engine, seed)"}, {"doc": "Create a random initial electromagnetic field configuration.\n\nReturns a (3, H, W) complex tensor [Ex, Ey, Bz] and a scalar energy.", "kind": "method", "line": 954, "name": "_generate_initial_fields", "signature": "def _generate_initial_fields(self, source, sample_seed)"}, {"doc": "Advance the EM field through multiple time steps under the Maxwell operator.", "kind": "method", "line": 983, "name": "_time_evolve_fields", "signature": "def _time_evolve_fields(self, fields, source, energy)"}, {"doc": "Convert (3, H, W) complex tensor to (6, H, W) real tensor.", "kind": "method", "line": 1012, "name": "_fields_to_real_imag", "signature": "def _fields_to_real_imag(self, fields)"}, {"doc": "Number of training samples.", "kind": "method", "line": 1020, "name": "__len__", "signature": "def __len__(self)"}, {"doc": "Return (input, target) pair for training.", "kind": "method", "line": 1024, "name": "__getitem__", "signature": "def __getitem__(self, idx)"}, {"doc": "Return the full validation set as a single batch.", "kind": "method", "line": 1028, "name": "get_validation_batch", "signature": "def get_validation_batch(self)"}, {"doc": "Precompute wavenumber magnitude grid.", "kind": "method", "line": 1036, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return magnitude, phase, power, radial profile, and derived statistics.", "kind": "method", "line": 1045, "name": "compute_full_spectrum", "signature": "def compute_full_spectrum(self, spectral_field)"}, {"doc": "Identify local maxima in the power spectrum exceeding a statistical threshold.", "kind": "method", "line": 1098, "name": "detect_bragg_peaks", "signature": "def detect_bragg_peaks(self, power_spectrum, threshold_sigma)"}, {"doc": "Aggregate spectral concentration, phase coherence, and Bragg analysis.", "kind": "method", "line": 1146, "name": "compute_resonance_metrics", "signature": "def compute_resonance_metrics(self, spectral_field)"}, {"doc": "Initialise wavenumber grids and full Fourier sub-analyzer.", "kind": "method", "line": 1186, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return centre of mass, inertia tensor, anisotropy, and resonance diagnostics.", "kind": "method", "line": 1195, "name": "compute_mass_center", "signature": "def compute_mass_center(self, spectral_field)"}, {"doc": "Initialise history buffers and state variables.", "kind": "method", "line": 1250, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run full topological phase detection and return diagnostic dict.", "kind": "method", "line": 1258, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"doc": "Return the mean complex spectral kernel across all spectral layers.", "kind": "method", "line": 1316, "name": "extract", "signature": "def extract(model, grid_size)"}, {"doc": "Initialise with base lambda pressure.", "kind": "method", "line": 1336, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute quadrant, localisation, and resonance penalty terms.", "kind": "method", "line": 1342, "name": "forward", "signature": "def forward(self, phase_info, epoch)"}, {"doc": "Store pressure decay rate from config.", "kind": "method", "line": 1368, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Multiplicatively decay parameters when crystal phase is detected.", "kind": "method", "line": 1373, "name": "apply", "signature": "def apply(self, model, phase_info)"}, {"doc": "Initialise all topological sub-components.", "kind": "method", "line": 1387, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Extract spectral field, detect phase, compute loss, return full metrics dict.", "kind": "method", "line": 1395, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Delegate pressure application to the sub-component.", "kind": "method", "line": 1429, "name": "apply_crystallization_pressure", "signature": "def apply_crystallization_pressure(self, model, topo_metrics)"}, {"doc": "Return a zero-valued metrics dict when topological analysis is disabled.", "kind": "method", "line": 1436, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"doc": "Return a scalar in [0, 1] measuring weight diversity.", "kind": "method", "line": 1457, "name": "compute_local_complexity", "signature": "def compute_local_complexity(weights, epsilon)"}, {"doc": "Return the mean absolute off-diagonal Pearson correlation.", "kind": "method", "line": 1476, "name": "compute_superposition", "signature": "def compute_superposition(weights)"}, {"doc": "Store config and create logger.", "kind": "method", "line": 1501, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Facade that delegates to compute_all_metrics.", "kind": "method", "line": 1506, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Gradient covariance condition number kappa = lambda_max / lambda_min.", "kind": "method", "line": 1512, "name": "compute_kappa", "signature": "def compute_kappa(self, model, val_x, val_y, num_batches)"}, {"doc": "delta = max_i |theta_i - round(theta_i)|.", "kind": "method", "line": 1563, "name": "compute_discretization_margin", "signature": "def compute_discretization_margin(self, model)"}, {"doc": "alpha = -log(delta).", "kind": "method", "line": 1572, "name": "compute_alpha_purity", "signature": "def compute_alpha_purity(self, model)"}, {"doc": "Quantum-regularised condition number with hbar regularisation.", "kind": "method", "line": 1579, "name": "compute_kappa_quantum", "signature": "def compute_kappa_quantum(self, model)"}, {"doc": "Compute the electromagnetic Poynting-like energy flow through the network.", "kind": "method", "line": 1601, "name": "compute_poynting_vector", "signature": "def compute_poynting_vector(self, model)"}, {"doc": "hbar_eff = delta^2 * lambda / omega.", "kind": "method", "line": 1651, "name": "compute_hbar_effective", "signature": "def compute_hbar_effective(self, model, lambda_pressure)"}, {"doc": "Compute delta, alpha, kappa, kappa_q, poynting, purity, and is_crystal.", "kind": "method", "line": 1661, "name": "compute_all_metrics", "signature": "def compute_all_metrics(self, model, val_x, val_y)"}, {"doc": "Store config reference.", "kind": "method", "line": 1702, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return all thermodynamic observables.", "kind": "method", "line": 1706, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "T_eff = (lr / 2) * Var(grad).", "kind": "method", "line": 1727, "name": "compute_effective_temperature", "signature": "def compute_effective_temperature(self, gradient_buffer, learning_rate)"}, {"doc": "C_v = Var(U) / T^2.", "kind": "method", "line": 1750, "name": "compute_specific_heat", "signature": "def compute_specific_heat(self, loss_history, temp_history)"}, {"doc": "G = delta - T * (-alpha).", "kind": "method", "line": 1762, "name": "compute_gibbs_free_energy", "signature": "def compute_gibbs_free_energy(self, delta, alpha, temperature)"}, {"doc": "T_c = T_0 * exp(-c * alpha).", "kind": "method", "line": 1768, "name": "compute_critical_temperature", "signature": "def compute_critical_temperature(self, alpha)"}, {"doc": "Store config reference.", "kind": "method", "line": 1776, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute spectral geometry observables from weight outer product.", "kind": "method", "line": 1780, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}) over consecutive spacings.", "kind": "method", "line": 1806, "name": "_compute_level_spacing_ratio", "signature": "def _compute_level_spacing_ratio(self, spacings)"}, {"doc": "Store config reference.", "kind": "method", "line": 1822, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute Ricci scalar and sectional curvatures from weight metric.", "kind": "method", "line": 1826, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Ricci scalar via inverse eigenvalue sum.", "kind": "method", "line": 1842, "name": "_compute_ricci_scalar", "signature": "def _compute_ricci_scalar(self, metric)"}, {"doc": "Sample 2x2 sub-block determinants as sectional curvature proxies.", "kind": "method", "line": 1851, "name": "_estimate_sectional_curvatures", "signature": "def _estimate_sectional_curvatures(self, metric)"}, {"doc": "Initialise curvature history and surgery counter.", "kind": "method", "line": 1868, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Fast Ricci scalar estimate from normalised weight outer product.", "kind": "method", "line": 1877, "name": "compute_ricci_scalar_fast", "signature": "def compute_ricci_scalar_fast(self, model)"}, {"doc": "Second-difference curvature estimate along the flattened parameter.", "kind": "method", "line": 1907, "name": "compute_local_curvature", "signature": "def compute_local_curvature(self, param)"}, {"doc": "Ratio of smallest to largest covariance eigenvalue of the weight vector.", "kind": "method", "line": 1916, "name": "compute_anisotropy", "signature": "def compute_anisotropy(self, model)"}, {"doc": "Smoothness penalty proportional to second-difference curvature.", "kind": "method", "line": 1941, "name": "compute_ricci_regularization_loss", "signature": "def compute_ricci_regularization_loss(self, model)"}, {"doc": "One step of diffusive Ricci flow smoothing on all parameters.", "kind": "method", "line": 1959, "name": "apply_ricci_flow_step", "signature": "def apply_ricci_flow_step(self, model, lr)"}, {"doc": "Cut singularities (outlier weights) when curvature exceeds the surgery threshold.", "kind": "method", "line": 1989, "name": "perform_perelman_surgery", "signature": "def perform_perelman_surgery(self, model, ricci_scalar)"}, {"doc": "Reduce learning rate when curvature spikes above recent average.", "kind": "method", "line": 2031, "name": "compute_adaptive_lr_factor", "signature": "def compute_adaptive_lr_factor(self, model)"}, {"doc": "Return summary Ricci-flow diagnostics.", "kind": "method", "line": 2047, "name": "get_flow_metrics", "signature": "def get_flow_metrics(self, model)"}, {"doc": "Store config reference.", "kind": "method", "line": 2064, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute weight diffraction pattern and spectral entropy.", "kind": "method", "line": 2068, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "FFT of concatenated weights with peak detection.", "kind": "method", "line": 2073, "name": "compute_weight_diffraction", "signature": "def compute_weight_diffraction(self, coeffs)"}, {"doc": "Shannon entropy of the normalised power spectrum.", "kind": "method", "line": 2092, "name": "_compute_spectral_entropy", "signature": "def _compute_spectral_entropy(power_spectrum)"}, {"doc": "Initialise lambda in float64 precision.", "kind": "method", "line": 2104, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Current pressure value.", "kind": "method", "line": 2114, "name": "current_lambda", "signature": "def current_lambda(self)"}, {"doc": "Increase lambda at fixed epoch intervals.", "kind": "method", "line": 2118, "name": "step", "signature": "def step(self, epoch)"}, {"doc": "L2 penalty on distance from nearest integer for each parameter.", "kind": "method", "line": 2126, "name": "compute_regularization_loss", "signature": "def compute_regularization_loss(self, model)"}, {"doc": "Directly set the lambda value.", "kind": "method", "line": 2139, "name": "set_lambda", "signature": "def set_lambda(self, value)"}, {"doc": "Initialise base and accelerated growth factors.", "kind": "method", "line": 2147, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Grow lambda faster when topological order is emerging.", "kind": "method", "line": 2153, "name": "step_adaptive", "signature": "def step_adaptive(self, epoch, topo_phase_state)"}, {"doc": "Initialise temperature schedule.", "kind": "method", "line": 2172, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Current annealing temperature.", "kind": "method", "line": 2180, "name": "temperature", "signature": "def temperature(self)"}, {"doc": "Cool by one step.", "kind": "method", "line": 2184, "name": "step", "signature": "def step(self)"}, {"doc": "Metropolis acceptance criterion.", "kind": "method", "line": 2188, "name": "accept_perturbation", "signature": "def accept_perturbation(self, delta_loss)"}, {"doc": "Whether the current state has drifted too far from best.", "kind": "method", "line": 2197, "name": "should_restart", "signature": "def should_restart(self, current_delta, best_delta)"}, {"doc": "Initialise with base cooling rate.", "kind": "method", "line": 2205, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Slow cooling when alignment is growing, speed up when it recedes.", "kind": "method", "line": 2210, "name": "step_adaptive", "signature": "def step_adaptive(self, alignment_trend, resonance_score)"}, {"doc": "Initialise metric history buffers.", "kind": "method", "line": 2225, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Append each provided metric to its history list.", "kind": "method", "line": 2257, "name": "update_metrics", "signature": "def update_metrics(self)"}, {"doc": "Linear regression slope of recent delta values.", "kind": "method", "line": 2269, "name": "compute_delta_slope", "signature": "def compute_delta_slope(self)"}, {"doc": "Format all metrics into a multi-line progress string.", "kind": "method", "line": 2282, "name": "format_progress_bar", "signature": "def format_progress_bar(self, epoch, total_epochs, phase)"}, {"doc": "Create checkpoint directory and initialise timer.", "kind": "method", "line": 2356, "name": "__init__", "signature": "def __init__(self, config, checkpoint_dir)"}, {"doc": "True when at least CHECKPOINT_INTERVAL_MINUTES have elapsed.", "kind": "method", "line": 2366, "name": "should_save_checkpoint", "signature": "def should_save_checkpoint(self)"}, {"doc": "Save model, optimiser, metrics, and config to a timestamped file and latest link.", "kind": "method", "line": 2370, "name": "save_checkpoint", "signature": "def save_checkpoint(self, model, optimizer, epoch, metrics, phase, lambda_value, config_snapshot)"}, {"doc": "Load the latest checkpoint if it exists.", "kind": "method", "line": 2399, "name": "load_latest_checkpoint", "signature": "def load_latest_checkpoint(self)"}, {"doc": "Initialise patience buffer.", "kind": "method", "line": 2410, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return True if recent metrics indicate glass formation.", "kind": "method", "line": 2416, "name": "should_stop", "signature": "def should_stop(self, epoch, lc, sp, kappa, delta, temp, cv)"}, {"doc": "Return True if all metrics are below crystal thresholds.", "kind": "method", "line": 2452, "name": "is_crystal_formed", "signature": "def is_crystal_formed(self, lc, sp, kappa, delta, temp, cv)"}, {"doc": "Return integrity report with counts and corruption ratio.", "kind": "method", "line": 2471, "name": "check", "signature": "def check(model)"}, {"doc": "Instantiate all metric calculators.", "kind": "method", "line": 2501, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Local complexity and superposition averaged over all weight matrices.", "kind": "method", "line": 2515, "name": "compute_weight_metrics", "signature": "def compute_weight_metrics(self, model)"}, {"doc": "Relative norm difference between input and output.", "kind": "method", "line": 2530, "name": "compute_norm_conservation_error", "signature": "def compute_norm_conservation_error(self, model, val_x)"}, {"doc": "Run one epoch of gradient descent with optional regularisation.", "kind": "method", "line": 2540, "name": "train_single_epoch", "signature": "def train_single_epoch(self, model, optimizer, dataloader, epoch, lambda_scheduler, ricci_flow)"}, {"doc": "Compute validation loss and accuracy.", "kind": "method", "line": 2578, "name": "validate", "signature": "def validate(self, model, val_x, val_y)"}, {"doc": "Compute every metric from the paper and return as a flat dict.", "kind": "method", "line": 2590, "name": "collect_all_metrics", "signature": "def collect_all_metrics(self, model, monitor, val_x, val_y, lambda_scheduler, annealing_scheduler, current_lr, epoch)"}, {"doc": "Initialise spectral statistics calculator.", "kind": "method", "line": 2673, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Sweep imaginary ratios and return the one with lowest combined GUE loss.", "kind": "method", "line": 2679, "name": "optimize_kernel_ratio", "signature": "def optimize_kernel_ratio(self)"}, {"doc": "Store engine reference and optimal imaginary ratio.", "kind": "method", "line": 2730, "name": "__init__", "signature": "def __init__(self, config, hamiltonian_engine, imaginary_ratio)"}, {"doc": "Train briefly at each candidate batch size and return the best.", "kind": "method", "line": 2737, "name": "prospect", "signature": "def prospect(self)"}, {"doc": "Store references for dataset and model creation.", "kind": "method", "line": 2789, "name": "__init__", "signature": "def __init__(self, config, hamiltonian_engine, batch_size, imaginary_ratio)"}, {"doc": "Evaluate seeds and return the one with best delta velocity and kappa.", "kind": "method", "line": 2798, "name": "mine", "signature": "def mine(self)"}, {"doc": "Store all training configuration.", "kind": "method", "line": 2884, "name": "__init__", "signature": "def __init__(self, config, hamiltonian_engine, seed, batch_size, imaginary_ratio)"}, {"doc": "Execute Phase 3 and return (model, optimiser, monitor).", "kind": "method", "line": 2894, "name": "run_phase3_training", "signature": "def run_phase3_training(self, start_epoch, model)"}, {"doc": "Store all refinement parameters.", "kind": "method", "line": 3005, "name": "__init__", "signature": "def __init__(self, config, hamiltonian_engine, model, optimizer, monitor, seed, batch_size, imaginary_ratio)"}, {"doc": "Run Phase 4 refinement and return the best model.", "kind": "method", "line": 3021, "name": "run_phase4_refinement", "signature": "def run_phase4_refinement(self, start_epoch)"}, {"kind": "method", "line": 3193, "name": "load_latest_checkpoint", "signature": "def load_latest_checkpoint(mdl, checkpoint_paths)"}, {"kind": "method", "line": 1672, "name": "safe_compute", "signature": "def safe_compute(func)"}, {"kind": "method", "line": 2286, "name": "safe_get", "signature": "def safe_get(key)"}]}, {"doc": "maxwell_crystallography_suite.py  Comprehensive crystallographic and physical analysis suite for Maxwell equation neural network checkpoints.  Integrates Berry phase, MBL analysis, Ricci flow, control theory, Schrodinger analysis, thermodynamic metrics, and Chapter 10 GOE/GUE spectral universality diagnostics.  The GOE/GUE analysis measures the imaginary-to-real kernel ratio of each SpectralLayer and evaluates nearest-neighbour spacing P(s), pair correlation R_2(s), and the Dyson beta index to determine whether the operator sits in the Gaussian Orthogonal (beta=1) or Gaussian Unitary (beta=2) universality class.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3", "id": "maxwell_crystallography_suite.py", "kind": "module", "label": "maxwell_crystallography_suite.py", "language": "py", "sha256": "6fc8175ae875ae32", "symbol_count": 123, "symbols": [{"doc": "Master configuration for the complete Maxwell crystallography suite.", "kind": "class", "line": 59, "name": "CrystallographySuiteConfig", "signature": "class CrystallographySuiteConfig"}, {"doc": "Factory for creating configured logger instances.", "kind": "class", "line": 201, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Protocol for metric calculation strategies.", "kind": "class", "line": 218, "name": "IMetricCalculator", "signature": "class IMetricCalculator(Protocol)"}, {"doc": "Protocol for phase detection strategies.", "kind": "class", "line": 226, "name": "IPhaseDetector", "signature": "class IPhaseDetector(Protocol)"}, {"doc": "Spectral convolution layer with tuneable imaginary ratio for GOE/GUE control.", "kind": "class", "line": 234, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).", "kind": "class", "line": 288, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Chapter 10 spectral universality analyzer.\n\nExtracts the spectral operator from each SpectralLayer, computes its\neigenvalue statistics, and determines proximity to GOE (beta=1) or\nGUE (beta=2) universality via P(s), R_2(s), and the Dyson index.", "kind": "class", "line": 331, "name": "GOEGUESpectralAnalyzer", "signature": "class GOEGUESpectralAnalyzer"}, {"doc": "Detect NaN and Inf corruption in model parameters.", "kind": "class", "line": 528, "name": "WeightIntegrityCalculator", "signature": "class WeightIntegrityCalculator"}, {"doc": "Delta, alpha purity, and spectral entropy of the weight distribution.", "kind": "class", "line": 559, "name": "DiscretizationCalculator", "signature": "class DiscretizationCalculator"}, {"doc": "Spectral gap, effective dimension, participation ratio, and level-spacing ratio.", "kind": "class", "line": 602, "name": "SpectralGeometryCalculator", "signature": "class SpectralGeometryCalculator"}, {"doc": "Ricci scalar and mean sectional curvature of the weight manifold.", "kind": "class", "line": 650, "name": "RicciCurvatureCalculator", "signature": "class RicciCurvatureCalculator"}, {"doc": "Berry phase from training checkpoint trajectory.", "kind": "class", "line": 695, "name": "BerryPhaseCalculator", "signature": "class BerryPhaseCalculator"}, {"doc": "Control theory stability analysis for neural network dynamics.", "kind": "class", "line": 784, "name": "ControlSystemAnalyzer", "signature": "class ControlSystemAnalyzer"}, {"doc": "Gibbs free energy, critical temperature, and phase classification.", "kind": "class", "line": 842, "name": "ThermodynamicCalculator", "signature": "class ThermodynamicCalculator"}, {"doc": "Complete 2D Fourier analysis with spectral concentration and resonance metrics.", "kind": "class", "line": 881, "name": "FullFourierAnalyzer", "signature": "class FullFourierAnalyzer"}, {"doc": "Centre-of-mass in Fourier space for topological phase detection.", "kind": "class", "line": 924, "name": "FourierMassCenterAnalyzer", "signature": "class FourierMassCenterAnalyzer"}, {"doc": "Hysteretic phase detector combining alignment and resonance signals.", "kind": "class", "line": 962, "name": "TopologicalPhaseDetector", "signature": "class TopologicalPhaseDetector"}, {"doc": "Extract spectral weight tensors from SpectralLayer modules.", "kind": "class", "line": 996, "name": "SpectralFieldExtractor", "signature": "class SpectralFieldExtractor"}, {"doc": "Topological metrics from model spectral fields.", "kind": "class", "line": 1015, "name": "TopologicalMetricsCalculator", "signature": "class TopologicalMetricsCalculator"}, {"doc": "Gradient covariance kappa and effective temperature.", "kind": "class", "line": 1051, "name": "GradientDynamicsCalculator", "signature": "class GradientDynamicsCalculator"}, {"doc": "Quantum mechanical analysis via Johnson-Lindenstrauss compressed wavefunction.", "kind": "class", "line": 1110, "name": "SchrodingerAnalyzer", "signature": "class SchrodingerAnalyzer"}, {"doc": "Generate multi-panel analysis figures for each checkpoint.", "kind": "class", "line": 1156, "name": "ComprehensiveVisualizer", "signature": "class ComprehensiveVisualizer"}, {"doc": "Main analyzer orchestrating all metric calculations on a single checkpoint.", "kind": "class", "line": 1451, "name": "CheckpointAnalyzer", "signature": "class CheckpointAnalyzer"}, {"doc": "Process all checkpoints in a directory, generating per-checkpoint and summary outputs.", "kind": "class", "line": 1575, "name": "BatchProcessor", "signature": "class BatchProcessor"}, {"doc": "Main entry point for the Maxwell crystallography analysis suite.", "kind": "class", "line": 1775, "name": "MaxwellCrystallographySuite", "signature": "class MaxwellCrystallographySuite"}, {"doc": "Parse arguments and run the Maxwell crystallography suite.", "kind": "method", "line": 1850, "name": "main", "signature": "def main()"}, {"doc": "Create and return a configured logger.", "kind": "method", "line": 205, "name": "create_logger", "signature": "def create_logger(name, level, config)"}, {"doc": "Compute metrics for the given model.", "kind": "method", "line": 221, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Detect phase from spectral field.", "kind": "method", "line": 229, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"doc": "Initialise real and imaginary kernel parameters.", "kind": "method", "line": 237, "name": "__init__", "signature": "def __init__(self, channels, grid_size, config, imaginary_ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 252, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Extract (channels x channels) complex Hermitian-like matrix for eigenvalue analysis.", "kind": "method", "line": 271, "name": "get_spectral_operator", "signature": "def get_spectral_operator(self)"}, {"doc": "Return the imaginary-to-real kernel norm ratio.", "kind": "method", "line": 279, "name": "get_kernel_ratio", "signature": "def get_kernel_ratio(self)"}, {"doc": "Build all sub-layers with the given architectural parameters.", "kind": "method", "line": 291, "name": "__init__", "signature": "def __init__(self, config, imaginary_ratio)"}, {"doc": "Forward pass through the full spectral network.", "kind": "method", "line": 309, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Compute effective imaginary-to-real kernel norm ratio across all layers.", "kind": "method", "line": 320, "name": "get_kernel_ratio", "signature": "def get_kernel_ratio(self)"}, {"doc": "Store configuration reference.", "kind": "method", "line": 340, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the complex spectral operator from every SpectralLayer in the model.", "kind": "method", "line": 344, "name": "extract_spectral_operators", "signature": "def extract_spectral_operators(self, model)"}, {"doc": "Unfold eigenvalues and return normalised nearest-neighbour spacings.", "kind": "method", "line": 353, "name": "compute_eigenvalue_spacing", "signature": "def compute_eigenvalue_spacing(self, eigenvalues)"}, {"doc": "MSE between empirical P(s) and Wigner surmise for GOE or GUE.", "kind": "method", "line": 368, "name": "compute_spacing_distribution_loss", "signature": "def compute_spacing_distribution_loss(self, spacings, target)"}, {"doc": "Estimate the Dyson beta from small-spacing power-law P(s) ~ s^beta.", "kind": "method", "line": 385, "name": "compute_dyson_index", "signature": "def compute_dyson_index(self, spacings)"}, {"doc": "Two-level correlation function R_2(s).", "kind": "method", "line": 402, "name": "compute_pair_correlation", "signature": "def compute_pair_correlation(self, eigenvalues)"}, {"doc": "MSE between empirical R_2(s) and analytical prediction.", "kind": "method", "line": 423, "name": "compute_correlation_loss", "signature": "def compute_correlation_loss(self, eigenvalues, target)"}, {"doc": "Run full GOE/GUE spectral analysis on all spectral layers.", "kind": "method", "line": 438, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Return zero-valued results when no spectral layers are found.", "kind": "method", "line": 512, "name": "_empty_results", "signature": "def _empty_results()"}, {"doc": "Store config reference.", "kind": "method", "line": 531, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return integrity report.", "kind": "method", "line": 535, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Store config reference.", "kind": "method", "line": 562, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute delta, alpha, spectral entropy, and per-layer deltas.", "kind": "method", "line": 566, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Shannon entropy of the normalised power spectrum of concatenated weights.", "kind": "method", "line": 588, "name": "_compute_spectral_entropy", "signature": "def _compute_spectral_entropy(self, weights)"}, {"doc": "Store config reference.", "kind": "method", "line": 605, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute spectral geometry observables from weight outer product.", "kind": "method", "line": 609, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Mean min(s_i, s_{i+1}) / max(s_i, s_{i+1}).", "kind": "method", "line": 638, "name": "_compute_level_spacing_ratio", "signature": "def _compute_level_spacing_ratio(self, spacings)"}, {"doc": "Store config reference.", "kind": "method", "line": 653, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute Ricci scalar and sectional curvatures from weight metric.", "kind": "method", "line": 657, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Ricci scalar via inverse eigenvalue sum.", "kind": "method", "line": 672, "name": "_compute_ricci_scalar", "signature": "def _compute_ricci_scalar(self, metric)"}, {"doc": "Sample 2x2 sub-block determinants as sectional curvature proxies.", "kind": "method", "line": 681, "name": "_estimate_sectional_curvatures", "signature": "def _estimate_sectional_curvatures(self, metric)"}, {"doc": "Initialise logger.", "kind": "method", "line": 698, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load all .pth files sorted by epoch.", "kind": "method", "line": 703, "name": "load_checkpoints", "signature": "def load_checkpoints(self, checkpoint_dir)"}, {"doc": "Parse epoch number from filename.", "kind": "method", "line": 720, "name": "_extract_epoch", "signature": "def _extract_epoch(self, filepath)"}, {"doc": "Concatenate all spectral layer kernels into a single complex vector.", "kind": "method", "line": 725, "name": "flatten_kernel_params", "signature": "def flatten_kernel_params(self, state_dict)"}, {"doc": "Discrete Berry connection between consecutive parameter snapshots.", "kind": "method", "line": 744, "name": "compute_berry_connection_discrete", "signature": "def compute_berry_connection_discrete(self, theta_prev, theta_curr)"}, {"doc": "Compute total Berry phase, winding number, and cumulative trajectory.", "kind": "method", "line": 755, "name": "calculate_berry_phase", "signature": "def calculate_berry_phase(self, checkpoint_dir)"}, {"doc": "Store config reference.", "kind": "method", "line": 787, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Extract a composite state-space (A, B, C, D) from weight matrices.", "kind": "method", "line": 791, "name": "extract_state_space", "signature": "def extract_state_space(self, model)"}, {"doc": "Eigenvalue stability analysis of the state matrix.", "kind": "method", "line": 821, "name": "analyze_stability", "signature": "def analyze_stability(self, A)"}, {"doc": "Run full control-theory analysis.", "kind": "method", "line": 836, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Store config reference.", "kind": "method", "line": 845, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute thermodynamic potentials from crystallographic observables.", "kind": "method", "line": 849, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Classify the thermodynamic phase of the model.", "kind": "method", "line": 866, "name": "_classify_phase", "signature": "def _classify_phase(self, delta, kappa, temp, alpha)"}, {"doc": "Precompute wavenumber grids.", "kind": "method", "line": 884, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return magnitude, phase, power, and derived statistics.", "kind": "method", "line": 893, "name": "compute_full_spectrum", "signature": "def compute_full_spectrum(self, spectral_field)"}, {"doc": "Aggregate spectral concentration into a resonance score.", "kind": "method", "line": 913, "name": "compute_resonance_metrics", "signature": "def compute_resonance_metrics(self, spectral_field)"}, {"doc": "Initialise wavenumber grids and sub-analyzers.", "kind": "method", "line": 927, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return centre-of-mass coordinates and resonance diagnostics.", "kind": "method", "line": 936, "name": "compute_mass_center", "signature": "def compute_mass_center(self, spectral_field)"}, {"doc": "Initialise history buffers.", "kind": "method", "line": 965, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Full topological phase detection returning diagnostic dict.", "kind": "method", "line": 973, "name": "detect", "signature": "def detect(self, spectral_field)"}, {"doc": "Return the mean complex spectral kernel across all spectral layers.", "kind": "method", "line": 1000, "name": "extract", "signature": "def extract(model, grid_size)"}, {"doc": "Initialise sub-components.", "kind": "method", "line": 1018, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run topological detection and return metrics dict.", "kind": "method", "line": 1024, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Zero-valued metrics when analysis is disabled or unavailable.", "kind": "method", "line": 1042, "name": "_empty_metrics", "signature": "def _empty_metrics()"}, {"doc": "Store config reference.", "kind": "method", "line": 1054, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute kappa, T_eff, and gradient variance from validation data.", "kind": "method", "line": 1058, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Initialise projection parameters.", "kind": "method", "line": 1113, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Project the full parameter vector to a fixed-dimension wavefunction.", "kind": "method", "line": 1119, "name": "extract_compressed_wavefunction", "signature": "def extract_compressed_wavefunction(self, model)"}, {"doc": "Random projection preserving pairwise distances.", "kind": "method", "line": 1134, "name": "_compress_johnson_lindenstrauss", "signature": "def _compress_johnson_lindenstrauss(self, vector)"}, {"doc": "Compute wavefunction entropy, participation ratio, and quantum coherence.", "kind": "method", "line": 1142, "name": "compute", "signature": "def compute(self, model)"}, {"doc": "Store config reference.", "kind": "method", "line": 1159, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render the full 5x4 analysis dashboard to a file.", "kind": "method", "line": 1163, "name": "visualize_checkpoint_analysis", "signature": "def visualize_checkpoint_analysis(self, results, output_path)"}, {"doc": "Pie chart of valid / NaN / Inf parameter counts.", "kind": "method", "line": 1194, "name": "_plot_weight_distribution", "signature": "def _plot_weight_distribution(self, results, ax)"}, {"doc": "Bar chart of spectral geometry observables.", "kind": "method", "line": 1206, "name": "_plot_spectral_analysis", "signature": "def _plot_spectral_analysis(self, results, ax)"}, {"doc": "Alpha vs T_eff phase diagram with crystal/glass boundaries.", "kind": "method", "line": 1217, "name": "_plot_phase_diagram", "signature": "def _plot_phase_diagram(self, results, ax)"}, {"doc": "Bar chart of Ricci curvature summary statistics.", "kind": "method", "line": 1232, "name": "_plot_curvature_distribution", "signature": "def _plot_curvature_distribution(self, results, ax)"}, {"doc": "Level spacing ratio with Wigner-Dyson and Poisson reference lines.", "kind": "method", "line": 1243, "name": "_plot_level_spacing", "signature": "def _plot_level_spacing(self, results, ax)"}, {"doc": "Largest and smallest eigenvalue on log scale.", "kind": "method", "line": 1253, "name": "_plot_eigenvalue_spectrum", "signature": "def _plot_eigenvalue_spectrum(self, results, ax)"}, {"doc": "Gibbs free energy, entropy proxy, and critical temperature.", "kind": "method", "line": 1267, "name": "_plot_thermodynamic_potentials", "signature": "def _plot_thermodynamic_potentials(self, results, ax)"}, {"doc": "Phase state, alignment, and resonance scores.", "kind": "method", "line": 1278, "name": "_plot_topological_metrics", "signature": "def _plot_topological_metrics(self, results, ax)"}, {"doc": "Berry phase arrow on the unit circle.", "kind": "method", "line": 1289, "name": "_plot_berry_phase", "signature": "def _plot_berry_phase(self, results, ax)"}, {"doc": "Stability margin and binary stability flag.", "kind": "method", "line": 1304, "name": "_plot_control_stability", "signature": "def _plot_control_stability(self, results, ax)"}, {"doc": "Wavefunction entropy, participation ratio, and coherence.", "kind": "method", "line": 1314, "name": "_plot_quantum_metrics", "signature": "def _plot_quantum_metrics(self, results, ax)"}, {"doc": "Text summary of key observables and phase classification.", "kind": "method", "line": 1325, "name": "_plot_summary_table", "signature": "def _plot_summary_table(self, results, ax)"}, {"doc": "Horizontal bar chart of per-layer discretization margins.", "kind": "method", "line": 1352, "name": "_plot_layer_deltas", "signature": "def _plot_layer_deltas(self, results, ax)"}, {"doc": "Spectral concentration and resonance score bars.", "kind": "method", "line": 1364, "name": "_plot_resonance_metrics", "signature": "def _plot_resonance_metrics(self, results, ax)"}, {"doc": "Scatter of spectral gap vs participation ratio.", "kind": "method", "line": 1374, "name": "_plot_spectral_concentration", "signature": "def _plot_spectral_concentration(self, results, ax)"}, {"doc": "Single-bar health score with traffic-light colouring.", "kind": "method", "line": 1384, "name": "_plot_health_score", "signature": "def _plot_health_score(self, results, ax)"}, {"doc": "Grouped bar chart comparing P(s) and R_2(s) losses for GOE and GUE.", "kind": "method", "line": 1393, "name": "_plot_goe_gue_losses", "signature": "def _plot_goe_gue_losses(self, results, ax)"}, {"doc": "Dyson beta index gauge with GOE and GUE reference markers.", "kind": "method", "line": 1410, "name": "_plot_dyson_beta", "signature": "def _plot_dyson_beta(self, results, ax)"}, {"doc": "Per-layer imaginary-to-real kernel norm ratios.", "kind": "method", "line": 1421, "name": "_plot_kernel_ratios", "signature": "def _plot_kernel_ratios(self, results, ax)"}, {"doc": "Horizontal gauge showing interpolation between GOE and GUE.", "kind": "method", "line": 1438, "name": "_plot_universality_gauge", "signature": "def _plot_universality_gauge(self, results, ax)"}, {"doc": "Instantiate all sub-calculators.", "kind": "method", "line": 1454, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load a checkpoint, run every analyzer, and return the aggregated results dict.", "kind": "method", "line": 1471, "name": "analyze_checkpoint", "signature": "def analyze_checkpoint(self, checkpoint_path, val_data)"}, {"doc": "Weighted average of integrity, purity, MBL, and topological scores.", "kind": "method", "line": 1553, "name": "_compute_health_score", "signature": "def _compute_health_score(self, results)"}, {"doc": "Initialise analyzer and visualizer.", "kind": "method", "line": 1578, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Iterate over all .pth files, analyze each, and save results.", "kind": "method", "line": 1585, "name": "process_directory", "signature": "def process_directory(self, checkpoint_dir, output_dir, val_data)"}, {"doc": "Aggregate statistics and rank checkpoints by delta, alpha, accuracy, and health score.", "kind": "method", "line": 1616, "name": "_generate_summary", "signature": "def _generate_summary(self, all_results)"}, {"doc": "Time-series plots of key metrics across training.", "kind": "method", "line": 1735, "name": "_generate_evolution_plots", "signature": "def _generate_evolution_plots(self, all_results, output_dir)"}, {"doc": "Initialise the suite with all sub-components.", "kind": "method", "line": 1778, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Execute full analysis: batch processing, Berry phase, and summary.", "kind": "method", "line": 1785, "name": "run_analysis", "signature": "def run_analysis(self, checkpoint_dir, output_dir)"}, {"doc": "Dedicated Berry phase figure with phasor diagram and summary text.", "kind": "method", "line": 1804, "name": "_generate_berry_phase_visualization", "signature": "def _generate_berry_phase_visualization(self, berry_results, output_dir)"}, {"kind": "method", "line": 1621, "name": "_extract", "signature": "def _extract(cat, key, default)"}, {"kind": "method", "line": 1624, "name": "_stats", "signature": "def _stats(vals)"}, {"kind": "method", "line": 1630, "name": "_checkpoint_id", "signature": "def _checkpoint_id(r)"}, {"kind": "method", "line": 1662, "name": "_best_entry", "signature": "def _best_entry(idx)"}]}, {"doc": "maxwell_field_hawking_suite.py  Combined electromagnetic field analysis and Hawking radiation thermodynamics for Maxwell spectral network checkpoints.  Implements two complementary physical analyses on trained neural network weights:  1. Hawking Radiation Thermodynamics Maps weight tensors to gravitational analogs (G_eff, hbar_eff, k_B_eff, c_eff, M_eff, A_eff) and computes Bekenstein-Hawking entropy, Hawking temperature, radiation power, Schwarzschild radius, evaporation timescale, surface gravity, tidal forces, and information escape rate.  2. Maxwell / Poisson Electromagnetic Field Analysis Maps weights to a 3D dielectric lattice, solves the Poisson equation for the electrostatic potential, computes EM scattering intensity (Bragg peaks vs Rayleigh diffuse), dielectric tensor anisotropy, photonic entropy, and bandgap estimation.  Crystal phases show sharp Bragg peaks, low entropy, and high anisotropy; glass phases show diffuse scattering, high entropy, and isotropy.  Both analyses operate on the kernel_real and kernel_imag parameters of the SpectralLayer modules inside a MaxwellSpectralNetwork checkpoint.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3", "id": "maxwell_field_hawking_suite.py", "kind": "module", "label": "maxwell_field_hawking_suite.py", "language": "py", "sha256": "0d3107ca26e9954e", "symbol_count": 99, "symbols": [{"doc": "Immutable master configuration for the combined analysis suite.", "kind": "class", "line": 67, "name": "AnalysisConfig", "signature": "class AnalysisConfig"}, {"doc": "Factory for creating configured logger instances.", "kind": "class", "line": 142, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Unpickler that handles unknown classes by creating dummy dict-like objects.", "kind": "class", "line": 158, "name": "CustomUnpickler", "signature": "class CustomUnpickler(Unpickler)"}, {"doc": "Load a checkpoint with multiple fallback strategies.", "kind": "method", "line": 185, "name": "load_checkpoint_robust", "signature": "def load_checkpoint_robust(path, device)"}, {"doc": "Spectral convolution layer with tuneable imaginary ratio.", "kind": "class", "line": 207, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).", "kind": "class", "line": 242, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Extract metadata (epoch, loss, delta) from checkpoint dicts.", "kind": "class", "line": 283, "name": "MetadataExtractor", "signature": "class MetadataExtractor"}, {"doc": "G_eff from weight distance to discrete attractor and gradient magnitude.", "kind": "class", "line": 331, "name": "GravitationalConstantCalculator", "signature": "class GravitationalConstantCalculator"}, {"doc": "hbar_eff from uncertainty, action quantisation, conductance, and information entropy.", "kind": "class", "line": 366, "name": "PlanckConstantCalculator", "signature": "class PlanckConstantCalculator"}, {"doc": "k_B_eff from configuration entropy and thermal fluctuations.", "kind": "class", "line": 412, "name": "BoltzmannConstantCalculator", "signature": "class BoltzmannConstantCalculator"}, {"doc": "c_eff from Planck relation and spectral velocity of weight matrices.", "kind": "class", "line": 440, "name": "SpeedOfLightCalculator", "signature": "class SpeedOfLightCalculator"}, {"doc": "M_eff from Planck mass formula, active parameter count, and energy-mass relation.", "kind": "class", "line": 466, "name": "InformationalMassCalculator", "signature": "class InformationalMassCalculator"}, {"doc": "A_eff from active parameter counts and entropy proxy.", "kind": "class", "line": 500, "name": "HorizonAreaCalculator", "signature": "class HorizonAreaCalculator"}, {"doc": "Full Hawking radiation thermodynamic analysis.", "kind": "class", "line": 520, "name": "HawkingRadiationCalculator", "signature": "class HawkingRadiationCalculator"}, {"doc": "Map neural network weights to a 3D dielectric lattice.", "kind": "class", "line": 596, "name": "WeightLatticeMapper", "signature": "class WeightLatticeMapper"}, {"doc": "Spectral Poisson solver: nabla^2 phi = -rho / eps_0.", "kind": "class", "line": 626, "name": "PoissonSolver", "signature": "class PoissonSolver"}, {"doc": "EM scattering from dielectric contrast: S(k) ~ |FT(delta_eps)|^2.", "kind": "class", "line": 652, "name": "ScatteringSolver", "signature": "class ScatteringSolver"}, {"doc": "Anisotropy analysis of the dielectric medium via the structure tensor.", "kind": "class", "line": 683, "name": "DielectricTensorAnalyzer", "signature": "class DielectricTensorAnalyzer"}, {"doc": "Shannon entropy of the EM field energy distribution and density of modes.", "kind": "class", "line": 714, "name": "PhotonicEntropyCalculator", "signature": "class PhotonicEntropyCalculator"}, {"doc": "Photonic bandgap estimation from radial Fourier profile.", "kind": "class", "line": 741, "name": "BandgapAnalyzer", "signature": "class BandgapAnalyzer"}, {"doc": "Crystal vs Glass classification from EM observables.", "kind": "class", "line": 773, "name": "ElectromagneticPhaseClassifier", "signature": "class ElectromagneticPhaseClassifier"}, {"doc": "Full Maxwell / Poisson electromagnetic field analysis pipeline.", "kind": "class", "line": 807, "name": "MaxwellFieldAnalyzer", "signature": "class MaxwellFieldAnalyzer"}, {"doc": "Generate multi-panel dashboard combining Hawking and Maxwell analyses.", "kind": "class", "line": 863, "name": "CombinedVisualizer", "signature": "class CombinedVisualizer"}, {"doc": "Orchestrator that runs both Hawking and Maxwell analyses on a single checkpoint.", "kind": "class", "line": 1065, "name": "CombinedAnalyzer", "signature": "class CombinedAnalyzer"}, {"doc": "Process all checkpoints in a directory.", "kind": "class", "line": 1129, "name": "BatchAnalyzer", "signature": "class BatchAnalyzer"}, {"doc": "Parse arguments and run the combined analysis suite.", "kind": "method", "line": 1227, "name": "main", "signature": "def main()"}, {"doc": "Create and return a configured logger.", "kind": "method", "line": 146, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"doc": "Override to handle missing classes gracefully.", "kind": "method", "line": 161, "name": "find_class", "signature": "def find_class(self, module, name)"}, {"doc": "Return a dummy class that acts like a dictionary.", "kind": "method", "line": 168, "name": "_create_dummy_class", "signature": "def _create_dummy_class(self, name)"}, {"doc": "Initialise real and imaginary kernel parameters.", "kind": "method", "line": 210, "name": "__init__", "signature": "def __init__(self, channels, grid_size, imaginary_ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 223, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Build all sub-layers.", "kind": "method", "line": 245, "name": "__init__", "signature": "def __init__(self, config, imaginary_ratio)"}, {"doc": "Forward pass through the full spectral network.", "kind": "method", "line": 263, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Return all parameters as a single flat tensor.", "kind": "method", "line": 274, "name": "get_flat_parameters", "signature": "def get_flat_parameters(self)"}, {"doc": "Return all named parameter tensors as numpy arrays.", "kind": "method", "line": 278, "name": "get_weight_dict", "signature": "def get_weight_dict(self)"}, {"doc": "Return a standardised metadata dict from any checkpoint format.", "kind": "method", "line": 287, "name": "extract", "signature": "def extract(checkpoint)"}, {"doc": "Recursively search for a delta value.", "kind": "method", "line": 312, "name": "_find_delta", "signature": "def _find_delta(data, depth)"}, {"doc": "Store config reference.", "kind": "method", "line": 334, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return G_alg, force, and crystallisation pressure.", "kind": "method", "line": 338, "name": "calculate", "signature": "def calculate(self, all_weights, delta)"}, {"doc": "Store config reference.", "kind": "method", "line": 369, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return four estimates of hbar and their weighted unification.", "kind": "method", "line": 373, "name": "calculate", "signature": "def calculate(self, all_weights, delta, loss)"}, {"doc": "Store config reference.", "kind": "method", "line": 415, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return entropy-based and thermal k_B estimates.", "kind": "method", "line": 419, "name": "calculate", "signature": "def calculate(self, all_weights_np, loss, loss_history)"}, {"doc": "Store config reference.", "kind": "method", "line": 443, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return multiple c estimates.", "kind": "method", "line": 447, "name": "calculate", "signature": "def calculate(self, all_weights_np, h_bar, G_alg)"}, {"doc": "Store config reference.", "kind": "method", "line": 469, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return multiple mass estimates.", "kind": "method", "line": 473, "name": "calculate", "signature": "def calculate(self, all_weights, G_alg, c_eff, h_bar)"}, {"doc": "Store config reference.", "kind": "method", "line": 503, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return effective area from active parameters and weight entropy.", "kind": "method", "line": 507, "name": "calculate", "signature": "def calculate(self, all_weights)"}, {"doc": "Instantiate all sub-calculators.", "kind": "method", "line": 523, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run the full Hawking radiation pipeline and return all results.", "kind": "method", "line": 533, "name": "calculate", "signature": "def calculate(self, model, loss, loss_history, precomputed_delta)"}, {"doc": "Store config reference.", "kind": "method", "line": 599, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return (charge_density, permittivity) as 3D arrays.\n\nWeights are flattened and embedded into a cubic grid.\nPermittivity = 1 + scale * w_i.\nCharge density = w_i.", "kind": "method", "line": 603, "name": "map", "signature": "def map(self, weight_dict)"}, {"doc": "Store config reference.", "kind": "method", "line": 629, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return the electrostatic potential phi on the 3D grid.", "kind": "method", "line": 633, "name": "solve", "signature": "def solve(self, charge_density, permittivity)"}, {"doc": "Return E = -grad(phi).", "kind": "method", "line": 647, "name": "compute_electric_field", "signature": "def compute_electric_field(self, potential)"}, {"doc": "Store config reference.", "kind": "method", "line": 655, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return scattering intensity map, central slice, and peak analysis.", "kind": "method", "line": 659, "name": "compute", "signature": "def compute(self, permittivity)"}, {"doc": "Store config reference.", "kind": "method", "line": 686, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return eigenvalues of the gradient structure tensor and anisotropy ratio.", "kind": "method", "line": 690, "name": "analyze", "signature": "def analyze(self, permittivity)"}, {"doc": "Store config reference.", "kind": "method", "line": 717, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return field entropy, mode entropy, and their sum.", "kind": "method", "line": 721, "name": "calculate", "signature": "def calculate(self, potential, intensity_3d)"}, {"doc": "Store config reference.", "kind": "method", "line": 744, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return radial profile, gap depth, and boolean bandgap detection.", "kind": "method", "line": 748, "name": "analyze", "signature": "def analyze(self, fourier_coeffs)"}, {"doc": "Store config reference.", "kind": "method", "line": 776, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return phase name, crystal/glass flags, and confidence score.", "kind": "method", "line": 780, "name": "classify", "signature": "def classify(self, anisotropy, scattering, photonic_entropy, delta, alpha)"}, {"doc": "Instantiate all sub-components.", "kind": "method", "line": 810, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Run the full EM pipeline on the model weights.", "kind": "method", "line": 821, "name": "analyze", "signature": "def analyze(self, model)"}, {"doc": "Store config reference.", "kind": "method", "line": 866, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Save a comprehensive 4x4 figure to disk.", "kind": "method", "line": 870, "name": "render", "signature": "def render(self, hawking, maxwell, metadata, output_path)"}, {"doc": "Hawking temperature and BH entropy bars.", "kind": "method", "line": 897, "name": "_plot_hawking_summary", "signature": "def _plot_hawking_summary(self, h, ax)"}, {"doc": "Temperature gauge.", "kind": "method", "line": 906, "name": "_plot_hawking_temperature", "signature": "def _plot_hawking_temperature(self, h, ax)"}, {"doc": "Bekenstein-Hawking entropy.", "kind": "method", "line": 914, "name": "_plot_hawking_entropy", "signature": "def _plot_hawking_entropy(self, h, ax)"}, {"doc": "Effective constants summary.", "kind": "method", "line": 921, "name": "_plot_hawking_constants", "signature": "def _plot_hawking_constants(self, h, ax)"}, {"doc": "Central slice of electrostatic potential.", "kind": "method", "line": 936, "name": "_plot_potential_slice", "signature": "def _plot_potential_slice(self, m, ax)"}, {"doc": "kx-ky scattering intensity.", "kind": "method", "line": 944, "name": "_plot_scattering_slice", "signature": "def _plot_scattering_slice(self, m, ax)"}, {"doc": "Dielectric tensor eigenvalues.", "kind": "method", "line": 954, "name": "_plot_dielectric_anisotropy", "signature": "def _plot_dielectric_anisotropy(self, m, ax)"}, {"doc": "Field and mode entropy bars.", "kind": "method", "line": 964, "name": "_plot_photonic_entropy", "signature": "def _plot_photonic_entropy(self, m, ax)"}, {"doc": "Radial Fourier profile and bandgap indicator.", "kind": "method", "line": 973, "name": "_plot_bandgap", "signature": "def _plot_bandgap(self, m, ax)"}, {"doc": "Electric field magnitude statistics.", "kind": "method", "line": 984, "name": "_plot_electric_field", "signature": "def _plot_electric_field(self, m, ax)"}, {"doc": "Phase classification text panel.", "kind": "method", "line": 992, "name": "_plot_em_classification", "signature": "def _plot_em_classification(self, m, ax)"}, {"doc": "Text summary combining both analyses.", "kind": "method", "line": 1010, "name": "_plot_combined_summary", "signature": "def _plot_combined_summary(self, h, m, meta, ax)"}, {"doc": "Radiation power bar.", "kind": "method", "line": 1032, "name": "_plot_hawking_radiation_power", "signature": "def _plot_hawking_radiation_power(self, h, ax)"}, {"doc": "Schwarzschild radius and surface gravity.", "kind": "method", "line": 1039, "name": "_plot_schwarzschild", "signature": "def _plot_schwarzschild(self, h, ax)"}, {"doc": "Evaporation timescale bar.", "kind": "method", "line": 1050, "name": "_plot_evaporation", "signature": "def _plot_evaporation(self, h, ax)"}, {"doc": "Delta and alpha purity bars.", "kind": "method", "line": 1057, "name": "_plot_purity", "signature": "def _plot_purity(self, m, ax)"}, {"doc": "Instantiate sub-analyzers and visualizer.", "kind": "method", "line": 1068, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load, analyze, visualize, and return aggregated results.", "kind": "method", "line": 1076, "name": "analyze_checkpoint", "signature": "def analyze_checkpoint(self, checkpoint_path, output_dir)"}, {"doc": "Instantiate the single-checkpoint analyzer.", "kind": "method", "line": 1132, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Analyze one file or all .pth files in a directory.", "kind": "method", "line": 1138, "name": "process", "signature": "def process(self, input_path, output_dir)"}, {"doc": "Aggregate statistics across checkpoints.", "kind": "method", "line": 1176, "name": "_build_summary", "signature": "def _build_summary(self, results)"}, {"doc": "Log the best checkpoint by delta and alpha.", "kind": "method", "line": 1203, "name": "_print_ranking", "signature": "def _print_ranking(self, results)"}, {"kind": "class", "line": 170, "name": "DummyClass", "signature": "class DummyClass"}, {"kind": "method", "line": 1185, "name": "_safe_stats", "signature": "def _safe_stats(vals)"}, {"kind": "method", "line": 1210, "name": "_info", "signature": "def _info(idx)"}, {"kind": "method", "line": 171, "name": "__init__", "signature": "def __init__(self)"}, {"kind": "method", "line": 176, "name": "get", "signature": "def get(self, key, default)"}, {"kind": "method", "line": 178, "name": "keys", "signature": "def keys(self)"}, {"kind": "method", "line": 180, "name": "items", "signature": "def items(self)"}]}, {"doc": "maxwell_magnetic_orbitals.py  Experimental probe of hydrogen orbital isomorphism in Maxwell spectral networks.  Inspired by Salcuni (2025): \"Magnetic Orbitals -- The First Visual Revelation of Quantum Geometries in the Macroscopic World\" (Zenodo 19024395).  Corrected implementation addressing: Fix 1: theta = pi/2 in equatorial plane (not arccos(x/r)) Fix 2: Analytical dipole B-field from vector potential, not ad-hoc Y_lm modulation Fix 3: Hall sensor at theta = pi/2 (equatorial) with multi-angle averaging Fix 4: Multipole source hierarchy -- dipole for l=1, quadrupole for l=2, etc.  Includes analytical control validation (no neural network) to establish the theoretical isomorphism baseline before testing the trained model.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3", "id": "maxwell_magnetic_orbitals.py", "kind": "module", "label": "maxwell_magnetic_orbitals.py", "language": "py", "sha256": "6af93dc98a051841", "symbol_count": 47, "symbols": [{"doc": "Configuration for the magnetic orbital isomorphism experiment.", "kind": "class", "line": 40, "name": "IsomorphismConfig", "signature": "class IsomorphismConfig"}, {"doc": "Factory for creating configured logger instances.", "kind": "class", "line": 82, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Spectral convolution layer with tuneable imaginary ratio.", "kind": "class", "line": 96, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).", "kind": "class", "line": 117, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Load the best Maxwell checkpoint.", "kind": "class", "line": 141, "name": "ModelLoader", "signature": "class ModelLoader"}, {"doc": "Analytical electromagnetic multipole sources.\n\nFix 2: Real dipole B-field from B = (mu0/4pi)(3(m.r_hat)r_hat - m)/r^3.\nFix 1: theta = pi/2 (equatorial) for all 2D projections.\nFix 4: Proper multipole hierarchy -- l=1 dipole, l=2 quadrupole, etc.", "kind": "class", "line": 184, "name": "AnalyticalMultipoleSource", "signature": "class AnalyticalMultipoleSource"}, {"doc": "Fix 3: Multi-angle averaged Hall projection at equatorial theta = pi/2.\n\nAt theta=pi/2: nx=cos(phi), ny=sin(phi), nz=0.\nWe average over HALL_SENSOR_NUM_ANGLES phi values and add |Bz|^2.", "kind": "class", "line": 267, "name": "HallProjectionCalculator", "signature": "class HallProjectionCalculator"}, {"doc": "Generate tomographic slices at different effective distances.", "kind": "class", "line": 292, "name": "TomographicScanner", "signature": "class TomographicScanner"}, {"doc": "Analytical hydrogen orbital wavefunctions.", "kind": "class", "line": 310, "name": "HydrogenOrbitalCalculator", "signature": "class HydrogenOrbitalCalculator"}, {"doc": "Quantify structural similarity between EM field patterns and hydrogen orbitals.", "kind": "class", "line": 376, "name": "IsomorphismMetricsCalculator", "signature": "class IsomorphismMetricsCalculator"}, {"doc": "Side-by-side EM field vs hydrogen orbital visualisation.", "kind": "class", "line": 404, "name": "OrbitalVisualizer", "signature": "class OrbitalVisualizer"}, {"doc": "Main experiment: analytical control + network response for each orbital.\n\nFix 4: Only l=1 (p orbitals) use true dipole sources.\nl=0 uses monopole proxy, l>=2 uses multipole scalar potential.", "kind": "class", "line": 480, "name": "MagneticOrbitalExperiment", "signature": "class MagneticOrbitalExperiment"}, {"doc": "Parse arguments and run the experiment.", "kind": "method", "line": 585, "name": "main", "signature": "def main()"}, {"doc": "Create and return a configured logger.", "kind": "method", "line": 85, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"kind": "method", "line": 98, "name": "__init__", "signature": "def __init__(self, channels, grid_size, imaginary_ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 106, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 119, "name": "__init__", "signature": "def __init__(self, config, imaginary_ratio)"}, {"kind": "method", "line": 132, "name": "forward", "signature": "def forward(self, x)"}, {"kind": "method", "line": 143, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return (model, info_dict) from the best available checkpoint.", "kind": "method", "line": 147, "name": "load", "signature": "def load(self, checkpoint_dir)"}, {"kind": "method", "line": 179, "name": "_fallback", "signature": "def _fallback(self)"}, {"doc": "Precompute coordinate grids in the equatorial plane.", "kind": "method", "line": 192, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return a (6,H,W) source tensor for the l-th multipole.", "kind": "method", "line": 205, "name": "generate", "signature": "def generate(self, l, m)"}, {"doc": "Analytical magnetic dipole B-field in equatorial plane.", "kind": "method", "line": 211, "name": "_dipole", "signature": "def _dipole(self, m)"}, {"doc": "Higher-order multipole from scalar potential gradient.", "kind": "method", "line": 229, "name": "_multipole", "signature": "def _multipole(self, l, m)"}, {"doc": "Isotropic l=0 proxy (current loop).", "kind": "method", "line": 243, "name": "_monopole_proxy", "signature": "def _monopole_proxy(self)"}, {"doc": "Sanitise, normalise, and pack into 6-channel tensor.", "kind": "method", "line": 250, "name": "_normalise_and_pack", "signature": "def _normalise_and_pack(self, Bx, By, Bz, scale)"}, {"doc": "Return normalised |B|^2 for analytical control (no network).", "kind": "method", "line": 260, "name": "get_analytical_density", "signature": "def get_analytical_density(self, l, m)"}, {"kind": "method", "line": 274, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Multi-angle averaged Hall projection.", "kind": "method", "line": 277, "name": "project", "signature": "def project(self, model_output)"}, {"kind": "method", "line": 294, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return a list of 2D Hall projection slices.", "kind": "method", "line": 297, "name": "scan", "signature": "def scan(self, model, source, n_slices)"}, {"kind": "method", "line": 312, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Non-relativistic radial wavefunction R_nl(r).", "kind": "method", "line": 315, "name": "radial_wavefunction", "signature": "def radial_wavefunction(self, n, l, r)"}, {"doc": "Real spherical harmonic Y_l^m.", "kind": "method", "line": 323, "name": "spherical_harmonic_real", "signature": "def spherical_harmonic_real(self, l, m, theta, phi)"}, {"doc": "Fix 1: |psi(r, theta=pi/2, phi)|^2 in equatorial plane.", "kind": "method", "line": 330, "name": "probability_density_2d", "signature": "def probability_density_2d(self, n, l, m, grid_size)"}, {"doc": "Monte Carlo rejection sampling of |psi|^2.", "kind": "method", "line": 345, "name": "sample_orbital_3d", "signature": "def sample_orbital_3d(self, n, l, m, num_samples)"}, {"kind": "method", "line": 378, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return spatial correlation, node overlap, symmetry correlation, KL divergence.", "kind": "method", "line": 381, "name": "compute", "signature": "def compute(self, em_density, quantum_density)"}, {"kind": "method", "line": 406, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render comparison figure with analytical control row.", "kind": "method", "line": 409, "name": "visualize_comparison", "signature": "def visualize_comparison(self, em_density, quantum_density, metrics, label, tomo_slices, orbital_3d, save_path, analytical_density)"}, {"kind": "method", "line": 487, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Execute the full protocol.", "kind": "method", "line": 498, "name": "run", "signature": "def run(self, output_dir, checkpoint_dir)"}, {"doc": "Full protocol for one orbital.", "kind": "method", "line": 528, "name": "_analyze", "signature": "def _analyze(self, model, n, l, m, label, out)"}, {"doc": "Aggregate.", "kind": "method", "line": 544, "name": "_summary", "signature": "def _summary(self, results, info)"}, {"doc": "Narrative interpretation.", "kind": "method", "line": 562, "name": "_interp", "signature": "def _interp(self, ma, mn, mp)"}, {"doc": "Log summary.", "kind": "method", "line": 573, "name": "_print", "signature": "def _print(self, s)"}]}, {"doc": "maxwell_magnetic_orbitals_v2.py  Corrected magnetic orbital isomorphism experiment addressing the input_proj collapse identified by the layer trace diagnostic.  The layer trace showed that the structure collapses at input_proj (Conv2d 6->32) because the random 1x1 convolution destroys the physical channel semantics. The analytical source has correlation ~0.97 with hydrogen orbitals, but after input_proj it drops to ~0.14 and never recovers.  This version implements three strategies to address the collapse:  Strategy A: BYPASS -- Skip the network entirely, use the Poisson field equation to evolve the analytical dipole source.  This tests whether Maxwell's equations themselves produce isomorphic structures (the pure-physics baseline).  Strategy B: CHANNEL_AWARE -- Replace the generic input_proj with a physically-informed projection that processes each field component (Ex, Ey, Bz) separately before combining them, preserving the angular structure within each component.  Strategy C: DIRECT_SPECTRAL -- Feed the source directly into the spectral layers (bypassing input_proj and expansion_proj) by reshaping the 6-channel input to match the expansion dimension via zero-padding.  This tests whether the trained spectral kernels preserve structure when they receive clean input.", "id": "maxwell_magnetic_orbitals_v2.py", "kind": "module", "label": "maxwell_magnetic_orbitals_v2.py", "language": "py", "sha256": "17e844d4bdf723b2", "symbol_count": 50, "symbols": [{"doc": "Configuration for the v2 isomorphism experiment.", "kind": "class", "line": 55, "name": "Config", "signature": "class Config"}, {"doc": "Factory for creating configured logger instances.", "kind": "class", "line": 91, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Spectral convolution layer.", "kind": "class", "line": 105, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics.", "kind": "class", "line": 129, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Analytical EM multipole sources.", "kind": "class", "line": 163, "name": "AnalyticalMultipoleSource", "signature": "class AnalyticalMultipoleSource"}, {"doc": "Strategy A: Evolve the dipole source using the Poisson equation.\n\nSolves nabla^2 phi = -rho in Fourier space, computes E = -grad(phi),\nand returns the field energy density.  This is pure Maxwell physics\nwith no neural network.", "kind": "class", "line": 234, "name": "PoissonEvolver", "signature": "class PoissonEvolver"}, {"doc": "Strategy B: Physically-informed input projection.\n\nInstead of a single Conv2d(6, 32, 1) that scrambles channels,\nthis processes each field component (Ex, Ey, Bz) separately with\nits own 2->hidden/3 projection, then concatenates.", "kind": "class", "line": 270, "name": "ChannelAwareProjection", "signature": "class ChannelAwareProjection(Module)"}, {"doc": "Multi-angle averaged Hall projection.", "kind": "class", "line": 296, "name": "HallProjector", "signature": "class HallProjector"}, {"doc": "Analytical hydrogen orbital wavefunctions.", "kind": "class", "line": 323, "name": "HydrogenOrbitalCalculator", "signature": "class HydrogenOrbitalCalculator"}, {"doc": "Cosine similarity between two flattened maps.", "kind": "method", "line": 387, "name": "spatial_corr", "signature": "def spatial_corr(a, b, eps)"}, {"doc": "Jaccard index of nodal regions.", "kind": "method", "line": 393, "name": "node_overlap", "signature": "def node_overlap(a, b, thr)"}, {"doc": "Correlation of angular Fourier power spectra.", "kind": "method", "line": 402, "name": "symmetry_corr", "signature": "def symmetry_corr(a, b)"}, {"doc": "Compute all isomorphism metrics.", "kind": "method", "line": 410, "name": "full_metrics", "signature": "def full_metrics(em, qd, config)"}, {"doc": "Comprehensive multi-strategy comparison visualisation.", "kind": "class", "line": 419, "name": "Visualizer", "signature": "class Visualizer"}, {"doc": "Multi-strategy isomorphism experiment.\n\nFor each orbital, runs:\n  A) Analytical control (no network)\n  B) Poisson evolution (pure physics)\n  C) Full network (standard forward pass)\n  D) Direct spectral (bypass input_proj, feed spectral layers directly)", "kind": "class", "line": 479, "name": "IsomorphismExperimentV2", "signature": "class IsomorphismExperimentV2"}, {"doc": "Parse arguments and run the v2 experiment.", "kind": "method", "line": 658, "name": "main", "signature": "def main()"}, {"doc": "Create and return a configured logger.", "kind": "method", "line": 94, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"doc": "Initialise real and imaginary kernel parameters.", "kind": "method", "line": 107, "name": "__init__", "signature": "def __init__(self, channels, grid_size, imaginary_ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 116, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Build all sub-layers.", "kind": "method", "line": 131, "name": "__init__", "signature": "def __init__(self, config, imaginary_ratio)"}, {"doc": "Standard forward pass.", "kind": "method", "line": 147, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Apply only the spectral layers (bypass input/expansion projections).", "kind": "method", "line": 156, "name": "forward_spectral_only", "signature": "def forward_spectral_only(self, x_expanded)"}, {"doc": "Precompute coordinate grids.", "kind": "method", "line": 165, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return a (6,H,W) source tensor.", "kind": "method", "line": 177, "name": "generate", "signature": "def generate(self, l, m)"}, {"doc": "Analytical magnetic dipole in equatorial plane.", "kind": "method", "line": 183, "name": "_dipole", "signature": "def _dipole(self, m)"}, {"doc": "Higher-order multipole from scalar potential gradient.", "kind": "method", "line": 201, "name": "_multipole", "signature": "def _multipole(self, l, m)"}, {"doc": "Isotropic l=0 proxy.", "kind": "method", "line": 212, "name": "_monopole", "signature": "def _monopole(self)"}, {"doc": "Normalise and pack into 6-channel tensor.", "kind": "method", "line": 218, "name": "_pack", "signature": "def _pack(self, Bx, By, Bz, scale)"}, {"doc": "Return normalised |B|^2 for analytical control.", "kind": "method", "line": 227, "name": "get_density", "signature": "def get_density(self, l, m)"}, {"doc": "Store config reference.", "kind": "method", "line": 242, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Treat the Bz channel as charge density, solve Poisson, return |E|^2.\n\nThis mimics what the network should ideally learn: the electrostatic\nresponse to a given source configuration.", "kind": "method", "line": 246, "name": "evolve", "signature": "def evolve(self, source_6ch)"}, {"doc": "Build per-component projections.", "kind": "method", "line": 278, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Process each (Re, Im) pair separately then concatenate.", "kind": "method", "line": 288, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Store config reference.", "kind": "method", "line": 298, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Project a 6-channel field tensor to scalar density.", "kind": "method", "line": 302, "name": "project_6ch", "signature": "def project_6ch(self, tensor)"}, {"doc": "Project an arbitrary multi-channel tensor to scalar energy density.", "kind": "method", "line": 316, "name": "project_energy", "signature": "def project_energy(self, tensor)"}, {"doc": "Store config reference.", "kind": "method", "line": 325, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Non-relativistic radial wavefunction R_nl(r).", "kind": "method", "line": 329, "name": "radial_wavefunction", "signature": "def radial_wavefunction(self, n, l, r)"}, {"doc": "Real spherical harmonic.", "kind": "method", "line": 337, "name": "spherical_harmonic_real", "signature": "def spherical_harmonic_real(self, l, m, theta, phi)"}, {"doc": "2D |psi|^2 in equatorial plane.", "kind": "method", "line": 344, "name": "density_2d", "signature": "def density_2d(self, n, l, m, grid_size)"}, {"doc": "Monte Carlo rejection sampling.", "kind": "method", "line": 357, "name": "sample_3d", "signature": "def sample_3d(self, n, l, m, num)"}, {"doc": "Store config reference.", "kind": "method", "line": 421, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Render comparison of all strategies for one orbital.", "kind": "method", "line": 425, "name": "render", "signature": "def render(self, label, strategies, qd, orbital_3d, save_path)"}, {"doc": "Initialise all sub-components.", "kind": "method", "line": 489, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Load trained checkpoint.", "kind": "method", "line": 499, "name": "_load_model", "signature": "def _load_model(self, checkpoint_dir)"}, {"doc": "Execute the full multi-strategy experiment.", "kind": "method", "line": 527, "name": "run", "signature": "def run(self, output_dir, checkpoint_dir)"}, {"doc": "Run all strategies for one orbital.", "kind": "method", "line": 557, "name": "_analyze", "signature": "def _analyze(self, model, n, l, m, label, output_dir)"}, {"doc": "Aggregate results across orbitals and strategies.", "kind": "method", "line": 591, "name": "_summary", "signature": "def _summary(self, results, info)"}, {"doc": "Narrative interpretation.", "kind": "method", "line": 624, "name": "_interpret", "signature": "def _interpret(self, agg, p_agg)"}, {"doc": "Log the summary.", "kind": "method", "line": 646, "name": "_print_summary", "signature": "def _print_summary(self, s)"}]}, {"doc": "maxwell_orbital_diagnostic.py  Layer-by-layer diagnostic for the Maxwell magnetic orbital isomorphism experiment.  Three operating modes:  1. PASSTHROUGH -- Identity-initialised network (spectral kernels = delta function). If isomorphism survives passthrough, the architecture is compatible. If not, the projection/comparison pipeline has a bug.  2. LAYER_TRACE -- Feed the dipole source through the trained network one layer at a time, measuring spatial correlation with the hydrogen orbital after each. Identifies the exact layer where the angular structure collapses.  3. SYMMETRY_LOSS_TRAINING -- Short training run with an additional rotational symmetry preservation loss that penalises the network for breaking the angular structure of the input.  Tests whether symmetry-aware training can recover the isomorphism.  Also fixes the m=0 sph_harm phase convention issue by ensuring Y_l^0 is computed with the correct real-part extraction (scipy uses theta as polar and phi as azimuthal, matching physics convention).  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3", "id": "maxwell_orbital_diagnostic.py", "kind": "module", "label": "maxwell_orbital_diagnostic.py", "language": "py", "sha256": "99010c8242e2a285", "symbol_count": 49, "symbols": [{"doc": "Configuration for the diagnostic suite.", "kind": "class", "line": 47, "name": "DiagnosticConfig", "signature": "class DiagnosticConfig"}, {"doc": "Factory for creating configured logger instances.", "kind": "class", "line": 80, "name": "LoggerFactory", "signature": "class LoggerFactory"}, {"doc": "Spectral convolution layer with tuneable imaginary ratio.", "kind": "class", "line": 94, "name": "SpectralLayer", "signature": "class SpectralLayer(Module)"}, {"doc": "Neural network for learning Maxwell equation dynamics.", "kind": "class", "line": 128, "name": "MaxwellSpectralNetwork", "signature": "class MaxwellSpectralNetwork(Module)"}, {"doc": "Analytical EM multipole sources (same as corrected main script).", "kind": "class", "line": 182, "name": "AnalyticalMultipoleSource", "signature": "class AnalyticalMultipoleSource"}, {"doc": "Multi-angle averaged Hall projection at equatorial theta = pi/2.", "kind": "class", "line": 254, "name": "HallProjectionCalculator", "signature": "class HallProjectionCalculator"}, {"doc": "Analytical hydrogen orbital wavefunctions.", "kind": "class", "line": 281, "name": "HydrogenOrbitalCalculator", "signature": "class HydrogenOrbitalCalculator"}, {"doc": "Cosine similarity between two flattened density maps.", "kind": "method", "line": 316, "name": "compute_spatial_correlation", "signature": "def compute_spatial_correlation(a, b, eps)"}, {"doc": "Mode 1: Identity-initialised network.\n\nIf isomorphism survives passthrough, the projection pipeline is correct.", "kind": "class", "line": 324, "name": "PassthroughTest", "signature": "class PassthroughTest"}, {"doc": "Mode 2: Layer-by-layer trace through a trained network.\n\nMeasures spatial correlation after every sub-layer to find where\nthe angular structure collapses.", "kind": "class", "line": 385, "name": "LayerTraceTest", "signature": "class LayerTraceTest"}, {"doc": "Mode 3: Short training with rotational symmetry preservation loss.\n\nLoss = MSE(output, target) + weight * SymmetryLoss\nwhere SymmetryLoss penalises changes in the angular power spectrum\nbetween input and output.", "kind": "class", "line": 499, "name": "SymmetryTrainingTest", "signature": "class SymmetryTrainingTest"}, {"doc": "Orchestrate all three diagnostic modes.", "kind": "class", "line": 596, "name": "DiagnosticSuite", "signature": "class DiagnosticSuite"}, {"doc": "Parse arguments and run the diagnostic suite.", "kind": "method", "line": 625, "name": "main", "signature": "def main()"}, {"doc": "Create and return a configured logger.", "kind": "method", "line": 83, "name": "create_logger", "signature": "def create_logger(name, level)"}, {"doc": "Initialise real and imaginary kernel parameters.", "kind": "method", "line": 96, "name": "__init__", "signature": "def __init__(self, channels, grid_size, imaginary_ratio)"}, {"doc": "Apply spectral convolution in Fourier space.", "kind": "method", "line": 105, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Initialise kernels near identity: real=small, imag=0.", "kind": "method", "line": 117, "name": "init_identity", "signature": "def init_identity(self, scale)"}, {"doc": "Build all sub-layers.", "kind": "method", "line": 130, "name": "__init__", "signature": "def __init__(self, config, imaginary_ratio)"}, {"doc": "Forward pass.", "kind": "method", "line": 146, "name": "forward", "signature": "def forward(self, x)"}, {"doc": "Forward pass returning the output after every sub-layer.", "kind": "method", "line": 155, "name": "forward_with_intermediates", "signature": "def forward_with_intermediates(self, x)"}, {"doc": "Initialise all layers near identity / passthrough.", "kind": "method", "line": 167, "name": "init_identity", "signature": "def init_identity(self)"}, {"doc": "Precompute coordinate grids in the equatorial plane.", "kind": "method", "line": 184, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Return a (6,H,W) source tensor for the l-th multipole.", "kind": "method", "line": 196, "name": "generate", "signature": "def generate(self, l, m)"}, {"doc": "Analytical magnetic dipole B-field in equatorial plane.", "kind": "method", "line": 202, "name": "_dipole", "signature": "def _dipole(self, m)"}, {"doc": "Higher-order multipole from scalar potential gradient.", "kind": "method", "line": 220, "name": "_multipole", "signature": "def _multipole(self, l, m)"}, {"doc": "Isotropic l=0 proxy.", "kind": "method", "line": 232, "name": "_monopole_proxy", "signature": "def _monopole_proxy(self)"}, {"doc": "Sanitise, normalise, pack into 6 channels.", "kind": "method", "line": 238, "name": "_pack", "signature": "def _pack(self, Bx, By, Bz, scale)"}, {"doc": "Return normalised |B|^2.", "kind": "method", "line": 247, "name": "get_analytical_density", "signature": "def get_analytical_density(self, l, m)"}, {"doc": "Store config reference.", "kind": "method", "line": 256, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Multi-angle averaged Hall projection.", "kind": "method", "line": 260, "name": "project", "signature": "def project(self, tensor)"}, {"doc": "Project an intermediate activation to a scalar energy density.", "kind": "method", "line": 273, "name": "project_intermediate", "signature": "def project_intermediate(self, tensor)"}, {"doc": "Store config reference.", "kind": "method", "line": 283, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Non-relativistic radial wavefunction R_nl(r).", "kind": "method", "line": 287, "name": "radial_wavefunction", "signature": "def radial_wavefunction(self, n, l, r)"}, {"doc": "Real spherical harmonic Y_l^m.", "kind": "method", "line": 295, "name": "spherical_harmonic_real", "signature": "def spherical_harmonic_real(self, l, m, theta, phi)"}, {"doc": "2D |psi|^2 in equatorial plane (theta=pi/2).", "kind": "method", "line": 302, "name": "probability_density_2d", "signature": "def probability_density_2d(self, n, l, m, grid_size)"}, {"doc": "Initialise sub-components.", "kind": "method", "line": 330, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Test all orbitals with an identity-initialised network.", "kind": "method", "line": 338, "name": "run", "signature": "def run(self, output_dir)"}, {"doc": "Initialise sub-components.", "kind": "method", "line": 392, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Trace a trained model layer by layer.", "kind": "method", "line": 400, "name": "run", "signature": "def run(self, checkpoint_dir, output_dir)"}, {"doc": "Find the layer where correlation drops most sharply.", "kind": "method", "line": 436, "name": "_find_collapse", "signature": "def _find_collapse(self, trace)"}, {"doc": "Plot correlation vs layer index for all orbitals.", "kind": "method", "line": 448, "name": "_plot_traces", "signature": "def _plot_traces(self, all_traces, output_dir)"}, {"doc": "Load the trained model.", "kind": "method", "line": 472, "name": "_load_model", "signature": "def _load_model(self, checkpoint_dir)"}, {"doc": "Initialise sub-components.", "kind": "method", "line": 507, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Compute the angular power spectrum of a 2D field via azimuthal FFT.", "kind": "method", "line": 515, "name": "compute_angular_power", "signature": "def compute_angular_power(self, tensor)"}, {"doc": "Penalise angular power spectrum distortion.", "kind": "method", "line": 522, "name": "symmetry_loss", "signature": "def symmetry_loss(self, input_tensor, output_tensor)"}, {"doc": "Train a fresh model with symmetry loss and track isomorphism.", "kind": "method", "line": 528, "name": "run", "signature": "def run(self, output_dir)"}, {"doc": "Plot training loss and correlation over epochs.", "kind": "method", "line": 572, "name": "_plot_history", "signature": "def _plot_history(self, history, output_dir)"}, {"doc": "Initialise all test modes.", "kind": "method", "line": 598, "name": "__init__", "signature": "def __init__(self, config)"}, {"doc": "Execute all three diagnostic modes and save results.", "kind": "method", "line": 606, "name": "run_all", "signature": "def run_all(self, output_dir, checkpoint_dir)"}]}], "type": "CodePropertyGraph", "version": "1.0"}
```

---

## Architecture Reference

### PY (7 files)

#### `app.py`
**Path:** `app.py`
**File Doc:** *app.py  Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:*

*No symbols extracted*

#### `maxwell_crystal.py`
**Path:** `maxwell_crystal.py`
**File Doc:** *maxwell_crystal.py  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date of creation: 2026 License: AGPL v3  Description: Maxwell Equations Grokking via Hamiltonian Topological Crystallization.  Maxwell equations in vacuum (CGS-Gauss units, c=1): curl E = -dB/dt curl B =  dE/dt div  E = 0 div  B = 0  2D TM polarization on a periodic grid (Ex, Ey, Bz): dBz/dt = -(dEy/dx - dEx/dy) dEx/dt =  dBz/dy dEy/dt = -dBz/dx  Five-phase protocol: Phase 0 - Spectral Kernel Ratio Optimization (Chapter 10: GOE-GUE transition) Phase 1 - Batch size prospecting with delta/dt velocity Phase 2 - Seed mining with decreasing delta criterion Phase 3 - Full training of best seed + batch size until grokking Phase 4 - Refinement via simulated annealing toward crystal state*

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
- `SpectralLayer` (line 610) `class SpectralLayer(Module)` - *Fourier-domain convolutional layer with tuneable imaginary ratio.

The imaginary_ratio parameter controls the transition between GOE-like
(real symmetric kernel) and GUE-like (complex Hermitian kernel)
spectral statistics of the operator.*
- `MaxwellSpectralNetwork` (line 688) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics on a 2D grid.

Input/output: 6 real channels encoding (Re, Im) of (Ex, Ey, Bz).
Architecture: 1x1 projection --> expansion --> spectral layers --> contraction --> 1x1.*
- `HamiltonianBackbone` (line 749) `class HamiltonianBackbone(Module)` - *Pre-trained backbone for single-channel Hamiltonian inference.*
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
- `TopologicalCrystallizationLoss` (line 1333) `class TopologicalCrystallizationLoss(Module)` - *Loss function driving the system toward topological crystal order.*
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

**Methods:**
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
**File Doc:** *maxwell_crystallography_suite.py  Comprehensive crystallographic and physical analysis suite for Maxwell equation neural network checkpoints.  Integrates Berry phase, MBL analysis, Ricci flow, control theory, Schrodinger analysis, thermodynamic metrics, and Chapter 10 GOE/GUE spectral universality diagnostics.  The GOE/GUE analysis measures the imaginary-to-real kernel ratio of each SpectralLayer and evaluates nearest-neighbour spacing P(s), pair correlation R_2(s), and the Dyson beta index to determine whether the operator sits in the Gaussian Orthogonal (beta=1) or Gaussian Unitary (beta=2) universality class.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3*

**Classes:**
- `CrystallographySuiteConfig` (line 59) `class CrystallographySuiteConfig` - *Master configuration for the complete Maxwell crystallography suite.*
- `LoggerFactory` (line 201) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `IMetricCalculator` (line 218) `class IMetricCalculator(Protocol)` - *Protocol for metric calculation strategies.*
- `IPhaseDetector` (line 226) `class IPhaseDetector(Protocol)` - *Protocol for phase detection strategies.*
- `SpectralLayer` (line 234) `class SpectralLayer(Module)` - *Spectral convolution layer with tuneable imaginary ratio for GOE/GUE control.*
- `MaxwellSpectralNetwork` (line 288) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
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

**Methods:**
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
**File Doc:** *maxwell_field_hawking_suite.py  Combined electromagnetic field analysis and Hawking radiation thermodynamics for Maxwell spectral network checkpoints.  Implements two complementary physical analyses on trained neural network weights:  1. Hawking Radiation Thermodynamics Maps weight tensors to gravitational analogs (G_eff, hbar_eff, k_B_eff, c_eff, M_eff, A_eff) and computes Bekenstein-Hawking entropy, Hawking temperature, radiation power, Schwarzschild radius, evaporation timescale, surface gravity, tidal forces, and information escape rate.  2. Maxwell / Poisson Electromagnetic Field Analysis Maps weights to a 3D dielectric lattice, solves the Poisson equation for the electrostatic potential, computes EM scattering intensity (Bragg peaks vs Rayleigh diffuse), dielectric tensor anisotropy, photonic entropy, and bandgap estimation.  Crystal phases show sharp Bragg peaks, low entropy, and high anisotropy; glass phases show diffuse scattering, high entropy, and isotropy.  Both analyses operate on the kernel_real and kernel_imag parameters of the SpectralLayer modules inside a MaxwellSpectralNetwork checkpoint.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3*

**Classes:**
- `AnalysisConfig` (line 67) `class AnalysisConfig` - *Immutable master configuration for the combined analysis suite.*
- `LoggerFactory` (line 142) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `CustomUnpickler` (line 158) `class CustomUnpickler(Unpickler)` - *Unpickler that handles unknown classes by creating dummy dict-like objects.*
- `SpectralLayer` (line 207) `class SpectralLayer(Module)` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 242) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
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

**Methods:**
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
**File Doc:** *maxwell_magnetic_orbitals.py  Experimental probe of hydrogen orbital isomorphism in Maxwell spectral networks.  Inspired by Salcuni (2025): "Magnetic Orbitals -- The First Visual Revelation of Quantum Geometries in the Macroscopic World" (Zenodo 19024395).  Corrected implementation addressing: Fix 1: theta = pi/2 in equatorial plane (not arccos(x/r)) Fix 2: Analytical dipole B-field from vector potential, not ad-hoc Y_lm modulation Fix 3: Hall sensor at theta = pi/2 (equatorial) with multi-angle averaging Fix 4: Multipole source hierarchy -- dipole for l=1, quadrupole for l=2, etc.  Includes analytical control validation (no neural network) to establish the theoretical isomorphism baseline before testing the trained model.  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3*

**Classes:**
- `IsomorphismConfig` (line 40) `class IsomorphismConfig` - *Configuration for the magnetic orbital isomorphism experiment.*
- `LoggerFactory` (line 82) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 96) `class SpectralLayer(Module)` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 117) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics (TM mode: Ex, Ey, Bz).*
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

**Methods:**
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
**File Doc:** *maxwell_magnetic_orbitals_v2.py  Corrected magnetic orbital isomorphism experiment addressing the input_proj collapse identified by the layer trace diagnostic.  The layer trace showed that the structure collapses at input_proj (Conv2d 6->32) because the random 1x1 convolution destroys the physical channel semantics. The analytical source has correlation ~0.97 with hydrogen orbitals, but after input_proj it drops to ~0.14 and never recovers.  This version implements three strategies to address the collapse:  Strategy A: BYPASS -- Skip the network entirely, use the Poisson field equation to evolve the analytical dipole source.  This tests whether Maxwell's equations themselves produce isomorphic structures (the pure-physics baseline).  Strategy B: CHANNEL_AWARE -- Replace the generic input_proj with a physically-informed projection that processes each field component (Ex, Ey, Bz) separately before combining them, preserving the angular structure within each component.  Strategy C: DIRECT_SPECTRAL -- Feed the source directly into the spectral layers (bypassing input_proj and expansion_proj) by reshaping the 6-channel input to match the expansion dimension via zero-padding.  This tests whether the trained spectral kernels preserve structure when they receive clean input.*

**Classes:**
- `Config` (line 55) `class Config` - *Configuration for the v2 isomorphism experiment.*
- `LoggerFactory` (line 91) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 105) `class SpectralLayer(Module)` - *Spectral convolution layer.*
- `MaxwellSpectralNetwork` (line 129) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics.*
- `AnalyticalMultipoleSource` (line 163) `class AnalyticalMultipoleSource` - *Analytical EM multipole sources.*
- `PoissonEvolver` (line 234) `class PoissonEvolver` - *Strategy A: Evolve the dipole source using the Poisson equation.

Solves nabla^2 phi = -rho in Fourier space, computes E = -grad(phi),
and returns the field energy density.  This is pure Maxwell physics
with no neural network.*
- `ChannelAwareProjection` (line 270) `class ChannelAwareProjection(Module)` - *Strategy B: Physically-informed input projection.

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

**Methods:**
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
**File Doc:** *maxwell_orbital_diagnostic.py  Layer-by-layer diagnostic for the Maxwell magnetic orbital isomorphism experiment.  Three operating modes:  1. PASSTHROUGH -- Identity-initialised network (spectral kernels = delta function). If isomorphism survives passthrough, the architecture is compatible. If not, the projection/comparison pipeline has a bug.  2. LAYER_TRACE -- Feed the dipole source through the trained network one layer at a time, measuring spatial correlation with the hydrogen orbital after each. Identifies the exact layer where the angular structure collapses.  3. SYMMETRY_LOSS_TRAINING -- Short training run with an additional rotational symmetry preservation loss that penalises the network for breaking the angular structure of the input.  Tests whether symmetry-aware training can recover the isomorphism.  Also fixes the m=0 sph_harm phase convention issue by ensuring Y_l^0 is computed with the correct real-part extraction (scipy uses theta as polar and phi as azimuthal, matching physics convention).  Author: Gris Iscomeback Email: grisiscomeback@gmail.com Date: 2026 License: AGPL v3*

**Classes:**
- `DiagnosticConfig` (line 47) `class DiagnosticConfig` - *Configuration for the diagnostic suite.*
- `LoggerFactory` (line 80) `class LoggerFactory` - *Factory for creating configured logger instances.*
- `SpectralLayer` (line 94) `class SpectralLayer(Module)` - *Spectral convolution layer with tuneable imaginary ratio.*
- `MaxwellSpectralNetwork` (line 128) `class MaxwellSpectralNetwork(Module)` - *Neural network for learning Maxwell equation dynamics.*
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

**Methods:**
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
