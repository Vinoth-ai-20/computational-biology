# Module 09 — Mini Projects

## MP01 — Synthetic Variant Calling Pipeline

**Portfolio artifact:** `portfolio/module09_variant_calling_pipeline.png`

**Goal:** A complete end-to-end variant calling pipeline implemented in Python,
operating entirely on synthetic data generated within the notebook.

**Steps:**
1. Simulate a 500 bp reference sequence
2. Simulate 100× coverage synthetic reads with known SNPs (5 SNPs) and error rate 0.5%
3. Parse simulated reads into a pileup (from scratch)
4. Call SNPs using a genotype likelihood model (from scratch)
5. Output a VCF-format file

**4-panel figure:**
- Panel A: Reference + reads coverage plot (simulated)
- Panel B: Pileup at each SNP position (allele frequencies)
- Panel C: Called vs. planted SNPs (precision/recall)
- Panel D: Genotype likelihood distributions (het vs. hom)

**Implementation rules:**
- All pileup and SNP calling code written from scratch
- SAM parsing from scratch (no pysam)
- VCF output follows the VCF4.2 spec

---

## MP02 — RNA-seq Differential Expression Analysis

**Portfolio artifact:** `portfolio/module09_rnaseq_de_analysis.png`

**Goal:** Implement core DESeq2 concepts from scratch on a synthetic count matrix,
produce a publication-quality DE analysis figure.

**Steps:**
1. Simulate count matrix: 200 genes, 6 samples (3 control, 3 treatment)
   - 50 genes are truly DE (30 up, 20 down); log2FC drawn from N(2, 0.5)
   - Counts from negative binomial with realistic dispersion
2. Compute size factors (median-of-ratios)
3. Estimate per-gene dispersion
4. Compute Wald test statistics and p-values
5. Apply BH correction
6. Classify genes: up-regulated, down-regulated, not significant

**4-panel figure:**
- Panel A: Raw vs. normalized count distributions (box plots)
- Panel B: MA plot (mean expression vs. log2FC)
- Panel C: Volcano plot (−log10 p-adj vs. log2FC)
- Panel D: Heatmap of top 20 DE genes

**Implementation rules:**
- Size factor normalization from scratch (no R or DESeq2 package)
- BH correction from scratch (`p_adjust_bh()`)
- All 50 planted DE genes must be recovered at FDR < 0.05
