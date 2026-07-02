# Module 14 — Assignments

## Assignment A01 — Sequence Model Comparison (DeepBind vs. Transformer)

**Scope:** Build two models for TF binding prediction on the same dataset (Module 13 NB13
sequence dataset, or a JASPAR-positive / shuffled-negative dataset):
1. A 1D CNN (NB03 architecture)
2. A small Transformer encoder (NB05 architecture)

**Requirements:**
- Implement both in PyTorch with a shared `Dataset` / `DataLoader`
- Nested CV for fair comparison (5-outer / 3-inner)
- Report: AUROC, AUPRC, training time per epoch, parameter count
- Visualize: attention maps (Transformer) and filter motifs (CNN)
- Written: 1-page comparison — when would you choose each? What does each representation capture?

**Deliverable:** One notebook. One 4-panel portfolio figure. Written section ≤400 words.

---

## Assignment A02 — scRNA-seq Latent Space Analysis

**Scope:** Apply a VAE to simulated scRNA-seq data (or real data from GEO if available):
1. Train a VAE (NB06 architecture) to learn a 10-dimensional latent space
2. Cluster the latent space (Module 13 NB10: k-means + ARI)
3. Identify differentially expressed genes per cluster using the decoder (perturbation analysis)
4. Visualize the latent space with UMAP (Module 13 NB11)

**Requirements:**
- The VAE must use negative binomial or Gaussian likelihood appropriate to the data
- Latent space ARI vs. known cell types must be reported
- Written: explain the ELBO objective in plain language (≤200 words)

**Deliverable:** One notebook. UMAP of latent space colored by (a) cell type, (b) batch.
