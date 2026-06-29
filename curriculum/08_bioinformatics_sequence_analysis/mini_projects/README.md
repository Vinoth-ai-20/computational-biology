# Module 08 — Mini Projects

---

## MP01 — NW+SW from Scratch vs. Biopython Benchmark

**Portfolio artifact:** `portfolio/module08_nw_sw_benchmark.png`

**Goal:** Validate your from-scratch NW and SW implementations against Biopython's
`Bio.Align.PairwiseAligner`. Produce a 4-panel figure:
- Panel A: Example NW alignment (two sequences), score and aligned strings annotated
- Panel B: Example SW alignment — show which subsequence is found
- Panel C: Score comparison: your NW vs. Biopython NW across 50 sequence pairs (scatter)
- Panel D: Runtime scaling: O(n²) validation for both algorithms

**Implementation rules:**
- All alignment functions written from memory; no copying from NB04/NB05
- Biopython used only for validation, not as the primary implementation
- 95% of test cases must match Biopython's score (tolerance for traceback tie-breaking)

---

## MP02 — Phylogenetics Pipeline on Real Data

**Portfolio artifact:** `portfolio/module08_phylogenetics_pipeline/`

**Goal:** An end-to-end reproducible pipeline:
1. Fetch sequences from NCBI (beta-globin or SARS-CoV-2 spike, 5–8 sequences)
2. Align with MAFFT (external tool; document exact command and version)
3. Compute pairwise distance matrix (JC or K2P, from scratch)
4. Build NJ tree (from scratch)
5. Produce a publication-ready annotated tree figure

**Output files:**
- `pipeline/sequences.fasta` — raw sequences
- `pipeline/alignment.fasta` — MAFFT output
- `pipeline/distance_matrix.csv` — computed distances
- `pipeline/nj_tree.newick` — NJ tree in Newick format
- `pipeline/figure.png` — the portfolio figure

**Implementation rules:**
- Distance and NJ code written from scratch (not from Biopython phylo module)
- MAFFT is the only external tool allowed; all other steps are Python
- Reproducibility: `pipeline/README.md` contains exact MAFFT command and version
