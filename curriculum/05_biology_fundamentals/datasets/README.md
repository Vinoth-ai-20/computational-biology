# Module 05 — Datasets

## DS01 — Synthetic population genetics data (generated in-notebook)

| Field | Value |
|-------|-------|
| Source | `numpy.random.default_rng` — generated in NB06, NB07, NB08 |
| Content | Allele frequency trajectories under drift and selection |
| Git status | Not stored; regenerated from fixed seed |

## DS02 — Human genetic code table

| Field | Value |
|-------|-------|
| Source | Standard NCBI codon table (built into Biopython) |
| Used in | NB03 — translate synthetic mRNA sequences |
| Git status | Not stored — accessed via `Bio.Data.CodonTable` |

## DS03 — Example genome-scale statistics (Ensembl / NCBI)

| Field | Value |
|-------|-------|
| Source | Ensembl species statistics (https://www.ensembl.org/info/about/species.html) |
| Content | Genome size, gene count, GC content for 10 reference species |
| Used in | NB04 — genome scale visualization |
| Git status | Small lookup table embedded in notebook |

## DS04 — 1000 Genomes allele frequency data (optional)

| Field | Value |
|-------|-------|
| Source | 1000 Genomes Project (https://www.internationalgenome.org/) |
| Content | Allele frequencies for HWE testing |
| Used in | NB06 (optional — real data for HWE test) |
| Git status | Gitignored — download instructions in NB06 |

## DS05 — Example phylogenetic tree (Newick format)

| Field | Value |
|-------|-------|
| Source | TimeTree database or NCBI Taxonomy |
| Content | Primate phylogeny in Newick format |
| Used in | NB09 |
| Git status | Small text file — can be stored directly in notebook |
