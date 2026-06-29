# Module 07 — Datasets

All datasets are either synthetic (generated in-notebook) or fetched via script.
No raw data files are committed to the repository (gitignored).

| ID | Dataset | Source | Used in | Fetch command |
|----|---------|--------|---------|---------------|
| DS01 | Synthetic enzyme kinetics data (Vmax=10, Km=2, + noise) | Generated in NB03 | NB03, NB08 | `numpy.random` — no fetch needed |
| DS02 | BRENDA enzyme kinetics example (lactate dehydrogenase) | BRENDA (brenda-enzymes.org) | NB03 | Manual download from BRENDA |
| DS03 | Human proteome amino acid composition | UniProt FASTA (reviewed, human) | NB02 | `scripts/fetch_uniprot_human.py` |
| DS04 | Simulated Western blot intensity data | Generated in NB07 | NB07 | `numpy.random` — no fetch needed |
| DS05 | PhosphoSitePlus top-10 phosphosites for EGFR | PhosphoSitePlus export | NB06 | Manual export from phosphosite.org |

---

## Notes on data ethics

- UniProt data is freely available under CC BY 4.0.
- BRENDA requires registration; do not redistribute raw BRENDA data in the public repo.
- PhosphoSitePlus data is free for academic use; cite the database in any publication.
