# Module 09 — Roadmap

## Part 1 — NGS Foundations

1. `01_ngs_technologies_and_applications.ipynb`
   — Illumina, PacBio, Oxford Nanopore; sequencing-by-synthesis; read length vs. accuracy trade-offs; applications (WGS, WES, RNA-seq, ChIP-seq, ATAC-seq); the full pipeline at a glance

2. `02_read_quality_control_fastqc.ipynb`
   — FastQC metrics (per-base quality, GC content, adapter content, overrepresented sequences); Phred scores revisited; quality trimming concepts (Trimmomatic/fastp parameters); simulate a FastQC-like report in Python

3. `03_short_read_alignment_concepts.ipynb`
   — FM-index and BWT for reference indexing; seed-and-extend alignment (BWA-MEM); seeding heuristics; alignment score vs. mapping quality (MAPQ); why spliced alignment is harder than genomic alignment

## Part 2 — Alignment Files

4. `04_sam_bam_format_deep_dive.ipynb`
   — SAM format: 11 mandatory fields (QNAME, FLAG, RNAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL); FLAG interpretation (paired-end, unmapped, reverse); CIGAR string decoding (M, I, D, S, H, N); parse SAM from scratch in Python

5. `05_alignment_statistics_mapq_coverage.ipynb`
   — MAPQ: Phred-scaled mapping probability; flagstat output; per-base coverage depth; coverage uniformity; compute coverage from SAM records in Python; idxstats; mosdepth concepts

6. `06_duplicate_marking_and_bqsr.ipynb`
   — PCR duplicates: what they are, why they matter; Picard MarkDuplicates logic; optical vs. PCR duplicates; Base Quality Score Recalibration (BQSR) concept and why it matters for variant calling; simulate duplicate detection from coordinates

## Part 3 — Variant Calling

7. `07_variant_calling_pileup_and_genotyping.ipynb`
   — The pileup: counting bases at each reference position; likelihood model for genotyping; binomial and diploid genotype likelihoods; simple SNP calling from pileup; PHRED-scaled genotype likelihoods (PL field in VCF); implement `pileup_snp_caller()` from scratch

8. `08_gatk_haplotypecaller_concepts.ipynb`
   — GATK HaplotypeCaller: local de novo assembly of haplotypes using active regions; realignment of reads to candidate haplotypes; genotype likelihoods with the PairHMM; VQSR vs. hard filtering; GVCF mode and joint genotyping; conceptual walkthrough (no actual GATK execution needed)

9. `09_vcf_format_reading_filtering_annotation.ipynb`
   — VCF format: header, CHROM/POS/ID/REF/ALT/QUAL/FILTER/INFO/FORMAT/SAMPLE columns; common INFO tags (DP, AF, AN, AC); FILTER field (PASS vs. LowQual); parsing VCF in Python from scratch; variant filtering by quality, depth, allele frequency; variant annotation concepts (SnpEff, VEP)

## Part 4 — RNA-seq

10. `10_rnaseq_spliced_alignment_star.ipynb`
    — Spliced alignment: why STAR/HISAT2 differ from BWA; splice junction detection; two-pass alignment; STAR output files (BAM, SJ.out.tab, Log.final.out); interpret STAR alignment statistics; simulate a splice-aware alignment concept in Python

11. `11_transcript_quantification_tpm_counts.ipynb`
    — Raw count matrix from featureCounts/HTSeq; TPM (transcripts per million): formula and biological interpretation; FPKM/RPKM: formula and why TPM is preferred; between-sample normalization; implement `compute_tpm()` and `compute_fpkm()` from scratch; TMM and median-of-ratios normalization concepts

12. `12_differential_expression_deseq2_statistics.ipynb`
    — The DE problem: why naive fold-change is insufficient; negative binomial model for count data; DESeq2: size factors (median-of-ratios normalization), dispersion estimation, Wald test; volcano plot interpretation; multiple testing correction (Benjamini-Hochberg); implement `deseq2_size_factors()` and `nb_log_fold_change()` concepts

## Part 5 — Visualization

13. `13_genome_browsers_igv_and_variant_visualization.ipynb`
    — IGV concepts: loading BAM, VCF, BED, GTF; interpreting coverage tracks; soft-clipping and realignment artifacts; visualizing a het vs. hom variant; reading a lollipop plot; implementing a basic coverage track plot in Python

## Part 6 — Portfolio

14. `14_mini_project_variant_calling_pipeline.ipynb`
    — Portfolio artifact 1: synthetic FASTQ → parse/QC → pileup → SNP calling → VCF output → 4-panel figure
    — Pass-3 gate: `pileup_snp_caller()` and `parse_sam()` written from memory

15. `15_mini_project_rnaseq_de_analysis.ipynb`
    — Portfolio artifact 2: synthetic count matrix → TMM/DESeq2 size factors → fold change → BH correction → volcano plot → 4-panel figure

## Part 7 — Assessment

16. `16_module_assessment.ipynb`
    — 50-point gate (40/50 = 80%); Sections A–D: conceptual (20), implementation (20), applied (6), mock interview (4)
