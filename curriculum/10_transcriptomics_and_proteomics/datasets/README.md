# Module 10 — Datasets

## DS01 — Synthetic scRNA-seq Count Matrix (generated in notebooks)
- **Format:** Cell × gene sparse matrix (numpy/scipy)
- **Size:** 500 cells × 2000 genes (synthetic)
- **Used in:** NB01–NB07, NB12
- **Source:** Simulated in Python with known cluster structure

## DS02 — PBMC 3k (10x Genomics public dataset)
- **Format:** 10x-format HDF5 (.h5) or MEX (matrix.mtx + barcodes + features)
- **Size:** 2700 cells × ~32,700 genes (filtered)
- **Used in:** NB02–NB07 (optional real-data extension)
- **Source:** 10x Genomics (https://www.10xgenomics.com/datasets/pbmc-3-k-pbm-cs-from-a-healthy-donor-1-standard-1-1-0)
- **Fetch:** `wget https://cf.10xgenomics.com/samples/cell/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz`

## DS03 — Synthetic Proteomics Matrix (generated in notebooks)
- **Format:** Protein × sample matrix (CSV)
- **Size:** 500 proteins × 6 samples (synthetic, with known missing value pattern)
- **Used in:** NB09–NB10
- **Source:** Simulated in Python

## DS04 — Mock MaxQuant proteinGroups.txt (generated in notebooks)
- **Format:** Tab-separated text (MaxQuant output format)
- **Size:** 200 proteins × 8 LFQ intensity columns
- **Used in:** NB09
- **Source:** Simulated with realistic column structure
