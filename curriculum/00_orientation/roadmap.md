# Module 00 — Orientation: Roadmap

Track progress by checking boxes as each item is completed. Do not start Module 01 until the completion checklist at the bottom is fully checked.

**Started:** __________
**Completed:** __________

---

## Part 1 — Repository and Environment (Days 1–2)

### Notebook 01 — Welcome and Repository Orientation

`notebooks/00_welcome_and_repository_orientation.ipynb`

- [ ] Read the repository overview — what this is, what it is not, why the design choices were made
- [ ] Read the 12-month sprint calendar in `Learning_Progress.md` §3
- [ ] Walk through the full directory structure: curriculum, portfolio, paper-notes, progress, scripts, utilities
- [ ] Understand the rules that never bend: 13-step lesson sequence, Three-Pass method, "no code ships that you can't explain"
- [ ] **Exercise:** draw the repository dependency graph from memory — which modules run in parallel in Month 1?

### Notebook 02 — Environment Setup and Verification

`notebooks/01_environment_setup_and_verification.ipynb`

- [ ] Work through `ENVIRONMENT.md` section by section
- [ ] Verify Python version
- [ ] Verify NumPy, SciPy, Pandas, Matplotlib install
- [ ] Verify JupyterLab, Jupytext, nbstripout, pre-commit
- [ ] Run `scripts/verify_environment.py` — all checks pass
- [ ] Seed `utilities/compbio_utils/` skeleton package structure
- [ ] Confirm `pip install -e utilities/compbio_utils` works
- [ ] **Exercise:** trigger a deliberate `ModuleNotFoundError`, diagnose it, fix it, document the fix

---

## Part 2 — Git, GitHub, and Reproducibility Infrastructure (Days 2–3)

### Notebook 03 — Git Fundamentals

`notebooks/02_git_fundamentals.ipynb`

- [ ] Understand why Git matters for reproducible research — the audit trail problem
- [ ] Practice core workflow: `init`, `add`, `commit`, `push`, `pull`, `log`, `diff`, `status`
- [ ] Create a module branch and merge it
- [ ] Write a commit message that serves a future reader
- [ ] Understand `.gitignore` — what to commit, what never to commit
- [ ] **Exercise:** create a branch, make a commit, push it, write the message as if explaining to a stranger six months from now

### Notebook 04 — GitHub Workflow

`notebooks/03_github_workflow.ipynb`

- [ ] Understand GitHub repository structure: README, releases, issues, Actions
- [ ] Set up a basic GitHub Actions CI workflow
- [ ] Practice common `gh` CLI operations: clone, view, pr create
- [ ] Make the repository public
- [ ] **Exercise:** use `gh` to view repository info; write a one-sentence elevator pitch for this repository as it would appear in a PhD application

### Notebook 05 — Markdown for Scientific Writing

`notebooks/04_markdown_for_scientific_writing.ipynb`

- [ ] Learn Markdown syntax: headers, lists, tables, code blocks
- [ ] Learn math in Markdown (KaTeX): inline and display
- [ ] Write a README that a stranger can follow in under 5 minutes
- [ ] Understand the difference between documentation and communication
- [ ] Practice cross-referencing between markdown files using relative links
- [ ] **Exercise:** write a two-paragraph summary of one module's README from memory, then compare to the actual file

---

## Part 3 — Notebook Workflow and Reproducibility Toolchain (Days 3–4)

### Notebook 06 — Jupyter and Jupytext Workflow

`notebooks/05_jupyter_and_jupytext_workflow.ipynb`

- [ ] Understand Jupyter notebook anatomy: cells, kernels, outputs, metadata
- [ ] Understand why raw `.ipynb` files produce unreadable git diffs
- [ ] Configure Jupytext pairing: `.ipynb` ↔ `.py` (percent format)
- [ ] Practice nbstripout: strip outputs, confirm the diff is clean
- [ ] Understand papermill: parametric notebook re-execution
- [ ] Walk through the full workflow: edit `.py` → sync → strip → commit → re-run
- [ ] **Exercise:** pair a new notebook, make a cell change, strip outputs, verify the diff is readable with `git diff`

### Notebook 07 — Python Environment and Packaging Basics

`notebooks/06_python_environment_and_packaging_basics.ipynb`

- [ ] Understand virtual environments and why isolation matters
- [ ] Compare `requirements.txt`, `environment.yml`, `pyproject.toml` — when to use which
- [ ] Compare `uv` and `conda` side by side
- [ ] Install `compbio_utils` as an editable package: `pip install -e utilities/compbio_utils`
- [ ] Understand pinned vs. unpinned dependencies
- [ ] **Exercise:** uninstall one package, restore from `requirements.txt`, verify with `verify_environment.py`

---

