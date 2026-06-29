# Module 08 — Bioinformatics: Sequence Analysis

**Depth tier:** Tier 1 — Master  
**Week budget:** Weeks 10–18 (parallel with Modules 06 and 07 early on)  
**Notebooks:** 18  
**Status:** ⏳ Not started

---

## Motivation

This is **the** canonical bioinformatics module. "How does BLAST work?" is a documented,
recurring interview question for every RA/JRF/Bioinformatics Engineer role surveyed in
the Track A research. Needleman-Wunsch and Smith-Waterman are the algorithmic core of
molecular biology's most important computational tool. If you can implement both from
scratch, explain every design decision, and correctly interpret a BLAST output — you
have answered the core competency question for most Track A interviews.

---

## Depth tier — what Tier 1 means here

- Can implement NW, SW, and the conceptual BLAST algorithm from scratch
- Can explain the E-value calculation and why it matters
- Can run a real alignment pipeline (MAFFT → NJ tree) on a public dataset
- Can produce a portfolio-quality phylogenetics figure
- Can answer "how does BLAST work?" in an interview in 3 minutes, correctly

---

## Track A relevance

**Tier 1 interview coverage:** The following documented bioinformatics interview questions
are directly addressed by this module:
- "How does BLAST work?" (k-mer seeding + ungapped/gapped extension + statistics)
- "What is the difference between global and local alignment?"
- "What is a BLOSUM matrix and what does it encode?"
- "How do you interpret an E-value?"
- "What is the difference between UPGMA and Neighbour-Joining?"

## Track B relevance

Sequence alignment is the foundation of comparative genomics, phylogenetics, and variant
calling — all of which appear in every computational biology PhD research group. A
working knowledge of NW/SW/BLAST is assumed in Module 09 (NGS), Module 13 (ML for
biology), and Module 20 (Capstone).

---

## Portfolio artifacts

1. `portfolio/module08_nw_sw_benchmark.png` — NW vs. SW comparison + Biopython validation
2. `portfolio/module08_phylogenetics_pipeline/` — A complete pipeline on a real gene family:
   sequences → MAFFT alignment → distance matrix → NJ tree → annotated figure
