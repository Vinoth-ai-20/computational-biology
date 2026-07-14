# Module 17 — Exercises

Each notebook in `notebooks/` has a corresponding exercise set here. Attempt the exercise before reading the solution or asking for a hint.

## Exercise files

| Notebook | Exercise file | Core task |
|----------|--------------|-----------|
| NB01 | `ex01_numpy_vectorization.py` | Vectorize a pairwise edit-distance matrix without loops |
| NB02 | `ex02_multiprocessing.py` | Parallelize BLAST-hit counting across 200 FASTA files using Pool.map |
| NB03 | `ex03_joblib_dask.py` | Dask array sliding window on a 50M-element signal; joblib k-mer count |
| NB04 | `ex04_numba_jit.py` | Numba-JIT a Smith-Waterman score matrix fill and benchmark vs NumPy |
| NB05 | `ex05_cython_basics.py` | Write the Cython `.pyx` source for a typed GC-content function |
| NB06 | `ex06_slurm.py` | Generate a 100-task SLURM job array script for BWA-MEM alignment |
| NB07 | `ex07_rust_fundamentals.py` | Python translation of three Rust programs (reverse complement, k-mer count, FASTA length histogram) |
| NB08 | `ex08_rust_ownership.py` | Python RC-model analogy exercise; explain three borrow-checker errors |
| NB09 | `ex09_rust_sequences.py` | Implement a Python k-mer spectrum function matching the Rust version's API |
| NB10 | `ex10_pyo3.py` | Write the Python fallback for `gc_content`, `reverse_complement`, `hamming_distance` matching PyO3 signatures |
| NB11 | `ex11_benchmarking.py` | Extend BenchmarkSuite to add a Numba implementation; re-run the scaling analysis |
| NB12 | `ex12_assessment.py` | Implement all 5 assessment stubs from the mini project |

## Instructions

1. Read the corresponding notebook first — all exercises assume the notebook material.
2. Write your solution in the exercise file.
3. Do not look at the notebook's implementation cells while working on the exercise.
4. After completing, compare your solution to the notebook — note differences.
5. Write a one-sentence reflection at the top of the file: what was harder than expected?

## Grading rubric (self-assessment)

- **Correctness:** Does it produce the right output on the test cases?
- **Readability:** Could another computational biologist understand this in 2 minutes?
- **Efficiency:** Did you avoid unnecessary loops where a vectorized solution exists?
- **Biological validity:** Does the code handle edge cases (empty sequences, non-ATCG characters)?
