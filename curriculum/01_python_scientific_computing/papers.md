# Module 01 — Python & Scientific Computing: Papers

Module 01 is primarily a software and methods module rather than a biology literature module. Its reading list focuses on scientific computing practice and the tools used throughout this program. Foundational biology literature begins in Module 05.

---

## Reading List

| Paper | Type | Why it matters | When to read | Difficulty | Prerequisites | Pass-3 required |
| ------- | ------ | ---------------- | -------------- | ------------ | --------------- | ----------------- |
| Wilson et al. (2017), *Good enough practices in scientific computing*, PLOS Computational Biology. DOI: 10.1371/journal.pcbi.1005510 | Foundational | The literal audit checklist applied to `compbio_utils` v0 in Notebook 18 and Assignment A02. Already read via Pass-3 in Module 00 — re-apply here as a code audit against real code being written. | Week 1 (reviewed again in Week 6 during Assignment A02) | Easy | None | Already done in Module 00; re-apply as audit |
| Harris et al. (2020), *Array programming with NumPy*, Nature. DOI: 10.1038/s41586-020-2649-2 | Software paper | The canonical NumPy citation. Relevant for understanding the design philosophy behind broadcasting, ufuncs, and the memory layout choices that make vectorization fast. | Week 3, after Notebook 05 | Easy | NumPy basics (Notebook 04) | No — Pass 1 plus one-paragraph summary |
| Virtanen et al. (2020), *SciPy 1.0: Fundamental algorithms for scientific computing in Python*, Nature Methods. DOI: 10.1038/s41592-019-0686-2 | Software paper | The canonical SciPy citation. Read the introduction and the section describing `solve_ivp` and its relationship to ODEPACK. Directly relevant to Notebook 12. | Week 4–5, before Notebook 11 | Easy–Moderate | Basic SciPy usage | No — Pass 1 plus the `solve_ivp` section at Pass 2 depth |
| Cock et al. (2009), *Biopython: freely available Python tools for computational molecular biology and bioinformatics*, Bioinformatics. DOI: 10.1093/bioinformatics/btp163 | Software paper | The Biopython citation. Short and readable. Useful for understanding the `SeqRecord` / `SeqIO` architecture decisions before Notebook 16. | Week 6, before Notebook 16 | Easy | None | No — Pass 1 sufficient |

---

## Research Paper Reading Session (Notebook 19)

**Assigned paper for Pass-3 reconstruction:** choose one.

**Option A — Harris et al. (2020):** Focus the reconstruction on the broadcasting section. With the paper closed, re-explain the shape-compatibility rule using three concrete examples of your own, one of which should involve a biological array (e.g., an expression matrix operation). If you cannot construct the third example without the paper, that is meaningful data — log it.

**Option B — Cock et al. (2009):** Focus the reconstruction on the `SeqRecord` / `SeqIO` architecture. With the paper closed, explain why the design uses a `SeqRecord` wrapper around `Seq` rather than a single `Sequence` class. Then implement a minimal `SeqRecord`-equivalent from scratch in 15 lines.

Log the reconstruction in `paper-notes/` using the template from Module 00's `papers.md`.

---

## Note on Reading Software Papers

Scientific software papers are read differently from biology research papers:

- Pass 1 is usually sufficient to understand what the tool does and why it exists.
- Pass 2 focuses on the methods section — how was it built, how was correctness validated — not on the results section.
- Pass 3 reconstruction for a software paper means: implement a minimal version of one described algorithm or interface, or write a correct usage example from memory, or explain one design decision in plain language without the paper.

This note applies to every software paper encountered throughout the program.

---

## Downstream Papers (read when the relevant module begins)

These papers appear in downstream modules but connect directly to the foundation laid in Module 01:

| Paper | Module | Connection to Module 01 |
| ------- | -------- | ------------------------ |
| Altschul et al. (1990), *Basic local alignment search tool*, J. Mol. Biol. | Module 08 | The k-mer seeding step uses NumPy array operations established in Notebooks 04–05 |
| Love, Huber & Anders (2014), DESeq2, Genome Biology | Module 09 | Differential expression statistics build on Module 03; the data loading and preprocessing use Pandas patterns established in Notebooks 08–09 |
| Wolf, Angerer & Theis (2018), SCANPY, Genome Biology | Module 10 | Scanpy's `AnnData` object is a Pandas-and-NumPy-backed data structure; understanding it requires Module 01 fluency |
| Grimm et al. (2020), ODD Protocol, JASSS | Module 15 | ABM notebooks use the SciPy ODE solver and NumPy random number infrastructure established in Notebooks 07 and 12 |

---

*See also: [roadmap.md](roadmap.md) — [references.md](references.md) — [CLAUDE.md](../../CLAUDE.md) §8 (Three-Pass Method)*
