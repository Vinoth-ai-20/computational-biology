# Module 13 — Mini Projects

## MP01 — Cancer Subtype Classification (Portfolio artifact)

**Portfolio artifact:** `portfolio/module13_cancer_classification.png`

**Goal:** End-to-end ML pipeline for multi-class cancer subtype classification from
simulated RNA-seq data resembling TCGA.

**Steps:**
1. Generate synthetic data: 500 samples × 2000 genes, 5 cancer subtypes with planted
   differential expression signal + biological noise (batch effects, dropout)
2. Preprocessing: log1p normalization, MAD-based feature selection (retain top 200 genes)
3. Dimensionality reduction: PCA to 50 components (from scratch via SVD)
4. Model comparison with stratified 5-fold CV:
   - Logistic Regression (L2, sklearn)
   - Random Forest (100 trees, sklearn)
   - SVM (RBF kernel, sklearn)
5. Evaluation: confusion matrix, per-class F1, macro-F1, ROC-AUC
6. Interpretability: top-20 feature importance genes (RF); biologically plausible?
7. Portfolio figure (4 panels):
   - Panel A: PCA plot colored by true subtype
   - Panel B: Confusion matrix (best model)
   - Panel C: ROC curves per class (one-vs-rest)
   - Panel D: Top-20 feature importance (bar chart)

**Implementation rules:**
- Data generation, PCA, metrics: from scratch
- Model training + CV: scikit-learn
- Feature importance: sklearn RF `.feature_importances_`

---

## MP02 — Drug-Target Binding Prediction

**Portfolio artifact:** `portfolio/module13_drug_target.png`

**Goal:** Binary classification — does a (drug, protein) pair bind?

**Steps:**
1. Generate feature-engineered dataset: 1000 pairs, features = molecular weight, logP,
   number of rotatable bonds, protein length, presence of known binding domain (5 features)
2. Class imbalance: 20% binders, 80% non-binders — apply class weighting
3. Model comparison: SVM (RBF), Random Forest, Logistic Regression
4. Nested CV: outer 5-fold for evaluation; inner 3-fold for hyperparameter selection
5. Evaluation: AUROC, AUPRC, F1 at optimal threshold
6. Portfolio figure: ROC and PR curves for all three models

**Implementation rules:**
- All metrics computed from scratch
- sklearn for model training only
