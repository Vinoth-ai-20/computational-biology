# Module 04 — Linear Algebra

**Tier:** 2 — Working competence  
**Week budget:** Weeks 3–9 (parallel with Modules 01, 03, 05)  
**Notebooks:** 10  
**Portfolio artifact:** `portfolio/module04_pca_expression_analysis.png`

## Objectives

By the end of this module you can:
- Represent biological data as matrices and reason about their structure
- Implement PCA from scratch using eigendecomposition and SVD
- Apply PCA to real expression data and interpret the result biologically
- Understand SVD as the general form of PCA and matrix factorization
- Formulate linear regression as a linear algebra problem (Normal equations)
- Construct and interpret graph Laplacians for network analysis

## Why this helps Track A

PCA on expression data is a practical task in almost every RA/bioinformatics role —
"plot a PCA of these samples" is a first-day task. Being able to explain *what PCA
computes* (not just call `sklearn.decomposition.PCA`) separates strong candidates.

## Why this helps Track B

Linear algebra is the mathematical substrate of dimensionality reduction, gene
regulatory network analysis, and every ML method downstream (Modules 13–14).
European PhD supervisors at EMBL/IMPRS expect quantitative fluency at this level.

## Module structure

```
04_linear_algebra/
├── README.md          ← this file
├── roadmap.md         ← notebook sequence
├── references.md      ← books, software, researchers
├── papers.md          ← key papers with Three-Pass tracking
├── notebooks/         ← 10 lecture notebooks
├── exercises/         ← posed problems, one file per notebook
├── assignments/       ← A01: PCA implementation audit
├── mini_projects/     ← MP01: PCA on public expression data
└── datasets/          ← synthetic + fetched expression data
```

## Depth-tier standard (Tier 2 — Working competence)

Can use standard tools correctly, explain what they do and why, and recognise
when something looks wrong. Full derivations from axioms are not required.
The implementation bar: PCA from scratch using `np.linalg.eig` / `np.linalg.svd`,
validated against `sklearn`, with a biological interpretation of the result.
