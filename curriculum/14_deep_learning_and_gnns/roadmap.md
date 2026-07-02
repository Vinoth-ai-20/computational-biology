# Module 14 — Roadmap

## Part 1: Foundations (NB01–NB03)

1. `01_neural_networks_from_scratch.ipynb` — MLP forward pass, backpropagation (chain rule, Jacobians), gradient descent update; implement XOR, regression, binary classification from scratch with numpy; loss landscape visualization
2. `02_pytorch_fundamentals.ipynb` — tensors and autograd, `nn.Module`, training loop (`forward`, `loss.backward`, `optimizer.step`), `Dataset`/`DataLoader`, GPU portability; implement the NB01 MLP in PyTorch and verify identical outputs
3. `03_cnn_for_sequence_classification.ipynb` — 1D convolution intuition (motif detector analogy), receptive field, pooling; build DeepBind-style CNN for TF binding prediction on one-hot DNA sequences; compare to k-mer baseline from Module 13

## Part 2: Sequence Models (NB04–NB05)

4. `04_recurrent_networks_for_sequences.ipynb` — vanilla RNN vanishing gradients, LSTM gates (input/forget/output/cell) and their equations, GRU; protein secondary structure prediction (3-class); sequence-to-scalar vs. sequence-to-sequence
5. `05_attention_and_transformers.ipynb` — self-attention as soft key-value lookup, scaled dot-product attention $\text{softmax}(QK^T/\sqrt{d_k})V$, multi-head attention, positional encoding; transformer encoder for sequence classification; connection to ESM/DNABERT pre-training

## Part 3: Generative and Latent Models (NB06)

6. `06_autoencoders_and_vaes.ipynb` — deterministic autoencoder (encoder/decoder, bottleneck), VAE ELBO derivation ($\mathcal{L} = \mathbb{E}[log p(x|z)] - D_{KL}(q(z|x)\|p(z))$), reparameterization trick; scVI architecture overview; latent space traversal on scRNA-seq-like data

## Part 4: Graph Neural Networks (NB07–NB08)

7. `07_graph_neural_networks.ipynb` — graph as data structure for biology (molecules, PPI, metabolic), message passing framework (aggregate → combine → update), GCN layer $H^{(l+1)} = \sigma(\hat{A} H^{(l)} W^{(l)})$, node classification on PPI network
8. `08_gnns_for_molecular_biology.ipynb` — molecular graphs (atoms=nodes, bonds=edges, features), graph-level prediction (property prediction), pooling (mean/sum/attention), GNN-based drug property prediction; connection to DiffDock/AlphaFold-Multimer

## Part 5: Training, Interpretability, Applications (NB09–NB12)

9. `09_training_best_practices.ipynb` — dropout, batch normalization, layer normalization; Adam optimizer (first/second moment estimates), learning rate scheduling (warmup + cosine decay); gradient clipping; debugging checklist (loss not decreasing, overfitting, NaN gradients)
10. `10_model_interpretability.ipynb` — saliency maps (gradient of output w.r.t. input), integrated gradients ($\int_0^1 \nabla_x F(x'+\alpha(x-x'))d\alpha$ numerically), attention visualization; attribution on CNN sequence model to recover motif positions
11. `11_alphafold_and_language_models.ipynb` — AlphaFold2 pipeline overview (MSA → evoformer → structure module → recycling); protein language models (ESM-2, ESM-3 concept); zero-shot variant effect prediction via log-likelihood ratio; practical: ESM-2 embeddings for protein property prediction
12. `12_mini_project_and_assessment.ipynb` — MP01: TF binding classification (DeepBind CNN vs. k-mer+SVM from scratch); 50-point assessment (backprop derivation, GCN update rule, VAE ELBO, attention formula, practical debugging)
