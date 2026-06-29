# Module 07 — References

---

## Textbooks (pull chapters, don't read cover-to-cover)

- **Nelson & Cox — Lehninger Principles of Biochemistry (8th ed.)**
  The gold-standard biochemistry reference. Chapters to prioritise at Tier 2:
  Ch. 3–4 (amino acids, protein structure), Ch. 6 (enzymes), Ch. 11–12 (lipids/membranes),
  Ch. 26–28 (gene expression/regulation)

- **Alberts et al. — Molecular Biology of the Cell (7th ed.)**
  Continued from Module 05. Key chapters for this module:
  Ch. 5 (DNA replication/repair), Ch. 6 (transcription), Ch. 7 (translation),
  Ch. 3 (proteins), Ch. 15 (cell signaling — kinase cascades)

- **Stryer, Berg & Tymoczko — Biochemistry (9th ed.)**
  Alternative to Lehninger — more visually focused, good for enzyme kinetics.

---

## Online resources

- **Khan Academy — Macromolecules; Enzymes; DNA replication**
  Excellent animated explanations for first-pass understanding.
  URL: khanacademy.org/science/ap-biology

- **RCSB Protein Data Bank (PDB)** — rcsb.org
  Structural viewer for proteins mentioned in any notebook. Habit: always look up
  the 3D structure of any enzyme you study.

- **PhosphoSitePlus** — phosphosite.org
  PTM database: phosphorylation sites, kinase–substrate relationships.

- **ExPASy ProtParam tool** — web.expasy.org/protparam
  Reference for molecular weight and physicochemical property calculations
  (verify your `molecular_weight()` implementation against this).

- **BRENDA Enzyme Database** — brenda-enzymes.org
  Km/Vmax values for thousands of enzymes. Use to reality-check any kinetics
  exercise values.

---

## Key researchers (track their recent work)

- **David Baker (U Washington)** — protein design; connects to Module 11
- **Jennifer Doudna / Emmanuelle Charpentier** — CRISPR biochemistry
- **Frances Arnold (Caltech)** — enzyme engineering; directed evolution
- **Venki Ramakrishnan (MRC-LMB)** — ribosome structure; Nobel 2009

---

## Software used in this module

- **Biopython** — `Bio.SeqUtils.ProtParam.ProteinAnalysis` for MW/pI calculation
- **SciPy** — `scipy.optimize.curve_fit` for Michaelis-Menten parameter estimation
- **NumPy/Matplotlib** — all kinetics visualizations
