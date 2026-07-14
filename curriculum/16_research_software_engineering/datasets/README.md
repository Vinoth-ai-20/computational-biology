# Module 16 — Datasets

This module uses **synthetic data and example biological sequences only**. No external datasets are required, and there are no large downloads needed to run the notebooks.

## Synthetic data used across notebooks

| Notebook | Data type | Generation method |
|---|---|---|
| NB01–NB07 | Short DNA sequences (10–100 bp) | Randomly generated in-notebook with `numpy.random` |
| NB08 | DNA sequences (100–10,000 bp) for ORF finding | Generated with `numpy.random`, codon-aware for ORF testing |
| NB09 | RNA-seq-like count matrices (100 genes × 20 samples) | Generated with `numpy.random.negative_binomial` |
| NB10 | FASTA and FASTQ files | Written to `tmp/` by notebook code, not committed |
| NB11 | None — packaging workflow only | N/A |
| NB12 | Reuses NB08–NB10 synthetic data | N/A |

## Notes

- All randomly generated data uses a fixed seed (`numpy.random.default_rng(42)`) so notebooks are reproducible.
- Synthetic FASTA/FASTQ files are written to a temporary directory and deleted at the end of each notebook run — they are not committed to the repository.
- If you wish to test with real biological sequences, any standard FASTA file works with the `compbio_utils.io` module. NCBI E-utilities or Biopython's `Entrez` interface can fetch sequences; see Module 08 (Bioinformatics Sequence Analysis) for examples.
