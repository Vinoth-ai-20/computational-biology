# Module 17 — Roadmap

Ordered notebook sequence. Complete in order; each notebook builds on the previous.

| # | Notebook | Key concepts | Estimated time |
|---|----------|-------------|----------------|
| 01 | `01_numpy_vectorization.ipynb` | Broadcasting rules, vectorized ops, `np.einsum`, loop-to-vector translation | 3 h |
| 02 | `02_multiprocessing_threading.ipynb` | GIL, `Pool.map`, `ProcessPoolExecutor`, `ThreadPoolExecutor`, Amdahl's law | 3 h |
| 03 | `03_joblib_and_dask.ipynb` | `joblib.Parallel`, `Memory` caching, Dask array, Dask dataframe, task graphs | 3 h |
| 04 | `04_numba_jit.ipynb` | `@numba.jit`, `@numba.vectorize`, `@numba.prange`, compilation overhead, warm/cold timing | 3 h |
| 05 | `05_cython_basics.ipynb` | `cdef`, `cpdef`, typed memoryviews, `nogil`, speedup progression | 2 h |
| 06 | `06_slurm_and_hpc.ipynb` | `#SBATCH` directives, job arrays, Snakemake DAG, cluster architecture | 3 h |
| 07 | `07_rust_fundamentals.ipynb` | Rust syntax, types, `Vec`, `HashMap`, `enum`, `match`, ownership model overview | 4 h |
| 08 | `08_rust_ownership_borrowing.ipynb` | Ownership rules, `&T`/`&mut T` references, borrow checker, lifetimes `'a` | 4 h |
| 09 | `09_rust_sequences_kmers.ipynb` | FASTA parser, k-mer counting, reverse complement in Rust; Python reference implementations | 4 h |
| 10 | `10_pyo3_rust_python.ipynb` | `#[pyfunction]`, `#[pymodule]`, `maturin develop`, Cargo.toml, fallback pattern | 3 h |
| 11 | `11_performance_benchmarking.ipynb` | `BenchmarkSuite` class, timeit, scaling curves, Amdahl's law, profiling waterfall | 3 h |
| 12 | `12_mini_project_and_assessment.ipynb` | Pairwise sequence identity (3 implementations), 5 assessment stubs | 4 h |

**Total estimated time:** ~35 hours over 3 weeks

## Milestone checkpoints

- After NB04: you can vectorize and JIT-compile any numerical biology kernel
- After NB06: you can write and submit a SLURM job array for a real pipeline
- After NB09: you can read Rust source code and write simple Rust functions
- After NB12: mini project submitted and 5 assessment functions implemented

## Exercises

Each notebook has a paired exercises file in `exercises/`. Attempt the exercise before opening the solutions.

## Mini project (Tier 2 deliverable)

See `mini_projects/README.md` — pairwise sequence identity benchmark across three implementations, delivered as a reproducible notebook with a results table and scaling plot.
