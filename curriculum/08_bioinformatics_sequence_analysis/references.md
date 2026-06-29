# Module 08 — References

---

## Primary textbooks

- **Durbin, Eddy, Krogh & Mitchison — Biological Sequence Analysis (1998)**
  The authoritative reference. Chapters 2 (pairwise alignment), 4 (probabilistic
  models), 5 (profile HMMs). Dense but rigorous. Read alongside the notebooks.

- **Compeau & Pevzner — Bioinformatics Algorithms: An Active Learning Approach (3rd ed.)**
  More accessible; chapter structure matches this module's sequence almost exactly.
  Available online with interactive exercises at bioinformaticsalgorithms.com.

- **Setubal & Meidanis — Introduction to Computational Molecular Biology (1997)**
  Good for assembly algorithms (overlap/De Bruijn graphs); older but clear.

---

## Online resources

- **Rosalind.info** — rosalind.info
  Problem-based learning for bioinformatics. NB15 uses this directly.
  Complete 'Bioinformatics Stronghold' track for core algorithm practice.

- **NCBI BLAST** — blast.ncbi.nlm.nih.gov
  Reference implementation. Use to validate your own BLAST-like implementation
  outputs. Read the BLAST manual for parameter explanations.

- **EMBL-EBI sequence analysis tools** — ebi.ac.uk/services/bioinformatics-tools
  Clustal Omega, MAFFT, MUSCLE web interfaces.

- **Biopython tutorial** — biopython.org/wiki/Documentation
  `Bio.pairwise2`, `Bio.Align.PairwiseAligner` — reference for NB16 benchmarking.

---

## Key software (used in this module)

- **MAFFT** — Multiple sequence alignment; outperforms ClustalW on most datasets
- **MUSCLE** — Alternative to MAFFT; faster for large datasets
- **BLAST+** — `blastn`, `blastp`, `makeblastdb` — command-line BLAST
- **Biopython** — `Bio.SeqIO`, `Bio.Align`, `Bio.Phylo`, `Bio.pairwise2`
- **FastTree** — Approximate ML tree from large MSA (used in NB17)

---

## Key researchers

- **Sean Eddy (Harvard)** — HMMER, Infernal; probabilistic models of sequence families
- **Webb Miller** — co-developed early alignment algorithms; BLAST lineage
- **David Lipman & Eugene Myers** — original BLAST (1990)
- **Desmond Higgins** — ClustalW/Omega; progressive MSA
- **Kazutaka Katoh** — MAFFT developer
