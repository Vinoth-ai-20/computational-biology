# Module 10 — Roadmap

**Tier 2 — Working competence | 12 notebooks | Weeks 20–26**

---

## Part 1 — Single-Cell RNA-seq: From Technology to Data

### NB01 — Why Single-Cell? Technology and Data Shape
Bulk vs. single-cell transcriptomics; 10x Genomics droplet microfluidics; UMI counts
vs. read counts; the cell-by-gene count matrix; key technical limitations (dropout,
doublets, ambient RNA).

### NB02 — scRNA-seq Quality Control and Cell Filtering
Per-cell QC metrics: total counts, n_genes, mitochondrial fraction; threshold-based
filtering; the mitochondrial fraction criterion; MAD-based adaptive thresholds;
doublet detection concepts (scrublet, DoubletFinder); AnnData structure.

### NB03 — Normalization and Log-Transformation
Why raw UMI counts need normalization; library-size normalization (per-cell total
scaling to 10,000); log1p transformation; HVG (highly variable gene) selection;
scran pooling-based normalization concept.

---

## Part 2 — Dimensionality Reduction

### NB04 — PCA for Single-Cell Data
Why PCA before UMAP; number of PCs to retain (elbow plot, variance explained);
batch effects visible in PCA; scaling before PCA; `scanpy.pp.pca()` internals.

### NB05 — UMAP and t-SNE Visualization
How UMAP works conceptually (graph construction + layout optimization); what UMAP
preserves vs. distorts; t-SNE comparison; perplexity/n_neighbors parameter effects;
the nearest-neighbor graph (kNN-graph) as the shared foundation.

---

## Part 3 — Clustering and Annotation

### NB06 — Clustering: Leiden and Louvain Algorithms
Graph-based clustering on the kNN-graph; modularity optimization; Leiden vs. Louvain;
resolution parameter and its effect on cluster granularity; cluster stability.

### NB07 — Marker Gene Identification and Cell Type Annotation
Wilcoxon rank-sum test for marker genes; log2 fold-change and p-value filtering;
cell type annotation from marker genes; reference-based vs. manual annotation;
`scanpy.tl.rank_genes_groups()`; dot plots and violin plots for marker visualization.

---

## Part 4 — Advanced scRNA-seq Concepts (survey)

### NB08 — Trajectory and Pseudotime Analysis (Survey)
RNA velocity concept; pseudotime ordering; Monocle/scVelo at usage level; when
trajectory analysis is appropriate; limitations of pseudotime.

---

## Part 5 — Proteomics

### NB09 — Mass Spectrometry Proteomics: Data Shape and Concepts
Shotgun proteomics workflow (digestion → LC-MS/MS → database search); the protein
identification pipeline; PSM (peptide-spectrum match); FDR control via target-decoy;
the protein-by-sample quantification matrix shape.

### NB10 — Protein Quantification Methods
Label-free quantification (LFQ): spectral counting, intensity-based (MaxLFQ);
isobaric labelling (TMT, iTRAQ): multiplexing, ratio distortion; MS1 vs. MS2
quantification; missing values in proteomics and imputation strategies.

---

## Part 6 — Multi-Omics and Integration

### NB11 — Multi-Omics Integration: Concepts and Survey
Why integrate? The central dogma re-examined; correlation of mRNA and protein levels;
late integration vs. early integration vs. model-based integration; MOFA+, Seurat v5
WNN; the difficulty of causal inference across omics layers.

---

## Part 7 — Portfolio and Assessment

### NB12 — Mini Project + Module Assessment
Synthetic scRNA-seq dataset walkthrough: simulate → QC → normalize → PCA → UMAP →
cluster → annotate → marker genes → 4-panel portfolio figure.
Assessment: 50-point gate (40/50 = 80%).
