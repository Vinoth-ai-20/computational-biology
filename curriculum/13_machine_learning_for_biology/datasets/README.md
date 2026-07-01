# Module 13 — Datasets

## DS01 — Synthetic RNA-seq (generated in notebooks)
- **Format:** NumPy array / CSV (samples × genes)
- **Size:** 500 samples × 2000 genes, 5 cancer subtypes
- **Used in:** NB01, NB03, NB08, NB10, NB11, NB15 (MP01)
- **Source:** Simulated with planted DE signal + noise (negative binomial-like)

## DS02 — Synthetic Clinical Features (generated in notebooks)
- **Format:** CSV (samples × features)
- **Size:** 300 patients × 10 clinical features (age, gender, stage, mutations, ...)
- **Used in:** NB04, NB06, NB09
- **Source:** Simulated from realistic clinical distributions

## DS03 — Synthetic Sequence Binding Data (generated in notebooks)
- **Format:** FASTA-like list of 100-nt sequences + binary labels
- **Size:** 2000 sequences (1000 binders, 1000 non-binders)
- **Used in:** NB05, NB13
- **Source:** Simulated with planted 8-mer motif for binders

## DS04 — Synthetic Variant Data (generated in notebooks)
- **Format:** CSV (variant × feature matrix + label)
- **Size:** 2000 variants (500 pathogenic, 1500 benign)
- **Used in:** NB09, NB12, NB13
- **Source:** Simulated with realistic feature distributions from ClinVar statistics

## DS05 — Real TCGA BRCA (optional, Assignment A01)
- **Format:** Tab-separated (samples × genes, log2 TPM+1)
- **Source:** UCSC Xena browser (xena.ucsc.edu) or GDC portal
- **License:** TCGA data is freely available for research use
- **Fetch:** See assignment A01 for download instructions

## DS06 — Real STRING + DisGeNET subset (optional, NB14)
- **Source:** DisGeNET public download (disgenet.org)
- **License:** Attribution required; free for non-commercial use
