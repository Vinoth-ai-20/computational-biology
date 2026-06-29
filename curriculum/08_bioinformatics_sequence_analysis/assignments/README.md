# Module 08 — Assignments

## A01 — Alignment Algorithm Comparison

Implement NW and SW from scratch (without referencing notebooks). Run both on the
same pair of sequences and compare: alignment score, aligned strings, positions of
gaps. Explain in writing why the SW result is a subset of the NW alignment space.
Time both implementations on sequences of length 50, 200, 500, 1000 bp. Plot
runtime vs. sequence length and characterise the scaling (O(n²) expected).

## A02 — BLAST Parameter Sensitivity Analysis

Using NCBI BLAST+ command-line tools (or the web interface), run blastp for the
human KRAS protein (NP_203524.1) against the nr database. Then repeat with:
(a) word size W=2 instead of default W=3
(b) E-value threshold 0.001 instead of default 10
(c) BLOSUM45 instead of BLOSUM62

For each change: how many hits are returned? How does the top hit's score change?
Write a 1-paragraph interpretation of each parameter's effect.

## A03 — Real Phylogenetics Analysis

Using the beta-globin gene sequences from DS03:
1. Align with MAFFT (local install or web)
2. Compute pairwise JC distances from the alignment
3. Build NJ and UPGMA trees from the distance matrix
4. Compare the two topologies — do they agree on the human-chimp-gorilla relationship?
5. Produce a single figure with both trees side by side, branch lengths annotated
