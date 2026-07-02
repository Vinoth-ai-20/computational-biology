# Module 14 — Exercises

One exercise set per notebook. Implement before reading the next notebook.

| Exercise | Paired notebook | Task |
|---|---|---|
| E01 | NB01 | Implement backpropagation for a 3-layer MLP on a 2D classification problem. Verify gradients with finite differences (`(f(w+ε) - f(w-ε)) / 2ε`). |
| E02 | NB02 | Port your NB01 numpy MLP to PyTorch. Compare training curves — they should be identical given the same random seed and initialization. |
| E03 | NB03 | Visualize the learned convolutional filters after training the CNN. Compute the PWM representation of each filter and compare to known JASPAR motifs using Pearson correlation. |
| E04 | NB04 | Implement the LSTM update equations from scratch in numpy for a single timestep. Verify the cell state and hidden state match PyTorch's `nn.LSTM` output. |
| E05 | NB05 | Implement scaled dot-product attention from scratch. Verify: (1) output is a weighted sum of values; (2) attention weights sum to 1 along the query dimension. |
| E06 | NB06 | Train a VAE on MNIST (or simulated scRNA-seq). Visualize the 2D latent space. Show that interpolating between two latent codes produces smooth transitions in the generated output. |
| E07 | NB07 | Implement one GCN layer (the $\hat{A} H W$ update) from scratch using sparse matrix multiplication. Verify it matches `torch_geometric.nn.GCNConv` on a small graph. |
| E08 | NB08 | Add edge features to the molecular GNN. Show that including bond type (single/double/aromatic) improves property prediction on the drug dataset. |
| E09 | NB09 | Train the NB03 CNN (a) with no dropout/BN, (b) with dropout only, (c) with batch norm only, (d) with both. Plot all four training curves. Which combination is most stable? |
| E10 | NB10 | Compute integrated gradients for 10 positive binding sequences. Visualize the attribution as a sequence logo (position × attribution magnitude). Do the highlighted positions match the true motif? |
| E11 | NB11 | Use ESM-2 (esm library) to extract embeddings for 20 protein sequences of known thermostability. Fit a Ridge regression to predict Tm. Compare to one-hot k-mer baseline. |
