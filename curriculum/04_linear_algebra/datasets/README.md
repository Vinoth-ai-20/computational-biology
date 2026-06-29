# Module 04 — Datasets

## DS01 — Synthetic expression matrix (generated in-notebook)

| Field | Value |
|-------|-------|
| Source | `numpy.random.default_rng` — generated in NB02, NB04, NB05 |
| Size | 500 genes × 50 samples |
| Structure | 3 hidden PCs (cell types) + noise |
| License | N/A — synthetic |
| Git status | Not stored; regenerated from fixed seed |

## DS02 — NCI-60 expression data (fetched)

| Field | Value |
|-------|-------|
| Source | NCI-60 DTP open data portal |
| Accession | Available via `rcellminer` R package or direct download |
| Size | ~60 cell lines × ~17,000 genes |
| Used in | NB09 (mini-project PCA) |
| License | Public domain (NCI) |
| Git status | Gitignored — fetch via `scripts/fetch_nci60.py` |

## DS03 — Any GEO expression matrix (fallback for NB09)

| Field | Value |
|-------|-------|
| Source | NCBI GEO — any accession with ≥30 samples and ≥2 groups |
| Suggested | GSE2034 (already used in Module 03) or GSE19188 |
| Used in | NB09 |
| Git status | Gitignored — fetch via GEOparse |

## Fetch instructions

```bash
# Synthetic datasets: generated in-notebook, no fetch needed

# NCI-60 (optional — Python):
python scripts/fetch_nci60.py

# GEO fallback:
pip install GEOparse
python -c "import GEOparse; GEOparse.get_GEO('GSE2034', destdir='curriculum/04_linear_algebra/datasets/raw/')"
```
