# Computational Biology — Comprehensive Audit + SOP Drafts + Interview Drills + Study Resources

## For: Vinoth | Generated: July 14, 2026 | Based on CLAUDE.md v2.0 standards

---

## HOW TO USE THIS DOCUMENT

This is three documents in one, in execution order:

1. **Part 1 — Module Audit** (pp. 1–4): What's thin in each active module against CLAUDE.md §6.1 and §7.1 standards. Fix these gaps before the IMPRS-ML deadline (Oct 7).
2. **Part 2 — SOP Drafts** (pp. 5–7): Paste-ready paragraphs for Theis, Stegle, and Huber, each referencing their actual most-recent papers and your specific completed artifacts. Personalize the `[bracketed]` placeholders.
3. **Part 3 — Interview Drills** (pp. 8–12): Track A + Track B mock questions for Modules 01, 03, 05 with answer frameworks. Never read the framework before attempting the question yourself.
4. **Part 4 — Study Resources** (pp. 13–15): One curated YouTube video per topic + free resource map.

---

## PART 1 — MODULE AUDIT

## Audit methodology

CLAUDE.md §6.1 requires every module folder to contain:
`README.md` · `roadmap.md` · `references.md` · `papers.md` · `notebooks/` · `exercises/` · `assignments/` · `mini_projects/` (Tier 1/2 only) · `datasets/`

CLAUDE.md §7.1 requires every notebook to follow the 13-step content order and end with:
quiz (3–5 active-recall items) · reflection prompt · papers referenced · future work/open questions.

CLAUDE.md §7.2 requires: Jupytext pairing · nbstripout hook · papermill-compatible parametrization.

The audit below checks each active module against all three standards.

---

## Module 01 — Python & Scientific Computing (Tier 1)

Active: July 2026 | Week budget: Weeks 1–6

### What CLAUDE.md requires at Tier 1

- 20 notebooks, each following the full 13-step sequence
- Full `papers.md` with Wilson et al. (2017), VanderPlas handbook, Biopython docs
- A polished portfolio artifact: `compbio_utils` v0 seeded with at least one real function
- Module assessment: Track A mock interview (Unix + NumPy + FizzBuzz-class live coding)
- `datasets/` folder with at least one real biological dataset fetched by a reproducible script

### Gaps to fill now (July 2026)

#### Gap 1 — `papers.md` is missing the reproducibility standard paper

Add this exact entry:

```text
| Wilson et al. (2017) | Good enough practices in scientific computing | Foundational | Week 1 — read before first commit | Easy | None | https://doi.org/10.1371/journal.pcbi.1005510 |
```

This paper is your `compbio_utils` design charter. Every function docstring should ask: "does this pass Wilson's checklist?"

#### Gap 2 — `datasets/` has no biological data yet

The Module 01 roadmap ends at notebook 20 (module assessment) but never specifies a real dataset for the `compbio_utils` v0 seed. Add this to `datasets/README.md`:

```text
Source: NCBI GenBank
Accession: NC_000913.3 (E. coli K-12 MG1655 complete genome, 4.6 MB)
License: Public domain (NCBI)
Fetch script: scripts/fetch_ecoli_genome.py
Purpose: First real biological string; used in notebook 16 (Biopython SeqIO) and as seed data for compbio_utils
```

#### Gap 3 — notebooks 13–18 (package → testing → Biopython → Unix) have no biological context in Step 3

Steps 1–2 of those notebooks jump straight to Python without biological background. Even for a programming notebook, Step 3 must exist. For notebook 17 (Unix/CLI):

- Biological background: "Bioinformatics pipelines process files that are too large to open in any GUI. FASTQ files for a single RNA-seq run are typically 5–50 GB. Unix is not optional — it's the only interface that works at this scale."

#### Gap 4 — Module assessment (notebook 20) has no Track A mock interview script

Add to `assignments/module_01_track_a_drill.md`:

```text
ASSESSMENT FORMAT: 45 minutes, no notes.
Part 1 (15 min): Unix — 5 commands from a bioinformatics scenario
Part 2 (15 min): NumPy — implement one vectorized operation from scratch, explain broadcasting
Part 3 (15 min): Live explain — "Walk me through what compbio_utils does and why you built it that way"
```

#### Gap 5 — Jupytext not configured

`.pre-commit-config.yaml` must exist at repo root with:

```yaml
repos:
  - repo: https://github.com/mwouts/jupytext
    rev: v1.16.4
    hooks:
      - id: jupytext
        args: [--sync]
  - repo: https://github.com/kynan/nbstripout
    rev: 0.7.1
    hooks:
      - id: nbstripout
```

Without this, diffs are unreadable and the repo fails the EMBL/IMPRS-ML implicit reproducibility check.

### YouTube resources — Module 01

| Topic                        | Channel                                           | Video / Playlist                                         | Why                                               |
| ---------------------------- | ------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------- |
| NumPy fundamentals           | **Sentdex**                                 | "NumPy with Python" playlist (YouTube)                   | Fast, biological data framing                     |
| Broadcasting & vectorization | **3Blue1Brown**                             | "Essence of Linear Algebra" series — watch before NumPy | Builds the mental model first                     |
| Python packaging             | **ArjanCodes**                              | "How to Create a Python Package" (2024)                  | Directly prepares Module 16 compbio_utils work    |
| Biopython                    | **Bioinformatics with Biopython** (channel) | "Biopython Tutorial: SeqIO"                              | Exact module content                              |
| Unix for bioinformatics      | **Bioinformatics Coach** (channel)          | "Linux for Bioinformatics" playlist                      | Track A interview direct prep                     |
| Scientific visualization     | **Corey Schafer**                           | "Matplotlib Tutorial" series                             | Python 5/5 level — use as reference not tutorial |

---

## Module 03 — Statistics & Probability (Tier 1)

Active: July 2026 | Week budget: Weeks 2–10

### What CLAUDE.md requires at Tier 1 (Module 03)

- 18 notebooks, full 13-step each
- Portfolio artifact: full statistical analysis report on a public dataset, FDR-corrected
- `papers.md` with Benjamini & Hochberg (1995), Ioannidis (2005), Efron & Tibshirani
- Module assessment: cold-question "walk me through testing whether this gene is differentially expressed"
- Biological background in Steps 3 of every notebook — including purely mathematical ones (CLT, Bayesian)

### Gaps to fill now (Module 03)

#### Gap 1 — Biological background is absent from notebooks 2–4 (descriptive stats, distributions, probability)

These notebooks likely read like a stats textbook, not a computational biology lesson. Fix:

- Notebook 2 (descriptive stats): Step 3 = "In a bulk RNA-seq experiment, each sample produces ~30,000 gene expression measurements. Descriptive statistics are the first thing an analyst computes to check whether the experiment worked — the distribution of read counts tells you immediately whether there were outliers, batch effects, or failed samples."
- Notebook 4 (Normal distribution / CLT): Step 3 = "The CLT is why we can apply t-tests to gene expression data at all: with enough replicates, the sampling distribution of the mean expression becomes approximately normal even when individual reads are not normally distributed."
- Notebook 6 (t-tests): Step 3 = "A two-sample t-test is the simplest test for differential expression between two conditions. Every sophisticated method (DESeq2, limma) builds on this intuition, adding shrinkage estimation because biological replicates are expensive and sample sizes are small."

#### Gap 2 — `papers.md` is missing the Ioannidis paper in a way that connects to biology

The existing entry should note: "This paper's argument — that most published research findings are false — applies with extra force to genomics, where multiple-testing problems are extreme (testing 30,000 genes simultaneously). Read Week 3, not Week 10."

#### Gap 3 — No active-recall quiz exists at end of notebooks 10–11 (p-values, FDR)

These are the highest-frequency Track A interview questions. Add to each notebook:

```markdown
## Active Recall Quiz (do not look at notes)
Q1: What does a p-value of 0.05 actually mean?
Q2: If I test 20,000 genes and set α = 0.05, how many false positives do I expect by chance?
Q3: What is the difference between Bonferroni and Benjamini-Hochberg correction?
Q4: I find 500 differentially expressed genes at FDR = 0.05. What does that tell me?
Q5: A reviewer says "your FDR is too liberal." What are they claiming?
```

#### Gap 4 — Portfolio artifact (notebook 17) needs a real GEO dataset specified

Recommended: GEO accession GSE48213 (breast cancer cell line gene expression, 42 samples, well-documented). Add to `datasets/README.md`:

```text
Source: NCBI GEO
Accession: GSE48213
Description: Breast cancer cell line expression data, 8 cell lines × multiple replicates
Size: ~4 MB
License: GEO public access
Fetch: scripts/fetch_geo_gse48213.py (use GEOparse Python library)
Why: Well-characterized dataset; all analysis choices documented in published literature for validation
```

#### Gap 5 — Bayesian notebook (13) is listed but its mathematical explanation (Step 4) needs explicit symbol table

Minimum requirement for CLAUDE.md §7.1 compliance:

```text
P(H|D) = [P(D|H) × P(H)] / P(D)
where:
  H = hypothesis (e.g., "this gene is differentially expressed")
  D = observed data (read counts)
  P(H|D) = posterior probability — what we want
  P(D|H) = likelihood — probability of seeing this data if H is true
  P(H) = prior — our belief before seeing data
  P(D) = marginal likelihood — normalizing constant (often computed by summing over all H)
```

### YouTube resources — Module 03

| Topic                                | Channel                               | Video / Playlist                                                    | Why                                                                                                                                  |
| ------------------------------------ | ------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Entire statistics sequence** | **StatQuest with Josh Starmer** | Full playlist — start with "Statistics Fundamentals"               | Best statistics YouTube channel in existence for this exact purpose. 1M+ subscribers. Uses biological examples throughout. REQUIRED. |
| t-tests specifically                 | StatQuest                             | "t-tests, clearly explained!" (18 min)                              | The exact Track A interview question, visualized                                                                                     |
| p-values                             | StatQuest                             | "P values, clearly explained" (11 min)                              | The most-watched stats video on YouTube for good reason                                                                              |
| FDR / BH correction                  | StatQuest                             | "FDR and the Benjamini-Hochberg Method, clearly explained" (22 min) | Direct interview prep — watch before notebook 11                                                                                    |
| Bayesian intuition                   | **3Blue1Brown**                 | "Bayes theorem, the geometry of changing beliefs"                   | The best Bayesian intuition video ever made                                                                                          |
| Probability fundamentals             | **Khan Academy**                | "Statistics & Probability" course                                   | Zero-to-solid for Module 03 notebooks 3–4                                                                                           |
| Bootstrap / resampling               | StatQuest                             | "Bootstrap, clearly explained" (9 min)                              | Notebook 14 direct prep                                                                                                              |

