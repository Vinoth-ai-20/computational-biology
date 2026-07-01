# Module 09 — Genomics and Next-Generation Sequencing (NGS)

**Depth tier:** Tier 1 — Master  
**Week budget:** Weeks 19–26 (8 weeks)  
**Notebooks:** 16  
**Prerequisites:** Module 08 (sequence alignment, FASTA/FASTQ, k-mer concepts)

---

## Motivation

NGS is the engine of modern genomics. Every genome sequencing project, variant calling
pipeline, RNA-seq experiment, and ChIP-seq assay runs through a common stack: quality
control → alignment → BAM processing → analysis. This module builds fluency with that
stack — both the computational concepts and the file formats — at the depth required
for Track A interviews and Track B research.

---

## Why this helps Track A

Indian RA/JRF/Bioinformatics Engineer roles routinely require:
- Knowledge of NGS pipelines (STAR, HISAT2, GATK, BWA, SAMtools)
- SAM/BAM/VCF format fluency — these appear in every technical screening
- Ability to compute coverage, MAPQ distributions, and flagstat metrics
- Basic RNA-seq: alignment, quantification, DESeq2 normalization

**Interview pattern:** "Walk me through a variant calling pipeline from FASTQ to VCF."
You must be able to answer this without hesitation.

---

## Why this helps Track B

European PhD programmes in computational genomics, systems biology, and bioinformatics
use NGS data throughout. Being able to run and interpret a variant calling or RNA-seq
pipeline from scratch — including the statistical models — demonstrates the research
independence that PhD applications require.

---

## Module structure (16 notebooks)

| Part | Notebooks | Topic |
|------|-----------|-------|
| 1 — Foundations | NB01–NB03 | Technologies, QC, alignment concepts |
| 2 — Alignment files | NB04–NB06 | SAM/BAM format, MAPQ, duplicate marking |
| 3 — Variant calling | NB07–NB09 | Pileup, GATK concepts, VCF format |
| 4 — RNA-seq | NB10–NB12 | Spliced alignment, TPM, DESeq2 |
| 5 — Visualization | NB13 | IGV concepts, genome browsers |
| 6 — Portfolio | NB14–NB15 | Variant calling pipeline, RNA-seq DE |
| 7 — Assessment | NB16 | 50-point gate (40/50 = 80%) |

---

## Portfolio artifacts

1. `portfolio/module09_variant_calling_pipeline.png` — synthetic FASTQ → alignment → coverage → SNP calls, 4-panel
2. `portfolio/module09_rnaseq_de_analysis.png` — count matrix → normalization → DE → volcano plot, 4-panel

---

## Key tools (know what each does, even before deep mastery)

| Tool | Function | Track A relevance |
|------|----------|------------------|
| BWA-MEM | Short-read alignment to reference | Core pipeline step |
| STAR / HISAT2 | Spliced RNA-seq alignment | RNA-seq screening question |
| SAMtools | BAM manipulation, flagstat, view | Ubiquitous, asked constantly |
| GATK HaplotypeCaller | SNP/indel calling | Standard variant calling pipeline |
| FastQC | Read QC | First step of any NGS pipeline |
| Trimmomatic / fastp | Quality trimming | Know the parameters |
| featureCounts / HTSeq | Count matrix from BAM | RNA-seq step 3 |
| DESeq2 / edgeR | Differential expression | Statistical model, not just the tool |
