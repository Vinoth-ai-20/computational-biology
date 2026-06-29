# Module 08 — Datasets

| ID | Dataset | Source | Used in | Notes |
|----|---------|--------|---------|-------|
| DS01 | Synthetic short sequences for alignment exercises | Generated in-notebook | NB03–NB07 | No fetch needed |
| DS02 | BLOSUM62 matrix | NCBI / Biopython | NB06 | Available via `Bio.Align.substitution_matrices` |
| DS03 | Beta-globin gene family (human, chimp, gorilla, mouse, zebrafish) | NCBI GenBank (accession numbers in NB17) | NB17 | Fetch via Biopython Entrez; ~2 kb each |
| DS04 | SARS-CoV-2 spike protein sequences (5 variants) | NCBI SARS-CoV-2 database | NB17 alternative | Small, current, high interest |
| DS05 | Rosalind sample datasets | rosalind.info | NB15 | Download from problem pages |

---

## Fetch instructions

```bash
# DS03: Beta-globin sequences (NB17)
python scripts/fetch_betoglobin.py
# Uses Biopython Entrez: NM_000518 (human), XM_003316112 (gorilla), etc.

# DS04: SARS-CoV-2 spikes
python scripts/fetch_sarscov2_spikes.py
# From NCBI Virus database: NC_045512, MN908947, etc.
```

Raw fetched sequences go in `datasets/raw/` (gitignored).
Processed alignments go in `datasets/processed/`.
