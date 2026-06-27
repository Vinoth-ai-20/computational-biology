# Module 01 — Python & Scientific Computing

**Depth tier:** Tier 1 — Master
**Week budget:** Weeks 1–6 (parallel with Modules 02, 03, 05)
**Notebooks:** 20
**Status:** ⏳ Not started — 0 / 20 notebooks

---

## Motivation

Python is the computational substrate for every other module in this program. But "knowing Python" is not the objective — the goal is scientific Python: the specific library ecosystem, idioms, and reproducibility practices that define how computational biology is actually written, reviewed, and published.

This module bridges an existing strong Python background (5/5 on core Python) to the biology-specific toolchain. It is not a Python tutorial. The diagnostic quiz in Notebook 02 gates what can be skipped. The biology-specific content — Biopython, scientific data cleaning for biological metadata, Unix command-line workflows — is new even for an experienced Python programmer.

The module's primary deliverable is `compbio_utils` v0: a seeded, installable, tested utility package that every later module builds on. Getting this architecture right at the start pays compounding returns.

---

## Learning Objectives

By the end of this module you will be able to:

1. Use NumPy arrays fluently for biological data: sequences as arrays, expression matrices, distance matrices
2. Apply broadcasting and vectorization in place of Python loops in numerical code
3. Use Pandas to clean, reshape, and merge biological datasets including metadata tables
4. Produce publication-quality scientific figures with Matplotlib and Seaborn
5. Solve biological ODE problems with SciPy's `solve_ivp`
6. Write reusable scientific code organized as functions, modules, and a packaged library
7. Test scientific code with `pytest`, including floating-point-tolerant assertions
8. Use Biopython's `SeqIO` and `SeqRecord` for sequence data
9. Execute bioinformatics-flavored Unix workflows from the command line
10. Ship `compbio_utils` v0 as a working, installable, version-controlled package

---

## Track A Relevance

**Direct.** Python, NumPy, Pandas, and Unix fluency are the baseline expectation for every Track A posting found in this program's research. They are tested first, before domain content. Expect: a live-coding warm-up (FizzBuzz-class), a Pandas data-cleaning question, and a "what does NumPy broadcasting do?" explanation in the same interview session. Notebook 20's mock interview drill rehearses exactly this pattern.

## Track B Relevance

**Foundation.** Every notebook in every downstream module is written in the scientific Python established here. A PhD supervisor reading the repository evaluates code quality, structure, and testing discipline before reading the domain content.

---

## Portfolio Artifact

**`compbio_utils` v0** — a seeded, installable, tested Python package containing at minimum:

- `sequence.py` — GC content, nucleotide composition, complement, reverse complement, FASTA/FASTQ utilities wrapping Biopython
- `stats.py` — stubs for Module 03 content; `describe()` function as a baseline
- `plotting.py` — reusable biological plot functions: `expression_heatmap()`, `volcano_plot_scaffold()`, `pca_scatter()`
- `io.py` — FASTA and FASTQ reading utilities
- `tests/` — a `pytest` suite covering `sequence.py`'s public API
- `README.md` — install instructions, minimal usage example
- `pyproject.toml` — version `0.1.0`, properly declared

This package is a living artifact. It reaches `v1.0` in Module 16 after testing, documentation, and CI are properly set up. Every module between 01 and 16 adds to it.

---

## Prerequisites

- Module 00 (Orientation) complete — environment working, Git workflow understood, Jupytext pairing in use
- Existing Python programming experience — this module is not a Python introduction

---

## Expected Outcomes

After completing this module:

- You can reproduce any notebook in this module from a clean clone using only `ENVIRONMENT.md`
- `compbio_utils` installs cleanly: `pip install -e utilities/compbio_utils`
- The full `pytest` suite passes
- You pass the Track A mock interview drill in Notebook 20 (Unix + NumPy + live-coding warm-up) without notes

---

## Subtopics

See [`roadmap.md`](roadmap.md) for the full ordered notebook breakdown. Core topic areas:

- **NumPy:** arrays, broadcasting, vectorization, linear algebra operations, reproducible random number generation
- **Pandas:** data loading, cleaning, reshaping, merging biological metadata and expression tables
- **Matplotlib / Seaborn:** publication-quality scientific visualization for biological data
- **SciPy:** optimization (`curve_fit`, `minimize`), numerical integration, ODE solvers (`solve_ivp`)
- **Biopython:** `SeqRecord`, `Seq`, `SeqIO`, NCBI Entrez (with rate-limiting etiquette)
- **Unix:** command-line fluency for bioinformatics pipelines — pipes, `grep`, `awk`, `for` loops
- **Software engineering:** functions → modules → packages, `pytest`, `pyproject.toml`, semantic versioning

---

## References

See [`references.md`](references.md) for books, documentation, online resources, and key software versions.

## Papers

See [`papers.md`](papers.md) for reading assignments with timing, difficulty, and Pass-3 guidance.

---

*Module 02 (Mathematics for Biology), Module 03 (Statistics), and Module 05 (Biology Fundamentals) run in parallel with this module from Week 1.*

*See also: [CLAUDE.md](../../CLAUDE.md) §5 (coding philosophy), §7.1 (notebook content order) — [Learning_Progress.md](../../Learning_Progress.md) §4 Module 01*
