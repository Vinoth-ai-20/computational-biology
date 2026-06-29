# Module 08 — Roadmap

18 notebooks, Tier 1 (Master), Weeks 10–18

---

## Part 1 — Orientation and Data Formats (Week 10)

- [ ] **NB01** — Why sequence alignment is the canonical interview topic
  Module map, self-assessment, the interview question you must answer cold

- [ ] **NB02** — Sequence data formats: FASTA, FASTQ, quality scores
  Parse FASTA/FASTQ from scratch, Phred quality scores, QC metrics

## Part 2 — The Alignment Problem (Weeks 10–12)

- [ ] **NB03** — Edit distance and the alignment problem
  Levenshtein distance, DP recurrence, traceback from scratch

- [ ] **NB04** — Needleman-Wunsch: global alignment from scratch
  Full DP matrix, traceback, handle gaps; Pass-3 reconstruction target

- [ ] **NB05** — Smith-Waterman: local alignment from scratch
  Difference from NW (zeros, max-cell traceback); Pass-3 target

- [ ] **NB06** — Scoring matrices: PAM and BLOSUM
  Log-odds interpretation, BLOSUM62 from scratch (subset), PAM logic

- [ ] **NB07** — Gap penalties: linear vs. affine
  3-matrix DP for affine gaps (M, Ix, Iy); why affine is biologically better

## Part 3 — BLAST (Weeks 12–13)

- [ ] **NB08** — How BLAST actually works
  k-mer seeding → ungapped extension → gapped extension → E-value statistics;
  the interview answer, implemented step by step

## Part 4 — Multiple Sequence Alignment (Weeks 13–14)

- [ ] **NB09** — Multiple sequence alignment: progressive methods
  Pairwise → guide tree → progressive alignment; center-star heuristic;
  MAFFT/MUSCLE at usage level

## Part 5 — Phylogenetics from Alignment (Weeks 14–15)

- [ ] **NB10** — Distance matrices from alignments
  JC, K2P distance from MSA; pairwise distance matrix

- [ ] **NB11** — Phylogenetic trees: UPGMA
  Full UPGMA from scratch with ultrametric output

- [ ] **NB12** — Phylogenetic trees: Neighbour-Joining
  Full NJ from scratch; bootstrap support

- [ ] **NB13** — Reading and interpreting a phylogenetic tree
  Branch lengths, root, clade support, polytomies, unrooted trees

## Part 6 — Genome Assembly (Week 15)

- [ ] **NB14** — Genome assembly concepts
  Overlap graphs, De Bruijn graphs (conceptual + code); connection to NGS (Module 09)

## Part 7 — Practice and Portfolio (Weeks 16–17)

- [ ] **NB15** — Rosalind.info active-recall problem set
  Assigned problems solved and explained; not just output, but teach-back

- [ ] **NB16** — Mini project: NW+SW from scratch vs. Biopython benchmark
  Portfolio figure — accuracy + speed comparison

- [ ] **NB17** — Mini project: phylogenetics pipeline on real data
  End-to-end: fetch sequences → align (MAFFT) → distance matrix → NJ tree → figure

## Part 8 — Assessment (Week 18)

- [ ] **NB18** — Module assessment + mock interview
  60-point gate (48/60 = 80%); mandatory question: "How does BLAST work?"
