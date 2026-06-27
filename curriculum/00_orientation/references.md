# Module 00 — Orientation: References

---

## Core Methodology

### Scientific Computing Practice

| Resource | Type | Purpose |
|----------|------|---------|
| Wilson et al. (2017), *Good enough practices in scientific computing*, PLOS Computational Biology. DOI: 10.1371/journal.pcbi.1005510 | Foundational paper | The primary reading assignment and the literal audit checklist applied in Notebook 12. Every habit this module installs traces back to this paper. Read via the Three-Pass Method. |
| Wilkinson et al. (2016), *The FAIR Guiding Principles for scientific data management and stewardship*, Scientific Data. DOI: 10.1038/sdata.2016.18 | Foundational paper | The four principles (Findable, Accessible, Interoperable, Reusable) that govern this repository's `datasets/` structure and documentation. Short — two readable pages. |
| Keshav (2007), *How to Read a Paper*, ACM SIGCOMM Computer Communication Review | Methodology guide | The Three-Pass Method source. One page. Read before Notebook 09. |

---

## Version Control and Reproducibility

### Git and GitHub

| Resource | URL | Notes |
|----------|-----|-------|
| Pro Git Book (Chacon & Straub) — free online | https://git-scm.com/book | The definitive Git reference. Read Ch. 1–3 for this module. Refer back to specific chapters when the need arises. |
| GitHub Docs | https://docs.github.com | Actions, CLI, authentication, CI workflows. |
| Software Carpentry: Version Control with Git | https://swcarpentry.github.io/git-novice/ | Recommended companion for Notebook 02 if Git concepts are unfamiliar. |
| GitHub CLI documentation | https://cli.github.com/manual/ | Command reference for `gh`. |

### Jupytext and nbstripout

| Resource | URL | Notes |
|----------|-----|-------|
| Jupytext documentation | https://jupytext.readthedocs.io | The pairing workflow. Read "Getting started" and "Using Jupytext" before Notebook 05. |
| nbstripout GitHub | https://github.com/kynan/nbstripout | pre-commit integration instructions. |
| papermill documentation | https://papermill.readthedocs.io | Parametric notebook execution. Introduced in Notebook 05; used heavily in Module 16. |

---

## Python Environment Management

| Resource | URL | Notes |
|----------|-----|-------|
| uv documentation | https://docs.astral.sh/uv/ | The primary environment manager for this repository. |
| Conda documentation | https://docs.conda.io | Alternative, particularly useful for complex bioinformatics dependencies in later modules. |
| Python Packaging User Guide | https://packaging.python.org | `pyproject.toml`, building packages, publishing. Referenced again in Module 01. |

---

## Scientific Writing and Communication

| Resource | URL | Notes |
|----------|-----|-------|
| GitHub Markdown Guide | https://docs.github.com/en/get-started/writing-on-github | The syntax used in all `.md` files in this repository. |
| CommonMark Specification | https://commonmark.org | The rendering standard for this repository's Markdown files. |
| LaTeX Math in Markdown (KaTeX) | https://katex.org/docs/supported.html | Supported math syntax in JupyterLab and GitHub markdown. |

---

## Reference Management

| Resource | URL | Notes |
|----------|-----|-------|
| Zotero | https://www.zotero.org | Free, open-source reference manager. Recommended for managing all papers read in this program. BibTeX export integrates with `references.md`. |
| ORCID | https://orcid.org | Register in Month 2 — required for most European PhD applications and Track B outreach. |
| Semantic Scholar | https://www.semanticscholar.org | Often finds free PDF versions of papers; good for citation network exploration. |
| bioRxiv and arXiv | https://www.biorxiv.org / https://arxiv.org | Primary preprint servers — many papers in this program are freely available here. |

---

## Tools Introduced in This Module

| Tool | Purpose | Install |
|------|---------|---------|
| Git 2.40+ | Version control | https://git-scm.com/download |
| GitHub CLI (`gh`) | Repository management from the command line | `winget install GitHub.cli` / `brew install gh` |
| JupyterLab 4.x | Notebook environment | `pip install jupyterlab` |
| Jupytext 1.16+ | `.ipynb` ↔ `.py` pairing | `pip install jupytext` |
| nbstripout 0.7+ | Strip notebook outputs before commit | `pip install nbstripout` |
| papermill 2.x | Parametric notebook execution | `pip install papermill` |
| pre-commit | Git hook management | `pip install pre-commit` |
| uv | Fast Python package manager | https://docs.astral.sh/uv/ |
| pytest 8.x | Testing framework (introduced here, used throughout) | `pip install pytest` |
| Zotero | Reference manager | https://www.zotero.org |

---

*Next: [roadmap.md](roadmap.md) — [papers.md](papers.md) — [ENVIRONMENT.md](../../ENVIRONMENT.md)*
