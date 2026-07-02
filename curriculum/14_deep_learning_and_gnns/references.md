# Module 14 — References

## Books

- **Goodfellow, Bengio & Courville — "Deep Learning"** (MIT Press, free online)
  The standard deep learning textbook. Chapters 6–10 (MLP, CNN, RNN), 14 (autoencoders),
  20 (deep generative models). Read before NB01–06.
- **Zhang et al. — "Dive into Deep Learning" (d2l.ai)** (free, interactive)
  PyTorch-native. Excellent practical companion. Covers all architectures with runnable code.

## Frameworks

- **PyTorch** (`torch`, `torch.nn`, `torch.optim`, `torch.utils.data`) — primary framework
- **PyTorch Geometric (PyG)** — GNN toolkit: `torch_geometric.nn.GCNConv`, `MessagePassing`
- **scvi-tools** — VAE framework for single-cell data
- **ESM** (`fair-esm` package, Meta) — protein language model embeddings
- **einops** — readable tensor operations for transformer code

## Key software tools

- **DeepBind** — original TF binding CNN (basis for NB03)
- **Enformer** (DeepMind) — transformer for gene expression from sequence
- **AlphaFold2** — protein structure (ColabFold for practical access)
- **DiffDock** — GNN-based protein-ligand docking

## Key databases for applications

- **JASPAR** — TF binding motifs (ground truth for NB03)
- **UniProt/Swiss-Prot** — protein sequences and annotations (NB11)
- **PDB** (Protein Data Bank) — protein structures (NB11)
- **ChEMBL** — drug-target binding data (NB08)
- **ZINC** — molecular library for drug discovery GNNs

## Key labs

- **DeepMind AlphaFold team** (London) — protein structure
- **Meta AI (FAIR)** — ESM protein language models
- **Aviv Regev lab** (Genentech / Broad) — single-cell deep learning
- **David Baker lab** (UW) — protein design with DL
- **Bernhard Schölkopf / Julien Gagneur** (Helmholtz Munich) — regulatory genomics DL

## Courses

- **fast.ai Practical Deep Learning** — practical PyTorch, rapid iteration
- **CS231n** (Stanford) — CNNs and computer vision (architectures transfer to biology)
- **CS224W** (Stanford) — Graph Neural Networks
