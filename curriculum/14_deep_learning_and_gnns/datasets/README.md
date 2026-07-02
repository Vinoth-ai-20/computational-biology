# Module 14 — Datasets

All datasets in this module are synthetic (generated in-notebook) or fetched via script.
No copyrighted datasets are committed to the repository.

| ID | Name | Source | Size | Used in | Notes |
|---|---|---|---|---|---|
| DS01 | TF binding sequences (synthetic) | Generated in-notebook | 1,000 sequences × 30 nt | NB03, NB10, NB12, MP01 | Same motif structure as Module 13 NB13 |
| DS02 | Synthetic scRNA-seq (5 cell types) | Generated in-notebook | 500 cells × 1000 genes | NB06 | Negative binomial counts, planted cell-type markers |
| DS03 | PPI graph (synthetic, BA model) | Generated in-notebook | 300 nodes, ~900 edges | NB07 | Same as Module 12 NB07 |
| DS04 | Molecular drug properties (synthetic) | Generated in-notebook | 500 molecules × 15 features | NB08 | Simulates logP, MW, solubility prediction |
| DS05 | Protein sequences + Tm (optional, real) | UniProt/ProThermDB | ~100 proteins | NB11 | Download via `scripts/fetch_protherm.py`; fallback: synthetic |
| DS06 | ChIP-seq peaks (optional, real) | ENCODE portal | Variable | A01 | Use CTCF ChIP-seq, hg38, chr1; fallback: DS01 |

## Fetching optional datasets

```bash
# DS05: Thermostability data
python scripts/fetch_protherm.py --output datasets/processed/protherm_subset.csv

# DS06: CTCF ChIP-seq peaks (requires ENCODE API key)
python scripts/fetch_encode_peaks.py --experiment ENCSR000EGM --output datasets/raw/ctcf_peaks/
```