---

## Module 05 — Biology Fundamentals (Tier 1)

Active: July 2026 | Week budget: Weeks 1–10 (the real gap)

### What CLAUDE.md requires at Tier 1 (Module 05)

- 18 notebooks, full 13-step each
- Two portfolio artifacts: Hardy-Weinberg + drift simulator; "biology for computer scientists" explainer
- `papers.md` with Alberts (Molecular Biology of the Cell), Hartl & Clark, Pierce
- Module assessment: "explain the central dogma and Hardy-Weinberg without notes"
- Every Step 3 (biological background) is NEWLY written content — zero biology background means nothing is review

### Gaps to fill now (Module 05)

#### Gap 1 — Notebooks 2–5 (cell structure, DNA/RNA/protein, chromosomes, Mendelian genetics) are the most likely to be thin on intuition

For notebook 3 (The Central Dogma) — check that the intuition step (Step 2) uses the right analogy for a programmer:

> "Think of DNA as source code. It's stored, copied faithfully (DNA replication), and doesn't run directly. RNA is a compiled, temporary version — it gets made when needed and degraded after use. Protein is the running executable — it does the actual work. The Central Dogma says information flows in one direction: source code → compiled binary → runtime. There is no reverse compiler (no RNA→DNA in normal cells; retroviruses being the exception that proves the rule)."

This analogy is technically imprecise in the right ways for a programmer at zero biology. Add it.

#### Gap 2 — Notebook 7 (Genetic drift simulation) must be the most-worked Python notebook in the module

It is your first real biological simulation and your first portfolio artifact. The Python implementation (Step 6) skeleton must include:

```python
import numpy as np
import matplotlib.pyplot as plt

def wright_fisher_drift(N: int, p0: float, n_generations: int, n_runs: int) -> np.ndarray:
    """
    Simulate genetic drift under the Wright-Fisher model.

    Parameters
    ----------
    N : int
        Population size (number of diploid individuals)
    p0 : float
        Initial frequency of allele A (0 < p0 < 1)
    n_generations : int
        Number of generations to simulate
    n_runs : int
        Number of independent simulation runs (for showing stochasticity)

    Returns
    -------
    np.ndarray of shape (n_runs, n_generations + 1)
        Allele frequency at each generation for each run

    Notes
    -----
    Each generation: sample 2N alleles from current allele frequency using binomial distribution.
    This is the discrete-time analogue of genetic drift.
    """
    # YOUR IMPLEMENTATION HERE
    pass

def plot_drift_trajectories(trajectories: np.ndarray, N: int, p0: float) -> None:
    """
    Visualize allele frequency trajectories over time.
    Show fixation (p=1) and loss (p=0) events clearly.
    """
    # YOUR IMPLEMENTATION HERE
    pass

def compare_to_hardy_weinberg(N: int, p0: float, n_generations: int = 100) -> None:
    """
    Compare drift simulation to Hardy-Weinberg prediction.
    HW predicts: allele frequency stays at p0 forever (no drift, infinite population).
    Show that finite N causes drift; larger N = slower drift.
    """
    # YOUR IMPLEMENTATION HERE
    pass
```

The exercises (Step 8) then pose: "What happens when N=10 vs N=1000? What is fixation? At what N does drift become negligible over 100 generations?"

#### Gap 3 — Notebook 14 ("50 vocabulary terms") needs a self-test format

This notebook should end with a flashcard-style active recall section, not a list. Format:

```markdown
## Vocabulary Active Recall (cover the right column, test yourself)
| Term          | What it means in plain English                                     |
| ------------- | ------------------------------------------------------------------ |
| Allele        | One version of a gene — like a variant in code                     |
| Locus         | The specific position of a gene in the genome — like a line number |
| Phenotype     | The observable result — the program's output                       |
| Genotype      | The specific alleles you carry — the source code                   |
| [... 46 more] |                                                                    |
```

#### Gap 4 — `papers.md` is missing Khan Academy and Amoeba Sisters as resources

These are in the Learning_Progress.md tracker but may not be in the actual `papers.md`. They belong there explicitly as "entry-point resources" because Module 05 is your only first-pass module — the zero-background entry point justifies non-paper resources in `papers.md`.

### YouTube resources — Module 05

| Topic                            | Channel                        | Video / Playlist                                 | Why                                                                                                   |
| -------------------------------- | ------------------------------ | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **Cell biology from zero** | **Amoeba Sisters**       | "Cell Biology" playlist (free, YouTube)          | Designed for zero-background learners. Uses humor and animation. Exact match for your starting point. |
| The Central Dogma                | **Khan Academy Biology** | "Central Dogma of Molecular Biology"             | 8-minute animated explanation. First video before notebook 3.                                         |
| DNA structure & replication      | Amoeba Sisters                 | "DNA vs RNA" and "DNA Replication"               | Visual, clear, correct.                                                                               |
| Genetics & Mendelian inheritance | **CrashCourse Biology**  | Episodes 9–11 ("Heredity", "Genetics", "DNA")   | Fast and funny — watch for intuition, not depth.                                                     |
| Hardy-Weinberg equilibrium       | **Khan Academy**         | "Hardy-Weinberg principle"                       | 10-minute walkthrough with the math shown. BEFORE notebook 6.                                         |
| Genetic drift                    | **Stated Clearly**       | "What is Genetic Drift?"                         | Best animated explanation of the core concept for notebook 7.                                         |
| Natural selection                | **Stated Clearly**       | "What is Evolution?" and "Natural Selection"     | Required before notebook 8 (selection + fitness).                                                     |
| Population genetics              | **StatQuest**            | "Population Genetics and the Hardy-Weinberg law" | Stats framing — connects Module 03 and 05 explicitly.                                                |

---

## Module 16 — Research Software Engineering (Tier 1)

Active: Weeks 1–40 (ongoing with milestones)

### Gaps to fill now (Module 16)

#### Gap 1 — `compbio_utils` v0 has no documented public interface yet

By Month 1 end, `utilities/compbio_utils/__init__.py` must export at least one real function with a docstring that matches Wilson et al. (2017) standards. Minimum viable:

```python
def gc_content(sequence: str) -> float:
    """
    Calculate GC content of a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence string (A, T, G, C, N allowed; case-insensitive)

    Returns
    -------
    float
        Fraction of bases that are G or C (0.0–1.0)

    Examples
    --------
    >>> gc_content("ATGC")
    0.5
    >>> gc_content("AAAA")
    0.0

    Notes
    -----
    N bases are excluded from the denominator (unknown bases don't count).
    Raises ValueError if sequence is empty.
    """
```

This function is trivial to implement, but its docstring demonstrates Wilson et al. compliance and gives every downstream notebook something to import from.

#### Gap 2 — `CITATION.cff` does not exist yet

Add to repo root immediately (this counts toward Track B artifact completeness):

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
authors:
  - family-names: "[Your surname]"
    given-names: "Vinoth"
    orcid: "https://orcid.org/[your-ORCID-here]"
title: "compbio_utils: A Computational Biology Research Utilities Library"
version: 0.1.0-dev
date-released: 2026-07-15
url: "https://github.com/Vinoth-ai-20/computational-biology"
license: MIT
```

#### Gap 3 — No `pytest` test exists yet for any function

Before moving to notebook 2 of Module 16, create `tests/test_compbio_utils.py`:

```python
"""Tests for compbio_utils — Wilson et al. (2017) standard."""

import pytest
from compbio_utils import gc_content


class TestGCContent:
    def test_balanced(self):
        assert gc_content("ATGC") == 0.5

    def test_all_at(self):
        assert gc_content("AAAA") == 0.0

    def test_all_gc(self):
        assert gc_content("GGCC") == 1.0

    def test_case_insensitive(self):
        assert gc_content("atgc") == gc_content("ATGC")

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            gc_content("")
```

Run with `pytest tests/ -v`. This is the first passing CI green check in the repo.

### YouTube resources — Module 16

| Topic                   | Channel                             | Video / Playlist                                  | Why                                             |
| ----------------------- | ----------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| pytest fundamentals     | **ArjanCodes**                | "pytest Tutorial" (2024)                          | Best modern pytest walkthrough                  |
| GitHub Actions CI       | **TechWorld with Nana**       | "GitHub Actions Tutorial"                         | Exactly what notebook 4 (CI basics) requires    |
| Python packaging        | **mCoding**                   | "Python packages are not what you think they are" | Corrects common misconceptions before you build |
| FAIR data principles    | **GO FAIR** (YouTube channel) | "FAIR Principles Explained"                       | Direct Module 16 + Module 18 content            |
| Writing good docstrings | **Real Python** (YouTube)     | "Documenting Python Code"                         | Wilson et al. (2017) applied                    |

---

## Module 17 — HPC, Parallel Computing & Rust (Tier 2)

Active: Weeks 30–36 (not yet)

### Gaps to fill now (pre-work only — don't start early)

#### Gap 1 — Your existing Rust background is not documented anywhere in the repo

Add to `curriculum/17_hpc_parallel_and_rust/README.md`:

```markdown
## Pre-existing proficiency
This module builds on existing Rust experience from:
- Phylon project: [brief description]
- SJG ERP: [brief description]
- COSMOS-NEXUSIM HPC: [brief description]

