# Module 14 — Mini-Projects

## MP01 — DeepBind: CNN for TF Binding Prediction

**Task:** Reproduce the core DeepBind result (Alipanahi et al. 2015) on synthetic data.

**Steps:**
1. Generate a balanced binding dataset (500 positive sequences containing a 10-mer motif
   with 1–2 substitutions; 500 negative random sequences) — same format as Module 13 NB13
2. Build the CNN in PyTorch: Conv1d(4→16, kernel=10) → ReLU → MaxPool → FC(16→1) → Sigmoid
3. Train with BCE loss, Adam optimizer, early stopping on validation AUC
4. Compare to k-mer + SVM baseline (Module 13 NB13)
5. Visualize the learned filters as sequence logos
6. Compute integrated gradients for 10 positive sequences — do they highlight the motif?

**Deliverable:** 4-panel figure: (A) training curves, (B) ROC+PR, (C) filter logos, (D) attribution heatmap.

**Portfolio value:** DeepBind is a canonical demonstration of why CNNs outperform PWMs
for TF binding. This mini-project, cleanly implemented and visualized, is a strong Track A/B portfolio artifact.
