# Module 13 — Roadmap

## Part 1: Foundations and the ML Pipeline (NB01–NB03)
1. `01_what_is_machine_learning_and_the_ml_pipeline.ipynb` — supervised vs unsupervised, the bias-variance tradeoff, overfitting, the no-free-lunch theorem; biology-specific challenges (high-dimensional, small-n, batch effects, class imbalance)
2. `02_linear_regression_from_scratch.ipynb` — OLS derivation, normal equations, gradient descent, regularization (Ridge/Lasso), geometric interpretation, assumptions and diagnostics; application: gene expression dose-response
3. `03_logistic_regression_from_scratch.ipynb` — sigmoid, cross-entropy loss, gradient descent, Newton's method, L1/L2 regularization, decision boundary; application: binary cancer classification

## Part 2: Core Classifiers (NB04–NB07)
4. `04_decision_trees_and_random_forests.ipynb` — information gain (entropy), Gini impurity, recursive splitting, pruning; bagging, feature importance; application: clinical feature classification
5. `05_support_vector_machines.ipynb` — maximum margin hyperplane, support vectors, soft margin, kernel trick (RBF, polynomial); dual problem intuition; application: protein sequence classification
6. `06_k_nearest_neighbors_and_naive_bayes.ipynb` — kNN distance metrics, curse of dimensionality, vote aggregation; Gaussian/Bernoulli Naive Bayes, independence assumption; application: cell-type annotation
7. `07_ensemble_methods_gradient_boosting.ipynb` — bagging vs boosting, AdaBoost, gradient boosting (GBDT), XGBoost overview; application: variant pathogenicity prediction

## Part 3: Model Evaluation and Selection (NB08–NB09)
8. `08_cross_validation_and_model_selection.ipynb` — holdout, k-fold, stratified k-fold, leave-one-out, nested CV; hyperparameter tuning (grid search, random search); learning curves; biological pitfalls (data leakage, patient-level splits)
9. `09_evaluation_metrics_for_imbalanced_data.ipynb` — confusion matrix, precision/recall, F1, ROC-AUC, PR-AUC, MCC; class weighting, SMOTE; application: rare variant detection, rare disease diagnosis

## Part 4: Unsupervised Learning (NB10–NB12)
10. `10_clustering_kmeans_and_hierarchical.ipynb` — k-means from scratch (Lloyd's algorithm), k-means++ initialization, elbow method, silhouette; hierarchical clustering (linkage criteria, dendrogram); application: patient stratification
11. `11_dimensionality_reduction_pca_and_umap.ipynb` — PCA from scratch (SVD), scree plot, loadings, explained variance; t-SNE intuition; UMAP (tool usage); application: bulk RNA-seq and single-cell visualization
12. `12_feature_selection_and_engineering.ipynb` — filter methods (variance, correlation, mutual information), wrapper methods (RFE), embedded methods (Lasso), domain-specific features for biological data; curse of dimensionality; application: genomics feature selection

## Part 5: Biological Applications and Portfolio (NB13–NB15)
13. `13_ml_for_genomics_and_sequence_data.ipynb` — sequence encoding (one-hot, k-mer, positional), ML for variant effect prediction, enhancer prediction, splice site detection; tools: sklearn + Biopython
14. `14_ml_for_clinical_omics.ipynb` — survival analysis (Cox regression, Kaplan-Meier), multi-omics integration for clinical prediction, TCGA example; batch effect correction overview (ComBat); deployment considerations
15. `15_mini_projects_and_assessment.ipynb` — MP01: cancer subtype classification (simulated TCGA-like RNA-seq, 500 samples × 2000 genes, 5 subtypes, full pipeline from scratch + sklearn); MP02: drug-target binding prediction (feature-engineered binding problem, SVM + RF); 60-point assessment