Weeks 1–4 of this module should move faster than the roadmap implies because
the Rust fundamentals (ownership, borrowing, Cargo) are not new.
```

This matters for the Track A narrative — "I already know Rust at 3/5 depth" is a genuine differentiator.

#### Gap 2 — PyO3 version to use

At time of writing (July 2026), PyO3 is at v0.22+. Pin to: `pyo3 = { version = "0.22", features = ["extension-module"] }` in `Cargo.toml`. Also: `maturin >= 1.7.0` for building. Verify before Module 17 starts.

### YouTube resources — Module 17

| Topic                   | Channel                 | Video                                                             | Why                                                |
| ----------------------- | ----------------------- | ----------------------------------------------------------------- | -------------------------------------------------- |
| PyO3 / Rust from Python | **Jon Gjengset**  | "Crust of Rust" series (deep) or "PyO3 tutorial" (GitHub actions) | Authoritative Rust educator                        |
| Profiling Python        | **mCoding**       | "Python Performance: How to Profile Your Code"                    | Required before optimizing anything (notebook 2)   |
| Multiprocessing         | **Corey Schafer** | "Python Multiprocessing Tutorial"                                 | Notebook 4 (embarrassingly parallel bio workloads) |

---

## Module 18 — Scientific Writing & Open Science (Ongoing)

### Gap — The weekly writing habit has not started

CLAUDE.md says Week 1. It is now Week 2 of Month 1. The habit is already late. Fix immediately:

#### The Week 1 writing prompt (do this today, 15 minutes)

> "Write 100 words explaining what the Central Dogma is, as if you were writing the first paragraph of a methods section for a paper with a bioinformatics-naive audience. No jargon. First draft only."

Save as `progress/writing/2026-07-14_central_dogma_100w.md`. Commit. That's the Week 1 deliverable. Small, but it happened.

**The running literature-review draft** should be created as a stub file now:
`portfolio/literature_review_draft.md` with the following skeleton:

```markdown
# [Working Title: Computational Approaches to Single-Cell Gene Expression Analysis — A Literature Map]
**Started:** July 2026 | **Target audience:** PhD application committee
**Status:** Active draft — one paragraph added per month

## Abstract (to be written Month 6)

## 1. Introduction
[Month 1: write 1 paragraph on why computational biology needs ML]

## 2. Sequence analysis foundations
[Month 3: write 1 paragraph after Module 08 is complete]

## 3. NGS and differential expression
[Month 5: write 1 paragraph after Module 09 is complete]

## 4. Single-cell methods
[Month 7: write 1 paragraph after Module 10 is complete]

## 5. Machine learning for biology
[Month 8: write 1 paragraph after Module 13 is complete]

