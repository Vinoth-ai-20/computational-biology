# Module 13 — Assignments

## A01 — Full ML Pipeline on Real Genomic Data

Use the TCGA breast cancer (BRCA) RNA-seq dataset (available via UCSC Xena or GDC portal):

1. Download and preprocess: log2(TPM+1), remove low-variance genes (retain top 5000 by MAD)
2. Reduce to top 500 features using variance filtering
3. Apply stratified 5-fold CV with: Logistic Regression, Random Forest, SVM (RBF kernel)
4. Report: balanced accuracy, macro-F1, ROC-AUC per fold (mean ± std)
5. Identify the top 20 most important features (Random Forest feature importance)
6. Look up the top 5 genes — are they known breast cancer genes?

Submit: notebook + table of results + 1-paragraph biological interpretation.

## A02 — Variant Pathogenicity Prediction

Using the ClinVar database (or a provided subset):

1. Encode each variant: position, REF/ALT allele, conservation score (GERP++), MAF, predicted functional impact
2. Binary classification: benign (0) vs. pathogenic (1) — class-imbalanced dataset
3. Compare: Logistic Regression vs. Random Forest vs. XGBoost, with appropriate class weighting
4. Use nested CV for honest evaluation
5. Report: AUROC, AUPRC, F1 at optimal threshold
6. Explain which features drive predictions (SHAP or RF feature importance)

Submit: notebook + ROC/PR curves figure + 1-paragraph comparison.
