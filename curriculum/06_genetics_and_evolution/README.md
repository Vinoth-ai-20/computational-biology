# Module 06 — Genetics and Evolution

## Tier: 2 — Working Competence | Weeks 8–14

**What this module is:** A deeper treatment of genetics and evolutionary theory,
building on Module 05's foundations. This is not a repeat — Module 05 established the
vocabulary and intuitions; Module 06 formalises the models, covers edge cases, and
introduces concepts (coalescent theory, evolutionary game theory, molecular clocks)
that appear in the research literature.

**Depth target:** Can use the standard tools correctly, explain what they do and why,
and recognise when a result looks wrong. No expectation of deriving coalescent
theory from first principles or implementing a full maximum-likelihood phylogenetics
package — but the *ideas* should be clear enough to read papers that use them.

---

## Why This Helps Track A

Genomics RA and Bioinformatics Engineer roles in India increasingly mention
"evolutionary analysis" and "phylogenetics" in their requirements (2026 evidence).
The specific skills tested: interpreting a phylogenetic tree, explaining HWE
departures, describing what a molecular clock assumes.

## Why This Helps Track B

European PhD applications in computational biology, systems biology, and computational
ecology all expect familiarity with evolutionary thinking. The EMBL EIPP and IMPRS
programmes list "evolutionary genomics" among topic areas. Papers in any subfield
that involves multiple species or populations will use the concepts from this module.

---

## Prerequisite Modules

- **Module 05 — Biology Fundamentals** (mandatory — all NB06, NB07, NB08, NB09)
- **Module 03 — Statistics** (for chi-square tests, likelihood concepts)

---

## Week Budget: 7 weeks (Weeks 8–14), parallel with Module 07 start

| Week | Notebooks |
|------|-----------|
| 8    | NB01, NB02 |
| 9    | NB03, NB04 |
| 10   | NB05, NB06 |
| 11   | NB07, NB08 |
| 12   | NB09, NB10 |
| 13   | NB11 (mini-project) |
| 14   | NB12 (assessment) |

---

## Portfolio Artifact

`portfolio/module06_wright_fisher_vs_hardy_weinberg.png`

A 4-panel figure comparing Wright-Fisher simulation trajectories against Hardy-Weinberg
expectations, showing how drift, selection, and population size interact to maintain
or break HWE. Publishable quality.

---

## Module Folder Structure

```
06_genetics_and_evolution/
├── README.md          ← this file
├── roadmap.md         ← ordered notebook list
├── references.md      ← books, tools, key researchers
├── papers.md          ← paper reading table
├── notebooks/         ← 12 notebooks
├── exercises/         ← paired exercise files
├── assignments/       ← A01: comparative population genetics
├── mini_projects/     ← MP01: WF vs HWE portfolio figure
└── datasets/          ← synthetic + public datasets
```
