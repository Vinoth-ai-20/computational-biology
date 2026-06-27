# Module 00 — Orientation: Papers

This module has a short, essential reading list. All three papers are read via the Three-Pass Method (see [CLAUDE.md](../../CLAUDE.md) §8). The Pass-3 reconstruction of Wilson et al. (2017) is the concrete assessment for this module.

---

## Reading List

| Paper | Type | Why it matters | When to read | Difficulty | Prerequisites | Pass-3 required |
| ------- | ------ | ---------------- | -------------- | ------------ | --------------- | ----------------- |
| Wilson et al. (2017), *Good enough practices in scientific computing*, PLOS Computational Biology. DOI: 10.1371/journal.pcbi.1005510 | Foundational | Sets the concrete standard for every notebook, every piece of code, and every dataset in this entire program. The reproducibility checklist in Notebook 12 is derived directly from this paper. | Day 1, before Notebook 07 | Easy | None | **Yes — Module 00 assessment** |
| Wilkinson et al. (2016), *The FAIR Guiding Principles for scientific data management and stewardship*, Scientific Data. DOI: 10.1038/sdata.2016.18 | Foundational | Two readable pages. Defines the four principles this repository's `datasets/` structure and documentation are designed to satisfy. Directly applicable to every module's dataset folder. | Day 1, after Wilson et al. | Easy | None | No — one-paragraph written summary required |
| Keshav (2007), *How to Read a Paper*, ACM SIGCOMM Computer Communication Review | Methodology | One page. The source of the Three-Pass Method. Read it before Notebook 09 — it takes five minutes and directly shapes how every other paper in this program gets read. | Day 5, before Notebook 09 | Easy | None | No — it is itself about how to read; practicing it on Wilson et al. is sufficient |

---

## How to Log a Paper in `paper-notes/`

After completing a Three-Pass reading, create one file in `paper-notes/`. Use the filename format: `author_year_short_title.md`.

Example: `paper-notes/wilson_2017_good_enough_practices.md`

Template:

```markdown
---
title: "Good enough practices in scientific computing"
authors: Wilson, Bryan, Cranston, Kitzes, Nederbragt, Teal
year: 2017
journal: PLOS Computational Biology
doi: 10.1371/journal.pcbi.1005510
module: 00_orientation
date_read: YYYY-MM-DD
pass3_unaided: true/false
---

## Pass 1 — Skim (5 min)
What is the central claim?

## Pass 2 — Intent
What is the method and the evidence? What remains fuzzy after reading?

## Pass 3 — Reconstruction
Re-explain the core argument with the paper closed. Did it succeed unaided?
If not: what was the specific gap? What needed to be re-read?

## Key takeaways
3–5 sentences, plain English, no jargon.

## Open questions
What is not yet understood? Where would you go next?
```

The `pass3_unaided: true/false` field is the metric that matters, not the paper count. The trend in this field across all entries in `paper-notes/` is tracked in the Monthly review (§11 of `Learning_Progress.md`).

---

## Note on Copyrighted Material

Do not commit PDF files to this repository. Store citation metadata and personal notes here. Link to the DOI for the full text. All three papers listed in this module are freely available via their DOIs.

---

## Track A Connection

Being handed a paper cold and asked to explain it in plain English is one of the most commonly reported patterns in bioinformatics engineer and RA interviews. Consistent Pass-3 practice — logged honestly in `paper-notes/` — is direct rehearsal for this pattern. Start the habit in Orientation, before any domain content.

---

*See also: [roadmap.md](roadmap.md) — [references.md](references.md) — [CLAUDE.md](../../CLAUDE.md) §8 (Three-Pass Method)*