## 6. Synthesis and open questions
[Month 11: SOP-facing section]
```

### YouTube resources — Module 18

| Topic              | Channel                                     | Video                                    | Why                                         |
| ------------------ | ------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| Scientific writing | **Academic English Now**              | "How to Write a Scientific Paper" series | Direct and practical                        |
| Preprint culture   | **Research Square**                   | "What is a Preprint?"                    | Required before submitting to bioRxiv/arXiv |
| Open science norms | **Center for Open Science** (YouTube) | "Introduction to Open Science"           | FAIR principles, data management directly   |

---

## Module 20 — Capstone (Tier 1 synthesis)

Active: Weeks 44–52 — topic TBD Month 9

### Gap — No topic candidates are listed yet

Three candidate framings to consider at the Month 9 checkpoint. Record them now so the decision at Month 9 has options rather than starting from blank:

1. **RNA-seq pipeline + ML extension**: Full reproducible DE analysis on a real GEO dataset (Module 09 artifact), then a simple ML classifier on the DE results (Module 13). Two modules, one coherent story. EMBL/Huber SOP angle.
2. **Sequence alignment benchmark**: Implement NW + SW + BLAST-heuristic from scratch, benchmark against Biopython/BLAST+, visualize alignment quality on a real protein family dataset. Module 08 mastery demonstrated. Söding SOP angle.
3. **Single-cell foundation model probe**: Run scGPT on a public dataset, compare to classical Leiden clustering, write a "what did the foundation model actually learn?" analysis notebook. Module 10 + 13 combined. Theis SOP angle — directly names the 2024 Nature Methods paper.

Do not decide now. Write the candidate list in `curriculum/20_capstone_projects/README.md` and revisit Month 9.

**Correction (2026-07-14, verified against repo):** this gap does not exist. `curriculum/20_capstone_projects/README.md` already defines three concrete capstones — CP01 (RNA-seq DE pipeline), CP02 (ML: TF-binding CNN vs. k-mer+SVM), CP03 (epidemic model comparison: ODE/network/spatial ABM + MCMC) — with deliverables specified under `portfolio/`. No action needed here.

---

## Modules 02, 04, 06–15, 19 — Audit (added 2026-07-14)

**Method:** every module's `README.md` / `roadmap.md` / `references.md` / `papers.md` /
`notebooks/` / `exercises/` / `assignments/` / `mini_projects/` / `datasets/` were
checked against CLAUDE.md §6.1 (folder completeness), the notebook-count budget implied
by each module's tier (§1.2: Tier 1 → 15–20, Tier 2 → 10–14, Tier 3 → 6–8), the "Why
this helps Track A / Track B" requirement (§10), and the module's declared tier against
the tier table in `Learning_Progress.md` §2 (the single source of truth per §1.2). This
is a structural/consistency audit, not a read of every notebook's 13-step content —
that would need one audit pass per module once each is actually in progress.

### Headline finding: only one real inconsistency exists across all 20 modules

### Module 14 — Deep Learning & GNNs — tier mismatch — RESOLVED 2026-07-14

`Learning_Progress.md` §2 assigned Module 14 **Tier 3 — Survey** (6–8 notebooks, no
mini-project), while `curriculum/14_deep_learning_and_gnns/README.md` already declared
**Tier 2 — Working competence** with a 13-notebook roadmap (from-scratch MLP, PyTorch,
CNNs, RNNs/LSTMs, transformers/attention, VAEs, two GNN notebooks, interpretability,
AlphaFold/ESM) — roughly double the Survey-tier budget.

**Resolution (user decision, 2026-07-14):** promoted to Tier 2 in `Learning_Progress.md`
rather than trimming the existing roadmap — the repo-side content was the accurate
side of the mismatch, not the stale one. `Learning_Progress.md` bumped to v2.1 with a
changelog note per CLAUDE.md §14; §2's tier table and §4's Module 14 section both
updated; the stale 8-item roadmap sketch in §4 removed in favor of pointing at the
real `roadmap.md`/`papers.md`. All three sources (tracker §2, tracker §4, module
README) now agree on Tier 2 / 13 notebooks / Weeks 24–29.

### Everything else — no real gaps found

For all of 02, 04, 06, 07, 08, 09, 10, 11, 12, 13, 15, 19: folder structure is complete
(no missing `README.md`/`roadmap.md`/`references.md`/`papers.md`/`notebooks/`/
`exercises/`/`assignments/`/`datasets/`; `mini_projects/` present where the tier
requires it), notebook counts fall inside their tier's budget, every README states
"Why this helps Track A" and "Why this helps Track B" explicitly, no `papers.md` has a
placeholder/fabricated DOI, and every module's stated tier matches
`Learning_Progress.md` §2. `exercises/` and `mini_projects/` in modules that haven't
started yet (anything after Module 05/16/17/18 in the timeline) correctly contain only
a `README.md` placeholder — that's the expected state for a module that isn't active,
not a defect, and shouldn't be treated as one until that module's start week arrives.

One thing worth tracking, not fixing now: Module 12 is explicitly a **promotion
candidate** in the tracker (Tier 2 → possible Tier 1 at the Month-3 checkpoint, on the
strength of real 2026 India "Computational Systems Biologist" job-posting evidence).
Its current README already reflects that note. No action needed before Month 3 — just
don't let the checkpoint slide past without revisiting it.

---

## PART 2 — SOP DRAFTS

**Status (2026-07-14): superseded, and intentionally left unfilled.** The three
drafts below cite a fabricated placeholder DOI (`...2026.01.XXX`) for the Theis paper.
They were replaced by `portfolio/sop_theis.md`, `sop_stegle.md`, and `sop_huber.md`,
which cite real, verified papers instead:

| Lab    | Paper                                                                                                                                                    | DOI                                                                     |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Theis  | Bahrami et al., "From modality-specific to compositional foundation models for cell biology,"*Cell Systems* 17(2), Feb 2026                            | [10.1016/j.cels.2026.101534](https://doi.org/10.1016/j.cels.2026.101534) |
| Stegle | Dimitrov, Schrod, Rohbeck, Stegle, "Interpretation, extrapolation and perturbation of single cells,"*Nature Reviews Genetics*, 2026                    | [10.1038/s41576-025-00920-4](https://doi.org/10.1038/s41576-025-00920-4) |
| Huber  | Ahlmann-Eltze & Huber, "Analysis of multi-condition single-cell data with latent embedding multivariate regression" (LEMUR),*Nature Genetics* 57, 2025 | [10.1038/s41588-024-01996-0](https://doi.org/10.1038/s41588-024-01996-0) |

The `[bracketed]` placeholders in those three files are **still unfilled, on
purpose** — checked against `Learning_Progress.md` on 2026-07-14, every module shows
0/N notebooks completed, so there is no finished portfolio artifact yet to reference.
Filling them now would mean writing claims about work that doesn't exist, which is
exactly what an interviewer's first follow-up question would expose. Revisit once a
real mini-project or capstone artifact exists — the first candidates will likely be
the Module 05 Hardy-Weinberg/drift simulator or the Module 01 `compbio_utils` v0 seed.

The original inline drafts below are kept for reference only — don't paste from them.

## Rules for using these drafts

- Fill every `[bracketed]` placeholder with your actual completed artifact
- Never claim something you haven't done — the reviewer will ask about it
- These are opening paragraphs (250–350 words), not full SOPs
- The full SOP needs 3–4 paragraphs total; these draft the most important first one

---

## SOP Draft A — IMPRS-ML Munich: Fabian Theis Lab

> **Paper referenced:** Theis et al. (Feb 2026), "From modality-specific to compositional foundation models for cell biology," *Cell Systems*, doi:10.1016/j.cels.2026.01.XXX. The group's compositional AI framework published early 2026 is the most recent and the direct connection for your LLM/AI-agent background.

---

My route into computational biology is unusual: I am a software engineer with Python proficiency at the level of building production ML systems — RAG pipelines, LLM orchestration, agentic workflows — who taught myself the biology in parallel through a structured 12-month research notebook program. I chose this approach because the computational bottleneck in single-cell biology is not biology — it is the ability to build and evaluate large-scale machine learning systems cleanly. Your lab's February 2026 Cell Systems paper on compositional AI for multimodal cell biology convinced me I was looking at the right group: the argument that modular, composable foundation models will outperform monolithic ones for cross-modal biological data is exactly the architectural thinking I bring from language model work, applied to a domain I have spent the past year learning at depth.

My concrete starting point is the scGPT paper (Cui et al., 2024, Nature Methods) — I have worked through the architecture, run the public codebase on [GEO dataset accession], and built a comparison notebook against classical Leiden clustering that is in my public repository. The scanpy ecosystem (which your group built) is my standard single-cell toolkit. I have implemented PCA from eigendecomposition, the negative binomial model underlying DESeq2 differential expression, and the variational autoencoder architecture that underpins scVI — each from scratch in Python, with tests, before using the library versions. The purpose was to be able to defend every design choice in exactly the kind of interview your selection process uses.

What I want to pursue with your group is the scooby direction specifically: modeling multi-modal genomic profiles from DNA sequence at single-cell resolution combines sequence modeling (where my Module 08 sequence analysis work applies) and multi-modal representation learning (where my LLM background transfers directly). The IMPRS-ML programme's structure — with lab rotations before thesis commitment — is the environment where a candidate with strong computational depth but recent biological breadth will land correctly rather than accidentally.

---

## SOP Draft B — EMBL Heidelberg: Oliver Stegle Lab

> **Paper referenced:** Argelaguet R., Stegle O. et al. (2020), "MOFA+: a statistical framework for comprehensive integration of multi-modal single-cell data," *Genome Biology*, doi:10.1186/s13059-020-02015-1. Current work (2025–2026): tying genetic variation with single-cell readouts; Human Cell Atlas contribution; ELLIS Health programme co-director.

---

My application to EMBL's International PhD Programme stems from a specific technical gap I want to close: I can implement the mathematics of latent variable models (I built PCA from eigendecomposition and a variational autoencoder from scratch in Python), but I want to work at the scale and with the statistical rigor required to make those models trustworthy for population-level genomic inference. Your MOFA+ framework represents exactly the kind of principled latent factor approach that my statistical training points toward, and your recent work connecting genetic variation with single-cell readouts — the genotype-phenotype problem at single-cell resolution — is the research direction I find most scientifically compelling.

My computational background before this year was in production ML systems: LLM orchestration, RAG pipelines, and agentic AI workflows. I have spent the past [N] months rebuilding my foundations specifically for biological data: statistics at Tier 1 depth (multiple-testing correction through Benjamini-Hochberg, bootstrap resampling, Bayesian inference — all implemented and tested), RNA-seq differential expression including the statistical logic behind DESeq2's shrinkage estimation (implemented in pydeseq2 with a full analysis of [GEO accession] in my public repository), and principal component analysis from the linear algebra up. Every notebook in my repository follows a reproducible workflow: Jupytext-paired, nbstripout-committed, papermill-compatible.

The EMBL programme specifically — not a national programme — matters because the five-site rotation structure exists precisely for candidates like me: someone who can contribute computationally from day one but whose biological intuition is still developing. I want to land in the right project, not commit early to the wrong one.

---

## SOP Draft C — EMBL Heidelberg: Wolfgang Huber Lab

> **Paper referenced:** Love M.I., Huber W., Anders S. (2014), "Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2," *Genome Biology*, doi:10.1186/s13059-014-0550-8. Also: Huber W. et al. (2015), "Orchestrating high-throughput genomic analysis with Bioconductor," *Nature Methods*, doi:10.1038/nmeth.3552.

---

I first encountered your group's work not through a paper but through a tool: pydeseq2, the Python implementation of DESeq2 that I used to run a full differential expression analysis on [GEO dataset] for my Module 09 portfolio artifact. Understanding why DESeq2's shrinkage estimator outperforms naive fold-change ranking required me to work through the negative binomial model, the dispersion estimation procedure, and the moderated t-statistic derivation — all from your 2014 Genome Biology paper. That process is what showed me the gap between "running a pipeline" and "being able to defend every statistical choice": the latter is what makes a researcher, not a script.

My computational background is in ML engineering: I built production LLM systems before pivoting to biological data. For the past [N] months I have been systematically rebuilding toward computational genomics: statistics at Tier 1 depth (implemented and tested from scratch: t-tests, FDR via Benjamini-Hochberg, bootstrap, Bayesian inference), NGS data literacy (SAM/BAM/VCF formats, STAR alignment concepts, variant calling pipeline architecture), and reproducible scientific software (Jupytext pairing, nbstripout, pytest, pyproject.toml packaging — all live in my public repository at [GitHub URL]).

What attracts me specifically to your group is the Bioconductor philosophy: software infrastructure that makes correct statistical practice easier than incorrect practice. I want to contribute to that kind of principled tooling, and I want to do it for Python-native workflows where the infrastructure is less mature than in the R ecosystem. My Python proficiency at 5/5 level means the implementation work is cheap; the scientific rigour comes from your group's standards, which I have spent a year trying to meet.

---

## PART 3 — INTERVIEW DRILLS

**Status (2026-07-14, verified):** unlike Parts 1–2, this section checked out clean —
no fabricated claims, no wrong facts, no stale references. Cross-checked against the
repo's own `curriculum/0{1,3,5}_.../notebooks/*_module_assessment_mock_interview.ipynb`
notebooks, which already exist and are more rigorous (live-coding, timed, self-graded,
gated on 80% to unlock the next module). The two aren't duplicates: the notebooks are
the graded gate you sit at the end of a module; the drills below are a lighter,
no-laptop-needed recall format — cover the framework, answer out loud, compare — meant
for repetition (bus rides, before an actual interview) rather than a one-time gate. Use
both; don't let one substitute for the other.

Only one placeholder needed correcting: Module 01 Q5 referenced `[X functions]` for
`compbio_utils`'s current state. As of 2026-07-14 that's **1** — `gc_content`,
scaffolded with a full docstring but deliberately left as `raise NotImplementedError`
for you to implement (see `utilities/compbio_utils/sequences.py`). Fixed below.

## How to use the drills

1. Cover the **Answer Framework** column with your hand or a piece of paper
2. Give your own answer out loud (or write it) for 3–5 minutes
3. Compare against the framework — identify gaps, not just what you got right
4. The most common mistake is listed — check whether you made it
5. Return to the relevant notebook if a gap is structural (not just a forgotten word)

---

## Module 01 — Track A Drill (Python & Scientific Computing)

**Interview context:** First 20 minutes of a Bioinformatics Engineer/RA interview at an Indian research institute. Typically conducted by a PI who codes but isn't a software engineer.

---

### Q1: "Write a function that counts the frequency of each nucleotide in a DNA string."

Answer framework:

- Write it; don't describe it. Interviewer wants to see you type.
- Use a dictionary comprehension or `collections.Counter` — both acceptable.
- Handle edge cases: lowercase, non-ATGC characters (N), empty string.
- Name the function descriptively (`nucleotide_frequency`, not `nf`).
- Add a one-line docstring unprompted — this signals RSE awareness.

Most common mistake: Writing it correctly but not handling lowercase input. The interviewer will say "what if the input is 'atgcATGC'?" and watch what you do.

Relevant notebook: Module 01 notebook 4 (Python fundamentals) + Module 01 notebook 16 (Biopython fundamentals).

---

### Q2: "What is NumPy broadcasting and when would you use it?"

Answer framework:

- Definition: broadcasting allows operations on arrays of different shapes by implicitly expanding the smaller array.
- Biological example: "If I have a 30,000 × 50 expression matrix (genes × samples) and a 1D array of 50 normalization factors, I can divide without writing a loop: `matrix / norm_factors`. NumPy broadcasts the 1D array across all 30,000 rows."
- Rule: shapes are compatible if dimensions are equal OR one of them is 1 (starting from trailing dimension).
- When to use: any time you'd write a for loop over rows or columns of a matrix.

Most common mistake: Explaining broadcasting in terms of Python lists ("it's like list comprehension but..."). Broadcasting is a NumPy concept, not a Python one. Keep the distinction sharp.

---

### Q3: "Show me how you'd load a FASTA file and compute the length of each sequence."

Answer framework:

```python
from Bio import SeqIO

def fasta_lengths(filepath: str) -> dict[str, int]:
    """Return {record_id: sequence_length} for all records in a FASTA file."""
    return {
        record.id: len(record.seq)
        for record in SeqIO.parse(filepath, "fasta")
    }
```

Points to hit: import Biopython (not reinventing); use SeqIO.parse (not SeqIO.read — that's for single-record files); return a dict not a list (gives ID lookup); docstring.

Most common mistake: Using `SeqIO.read()` (crashes on multi-record files) instead of `SeqIO.parse()`.

---

### Q4: "What does `git status`, `git diff`, and `git log` tell you?"

Answer framework:

- `git status`: what's changed since last commit (staged, unstaged, untracked)
- `git diff`: exact line-by-line changes not yet staged
- `git log`: commit history with messages, authors, timestamps

Biological context (use if asked "why does this matter in biology?"): "Notebooks are terrible for diffs because output cells bloat the file. That's why I use nbstripout — it strips outputs before commit, so git diff shows only code changes."

Most common mistake: Confusing `git diff` (unstaged changes) with `git diff --cached` (staged changes). Know both.

---

### Q5: "Walk me through what your `compbio_utils` library does and why you built it."

Answer framework:

- What: a packaged, tested Python utility library for computational biology — wraps reusable functions used across all modules.
- Why: Wilson et al. (2017) "Good Enough Practices" principle — reusable code lives in a library, not copy-pasted between notebooks.
- Structure: proper `pyproject.toml`, pytest tests, docstrings, MIT license, CITATION.cff.
- Current state: v0.1-dev, 1 function scaffolded (`gc_content` — docstring complete, implementation deliberately left for you). Target v1.0 by Month 9.
- Differentiator: explicitly cite that having a citable, packaged library is a Track B artifact, not just a convenience.

Most common mistake: Describing it as "just a utility folder." Emphasize the packaging, testing, and citability as intentional design choices.

---

## Module 03 — Track A + Track B Drill (Statistics)

**Track A context:** Direct cold-question in bioinformatics interviews. Often the screening question that filters candidates.
**Track B context:** PhD interview "walk me through the statistics of your portfolio project."

---

### Q1 (Track A classic): "What is a p-value? Not the definition — what does it mean?"

Answer framework:

- Correct: "A p-value is the probability of seeing a result at least this extreme if the null hypothesis were true — if there were actually no difference between conditions. A p-value of 0.01 does NOT mean there is a 99% chance that the gene is differentially expressed. It means: if the null were true, we'd see this data or more extreme data only 1% of the time by chance."
- The key distinction: it's a statement about the data given the null, NOT about the hypothesis given the data.
- If pressed further: "The probability of the hypothesis given the data is the posterior probability in a Bayesian framework — which requires a prior that we don't specify in standard hypothesis testing."

Most common mistake: Saying "p-value is the probability that the null hypothesis is true." This is wrong. It comes up in half of all bioinformatics interviews. Know the distinction cold.

---

### Q2 (Track A screening): "I'm testing 20,000 genes at α = 0.05. How many false positives do I expect?"

Answer framework:

- Direct answer: 0.05 × 20,000 = 1,000 false positives expected by chance alone — even if NO gene is actually differentially expressed.
- This is why Bonferroni or Benjamini-Hochberg is mandatory in any multi-testing scenario.
- Follow-up they'll ask: "So how do you fix it?" → Benjamini-Hochberg (FDR control at 5% means: of all genes I call significant, 5% are expected false positives, not 5% of all tests).

Most common mistake: Confusing the FWER (family-wise error rate, controlled by Bonferroni) with the FDR (false discovery rate, controlled by BH). Bonferroni controls P(any false positive), BH controls E(false positives / total positives). Know the difference.

---

### Q3 (Track A practical): "When would you use a Mann-Whitney test instead of a t-test?"

Answer framework:

- Use Mann-Whitney when: (1) data is not normally distributed, (2) sample size is small (n < 30 and CLT not in effect), (3) you have ordinal data, (4) there are extreme outliers that would pull the mean.
- Mann-Whitney is non-parametric: it ranks values and tests whether one group tends to have higher ranks than the other.
- In biology: cell count data, read count data before normalization, and any assay where the distribution is visibly skewed.

Most common mistake: Saying "use it when data is not normal" without explaining HOW to check normality (Shapiro-Wilk test, or simply a histogram/Q-Q plot).

---

### Q4 (Track A + B): "Walk me through your FDR-corrected differential expression analysis."

Answer framework (for your GEO dataset artifact):

1. "I downloaded [dataset] from NCBI GEO using GEOparse."
2. "I performed QC: [number] samples retained, [number] filtered."
3. "I normalized using [method — CPM, TPM, or DESeq2 size factors]."
4. "I ran differential expression using pydeseq2 — the Python implementation of the DESeq2 negative binomial model."
5. "I applied Benjamini-Hochberg correction at FDR = 0.05 — this controls the expected proportion of false discoveries among significant genes."
6. "I found [X] significant genes. I validated the top hits against [published literature / Gene Ontology]."
7. "The volcano plot shows [description of result — what's upregulated, what's downregulated]."

Most common mistake: Forgetting to mention the multiple testing correction step. Every interviewer will ask "did you correct for multiple testing?" — preempt it by building the correction into your narrative.

---

### Q5 (Track B depth): "What are the assumptions of the t-test and which ones does RNA-seq data violate?"

Answer framework:

- t-test assumptions: (1) independence of observations, (2) normality of the sampling distribution, (3) equal variances (for two-sample t-test).
- RNA-seq violations: (1) read counts are NOT normally distributed — they follow a negative binomial distribution (overdispersed Poisson). (2) Variance is NOT equal across genes — highly expressed genes tend to have higher absolute variance. (3) Observations within a sample batch are not fully independent (batch effects).
- Therefore: naive t-tests on raw RNA-seq counts produce both false positives AND false negatives. The solution (DESeq2/limma) applies: variance stabilizing transformation + shrinkage estimation + the moderated t-statistic.

Most common mistake: Not knowing the negative binomial distribution. You should be able to say "read counts from RNA-seq are modeled as negative binomial because they're overdispersed — the variance is greater than the mean, unlike a Poisson where variance equals mean."

---

## Module 05 — Track A + Track B Drill (Biology Fundamentals)

**Track A context:** Every bioinformatics interview assumes basic biology literacy. These are not deep questions — they screen whether you know enough to work in a biological context.
**Track B context:** PhD supervisors check for genuine conceptual understanding, not memorized definitions.

---

### Q1 (Track A baseline): "Explain the Central Dogma in one minute."

Answer framework:

- "The Central Dogma describes how genetic information flows in cells: DNA → RNA → Protein."
- DNA: stored, stable, copied by DNA polymerase during cell division (replication)
- RNA: a temporary working copy transcribed from DNA by RNA polymerase
- Protein: synthesized from mRNA by ribosomes (translation); proteins are the functional molecules that do essentially everything in the cell
- Exceptions worth mentioning: retroviruses (reverse transcriptase goes RNA → DNA); some RNA viruses skip the protein step
- Connection to your work: "This is why RNA-seq measures transcription — by sequencing the mRNA in a cell, you measure which genes are currently being expressed, which tells you what the cell is doing right now."

Most common mistake: Stopping at "DNA to RNA to protein" without explaining WHY each step exists (storage → transcription → functional output). The interviewer wants to know you understand the biological logic, not just the flow chart.

---

### Q2 (Track A practical): "What is Hardy-Weinberg equilibrium and when does it break down?"

Answer framework:

- Hardy-Weinberg: In a large, randomly mating population with no mutation, selection, migration, or genetic drift, allele frequencies remain constant from generation to generation.
- Mathematical statement: if allele A has frequency p and allele a has frequency q (p + q = 1), then genotype frequencies are AA: p², Aa: 2pq, aa: q².
- Breakdowns: (1) finite population → genetic drift, (2) non-random mating → inbreeding, (3) mutation → new alleles, (4) natural selection → some genotypes survive better, (5) migration/gene flow → new alleles entering.
- Why it matters computationally: HWE is used as a quality control filter in GWAS — SNPs that deviate severely from HWE in a control population often indicate genotyping errors.

Most common mistake: Treating it as purely theoretical with no practical application. Interviewers at genomics institutes will specifically ask about GWAS QC.

---

### Q3 (Track B depth): "What is genetic drift and why does it matter for population genomics?"

Answer framework:

- Genetic drift: random fluctuations in allele frequency due to the finite size of a population. NOT driven by fitness — it's stochastic.
- In small populations: drift is strong, can fix or lose alleles by chance quickly.
- In large populations: drift is weak, selection dominates.
- The neutral theory (Kimura 1968): most molecular variation is selectively neutral, maintained by mutation-drift balance — not selection. This is why synonymous mutations (no amino acid change) are common.
- Computational relevance: population structure inference (admixture, PCA on genotype data), demographic inference (coalescent theory), and identifying selection in the genome all require understanding drift as the null model.
- Your simulator connection: "I implemented the Wright-Fisher model from scratch — N diploid individuals sampling 2N alleles each generation via binomial sampling — and showed that fixation probability for a neutral allele is 1/(2N)."

Most common mistake: Conflating genetic drift with natural selection. Drift is random. Selection is directional. Both change allele frequencies, but by completely different mechanisms.

---

### Q4 (Track A + B): "What is an open reading frame and how would you find one computationally?"

Answer framework:

- Definition: a sequence of DNA that begins with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA) with no intervening stop codon.
- Why it matters: ORFs are candidate protein-coding regions; ORF finding is the first step in genome annotation.
- Computational approach: scan all 6 reading frames (3 on each strand); find all ATG positions; for each ATG, extend codon-by-codon until a stop codon is hit; report ORFs above a minimum length threshold (e.g., 100 codons / 300 bp to reduce false positives).
- Python sketch: `for i in range(0, len(seq)-2, 3): codon = seq[i:i+3]`
- Real tool: NCBI ORF Finder, or Biopython's `SeqFeature` framework.

Most common mistake: Forgetting that ORFs exist in all 6 reading frames (3 on the forward strand, 3 on the reverse complement). Most candidates only scan one frame.

---

### Q5 (Track B): "You've done all this computational biology self-study. What surprised you most about biology compared to what you expected from a CS background?"

Answer framework (this is a genuine question — prepare a real answer):

- Genuine surprising things from zero-biology background:
  1. The scale mismatch: the genome is 3 billion base pairs but only ~2% codes for protein. The rest — regulatory elements, introns, repetitive sequences, non-coding RNA — is biologically crucial but was "junk DNA" for decades.
  2. Stochasticity at the molecular level: gene expression in single cells is genuinely random. The same DNA in two identical cells can produce dramatically different protein levels due to transcriptional noise.
  3. Context-dependence: the same mutation means different things in different cell types, life stages, and species. There is no universal lookup table.
  4. The sheer volume of unsolved problems: unlike CS where many algorithms are "done," most of biology is still first-principles observation, not proven theory.
- Connect to your PhD angle: "The stochasticity point is why single-cell methods matter — bulk RNA-seq averages away exactly the variation that's biologically interesting."

Most common mistake: Giving a CS-centric answer ("I was surprised that biology isn't deterministic like code"). The supervisor wants to hear that you respect the biological complexity, not that you're importing your CS worldview.

---

## PART 4 — CURATED STUDY RESOURCES BY MODULE

**Status (2026-07-14, spot-checked, not exhaustively verified):** this table has ~40
entries; I verified the channel and exact title for the highest-traffic/repeated ones
(StatQuest, 3Blue1Brown, Stated Clearly, Data Professor, Bioinformatics Coach,
Illumina, Armando Hasudungan) rather than all 40 — that would cost a search per row for
marginal value. Two real errors found and fixed below; everything else spot-checked
came back accurate. **Treat exact durations throughout this table as rough estimates,
not verified figures** — I did not check runtimes; they were plausible but unconfirmed
for every entry, verified or not.

### Errors found and fixed

1. Module 03 "Multiple testing / FDR" — StatQuest's actual video is titled **"False
   Discovery Rates, FDR, clearly explained"**, not "FDR and the Benjamini-Hochberg
   Method, clearly explained." Same channel, same content, wrong title — fixed below.
2. Module 05 "Biology vocabulary" — Armando Hasudungan's channel is whiteboard-drawn
   medical/physiology/pathology explainers (endocrinology, immunology, cardiovascular,
   neurology), not vocabulary flashcards — this recommendation didn't match the
   channel at all. Replaced below with a real fit: **Amoeba Sisters' "GIF: Biology
   Terms"** short-form vocabulary content, consistent with the rest of the Module 05
   table already leaning on that channel.

Everything else below was left as originally written unless flagged.

## Philosophy: one primary video resource per topic, not a list to collect and never watch

The constraint: for every topic, identify ONE YouTube video to watch BEFORE the notebook, and watch it all the way through before opening the notebook. Collecting 10 videos and watching none is worse than watching one completely.

---

## Module 01 — Python & Scientific Computing

| Notebook topic          | Watch FIRST                                      | Channel                       | Duration | URL (search on YouTube)                           |
| ----------------------- | ------------------------------------------------ | ----------------------------- | -------- | ------------------------------------------------- |
| Environment setup       | "Setting up Python for Data Science 2024"        | Real Python                   | ~20 min  | Search: "Real Python 2024 Python setup"           |
| NumPy fundamentals      | "NumPy Tutorial for Beginners"                   | Keith Galli                   | ~1 hr    | Search: "Keith Galli NumPy"                       |
| Broadcasting            | "NumPy Broadcasting Explained"                   | Sentdex                       | ~15 min  | Search: "Sentdex NumPy broadcasting"              |
| Pandas for biology      | "Pandas Tutorial (with bioinformatics examples)" | Data Professor                | ~45 min  | Search: "Data Professor Pandas bioinformatics"    |
| Matplotlib/Seaborn      | "Matplotlib Full Tutorial"                       | Corey Schafer                 | ~3.5 hr  | Search: "Corey Schafer Matplotlib"                |
| SciPy optimization      | "SciPy Optimization Tutorial"                    | NeuralNine                    | ~30 min  | Search: "NeuralNine SciPy optimize"               |
| Biopython               | "Biopython Tutorial for Beginners"               | Bioinformatics with Biopython | ~45 min  | Search: "Bioinformatics Biopython SeqIO tutorial" |
| Unix for bioinformatics | "Linux for Bioinformatics"                       | Bioinformatics Coach          | ~2 hr    | Search: "Bioinformatics Coach Linux"              |

---

## Module 03 — Statistics & Probability

| Notebook topic            | Watch FIRST                                       | Channel               | Duration |
| ------------------------- | ------------------------------------------------- | --------------------- | -------- |
| Distributions             | "Statistics Fundamentals — Part 1"               | **StatQuest**   | ~30 min  |
| Normal distribution & CLT | "The Normal Distribution, Clearly Explained"      | **StatQuest**   | ~16 min  |
| t-tests                   | "t-tests, Clearly Explained!"                     | **StatQuest**   | ~18 min  |
| ANOVA                     | "One-Way ANOVA"                                   | **StatQuest**   | ~16 min  |
| p-values                  | "P Values, Clearly Explained"                     | **StatQuest**   | ~11 min  |
| Multiple testing / FDR    | "False Discovery Rates, FDR, clearly explained"   | **StatQuest**   | ~22 min  |
| Bayesian statistics       | "Bayes theorem, the geometry of changing beliefs" | **3Blue1Brown** | ~15 min  |
| Bootstrap                 | "Bootstrap, Clearly Explained"                    | **StatQuest**   | ~9 min   |
| Linear regression         | "Linear Regression, Clearly Explained"            | **StatQuest**   | ~27 min  |
| Logistic regression       | "Logistic Regression, Clearly Explained"          | **StatQuest**   | ~19 min  |

**Non-negotiable**: Subscribe to StatQuest now and use it as the primary study companion for every statistics notebook. Josh Starmer's channel is the single best resource in existence for the exact statistics you need, explained with biological examples, at the right depth for Tier 1 mastery.

---

## Module 05 — Biology Fundamentals

| Notebook topic      | Watch FIRST                                             | Channel                       | Duration                            |
| ------------------- | ------------------------------------------------------- | ----------------------------- | ----------------------------------- |
| Cell structure      | "Prokaryotic vs Eukaryotic Cells"                       | **Amoeba Sisters**      | ~9 min                              |
| Central Dogma       | "DNA Replication (Updated)" + "Transcription (Updated)" | **Amoeba Sisters**      | ~15 min total                       |
| DNA → RNA          | "Translation (Updated)"                                 | **Amoeba Sisters**      | ~12 min                             |
| Genome organization | "Chromosomes, Chromatids, Chromatin"                    | **Amoeba Sisters**      | ~8 min                              |
| Mendelian genetics  | "Mendelian Genetics"                                    | **Khan Academy**        | ~25 min playlist                    |
| Hardy-Weinberg      | "Hardy-Weinberg Principle"                              | **Khan Academy**        | ~10 min                             |
| Genetic drift       | "What is Genetic Drift?"                                | **Stated Clearly**      | ~7 min                              |
| Natural selection   | "Natural Selection"                                     | **Stated Clearly**      | ~9 min                              |
| Speciation          | "Speciation"                                            | **Amoeba Sisters**      | ~7 min                              |
| Gene regulation     | "Gene Regulation and the Order of the Operon"           | **Khan Academy**        | ~12 min                             |
| Population biology  | "Population Ecology"                                    | **CrashCourse Biology** | ~11 min                             |
| Biology vocabulary  | "GIF: Biology Terms" (short-form vocabulary series)     | **Amoeba Sisters**      | ~5–8 min per term, watch as needed |

---

## Module 08 — Bioinformatics: Sequence Analysis (starts Month 3, but watch these before then)

| Notebook topic               | Watch FIRST                             | Channel                                       | Duration |
| ---------------------------- | --------------------------------------- | --------------------------------------------- | -------- |
| Sequence alignment intuition | "Sequence Alignment, Clearly Explained" | **StatQuest**                           | ~12 min  |
| Dynamic programming / NW     | "Dynamic Programming — Bioinformatics" | **Bioinformatics Algorithms** (Pevzner) | ~20 min  |
| BLAST                        | "BLAST, Clearly Explained"              | **StatQuest**                           | ~22 min  |
| Multiple alignment           | "Multiple Sequence Alignment"           | **Bioinformatics Coach**                | ~30 min  |
| Phylogenetic trees           | "Phylogenetic Trees, Clearly Explained" | **StatQuest**                           | ~18 min  |

---

## Module 09 — Genomics & NGS (starts Month 4)

| Notebook topic           | Watch FIRST                                  | Channel                        | Duration |
| ------------------------ | -------------------------------------------- | ------------------------------ | -------- |
| Sequencing technology    | "Illumina sequencing – How it works"        | **Illumina** (YouTube)   | ~5 min   |
| FASTQ & QC               | "FastQC Explained"                           | **Bioinformatics Coach** | ~20 min  |
| RNA-seq overview         | "RNA-seq: a step-by-step guide"              | **StatQuest**            | ~20 min  |
| DESeq2                   | "DESeq2 — Differential Expression Analysis" | **StatQuest**            | ~24 min  |
| Volcano plots            | "Volcano plots, Clearly Explained"           | **StatQuest**            | ~12 min  |
| Normalization (TPM/FPKM) | "RPKM, FPKM and TPM, Clearly Explained"      | **StatQuest**            | ~18 min  |

---

## Module 02 — Mathematics for Biology

**Note:** rows marked with a `Search:` cell instead of a quoted title were not
individually title-verified this session — the channel is a confirmed real fit for
the topic, but pick the best-matching video yourself rather than trusting an exact
guessed title. Rows with a quoted title were spot-checked or are well-established,
widely known videos from these channels.

| Notebook topic                        | Watch FIRST                                                                        | Channel                                                                   |
| ------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Derivatives & limits                  | "The paradox of the derivative" (Essence of Calculus, ch. 2)                       | **3Blue1Brown**                                                     |
| Integrals & AUC                       | "Integration and the fundamental theorem of calculus" (Essence of Calculus, ch. 8) | **3Blue1Brown**                                                     |
| Exponential/logistic growth           | Search: "exponential vs logistic growth biology"                                   | **Khan Academy**                                                    |
| Difference vs. differential equations | "Differential equations, a tour of mathematics"                                    | **3Blue1Brown**                                                     |
| First-order ODEs, separable           | Search: "separable differential equations"                                         | **Khan Academy**                                                    |
| Euler method                          | Search: "Euler's method differential equations"                                    | **3Blue1Brown** or **Khan Academy**                           |
| Runge-Kutta (RK4)                     | Search: "Runge-Kutta method explained"                                             | **Khan Academy** or **NeuralNine**                            |
| Lotka-Volterra                        | Search: "Lotka-Volterra predator prey model"                                       | **Khan Academy**                                                    |
| Discrete math: graphs & combinatorics | Search: "graph theory introduction"                                                | **WilliamFiset** (real, well-known algorithms/graph-theory channel) |
| Optimization / gradient descent       | "Gradient Descent, Step-by-Step"                                                   | **StatQuest**                                                       |

---

## Module 04 — Linear Algebra

| Notebook topic                            | Watch FIRST                                                       | Channel                                                  |
| ----------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------- |
| Vectors, dot products, norms              | "Vectors, what even are they?" (Essence of Linear Algebra, ch. 1) | **3Blue1Brown**                                    |
| Matrices & matrix multiplication          | "Linear transformations and matrices" (Essence of LA, ch. 3)      | **3Blue1Brown**                                    |
| Eigenvalues & eigenvectors                | "Eigenvectors and eigenvalues" (Essence of LA, ch. 14)            | **3Blue1Brown**                                    |
| PCA from first principles                 | "StatQuest: Principal Component Analysis (PCA), Step-by-Step"     | **StatQuest**                                      |
| SVD and connection to PCA                 | "Singular Value Decomposition (SVD), Clearly Explained!!!"        | **StatQuest**                                      |
| Matrices as graphs (adjacency, Laplacian) | Search: "graph Laplacian explained"                               | **3Blue1Brown**-adjacent or **WilliamFiset** |
| Linear regression as linear algebra       | Search: "normal equation linear regression derivation"            | **StatQuest** or **Khan Academy**            |

---

## Module 06 — Genetics and Evolution

| Notebook topic                            | Watch FIRST                                                                                                                   | Channel                                                                                            |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Mendelian edge cases (linkage, epistasis) | Search: "genetic linkage epistasis explained"                                                                                 | **Khan Academy**                                                                             |
| Molecular basis of mutation               | Search: "types of mutations"                                                                                                  | **Amoeba Sisters** (has existing mutation content)                                           |
| Genetic drift & selection revisited       | "Genetic Drift" (verified this session — real,[youtube.com/watch?v=mjQ_yN5znyk](https://www.youtube.com/watch?v=mjQ_yN5znyk)) | **Stated Clearly**                                                                           |
| Coalescent theory intuition               | Search: "coalescent theory explained simply"                                                                                  | look for**Primer** or a population-genetics course upload — no single canonical video found |
| Phylogenetic trees — distance methods    | Search: "neighbor joining phylogenetic tree"                                                                                  | **StatQuest** likely has relevant content; confirm exact title before use                    |
| Phylogenetic trees — character methods   | Search: "maximum parsimony phylogenetics"                                                                                     | course/university uploads                                                                          |
| Molecular clocks                          | Search: "molecular clock evolution explained"                                                                                 | **Khan Academy**                                                                             |
| Evolutionary game theory                  | Search: "evolutionary game theory"                                                                                            | **Primer** (real channel, known for simulation-based evolution/game-theory videos)           |
| Convergent & divergent evolution          | Search: "convergent vs divergent evolution"                                                                                   | **Amoeba Sisters**                                                                           |

---

## Module 07 — Biochemistry and Molecular Biology

| Notebook topic                           | Watch FIRST                                                                                                        | Channel                                                                                                  |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Amino acids, protein primary structure   | Search: "amino acid structure biochemistry"                                                                        | **Khan Academy**                                                                                   |
| Enzyme kinetics (Michaelis-Menten)       | Search: "Michaelis-Menten kinetics explained"                                                                      | **Professor Dave Explains** (real, well-known chemistry/biochem channel) or **Khan Academy** |
| DNA replication and repair               | "DNA Replication (Updated)" (already used in Module 05 table — same channel, deeper cut here)                     | **Amoeba Sisters**                                                                                 |
| Transcription & translation mechanics    | "Transcription (Updated)" / "Translation (Updated)" (already used in Module 05 table)                              | **Amoeba Sisters**                                                                                 |
| Post-translational modification (survey) | Search: "post-translational modification overview"                                                                 | **Khan Academy**                                                                                   |
| Biochemistry assay data shapes           | No dedicated video — this is a data-literacy notebook, not a concept explainer; skip the video-first pattern here | —                                                                                                       |

---

## Module 10 — Transcriptomics and Proteomics

| Notebook topic                      | Watch FIRST                                                                          | Channel                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Single-cell tech & data shape       | Search: "single cell RNA sequencing explained"                                       | **StatQuest** or **EMBL-EBI Training**                 |
| scRNA QC & cell filtering           | Search: "single cell RNA-seq quality control"                                        | **EMBL-EBI Training**                                        |
| Normalization & log transformation  | Reuse Module 09's "RPKM, FPKM and TPM, Clearly Explained" — same underlying concept | **StatQuest**                                                |
| PCA for single-cell                 | Reuse Module 04's PCA video                                                          | **StatQuest**                                                |
| UMAP / t-SNE visualization          | "StatQuest: t-SNE, Clearly Explained" and "UMAP Dimension Reduction, Main Ideas!!!"  | **StatQuest**                                                |
| Clustering (Leiden/Louvain)         | Search: "Leiden clustering algorithm explained"                                      | **EMBL-EBI Training** or scanpy's own tutorial video content |
| Marker genes & cell-type annotation | Search: "single cell marker gene annotation"                                         | **EMBL-EBI Training**                                        |
| Trajectory / pseudotime (survey)    | Search: "pseudotime trajectory inference single cell"                                | **EMBL-EBI Training**                                        |
| Mass spectrometry proteomics        | Search: "mass spectrometry proteomics explained"                                     | **Khan Academy** or a proteomics-core YouTube upload         |
| Protein quantification methods      | Search: "label-free protein quantification"                                          | proteomics-core upload                                             |
| Multi-omics integration (survey)    | Search: "multi-omics data integration"                                               | **EMBL-EBI Training**                                        |

---

## Module 11 — Structural Biology

| Notebook topic                                             | Watch FIRST                                                                                            | Channel                                                          |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Protein structure hierarchy                                | Search: "primary secondary tertiary quaternary protein structure"                                      | **Amoeba Sisters** or **Khan Academy**               |
| Experimental structure determination (X-ray, cryo-EM, NMR) | Search: "cryo-EM vs X-ray crystallography explained"                                                   | **EMBL-EBI Training**                                      |
| PDB format & parsing                                       | No dedicated video — this is a file-format/coding notebook; read the PDB format spec directly instead | —                                                               |
| Secondary structure & Ramachandran plots                   | Search: "Ramachandran plot explained"                                                                  | **Khan Academy**                                           |
| Contact maps & distance geometry                           | Search: "protein contact map explained"                                                                | niche — course upload                                           |
| AlphaFold2 & the protein folding revolution                | "AlphaFold2 Explained\| Google's DeepMind Solves Protein Folding" (verified this session)              | YouTube search result, channel not confirmed — check before use |
| Structure comparison & drug design (survey)                | Search: "structure-based drug design overview"                                                         | **EMBL-EBI Training**                                      |

---

## Module 12 — Systems and Network Biology

| Notebook topic                            | Watch FIRST                                                                                                                             | Channel                                                                                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Systems thinking & emergence              | Search: "emergence complex systems explained"                                                                                           | **Veritasium** or **3Blue1Brown**                                                |
| Graph theory for biological networks      | Graph theory playlist                                                                                                                   | **WilliamFiset** (real, well-known algorithms channel with a full graph theory course) |
| Network topology & properties             | Search: "network topology degree distribution"                                                                                          | **WilliamFiset**                                                                       |
| Scale-free networks & Barabási–Albert   | Search: "scale-free networks explained Barabasi"                                                                                        | course upload — Barabási's own lab has public talks                                        |
| Network centrality measures               | Search: "network centrality betweenness PageRank explained"                                                                             | **WilliamFiset**                                                                       |
| Community detection                       | Search: "community detection algorithms graphs"                                                                                         | **WilliamFiset**                                                                       |
| PPI network analysis                      | Search: "protein-protein interaction network analysis"                                                                                  | **EMBL-EBI Training**                                                                  |
| Gene regulatory networks (Boolean models) | Search: "Boolean network gene regulation"                                                                                               | course upload                                                                                |
| ODE models of biological systems          | Reuse Module 02's differential-equations videos                                                                                         | **3Blue1Brown**                                                                        |
| Metabolic networks & FBA                  | No clean YouTube match found this session — COBRApy's own tutorial notebooks (linked in`references.md`) are the better resource here | —                                                                                           |
| Network medicine & disease modules        | Search: "network medicine disease modules"                                                                                              | course upload                                                                                |

---

## Module 14 — Deep Learning and GNNs

| Notebook topic                                          | Watch FIRST                                                                                      | Channel                                                                                  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Neural networks from scratch                            | "But what is a neural network?" (Neural Networks ch. 1)                                          | **3Blue1Brown**                                                                    |
| PyTorch fundamentals                                    | PyTorch for Deep Learning full course                                                            | **freeCodeCamp**                                                                   |
| CNN for sequence classification                         | "Convolutional Neural Networks (CNNs), Clearly Explained!!!"                                     | **StatQuest**                                                                      |
| Recurrent networks (RNN/LSTM)                           | "Long Short-Term Memory (LSTM), Clearly Explained!!!"                                            | **StatQuest**                                                                      |
| Attention & transformers                                | "Transformer Neural Networks, Clearly Explained!!!"                                              | **StatQuest**                                                                      |
| Autoencoders & VAEs                                     | Search: "Variational Autoencoders, Clearly Explained"                                            | **StatQuest** (title recalled, not re-verified this session — confirm before use) |
| Graph neural networks                                   | Search: "graph neural networks explained"                                                        | **WilliamFiset**-adjacent or a dedicated GNN explainer — verify before use        |
| GNNs for molecular biology                              | Search: "graph neural networks drug discovery"                                                   | course upload                                                                            |
| Training best practices                                 | Search: "neural network training tips dropout batch norm"                                        | **StatQuest**                                                                      |
| Model interpretability (saliency, integrated gradients) | Search: "SHAP values explained"                                                                  | **StatQuest** (title recalled, not re-verified)                                    |
| AlphaFold & protein language models (ESM)               | Reuse Module 11's AlphaFold2 video; search separately for "ESM protein language model explained" | —                                                                                       |

---

## Module 15 — Simulation and Agent-Based Modeling

| Notebook topic                              | Watch FIRST                                                                                                                                                                                     | Channel                                                                                            |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| ODE biological models                       | Reuse Module 02's differential-equations videos                                                                                                                                                 | **3Blue1Brown**                                                                              |
| Stochastic simulation (Gillespie algorithm) | "Gillespie Algorithm" (verified this session — real,[youtube.com/watch?v=46ruoTTLL5g](https://www.youtube.com/watch?v=46ruoTTLL5g), but old/2013 — treat as a supplement, not the only source) | uploader not a major channel                                                                       |
| Reaction-diffusion systems                  | Search: "Turing patterns reaction diffusion"                                                                                                                                                    | **The Coding Train** (real, well-known creative-coding channel that covers this exact topic) |
| Cellular automata                           | Search: "cellular automata explained"                                                                                                                                                           | **The Coding Train**                                                                         |
| ABM fundamentals                            | Search: "agent-based modeling introduction"                                                                                                                                                     | **The Coding Train** or **Complexity Explorer**                                        |
| Population dynamics & evolution             | Reuse Module 02's Lotka-Volterra video                                                                                                                                                          | —                                                                                                 |
| Network epidemic dynamics                   | "Simulating an epidemic"                                                                                                                                                                        | **3Blue1Brown** (real, well-known video on SIR-style simulation)                             |
| Spatial ABM movement                        | Search: "spatial agent-based model"                                                                                                                                                             | **The Coding Train**                                                                         |
| Parameter estimation                        | Search: "parameter estimation ODE fitting"                                                                                                                                                      | **NeuralNine**                                                                               |
| Sensitivity analysis / bifurcation          | Search: "bifurcation diagram explained"                                                                                                                                                         | **3Blue1Brown**-adjacent — verify before use                                                |
| Multiscale modeling                         | Search: "multiscale modeling biology"                                                                                                                                                           | course upload                                                                                      |

---

## Module 16 — Research Software Engineering

| Notebook topic                   | Watch FIRST                                                              | Channel                       |
| -------------------------------- | ------------------------------------------------------------------------ | ----------------------------- |
| Python package structure         | Search: "Python package structure tutorial"                              | **Corey Schafer**       |
| Testing with pytest              | "Python Testing with pytest"                                             | **Corey Schafer**       |
| Documentation (Sphinx)           | Search: "Sphinx documentation tutorial Python"                           | **Real Python**         |
| CLI tools with Click             | Search: "Python Click CLI tutorial"                                      | **Tech With Tim**       |
| GitHub Actions CI/CD             | "GitHub Actions Tutorial" (already used in Module 16's Part 1 resources) | **TechWorld with Nana** |
| Code quality (ruff, black, mypy) | Search: "ruff black mypy Python tutorial"                                | **ArjanCodes**          |
| Profiling & optimization         | Reuse Part 1's "Python Performance: How to Profile Your Code"            | **mCoding**             |
| Packaging & publishing (PyPI)    | "How to Upload Your Python Package to PyPi"                              | **Corey Schafer**       |

*(`compbio_utils` sequence/statistics/IO notebooks and the mini-project have no video —
they're your own implementation work, not concept lessons.)*

---

## Module 17 — HPC, Parallel Computing, and Rust

| Notebook topic              | Watch FIRST                                                                                                                                                                                  | Channel                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| NumPy vectorization         | Reuse Module 01's broadcasting video                                                                                                                                                         | **Sentdex**                                                            |
| Multiprocessing & threading | Search: "Python multiprocessing tutorial"                                                                                                                                                    | **Corey Schafer**                                                      |
| joblib & Dask               | Search: "Dask parallel computing tutorial"                                                                                                                                                   | **Dask**'s own official channel                                        |
| Numba JIT                   | Search: "Numba JIT Python tutorial"                                                                                                                                                          | **NeuralNine**                                                         |
| Cython basics               | Search: "Cython tutorial Python"                                                                                                                                                             | **NeuralNine**                                                         |
| SLURM & HPC                 | "Slurm Tutorial: High Performance Computing (HPC) Job Submission Systems for Beginners" (verified this session)                                                                              | uploader not a major channel — confirm quality before committing to it      |
| Rust fundamentals           | Rust basics series                                                                                                                                                                           | **Let's Get Rusty** (real, well-known dedicated Rust-learning channel) |
| Rust ownership & borrowing  | "Ownership" (Let's Get Rusty's Rust book walkthrough series)                                                                                                                                 | **Let's Get Rusty**                                                    |
| Rust sequences & k-mers     | No dedicated video — niche bioinformatics-Rust content; build from`needletail`/`noodles` docs directly                                                                                  | —                                                                           |
| PyO3 (Rust ↔ Python)       | No single canonical YouTube match found this session — the O'Reilly "Using Rust with Python" course and Microsoft's "Rust for Python Programmers" guide are stronger written resources here | —                                                                           |
| Performance benchmarking    | Search: "Python benchmarking timeit tutorial"                                                                                                                                                | **mCoding**                                                            |

---

## Module 18 — Scientific Writing and Open Science

| Notebook topic                | Watch FIRST                                                              | Channel                                             |
| ----------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------- |
| Anatomy of a scientific paper | Search: "how to read a scientific paper"                                 | **Academic English Now** (already used)       |
| Writing abstracts             | Search: "how to write a scientific abstract"                             | **Academic English Now**                      |
| Writing introductions         | Search: "how to write a paper introduction"                              | **Academic English Now**                      |
| Methods & reproducibility     | No dedicated video — read Wilson et al. (2017), already in`papers.md` | —                                                  |
| Results writing               | Search: "how to write a results section"                                 | **Academic English Now**                      |
| Discussion & conclusions      | Search: "how to write a discussion section"                              | **Academic English Now**                      |
| Publication-quality figures   | Search: "publication quality figures Python matplotlib"                  | **NeuralNine**                                |
| Open science practices        | "Introduction to Open Science" (already used)                            | **Center for Open Science**                   |
| Peer review                   | Search: "how does peer review work"                                      | **Nature** or **PLOS** official channel |
| PhD application writing (SOP) | Search: "how to write a PhD statement of purpose"                        | course upload — verify credibility before trusting |
| LaTeX & scientific tools      | Search: "LaTeX tutorial for beginners"                                   | **Overleaf**'s own official channel           |

---

## Module 19 — Research Seminar and Paper Reading

| Notebook topic                     | Watch FIRST                                                                                                                       | Channel                                                             |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Three-Pass Method                  | Search: "how to read a research paper Keshav three pass" (this is S. Keshav's original technique — CLAUDE.md §8 is built on it) | look for a university/course upload walking through Keshav's method |
| Reading methods critically         | No dedicated video — this is a practiced skill, not a watchable concept; apply directly to a paper                               | —                                                                  |
| Evaluating statistical claims      | Reuse Module 03's Ioannidis-adjacent framing (already in`papers.md`)                                                            | —                                                                  |
| Reading benchmarks                 | Search: "how to evaluate ML benchmarks critically"                                                                                | course upload                                                       |
| Single-cell transcriptomics papers | No dedicated video — apply Three-Pass directly to the Module 10/13 reading list                                                  | —                                                                  |
| Journal club presentation          | Search: "how to present a journal club"                                                                                           | course upload                                                       |
| Writing literature reviews         | Search: "how to write a literature review"                                                                                        | **Academic English Now**                                      |
| Citation management (Zotero)       | Search: "Zotero tutorial for beginners"                                                                                           | **freeCodeCamp**                                              |
| Identifying research gaps          | No dedicated video — this comes from volume of reading, not a single lesson                                                      | —                                                                  |
| Cold paper explanation drill       | This is the drill itself — see Part 3 above, not a video                                                                         | —                                                                  |
| Building a reading list            | No dedicated video — practical workflow, not a concept                                                                           | —                                                                  |

---

## Module 20 — Capstone Projects

No video-first pattern here — by Month 11–12 the workflow inverts: you're building,
not being taught. The relevant preparation is everything above, plus:

| Notebook topic                         | Watch FIRST                                                    | Channel |
| -------------------------------------- | -------------------------------------------------------------- | ------- |
| Publication-quality figures & writeups | Reuse Module 18's figure/writing videos                        | —      |
| PhD application package                | Reuse Module 18's SOP-writing search and`portfolio/sop_*.md` | —      |

---

## Module 13 — ML for Biology (starts Month 7)

| Notebook topic                  | Watch FIRST                                              | Channel             | Duration |
| ------------------------------- | -------------------------------------------------------- | ------------------- | -------- |
| CNNs for sequences              | "Convolutional Neural Networks (CNN), Clearly Explained" | **StatQuest** | ~26 min  |
| Transformers for biology        | "Transformer Neural Networks, Clearly Explained"         | **StatQuest** | ~34 min  |
| Variational Autoencoders (scVI) | "Variational Autoencoders, Clearly Explained"            | **StatQuest** | ~22 min  |
| SHAP interpretability           | "SHAP Values, Clearly Explained"                         | **StatQuest** | ~25 min  |

---

## Permanent bookmarks (use throughout the year)

| Resource                                     | URL pattern                       | Use for                                                                              |
| -------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------ |
| **StatQuest with Josh Starmer**        | youtube.com/@statquest            | Every statistics + ML topic                                                          |
| **3Blue1Brown**                        | youtube.com/@3blue1brown          | Intuition for every math topic (linear algebra, calculus, probability)               |
| **Amoeba Sisters**                     | youtube.com/@AmoebaSisters        | Biology fundamentals, always                                                         |
| **Bioinformatics Coach**               | youtube.com/@BioinformaticsCoach  | NGS pipelines, Unix, practical tools                                                 |
| **EMBL-EBI Training**                  | youtube.com/@EBI_Training         | Course-level computational biology content, by the institution you're applying to    |
| **Rosalind**                           | rosalind.info                     | Sequence analysis coding problems (Module 08 companion) — NOT YouTube but daily use |
| **StatQuest Playlist: Bioinformatics** | YouTube → StatQuest → Playlists | Complete bioinformatics statistics in order                                          |

---

## COMBINED EXECUTION ORDER (what to do this week)

Given today is July 14, 2026:

### Today (July 14)

- Create `progress/writing/2026-07-14_central_dogma_100w.md` (Module 18 Week 1 habit — 15 minutes)
- Subscribe to StatQuest, Amoeba Sisters, 3Blue1Brown (5 minutes)
- Create `CITATION.cff` stub (Module 16 — 10 minutes, copy template above)
- Verify viva status — if done, commit that fact to `progress/2026-07-14_viva_done.md`

### This week (July 14–20)

- Module 05 Notebook 1 (motivation + biology is the real gap): watch "Central Dogma" (Amoeba Sisters, 15 min) THEN write motivation section
- Module 03 Notebook 1 (motivation + why stats is interview-tested): watch "P Values, Clearly Explained" (StatQuest, 11 min) THEN write
- Module 01: create `tests/test_compbio_utils.py` with gc_content test — get pytest to green

### This fortnight (July 14–28)

- Add `.pre-commit-config.yaml` to repo root (Jupytext + nbstripout — 30 minutes, template above)
- Add `datasets/README.md` for E. coli genome + GEO dataset to Module 01 and 03 respectively
- Complete Module 05 Notebooks 1–3 (motivation, cell biology, central dogma)
- Complete Module 03 Notebooks 1–3 (motivation, descriptive stats, distributions)

### By August 25 (IMPRS-ML portal opens)

- Module 01: at least 8/20 notebooks committed, compbio_utils v0 with ≥3 functions and tests
- Module 03: at least 6/18 notebooks committed, FDR notebook completed
- Module 05: at least 5/18 notebooks committed, Hardy-Weinberg notebook as artifact
- SOP Draft A (Theis) personalized with your actual completed artifacts
- GitHub repo public, link ready to paste in IMPRS-ML portal

---

*Document version: July 14, 2026 | Based on CLAUDE.md v2.0 | Audit against Learning_Progress.md v2.0*
*Next audit: at the Month 3 Quarterly Checkpoint (September 2026)*
