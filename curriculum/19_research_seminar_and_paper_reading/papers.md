# Module 19 — Papers

These are landmark papers to read as part of the research seminar practice. Each is used as a reading exercise — the goal is not to master the method (that happens in its home module) but to practice the Three-Pass Method and build cold-explanation fluency.

## Reading schedule guidance

- **Weeks 1–4:** Read one foundational paper per week as your first four Three-Pass attempts.
- **Months 2–6:** One landmark paper per week, drawn from your current module(s).
- **Months 7–12:** One paper per week, self-selected based on your emerging research interests.

## Paper table

| # | Paper | Type | Why it matters | When to read | Difficulty | Prerequisites |
|---|-------|------|----------------|--------------|------------|---------------|
| 1 | Needleman & Wunsch (1970). "A general method applicable to the search for similarities in the amino acid sequence of two proteins." J Mol Biol 48(3):443–453. | Foundational | Invented dynamic programming for sequence alignment — the basis of all sequence search. | Week 1 (first Three-Pass exercise) | Low | Module 01 Python basics |
| 2 | Smith & Waterman (1981). "Identification of common molecular subsequences." J Mol Biol 147(1):195–197. | Foundational | Local alignment variant of Needleman-Wunsch; used in BLAST. Just 3 pages — perfect for first cold-explanation practice. | Week 2 | Low | NB01 completed |
| 3 | Altschul et al. (1990). "Basic local alignment search tool." J Mol Biol 215(3):403–410. (BLAST) | Landmark | One of the most-cited papers in biology. Introduced BLAST heuristic. Track A: "how does BLAST work" is a direct interview question. | Week 3 | Medium | Needleman-Wunsch read |
| 4 | Dobin et al. (2013). "STAR: ultrafast universal RNA-seq aligner." Bioinformatics 29(1):15–21. | Landmark | Standard RNA-seq aligner. Track A: must know STAR. Methods section is a model of clarity. | Week 4 | Medium | Module 09 context |
| 5 | Love, Huber & Anders (2014). "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2." Genome Biology 15:550. | Landmark | Standard differential expression tool. Statistical model is worth understanding. | Month 2 | Medium–High | Module 03 stats |
| 6 | Li (2013). "Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM." arXiv:1303.3997. | Landmark | BWA-MEM is the standard short-read aligner. Not peer-reviewed but functionally the reference paper. | Month 2 | Medium | Module 09 |
| 7 | Butler et al. (2018). "Integrating single-cell transcriptomic data across different conditions, technologies, and species." Nature Biotechnology 36:411–420. (Seurat v2) | Landmark | First widely adopted single-cell integration paper. Introduced CCA-based alignment. | Month 3 | High | Module 10 |
| 8 | Wolf et al. (2018). "SCANPY: large-scale single-cell gene expression data analysis." Genome Biology 19:15. | Landmark | Python ecosystem for single-cell analysis. Essential for NB05 and Module 10 work. | Month 3 | Medium | Module 10 |
| 9 | Korsunsky et al. (2019). "Fast, sensitive and accurate integration of single-cell data with Harmony." Nature Methods 16:1289–1296. | Landmark | Harmony batch correction — standard in scRNA-seq pipelines. | Month 4 | High | Seurat read |
| 10 | McInnes, Healy & Melville (2018). "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction." arXiv:1802.03426. | Landmark | Mathematical foundation of UMAP — used everywhere in scRNA-seq and ML. Good for practicing math-heavy methods reading. | Month 4 | High | Module 04 linear algebra |
| 11 | Jumper et al. (2021). "Highly accurate protein structure prediction with AlphaFold." Nature 596:583–589. | Landmark | AlphaFold2 — the single most important computational biology paper of the decade. Read for the abstract and key figures first; full methods are very dense. | Month 5 | Very high | Module 11, Module 14 |
| 12 | Keshav, S. (2007). "How to Read a Paper." ACM SIGCOMM CCR 37(3):83–84. | Survey | The Three-Pass Method paper itself. 2 pages. Read in Week 1 before NB01. | Week 1 | Very low | None |
| 13 | Mangul et al. (2019). "Systematic benchmarking of omics computational tools." Nature Communications 10:1393. | Survey | Model of a good benchmark paper. Use alongside NB04. | Month 2 | Medium | NB04 completed |
| 14 | Ioannidis (2005). "Why Most Published Research Findings Are False." PLOS Medicine 2(8):e124. | Survey | Statistical literacy foundational reading. Controversial but essential. Read alongside NB03. | Month 1 | Low–Medium | NB03 started |
| 15 | Pautasso (2013). "Ten Simple Rules for Writing a Literature Review." PLOS Comp Bio 9(7):e1003149. | Survey | Practical guide for NB07. Read before attempting a literature review. | Month 3 | Low | NB07 |

## Paper-notes/ template

For each paper read, create a file in `paper-notes/` at the repository root:

```
paper-notes/
└── needleman_wunsch_1970.md
```

Each file contains:
```markdown
# [Author(s)] ([Year]). "[Title]"

**DOI:** ...
**Read date:** YYYY-MM-DD
**Module connection:** Module XX

## Pass 1 — Skim (5–10 min)
One-sentence summary:

## Pass 2 — Read (45–90 min)
Key claims:
- ...
Fuzzy points marked during reading:
- ...

## Pass 3 — Reconstruct (unaided)
**Success:** Y / N
Core method re-explanation (closed paper):

## Questions remaining
- ...
```
