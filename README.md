# Computational Biology — 12-Month Research Accelerator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-20-green.svg)]()
[![Track A Progress](https://img.shields.io/badge/Track%20A-0%25-lightgrey.svg)](Learning_Progress.md)
[![Track B Progress](https://img.shields.io/badge/Track%20B-0%25-lightgrey.svg)](Learning_Progress.md)
[![Notebooks Completed](https://img.shields.io/badge/Notebooks-0%2F164-lightgrey.svg)](Learning_Progress.md)

A structured, portfolio-driven 12-month Research Accelerator in Computational Biology, designed around two simultaneous real-world targets:

- **Track A** — employable as a Project Associate / Junior Research Fellow / Bioinformatics Engineer in India by Month 6
- **Track B** — a competitive, fully funded European PhD application in Computational Biology, Bioinformatics, Systems Biology, or adjacent fields by Month 12

This is not a university syllabus. Every design decision — module depth, sequencing, portfolio artifacts — exists to answer one question: *what is the highest-leverage use of the next 12 months?*

---

## Motivation

Computational biology sits at the intersection of programming, mathematics, statistics, and life sciences. Mastering all of it in 12 months is not possible. This repository makes an honest architectural choice instead: **depth-tiered, deliberately lopsided coverage, sequenced by leverage, inside a hard 12-month box.**

The approach is shaped by real constraints:

- A zero-biology background that must become genuine literacy, not shallow familiarity
- Existing 5/5 Python and 3/5 ML fluency that makes some modules cheap to bring to mastery
- Two concrete deadlines: 6-month Track A employability bar, 12-month Track B application deadline
- Interviews that test specific, documented patterns — BLAST mechanics, RNA-seq pipeline defense, statistics cold

---

## Learning Philosophy

Four interlocking principles drive every design decision:

1. **Depth tiering** — every module is explicitly Tier 1 (Master), Tier 2 (Working), or Tier 3 (Survey). Going deeper than a module's assigned tier must justify itself against the 12-month box.
2. **Parallel tracks** — foundational modules run concurrently, not serially. Multiple modules are active in any given week.
3. **Portfolio-first sequencing** — the first interview-ready artifact exists by Month 3–4, not Month 11.
4. **Hard timeboxing** — every module has a week-budget. When the clock runs out, ship what exists and move on.

Every notebook follows a mandatory 13-step teaching sequence — motivation → intuition → biological background → mathematics → computational explanation → Python implementation → visualization → exercises → implementation → review → improvement → reflection → continuation — that never compresses under time pressure.

See [CLAUDE.md](CLAUDE.md) for the full project constitution and [Learning_Progress.md](Learning_Progress.md) for the live tracker.

---

## Repository Architecture

```bash
computational-biology/
├── README.md                          ← this file
├── ENVIRONMENT.md                     ← exact setup, pinned versions, one-command bootstrap
├── CLAUDE.md                          ← project constitution (philosophy, rules, teaching method)
├── Learning_Progress.md               ← 12-month sprint tracker (live document)
├── environment.yml                    ← conda environment specification
├── requirements.txt                   ← pip dependency list
├── pyproject.toml                     ← project metadata and packaging
├── LICENSE
├── .pre-commit-config.yaml            ← jupytext sync + nbstripout hooks
│
├── curriculum/                        ← 20 modules, each self-contained
│   ├── 00_orientation/                ← prerequisite — complete before Module 01
│   ├── 01_python_scientific_computing/
│   ├── 02_mathematics_for_biology/
│   ├── 03_statistics_and_probability/
│   ├── 04_linear_algebra/
│   ├── 05_biology_fundamentals/
│   ├── 06_genetics_and_evolution/
│   ├── 07_biochemistry_and_molecular_biology/
│   ├── 08_bioinformatics_sequence_analysis/
│   ├── 09_genomics_and_ngs/
│   ├── 10_transcriptomics_and_proteomics/
│   ├── 11_structural_biology/
│   ├── 12_systems_and_network_biology/
│   ├── 13_machine_learning_for_biology/
│   ├── 14_deep_learning_and_gnns/
│   ├── 15_simulation_and_agent_based_modeling/
│   ├── 16_research_software_engineering/
│   ├── 17_hpc_parallel_and_rust/
│   ├── 18_scientific_writing_and_open_science/
│   ├── 19_research_seminar_and_paper_reading/
│   └── 20_capstone_projects/
│
├── portfolio/                         ← curated, polished artifacts — linked in every application
├── paper-notes/                       ← one file per paper, Three-Pass Method output
├── progress/                          ← weekly and monthly progress logs
├── scripts/                           ← reusable CLI tools and data-fetch scripts
└── utilities/compbio_utils/           ← shared, tested, packaged Python utility library
```

Every module folder contains:

| File | Purpose |
| ------ | --------- |
| `README.md` | Objectives, depth tier, week-budget, Track A/B relevance |
| `roadmap.md` | Ordered notebook sequence, exercises, assignments, mini-projects |
| `references.md` | Books, documentation, key software, key labs, key researchers |
| `papers.md` | Foundational papers with timing, difficulty, and Pass-3 guidance |
| `notebooks/` | Lecture-equivalent notebooks, one per roadmap line item |
| `exercises/` | Posed-not-solved, paired 1:1 with notebooks |
| `assignments/` | Larger, less-scaffolded tasks |
| `mini_projects/` | Tier 1 and Tier 2 modules only |
| `datasets/` | `raw/` (gitignored, fetched by script) + `processed/` + per-dataset README |

---

## Curriculum Overview

| # | Module | Tier | Notebooks | Status |
| --- | -------- | ------ | ----------- | -------- |
| 00 | Orientation | Prerequisite | 13 | ⏳ Not started |
| 01 | Python & Scientific Computing | **Tier 1** | 20 | ⏳ 0 / 20 |
| 02 | Mathematics for Biology | Tier 2 | 12 | ⏳ 0 / 12 |
| 03 | Statistics & Probability | **Tier 1** | 18 | ⏳ 0 / 18 |
| 04 | Linear Algebra | Tier 2 | 10 | ⏳ 0 / 10 |
| 05 | Biology Fundamentals | **Tier 1** | 18 | ⏳ 0 / 18 |
| 06 | Genetics & Evolution | Tier 2 | 12 | ⏳ 0 / 12 |
| 07 | Biochemistry & Molecular Biology | Tier 2 | 10 | ⏳ 0 / 10 |
| 08 | Bioinformatics: Sequence Analysis | **Tier 1** | 18 | ⏳ 0 / 18 |
| 09 | Genomics & NGS | **Tier 1** | 18 | ⏳ 0 / 18 |
| 10 | Transcriptomics & Proteomics | Tier 2 | 10 | ⏳ 0 / 10 |
| 11 | Structural Biology | Tier 3 | 8 | ⏳ 0 / 8 |
| 12 | Systems & Network Biology | Tier 2* | 12 | ⏳ 0 / 12 |
| 13 | Machine Learning for Biology | **Tier 1** | 16 | ⏳ 0 / 16 |
| 14 | Deep Learning & GNNs | Tier 3 | 8 | ⏳ 0 / 8 |
| 15 | Simulation & Agent-Based Modeling | Tier 2 | 12 | ⏳ 0 / 12 |
| 16 | Research Software Engineering | **Tier 1** | 16 | ⏳ 0 / 16 |
| 17 | HPC, Parallel Computing & Rust | Tier 2 | 10 | ⏳ 0 / 10 |
| 18 | Scientific Writing & Open Science | Ongoing | — | ⏳ Habit not started |
| 19 | Research Seminar & Paper Reading | Ongoing | — | ⏳ 0 papers logged |
| 20 | Capstone Projects | **Tier 1 (synthesis)** | — | ⏳ Topic TBD at Month 9 |

*Module 12 is a Tier 1 promotion candidate — review explicitly at the Month 3 quarterly checkpoint.

**Tier distribution:** 8 Tier 1, 7 Tier 2, 2 Tier 3, 2 Ongoing, 1 Capstone.

---

## 12-Month Sprint Roadmap

Parallel tracks — multiple modules are active in any given month. The sprint calendar is a planning tool, not a contract.

| Month | Period | Active Modules | Key Milestone |
| ------- | -------- | ---------------- | --------------- |
| 1 | Jul 2026 | 01, 03, 05 | Repository live; environment working |
| 2 | Aug 2026 | 01, 02, 03, 04, 05 | First public commits; ORCID/EURAXESS registered |
| 3 | Sep 2026 | 03, 05, 06, 07, 08 | First mini-project public — **Quarterly checkpoint 1** |
| 4 | Oct 2026 | 06, 07, 08, 09 | First Track A applications sent |
| 5 | Nov 2026 | 09, 12 | Track A interviews begin |
| 6 | Dec 2026 | 10, 12 | **Month 6 checkpoint — Track A bar due** |
| 7 | Jan 2027 | 10, 13 | First formal PhD applications |
| 8 | Feb 2027 | 13, 16 | **Quarterly checkpoint 2** |
| 9 | Mar 2027 | 15, 16, 17 | `compbio_utils` v1.0 tagged; Capstone topic chosen |
| 10 | Apr 2027 | 11, 14, 17 | Survey sprints |
| 11 | May 2027 | 19, SOP | **Quarterly checkpoint 3** — applications finalized |
| 12 | Jun 2027 | 20 (Capstone) | **Month 12 checkpoint — Track B package due** |

---

## Technology Stack

**Core languages:** Python 3.11+, Rust (Modules 16–17)

**Scientific Python stack:**

| Library | Purpose |
| --------- | --------- |
| NumPy, SciPy | Numerical computing, ODE solvers, optimization |
| Pandas | Tabular data and biological metadata |
| Matplotlib, Seaborn | Scientific visualization |
| scikit-learn | Classical machine learning |
| PyTorch | Deep learning (Modules 13–14) |
| Biopython, scikit-bio | Sequence data, bioinformatics utilities |
| pydeseq2 | Differential expression (Module 09) |
| scanpy | Single-cell genomics (Module 10) |
| networkx, COBRApy | Network and metabolic modeling (Module 12) |
| Mesa | Agent-based modeling (Module 15) |

**Bioinformatics tools (usage level):** BWA, STAR, HISAT2, GATK, SAMtools, MAFFT, MUSCLE

**Infrastructure:**

| Tool | Purpose |
| ------ | --------- |
| JupyterLab + Jupytext | Notebooks paired with `.py` files for git-diffable history |
| nbstripout | Strip outputs before commit — keeps diffs readable |
| papermill | Parametric notebook re-execution |
| pytest + GitHub Actions | Testing and continuous integration |
| pre-commit | Git hooks (Jupytext sync + nbstripout) |
| uv or conda | Environment management |
| Docker (optional) | Strongest reproducibility guarantee |

**Rust toolchain (Modules 16–17):** Cargo, rustup, PyO3 + maturin (Python–Rust bridge)

---

## Repository Goals

**Month 6 — Track A bar:**

- Modules 01, 03, 05, 08, 09, 12 complete at interview depth
- ≥3 polished, public, reproducible notebooks in `portfolio/`
- Able to defend any portfolio artifact cold: BLAST mechanics, RNA-seq pipeline, statistics under questioning

**Month 12 — Track B package:**

- Complete public repository with consistent notebook quality across all Tier 1 modules
- `compbio_utils` v1.0 tagged with tests, documentation, and `CITATION.cff`
- ≥1 preprint or strong written artifact
- Applications submitted to EMBL EIPP, IMPRS-BAC, IMPRS-ML, and other live programmes

---

## How to Use This Repository

**New to this repository?**
Start with [`curriculum/00_orientation/`](curriculum/00_orientation/) — it is a prerequisite for everything else.

**Setting up the environment?**
Read [`ENVIRONMENT.md`](ENVIRONMENT.md) and follow the one-command bootstrap.

**Following the curriculum?**
Each module's `roadmap.md` lists notebooks in teaching order. Work through them sequentially. Multiple modules run in parallel — see the sprint calendar above.

**Reading papers?**
Follow the Three-Pass Method documented in [`CLAUDE.md`](CLAUDE.md) §8. Log every Pass-3 attempt in `paper-notes/`.

**Tracking progress?**
[`Learning_Progress.md`](Learning_Progress.md) is the single source of truth for what is done and what is next. Update it when a notebook or paper completes — not on a fixed schedule.

---

## Learning Workflow

Every notebook follows this 13-step sequence. It never compresses under time pressure. The lever for managing the 12-month constraint is module tier — fewer notebooks, less mini-project scope — never a shortcut through this sequence.

| Step | Description |
| ------ | ------------- |
| 1 | **Motivation** — why does this exist? What real problem does it solve? |
| 2 | **Intuition** — plain language, concrete analogy, no jargon yet |
| 3 | **Biological background** — the real biology underneath, even for math-heavy topics |
| 4 | **Mathematical explanation** — formalized, every symbol defined in plain English |
| 5 | **Computational explanation** — the algorithm or data structure, language-independent |
| 6 | **Python implementation** — built incrementally, narrated |
| 7 | **Visualization** — a figure that makes the result legible |
| 8 | **Exercises** — posed, never pre-solved in the notebook |
| 9 | **Implementation** — write the exercises yourself; review afterward |
| 10 | **Review** — correctness, style, biological soundness |
| 11 | **Improve** — revise based on the review |
| 12 | **Reflection** — one paragraph, plain English: what is understood and what is still fuzzy |
| 13 | **Continue** — only after the reflection is written |

---

## Progress

| Tracker | Current |
| --------- | --------- |
| Notebooks completed | 0 / ~164 |
| Papers read (Pass 3 logged) | 0 |
| Portfolio artifacts | 0 |
| Track A applications sent | 0 |
| Track B applications sent | 0 |

*Updated: June 2026 — see [`Learning_Progress.md`](Learning_Progress.md) for the live readiness scorecard.*

---

## License

Code in this repository is released under the [MIT License](LICENSE).

Dataset licenses vary — each `datasets/README.md` within a module documents the license for that specific dataset. Do not commit raw data that carries a license prohibiting redistribution; use a fetch script in `scripts/` instead.

---

## Acknowledgements

Built on the open-science infrastructure that makes reproducible research possible: Biopython, scikit-bio, NumPy, SciPy, EMBL-EBI training materials, and Software Carpentry.

Paper-reading methodology adapted from Keshav (2007), *How to Read a Paper*, ACM SIGCOMM Computer Communication Review.

Repository architecture and teaching philosophy documented in [CLAUDE.md](CLAUDE.md).

---

*This repository is part of a 12-month Research Accelerator Program. See [CLAUDE.md](CLAUDE.md) for the full project constitution and [Learning_Progress.md](Learning_Progress.md) for the live tracker.*
