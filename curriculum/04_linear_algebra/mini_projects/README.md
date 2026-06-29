# Module 04 — Mini-Projects

## MP01 — PCA on a Public Expression Dataset (NB09)

**Portfolio artifact:** `portfolio/module04_pca_expression_analysis.png`

**Goal:** Apply PCA from scratch to a real expression dataset and produce a
publication-quality analysis figure that can be linked in a Track A application.

**Requirements:**

1. Load a real public dataset (NCI-60 or a GEO series with ≥30 samples, ≥2 groups)
2. Normalize: log2(CPM + 1) or use provided normalized values
3. Filter: retain top 5,000 most-variable genes (by variance)
4. Center the data matrix
5. Run PCA from scratch (`np.linalg.eig` or `np.linalg.svd`)
6. Produce the following figure panels:
   - Panel A: Scree plot (explained variance per PC, cumulative)
   - Panel B: PC1 vs. PC2 scatter, colored by sample group / tissue
   - Panel C: Top 20 gene loadings on PC1 and PC2 (biplot-style)
   - Panel D: Heatmap of PC scores across samples
7. Write a 3-sentence biological interpretation of PC1 and PC2

**Pass standard:** All 4 panels present, labeled, interpretable. PCA validated
against sklearn. Biological interpretation is specific, not generic.
