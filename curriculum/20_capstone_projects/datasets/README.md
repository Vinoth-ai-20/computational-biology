# Module 20 — Datasets

All capstone datasets are generated synthetically within the notebooks. No external downloads are required to run the capstone notebooks, which ensures full reproducibility from a clean clone.

| ID | Dataset | Generated in | Used in | Notes |
|----|---------|-------------|---------|-------|
| DS01 | Synthetic RNA-seq count matrix (5000 genes × 6 samples, negative-binomial) | NB02 | NB02, NB03, NB04 | 300 injected DE genes (150 up, 150 down); RNG seed 42 |
| DS02 | GATAAG motif sequences (3000 × 101 bp) | NB05 | NB05, NB06, NB07 | 1500 positive (motif injected), 1500 negative (dinucleotide-shuffled) |
| DS03 | Synthetic epidemic incidence (SIR simulation with noise) | NB08 | NB08, NB09 | N=1000, β=0.3, γ=0.1, I₀=5; Poisson observation noise |
| DS04 | GO annotation table (synthetic) | NB04 | NB04 | 5000 genes × 50 GO terms, random assignment; for enrichment demo only |

## Note on real data
For Track A job interviews, familiarity with real datasets is valuable. After completing the capstones on synthetic data, consider running CP01's analysis on a small real GEO dataset (e.g., GSE48213 — breast cancer cell lines, small enough to process on a laptop). Instructions: download the count matrix from GEO, replace DS01 with it, and re-run NB02–NB04. The pipeline is designed to be data-agnostic.
