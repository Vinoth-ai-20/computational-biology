# Module 17 — Assignments

Assignments are larger, less-scaffolded tasks that integrate multiple notebooks. Complete after finishing the full notebook sequence.

## Assignment 1 — Parallel RNA-seq Pipeline Profiler

**After:** NB01–NB06  
**Estimated time:** 6–8 hours  
**Output:** A Jupyter notebook + a SLURM script

### Task

You are given 50 simulated RNA-seq count matrices (synthetic data, generated in the notebook). Your pipeline must:

1. Load each count matrix using Dask (out-of-core, never load all 50 at once)
2. Compute per-gene mean, variance, and coefficient of variation across samples — vectorized with NumPy
3. Identify the top-500 most variable genes using NumPy argsort (no pandas for the ranking step)
4. Parallelize steps 2–3 across the 50 matrices using joblib (n_jobs=-1)
5. Collect results and write a summary TSV
6. Generate a SLURM script that would run this pipeline on a real cluster (30 matrices per job, 2 jobs total, 4 cores each, 8 GB RAM, 2 hours)

**Deliverables:**
- `assignments/A1_rnaseq_pipeline_profiler.ipynb` — the complete pipeline, with timing at each step
- `assignments/A1_slurm_pipeline.sh` — the SLURM script
- A table showing wall time at each step (Python loop baseline vs. vectorized vs. joblib parallel)

## Assignment 2 — Rust k-mer Counter with PyO3 Bindings

**After:** NB07–NB10  
**Estimated time:** 4–6 hours (plus Rust installation if not yet done)  
**Output:** A Rust crate + Python test notebook

### Task

Build a Python-callable Rust module `compbio_rs` that exposes:

```python
def kmer_count(sequence: str, k: int) -> dict[str, int]: ...
def gc_content(sequence: str) -> float: ...
def reverse_complement(sequence: str) -> str: ...
```

Requirements:
1. The Rust implementation must handle sequences with non-ATCG characters gracefully (return an error via PyO3's `PyErr`)
2. `kmer_count` must use a `HashMap<String, usize>` internally
3. A Python fallback must exist for environments without the compiled extension
4. A test notebook `A2_pyo3_kmer_counter.ipynb` benchmarks Python vs Rust at N=10,000 sequences

**Deliverables:**
- `assignments/compbio_rs/src/lib.rs` — Rust source
- `assignments/compbio_rs/Cargo.toml`
- `assignments/compbio_rs/pyproject.toml`
- `assignments/A2_pyo3_kmer_counter.ipynb` — test + benchmark notebook

## Note on assignment grading

These assignments are self-assessed. After completing, answer:
1. What was harder than expected and why?
2. What would you do differently on a second attempt?
3. What question does this assignment leave open?

Log answers in the notebook's final reflection cell.
