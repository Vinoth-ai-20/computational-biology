# Module 17 — HPC, Parallel Computing, and Rust

**Tier:** 2 — Working competence  
**Week budget:** 3 weeks  
**Track A relevance:** HPC-adjacent roles (compute clusters, bioinformatics pipelines) require familiarity with parallel computing and vectorization; Rust competence is a rare differentiator.  
**Track B relevance:** PhD research involving large genomic datasets requires computational efficiency; Rust for bioinformatics (noodles, needletail) is actively used at Sanger and EMBL.

## Objectives

Vectorize NumPy computations; parallelize with multiprocessing and joblib; JIT-compile with Numba; understand SLURM job submission; write idiomatic Rust for sequence analysis; call Rust from Python via PyO3.

## Depth Tier: 2 — Working Competence

At the end of this module you can:
- Apply NumPy broadcasting rules to eliminate Python loops in biological computations
- Parallelize CPU-bound tasks with `multiprocessing.Pool` and `joblib.Parallel`
- Use Dask for out-of-core computation on large genomic datasets
- JIT-compile numerical kernels with Numba and measure the speedup
- Write and explain basic Rust code: ownership, borrowing, enums, structs
- Understand how PyO3 bridges Rust functions into Python modules
- Generate and submit SLURM job scripts for bioinformatics pipeline steps
- Build a reproducible benchmarking framework that validates correctness and measures scaling

## Track A — India RA/JRF/Bioinformatics Engineer

Interview patterns this module addresses:
- "Walk me through how you'd speed up a slow Python script" — vectorization → profiling → Numba → Rust, in that order
- Pipeline fluency: SLURM, Snakemake, job arrays, memory/time allocation
- "Have you worked on a cluster?" — SLURM literacy is expected for most wet-lab bioinformatics roles

## Track B — European PhD Competitiveness

- Rust is used in production at Sanger (noodles), EMBL, and multiple EBI teams for high-throughput sequence processing
- HPC competence signals that you can handle real data volumes — not just classroom-scale arrays
- A PyO3 extension module is a strong portfolio artifact: Python API, Rust performance, one `maturin develop` away from working

## Prerequisites

- Module 01 (Python), Module 04 (Linear Algebra / NumPy), Module 08 (Bioinformatics / sequences)
- Basic comfort with the command line and conda environments

## Week Budget

| Week | Focus |
|------|-------|
| Week 1 | NB01–NB04: NumPy vectorization, multiprocessing, joblib/Dask, Numba |
| Week 2 | NB05–NB09: Cython, SLURM/HPC, Rust fundamentals, ownership, sequences |
| Week 3 | NB10–NB12: PyO3, systematic benchmarking, mini project + assessment |
