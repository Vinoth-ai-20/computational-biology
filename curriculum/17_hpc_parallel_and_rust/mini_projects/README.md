# Module 17 — Mini Project

**Title:** Pairwise Sequence Identity: A Three-Implementation Benchmark  
**Tier 2 deliverable** — required for module completion

## Objective

Implement pairwise sequence identity (the fraction of matching positions between two aligned sequences) using three different approaches, benchmark all three, validate correctness, and produce a reproducible report.

## Problem statement

Given N=1000 DNA sequences of length L=200:

```
identity(a, b) = sum(a[i] == b[i] for i in range(L)) / L
```

Compute the full N×N identity matrix (1,000,000 pairs).

## Three implementations required

### Implementation 1 — Python loop (baseline)
```python
def pairwise_identity_python(seqs):
    N = len(seqs)
    result = np.zeros((N, N))
    for i in range(N):
        for j in range(i, N):
            match = sum(a == b for a, b in zip(seqs[i], seqs[j]))
            result[i, j] = result[j, i] = match / len(seqs[i])
    return result
```
This is O(N²L). For N=1000, L=200: 200 million character comparisons.

### Implementation 2 — NumPy broadcasting
Convert sequences to a NumPy integer array of shape (N, L), then use broadcasting to compute all pairwise comparisons in one vectorized expression. No Python loops over pairs.

### Implementation 3 — Numba parallel
JIT-compile the double loop with `@numba.njit(parallel=True)` and `numba.prange`.

## Deliverables

`mini_projects/MP01_pairwise_identity_benchmark.ipynb` containing:

1. Data generation: 1000 random DNA sequences, length 200, seeded for reproducibility
2. All three implementations, each in its own function
3. Correctness validation: assert all three implementations agree on a small test set (N=10)
4. Timing: `timeit` each implementation at N=[10, 50, 100, 500, 1000] where feasible (skip Python loop for N=1000 if it takes >5 minutes — estimate instead)
5. Results table: implementation × N → wall time (seconds)
6. Scaling plot: log-log, wall time vs N, all three implementations
7. Speedup table: NumPy/Python and Numba/Python ratios at each N
8. One-paragraph reflection: what does this exercise teach about the cost of Python abstraction?

## Assessment criteria

- Correctness: all implementations agree on the test set
- Reproducibility: the notebook runs top-to-bottom from a clean kernel with `np.random.seed(42)`
- Clarity: each implementation is explained in a markdown cell before the code
- Biological context: the reflection connects the benchmark to a real biological use case (e.g. multiple sequence alignment, phylogenetic distance matrix)

## Extension (optional, not required for Tier 2)

Add a fourth implementation using joblib to parallelize the Python loop across rows. How does it compare to NumPy broadcasting at large N?
