# Module 14 — Deep Learning and GNNs

**Depth tier:** Tier 2 — Working competence  
**Week budget:** 6 weeks  
**Notebooks:** 12  
**Mini-projects:** 1 (NB12)  
**Prerequisites:** Module 13 (Machine Learning for Biology), Module 04 (Linear Algebra)

---

## Motivation

Deep learning now dominates computational biology: AlphaFold solved protein structure
prediction, scVI models single-cell data as variational autoencoders, Enformer predicts
gene expression from DNA using transformers, and graph neural networks learn from
molecular and protein interaction graphs. A Tier 2 understanding means you can use
these models correctly, understand what they compute, and adapt pre-trained models
to new biological problems — without needing to implement every architecture from scratch.

---

## Objectives

By the end of this module you can:

1. Implement a multi-layer perceptron from scratch (forward pass + backpropagation)
2. Write a training loop in PyTorch (`Dataset`, `DataLoader`, `nn.Module`, `optimizer.step`)
3. Build and train a 1D CNN for sequence classification (DeepBind-style)
4. Explain LSTM gates and their role in long-range dependencies
5. Derive the self-attention mechanism and describe the Transformer encoder architecture
6. Explain the VAE ELBO objective and its role in scRNA-seq latent space models
7. Implement a graph convolutional network layer (message passing + aggregation)
8. Apply transfer learning from a pre-trained biological model to a small dataset
9. Compute saliency maps and integrated gradients for sequence attribution
10. Describe AlphaFold's key architectural innovations (evoformer, structure module, recycling)
11. Train a model with dropout, batch normalization, and a learning rate scheduler

---

## Depth tier definition (Tier 2 — Working competence)

Can use the standard tools correctly, explain what they compute and why, and recognize
when something looks wrong. Can train and fine-tune models, debug common failures,
and adapt existing architectures to new biological tasks. Cannot derive every
optimization from scratch — but can read the original papers and follow the derivations.

---

## Track A relevance

Bioinformatics engineer roles increasingly require PyTorch fluency. Being able to
train a CNN for sequence classification and fine-tune a pre-trained model covers
the majority of what research engineer positions test. AlphaFold familiarity is
now expected background knowledge in structural biology roles.

## Track B relevance

European PhD programmes in computational biology consistently look for PyTorch
proficiency and familiarity with at least one of: sequence models (transformers),
graph models (GNNs for molecular data), or generative models (VAE/diffusion).
This module provides the core of all three.
