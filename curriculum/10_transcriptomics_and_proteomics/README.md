# Module 10 — Transcriptomics and Proteomics

**Depth tier:** Tier 2 — Working competence  
**Week budget:** Weeks 20–26 (parallel with Module 12 start)  
**Notebooks:** 12  
**Assessment gate:** 40/50 points (80%)

---

## Motivation

Module 09 covered bulk RNA-seq. This module extends into **single-cell RNA-seq** (scRNA-seq)
— the dominant transcriptomics paradigm since 2015 — and introduces **mass-spectrometry
proteomics**. At Tier 2, the goal is tool fluency and conceptual literacy, not derivation
from first principles: you should be able to run a scanpy pipeline, explain every step,
and interpret the outputs, without needing to re-implement the underlying algorithms.

---

## Track A relevance

Single-cell analysis skills appear directly in 2026 India bioinformatics postings.
Knowing what `scanpy.tl.umap()` does (and what it cannot do) is a real interview
differentiator. Proteomics literacy is expected for any computational biology RA role
adjacent to mass-spec or drug-discovery labs.

## Track B relevance

Single-cell genomics is an explicit theme in EMBL EIPP, IMPRS-BAC, and most systems-
biology PhD programmes. A scanpy portfolio piece signals this literacy concisely.

---

## Portfolio artifact

`portfolio/module10_singlecell_walkthrough.png` — 4-panel figure from a synthetic
scRNA-seq dataset: QC metrics, PCA, UMAP with cluster labels, and top marker genes.

---

## Tool overview

| Tool | Purpose |
|------|---------|
| scanpy | Python scRNA-seq analysis framework (AnnData-based) |
| anndata | HDF5-backed data structure for annotated matrices |
| umap-learn | UMAP dimensionality reduction |
| leidenalg | Leiden community detection for cell clustering |
| matplotlib/seaborn | Visualization |

---

## Notebook sequence

See [roadmap.md](roadmap.md) for the full ordered list.

---

## Why Tier 2, not Tier 1

Deriving graph-Laplacian spectral methods or re-implementing Leiden from scratch
would take 4–6 weeks of Tier-1 depth. The 12-month box does not support that cost
here: the leverage point is tool fluency + conceptual literacy, which reaches
working competence in 6–8 weeks at this tier.
