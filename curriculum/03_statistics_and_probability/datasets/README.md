# Datasets — Module 03: Statistics and Probability

## Policy

Raw data files are gitignored. Fetch via the scripts below.
Processed/synthetic data generated inside notebooks is reproducible from the notebook itself.

---

## Datasets Used in This Module

### DS01 — Synthetic gene expression matrix (NB02, NB06, NB16)
- **Source:** Generated in NB02 using `numpy.random.default_rng(42)`
- **Format:** 200 genes × 20 samples (10 control, 10 treatment)
- **Fetch:** Run NB02 Cell 6.1 — no download required

### DS02 — GEO expression dataset (NB17 — mini project)
- **Source:** NCBI GEO — GSE2034 (Wang et al. 2005, breast cancer, Affymetrix)
- **Fetch:** `scripts/fetch_geo.py --accession GSE2034 --outdir datasets/raw/`
- **Format:** Tab-delimited expression matrix; sample metadata in series matrix
- **License:** Public domain (GEO terms of use)
- **Note:** 286 samples × ~22,000 probes — NB17 uses a 500-gene subset for speed

### DS03 — Synthetic allele frequency data (NB13)
- **Source:** Generated in NB13 using `numpy.random.default_rng(0)`
- **Format:** Simulated sequencing reads at a single SNP locus
- **Fetch:** Run NB13 — no download required

---

## Gitignore

```
datasets/raw/
datasets/processed/*.tsv
```

Processed notebooks always regenerate from scripts, not from committed data files.
