# Module 04 — Assignments

## A01 — PCA Implementation Audit

**Linked to:** NB05 and NB09  
**Due:** Before NB10 (module assessment)

Implement PCA entirely from scratch — no `sklearn`, no `scipy.linalg.svd` shortcuts.
Your implementation must:

1. Center the data matrix (subtract column means)
2. Compute the sample covariance matrix
3. Compute eigendecomposition using `np.linalg.eig`
4. Sort eigenpairs by descending eigenvalue
5. Project data onto top-k eigenvectors
6. Return explained variance ratios

Validate your output against `sklearn.decomposition.PCA(n_components=k)` on the
same dataset — PC scores must agree up to sign (PCs are defined up to sign flip).

**Deliverable:** A runnable notebook cell with `def pca_from_scratch(X, n_components)`,
its validation, and one paragraph explaining why PCA maximizes variance.
