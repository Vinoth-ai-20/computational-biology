# Module 04 — Linear Algebra: Roadmap

**Tier 2 — Working competence | 10 notebooks**

## Part 1 — Foundations (NB01–NB03)

- [ ] **NB01** `01_why_linear_algebra_for_biology.ipynb`  
  Motivating cases: PCA on expression data, adjacency matrices for gene networks,
  linear regression for eQTL. Why matrices are the right data structure for genomics.

- [ ] **NB02** `02_vectors_dot_products_norms.ipynb`  
  Vectors as gene expression profiles. Dot product as similarity. L1/L2/infinity norms.
  Cosine similarity for gene co-expression. Angle between expression vectors.

- [ ] **NB03** `03_matrices_and_matrix_multiplication.ipynb`  
  Matrix as a linear transformation. Matrix multiplication by hand and via NumPy.
  Transpose, inverse, identity. Rank and nullspace (intuition). Solving Ax=b.

## Part 2 — Core Decompositions (NB04–NB06)

- [ ] **NB04** `04_eigenvalues_and_eigenvectors.ipynb`  
  Geometric intuition: eigenvectors are directions a transformation doesn't rotate.
  Power iteration from scratch. Characteristic polynomial. Spectral decomposition.
  Covariance matrix eigenvectors = directions of maximum variance.

- [ ] **NB05** `05_pca_from_first_principles.ipynb`  
  PCA derivation: maximize variance → eigendecomposition of covariance matrix.
  Implementation from scratch with `np.linalg.eig`. Validation against `sklearn.decomposition.PCA`.
  Explained variance ratio. Scree plot. Interpreting PC scores biologically.

- [ ] **NB06** `06_svd_and_connection_to_pca.ipynb`  
  SVD: X = UΣVᵀ — factoring any matrix into rotation × scaling × rotation.
  PCA via SVD: right singular vectors = principal components.
  Low-rank approximation: image compression analogy, then gene expression matrix compression.
  Frobenius norm approximation error vs. rank k.

## Part 3 — Applications (NB07–NB08)

- [ ] **NB07** `07_matrices_as_graphs_adjacency_laplacian.ipynb`  
  Adjacency matrix of a gene regulatory network. Degree matrix. Graph Laplacian L = D − A.
  Laplacian eigenvectors = spectral clustering. Fiedler vector for community detection.
  Protein-protein interaction network example with NetworkX.

- [ ] **NB08** `08_linear_regression_as_linear_algebra.ipynb`  
  OLS: minimizing ‖y − Xβ‖² → Normal equations β = (XᵀX)⁻¹Xᵀy.
  Geometric interpretation: projection onto column space.
  Condition number and numerical stability. QR decomposition as stable solver.
  Ridge regression: β = (XᵀX + λI)⁻¹Xᵀy — shrinkage as regularization.

## Part 4 — Integration and Assessment (NB09–NB10)

- [ ] **NB09** `09_mini_project_pca_expression_data.ipynb`  
  **Portfolio artifact.** PCA on real public expression data (GEO or TCGA subset).
  Full pipeline: load → normalize → center → decompose → visualize → interpret.
  Biplot, sample clustering in PC space, loadings heatmap.
  Saved to `portfolio/module04_pca_expression_analysis.png`.

- [ ] **NB10** `10_module_assessment.ipynb`  
  **Pass gate: ≥32/40 (80%).**  
  Section A: conceptual (12 pts) — PCA, SVD, eigenvalues, graph Laplacian.  
  Section B: implementation (20 pts) — PCA from scratch, SVD factorization, OLS.  
  Section C: mock interview (8 pts) — "explain PCA to a biologist."
