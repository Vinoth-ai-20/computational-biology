# Module 09 — References

## Core books

- **Bioinformatics Data Skills** — Vince Buffalo (O'Reilly, 2015). The best practical
  guide to NGS pipelines. Chapters 10–11 (alignment), 12–13 (variant calling), 14 (RNA-seq).
- **Bioinformatics Algorithms** — Compeau & Pevzner, Vol. 2. Assembly and graph algorithms.
- **Statistical Methods in Bioinformatics** — Ewens & Grant. Statistical foundation for
  variant calling and differential expression.

## Key documentation

- **SAM/BAM specification:** https://samtools.github.io/hts-specs/SAMv1.pdf
  (Read sections 1–4 completely; the FLAG table must be memorised)
- **VCF specification:** https://samtools.github.io/hts-specs/VCFv4.2.pdf
- **GATK Best Practices:** https://gatk.broadinstitute.org/hc/en-us/articles/360035535932
- **DESeq2 vignette:** https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html

## Essential tools (know what each does)

| Tool | Purpose | Reference |
|------|---------|-----------|
| FastQC | Read QC | https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ |
| Trimmomatic | Quality/adapter trimming | Bolger et al., 2014 |
| BWA-MEM | Short-read alignment | Li & Durbin, 2009; Li, 2013 |
| STAR | Spliced RNA-seq alignment | Dobin et al., 2013 |
| HISAT2 | Spliced alignment (graph-based) | Kim et al., 2019 |
| SAMtools | BAM processing | Li et al., 2009 |
| Picard | Duplicate marking, metrics | Broad Institute |
| GATK | Variant calling | McKenna et al., 2010; Van der Auwera & O'Connor, 2020 |
| featureCounts | Count matrix from BAM | Liao et al., 2014 |
| DESeq2 | Differential expression | Love et al., 2014 |

## Key labs and resources

- **Broad Institute GATK team** — gold standard for variant calling pipelines
- **ENCODE Project** — ChIP-seq and ATAC-seq standards
- **Galaxy Project** — browser-based NGS pipeline construction
- **Rosalind** — Problems: BA9A (BWT), BA9D (pattern matching with BWT)
- **UCSC Genome Browser** — visualization reference
- **Ensembl** — genome annotation reference
