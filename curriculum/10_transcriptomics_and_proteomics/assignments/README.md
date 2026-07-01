# Module 10 — Assignments

## A01 — Real scRNA-seq Dataset Analysis (PBMC 3k)
Download the 10x PBMC 3k dataset. Run the full scanpy pipeline:
1. Load with `scanpy.read_10x_mtx()`
2. QC filtering (mitochondrial %, n_genes, total_counts)
3. Normalize, log-transform, HVG selection
4. PCA → kNN graph → UMAP → Leiden clustering
5. Find marker genes per cluster with `scanpy.tl.rank_genes_groups()`
6. Annotate at least 4 cell types using known PBMC markers

Submit: working notebook + UMAP plot colored by cluster + cell type annotation table.

## A02 — Proteomics Differential Abundance
Using the synthetic DS03 dataset (or a public MaxQuant proteinGroups.txt from PRIDE):
1. Load and parse the protein intensity matrix
2. Log2-transform + median normalization
3. Impute missing values (MinProb or KNN)
4. Run a t-test (treated vs. control) for each protein
5. Apply BH correction
6. Produce a volcano plot of differential abundance

Submit: working Python notebook + volcano plot + 1-paragraph interpretation.
