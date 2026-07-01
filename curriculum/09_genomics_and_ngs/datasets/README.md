# Module 09 — Datasets

| ID | Dataset | Source | Used in | Notes |
|----|---------|--------|---------|-------|
| DS01 | Synthetic paired-end FASTQ reads | Generated in NB14 | NB02, NB14 | Simulated from a 1000 bp reference with known variants |
| DS02 | Synthetic SAM file | Generated in NB04–NB05 | NB04, NB05, NB06 | 20 reads aligned to a 500 bp reference, includes duplicates |
| DS03 | Synthetic VCF file | Generated in NB09 | NB09 | 50 synthetic variants with INFO/FORMAT fields |
| DS04 | Synthetic RNA-seq count matrix | Generated in NB15 | NB11, NB12, NB15 | 200 genes × 6 samples (3 control, 3 treatment), 50 DE genes |
| DS05 | Real: NA12878 chr22 subset | GIAB / 1000 Genomes | NB14 (optional) | Validated variant set; download instructions in NB14 |
| DS06 | Real: ENCODE RNA-seq counts | ENCODE portal | NB15 (optional) | Public GM12878 RNA-seq, gene-level counts |

## Fetch instructions

```bash
# DS05: NA12878 chr22 (GIAB truth set — for advanced NB14 extension)
# ~2 GB; only fetch if running the optional GATK validation section
wget https://storage.googleapis.com/genomics-public-data/references/hg38/v0/Homo_sapiens_assembly38.fasta.gz

# DS06: ENCODE RNA-seq (optional extension for NB15)
# Download from: https://www.encodeproject.org/files/ENCFF779XGY/
# Use Biopython/wget; file is a TSV of gene counts
```

All synthetic datasets are generated within the notebooks; no download needed for core
exercises.
