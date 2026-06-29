# Datasets — Module 01: Python & Scientific Computing

## Raw datasets (not committed — fetched via scripts)

| Dataset | Source | Accession | Purpose | Fetch script |
|---------|--------|-----------|---------|--------------|
| GEO expression matrix (6–12 samples) | NCBI GEO | TBD | Assignment A01 — expression pipeline | `scripts/fetch_geo_dataset.py` |
| Gene family FASTA | NCBI Entrez | NM_007294.4 (BRCA1) | NB16 Biopython exercise | `scripts/fetch_brca1_fasta.py` |

Raw data files are gitignored. To reproduce:

```bash
python scripts/fetch_geo_dataset.py
python scripts/fetch_brca1_fasta.py
```

## Processed datasets (committed, small)

| File | Source | Notes |
|------|--------|-------|
| `processed/synthetic_clean.csv` | Generated in NB09 | Cleaned synthetic expression matrix |

## Data policy

- Never commit raw GEO or NCBI files (can be large and have usage terms)
- Always document accession numbers so data can be re-fetched
- Processed/synthetic files may be committed if < 1 MB
