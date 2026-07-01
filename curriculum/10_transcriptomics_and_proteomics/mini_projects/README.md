# Module 10 — Mini Projects

## MP01 — Synthetic scRNA-seq Walkthrough (Portfolio artifact)

**Portfolio artifact:** `portfolio/module10_singlecell_walkthrough.png`

**Goal:** Complete end-to-end scRNA-seq analysis pipeline on a simulated dataset
where the ground-truth cluster identities are known.

**Steps:**
1. Simulate 400 cells with 4 known cell types (100 cells each), 1500 genes
2. Apply QC filtering (mitochondrial %, total counts, n_genes)
3. Normalize to 10,000 counts per cell + log1p
4. Select top 200 highly variable genes
5. Run PCA (50 components)
6. Build kNN graph + UMAP layout
7. Leiden clustering (resolution sweep: 0.3, 0.5, 0.8)
8. Identify marker genes per cluster (Wilcoxon test)
9. Annotate clusters against known ground truth

**4-panel figure:**
- Panel A: QC metrics (violin plots: total_counts, n_genes, pct_mito)
- Panel B: PCA (PC1 vs PC2, colored by true cell type)
- Panel C: UMAP (colored by Leiden cluster label)
- Panel D: Dot plot of top 3 marker genes per cluster

**Implementation rules:**
- QC filtering, normalization, HVG selection implemented from scratch (numpy)
- PCA from scratch (Module 04 callback: `np.linalg.svd`)
- UMAP/Leiden via `umap-learn` and `leidenalg` (tool-usage level is correct for Tier 2)
- Portfolio figure saved to `portfolio/module10_singlecell_walkthrough.png`
