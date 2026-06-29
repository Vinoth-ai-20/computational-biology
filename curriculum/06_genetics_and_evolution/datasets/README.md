# Module 06 — Datasets

| ID | Name | Source | Size | Use |
|----|------|--------|------|-----|
| DS01 | Synthetic WF populations | Generated in NB04/NB11 | In-memory | Drift + selection simulations |
| DS02 | Synthetic genealogies | Generated in NB05 | In-memory | Coalescent simulations |
| DS03 | Primate cytochrome b alignment | NCBI (public) | ~10 sequences × 1140 bp | NB06 phylogenetics demo |
| DS04 | Human population allele frequencies | 1000 Genomes summary stats (public) | Small table | NB04 real-world drift example |
| DS05 | Hawk-Dove payoff matrices | Synthetic | In-memory | NB09 game theory |

## Notes

- DS03 is freely available from NCBI GenBank (accession numbers in datasets/ subfolder)
- DS04 uses only summary statistics (allele frequencies) — no individual-level genotypes
- All simulation data is generated with `numpy.random.default_rng(seed)` for full reproducibility
