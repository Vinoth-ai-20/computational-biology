# Module 09 — Assignments

## A01 — SAM/VCF Format Fluency

Parse a real BAM file (NA12878 chr22 subset from DS05, or any public BAM) using
only Python + `pysam`. For each read: decode the FLAG field, extract the CIGAR string,
compute the reference bases covered. Output a BED file of covered regions.

Then parse the matching VCF file: count the number of SNPs, indels, and multi-allelic
sites. For each variant, compute the allele frequency from the GT fields.

Submit: working Python script + output summary table + 1-paragraph interpretation.

## A02 — Variant Calling Pipeline on Public Data

Using GATK Best Practices:
1. Download NA12878 chr22 FASTQ from 1000 Genomes
2. Align with BWA-MEM to hg38 chr22
3. Mark duplicates with Picard
4. Call variants with GATK HaplotypeCaller (GVCF mode)
5. Genotype the GVCF
6. Compare to the GIAB truth set with hap.py

Report: precision, recall, F1 for SNPs and indels separately. Explain one category
of false positives you observe (examine them in IGV).

## A03 — RNA-seq DE Analysis

Using the DS06 ENCODE dataset (or equivalent public RNA-seq counts):
1. Implement DESeq2 size factor normalization from scratch
2. Compute log2 fold changes between two conditions
3. Apply BH multiple testing correction
4. Produce a volcano plot with top 10 DE genes labelled
5. Perform GO term enrichment (gprofiler2 API call or manual lookup for top 20 genes)

Submit: working Python notebook + volcano plot + 1-paragraph biological interpretation
of the top DE genes.