## Part 4 — Scientific Workflow and Code Standards (Day 4)

### Notebook 08 — Scientific Computing Workflow

`notebooks/07_scientific_computing_workflow.ipynb`

- [ ] Understand when to use a script vs. a notebook vs. a package
- [ ] Practice readable-first code: naming, structure, one-line docstrings
- [ ] Apply the "explain every line unprompted" rule to a 10-line toy function
- [ ] Understand why `pytest` catches what a notebook that "runs" misses
- [ ] Apply the Wilson et al. (2017) checklist to a toy `compbio_utils` function
- [ ] **Exercise:** take a piece of code from a personal project and audit it against the Wilson et al. checklist — document every failure honestly

---

## Part 5 — Literature Workflow and Three-Pass Reading (Days 5–6)

### Notebook 09 — Literature Review Workflow

`notebooks/08_literature_review_workflow.ipynb`

- [ ] Learn to find papers: PubMed, Google Scholar, bioRxiv, Semantic Scholar, EMBL-EBI
- [ ] Set up Zotero for reference management
- [ ] Understand DOI-based citation vs. PDF storage — why PDFs never go in the repository
- [ ] Fill in `references.md` for Module 01 using a keyword search
- [ ] **Exercise:** find three papers relevant to Module 01, save their DOIs and one-sentence annotations in `01_python_scientific_computing/papers.md`

### Notebook 10 — Three-Pass Paper Reading

`notebooks/09_three_pass_paper_reading.ipynb`

- [ ] Understand Pass 1 — Skim (5–10 min): title, abstract, figures, conclusion
- [ ] Understand Pass 2 — Intent (45–90 min): read in order, note method, mark fuzzy sections
- [ ] Understand Pass 3 — Reconstruct (1–2 hrs): re-explain the core method with the paper closed
- [ ] Understand what to log in `paper-notes/` and why `pass3_unaided` is the key metric
- [ ] **Apply all three passes** to Wilson et al. (2017), *Good enough practices in scientific computing*
- [ ] Log the Pass-3 reconstruction in `paper-notes/wilson_2017_good_enough_practices.md`
- [ ] **Exercise:** score the Pass-3 attempt honestly — did it succeed unaided? Log what was missing if not.

---

## Part 6 — Progress Tracking, Portfolio, and Reproducibility Audit (Days 6–7)

### Notebook 11 — Progress Tracking and Review Templates

`notebooks/10_progress_tracking_and_review_templates.ipynb`

- [ ] Understand the weekly review: three questions every Sunday
- [ ] Understand the monthly review: readiness score, Track A/B deadlines, repository health
- [ ] Understand the quarterly checkpoint: tier reassignment, specialization signal, calendar re-baseline
- [ ] Write the first weekly log entry in `progress/`
- [ ] **Exercise:** write the first weekly log as if it is Sunday of Week 1

### Notebook 12 — Portfolio Philosophy

`notebooks/11_portfolio_philosophy.ipynb`

- [ ] Understand the difference between a completed notebook and a portfolio artifact
- [ ] Understand the polishing checklist for moving work into `portfolio/`
- [ ] Understand what "defensible cold" means — and why every `portfolio/` artifact must meet this bar
- [ ] Identify the Month 3 artifact target
- [ ] **Exercise:** write one paragraph describing what the Month 3 artifact will be and why it is Track A and Track B relevant

### Notebook 13 — Reproducible Research Checklist

`notebooks/12_reproducible_research_checklist.ipynb`

- [ ] Apply all 24 Wilson et al. (2017) practices to this repository as a signed-off checklist
- [ ] Understand the four FAIR principles applied to `datasets/` structure
- [ ] Understand the difference between "runs on my machine" and reproducible
- [ ] Test the one-command bootstrap from a fresh clone in a temporary directory
- [ ] Sign off the checklist: this repository passes these criteria from the start
- [ ] **Exercise:** document every bootstrap step that required manual intervention

---

## Completion Checklist

Do not start Module 01 until every item below is checked:

- [ ] `scripts/verify_environment.py` passes all checks
- [ ] First commit pushed to the public repository
- [ ] Jupytext pairing confirmed working: diff is readable after a notebook edit
- [ ] nbstripout confirmed working: outputs stripped automatically on commit
- [ ] Pass-3 reconstruction of Wilson et al. (2017) logged in `paper-notes/`
- [ ] First weekly progress log entry written in `progress/`
- [ ] The 13-step lesson sequence can be recited unprompted
- [ ] One-command bootstrap tested: repository clones and environment installs cleanly from scratch

---

*See also: [README.md](README.md) — [references.md](references.md) — [papers.md](papers.md) — [CLAUDE.md](../../CLAUDE.md) — [ENVIRONMENT.md](../../ENVIRONMENT.md)*
