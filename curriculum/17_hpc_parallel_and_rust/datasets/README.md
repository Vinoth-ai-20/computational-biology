# Module 17 — Datasets

All datasets used in this module are either synthetically generated in-notebook or fetched by a script. No large files are committed to the repository.

## Synthetic datasets (generated in-notebook)

| Dataset | Generated in | Description |
|---------|-------------|-------------|
| Random DNA sequences (N×L array) | NB01, NB02, NB04, NB11, NB12 | `np.random.choice(['A','T','C','G'], size=(N,L))` — seeded for reproducibility |
| Simulated RNA-seq count matrices | NB03 | Negative binomial counts, 200 genes × 50 samples |
| Synthetic signal (sliding window) | NB01, NB03, NB04 | Gaussian noise + sinusoidal signal, 10M elements |
| Synthetic FASTA file | NB06, NB09 | 1000-sequence FASTA, generated with `scripts/generate_synthetic_fasta.py` |
| Gene expression TSV | NB03 | 10,000 genes × 100 samples, random floats |

## Real reference datasets (fetched by script, not committed)

These are placed in `datasets/raw/` which is gitignored.

| Dataset | Source | Fetch command |
|---------|--------|--------------|
| E. coli K-12 genome (FASTA) | NCBI RefSeq NC_000913.3 | `scripts/fetch_ecoli_genome.sh` |
| Human chromosome 22 (FASTA) | UCSC hg38 | `scripts/fetch_chr22.sh` |

## Directory layout

```
datasets/
├── README.md            ← this file
├── raw/                 ← gitignored; populated by fetch scripts
│   ├── ecoli_k12.fasta
│   └── chr22.fa
└── processed/           ← gitignored; produced by pipeline notebooks
    └── .gitkeep
```

## Reproducibility note

Every notebook that uses data begins with a seed-setting cell:
```python
import numpy as np
np.random.seed(42)
```
This ensures that synthetic datasets are identical across runs and across machines.
