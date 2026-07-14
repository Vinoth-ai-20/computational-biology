# Module 17 — Papers

Read these in the order shown. "When to read" maps to the notebook sequence.

| Paper | Type | Why it matters | When to read | Difficulty | Prerequisites |
|-------|------|---------------|--------------|------------|---------------|
| Lam, S.K. et al. (2015). "Numba: A LLVM-based Python JIT compiler." *Proc. 2nd Workshop on the LLVM Compiler Infrastructure in HPC*. ACM. | Foundational | Original Numba paper; explains the compilation model, `nopython` mode, and vectorize decorator; gives you the vocabulary to explain Numba in an interview | After NB04 | Medium | NB01–NB03 first |
| Mölder, F. et al. (2021). "Sustainable data analysis with Snakemake." *F1000Research* 10:33. | Foundational | Definitive Snakemake paper; explains the DAG-based pipeline model, reproducibility guarantees, and HPC integration (SLURM cluster profile); directly referenced in NB06 | After NB06 | Low | Basic pipeline familiarity |
| Kryuchkova-Mostacci, N. et al. (2025). "A Survey of Bioinformatics Tools in Rust." *Bioinformatics Advances* (preprint or recent publication). | Survey | Maps the Rust bioinformatics ecosystem (noodles, needletail, rust-bio, sourmash); gives context for NB07–NB10; signals to PhD committees that you're tracking the frontier | After NB10 | Low | NB07–NB09 first |
| Luiz Irber et al. (2022). "Lightweight compositional analysis of metagenomes with FracMinHash and minimum metagenome covers." *eLife* 11:e79849. | Application | Shows how a Rust-backed Python tool (sourmash) scales to metagenomic datasets that would be impossibly slow in pure Python; connects Rust performance to real biological questions | After NB10 | Medium | NB09, NB10 |
| Virshup, I. et al. (2024). "The scverse ecosystem for single-cell omics analysis." *Nature Methods* 21:229–232. | Survey | Covers Dask-backed AnnData for out-of-core single-cell analysis at scale; direct parallel to NB03's Dask content but in a high-profile biological context | After NB03 | Low–Medium | NB03 |

## Notes on the Rust survey paper

The Rust bioinformatics survey is a rapidly moving area. If the Kryuchkova-Mostacci paper is not yet available, substitute:

- Entriken, W. & Bhatt, A. (2023). "Experiences using Rust for bioinformatics." *BOSC/ISMB workshop talk*. Check the BOSC proceedings for the current year.
- Alternatively, the noodles README (https://github.com/zaeleus/noodles) functions as a curated survey of Rust bioinformatics file format support.

## Papers to add if specialising further (not required for Tier 2)

- Paszke, A. et al. (2019). "PyTorch: An Imperative Style, High-Performance Deep Learning Library." *NeurIPS*. — GPU parallelism, CUDA kernels, connects Numba GPU to ML
- Harris, C.R. et al. (2020). "Array programming with NumPy." *Nature* 585:357–362. — Original NumPy design paper; useful for interviews
- Regier, J. et al. (2019). "Efficient variational inference in large-scale Bayesian compressed sensing." — HPC Bayesian inference at scale; good for Track B proposals in computational statistics
