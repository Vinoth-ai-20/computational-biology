# Module 01 — Python & Scientific Computing: Roadmap

Track progress by checking boxes as each item is completed. Each notebook must satisfy the 13-step teaching sequence in [CLAUDE.md](../../CLAUDE.md) §4.1 before being marked done.

**Started:** __________
**Completed:** __________

---

## Part 1 — Environment and Python Foundations (Weeks 1–2)

### Notebook 01 — Environment Setup and `compbio_utils` Bootstrap

`notebooks/01_environment_setup.ipynb`

- [ ] Verify full toolchain inside a notebook: Python, NumPy, JupyterLab, Jupytext, nbstripout, pre-commit
- [ ] Run `scripts/verify_environment.py` and interpret every line of output
- [ ] Create `utilities/compbio_utils/` package skeleton: `__init__.py`, `sequence.py`, `stats.py`, `plotting.py`, `io.py`, `tests/`
- [ ] Confirm `pip install -e utilities/compbio_utils` and verify `import compbio_utils` works
- [ ] **Exercise:** add `compbio_utils.version()` returning the version from `pyproject.toml`; write a `pytest` test that validates it returns a valid semantic version string

### Notebook 02 — Python Syntax Diagnostic

`notebooks/02_python_syntax_diagnostic.ipynb`

- [ ] Complete 20-question diagnostic: list comprehensions, generators, decorators, context managers, dataclasses, type hints, f-strings, `*args`/`**kwargs`, error handling
- [ ] Identify gaps — only spend time on sections scored below 90%
- [ ] **Exercise:** implement `compbio_utils.sequence.gc_content()` using only built-in Python (no NumPy); write a property-based test verifying the return value is always in `[0.0, 1.0]`

### Notebook 03 — Functions, Modules, and Packages

`notebooks/03_functions_modules_packages.ipynb`

- [ ] Understand pure functions, side effects, and why they matter for testability
- [ ] Understand module organization: `__init__.py`, relative imports, public vs. private (`_name`)
- [ ] Read and understand `pyproject.toml` anatomy for `compbio_utils`
- [ ] Understand semantic versioning: what `v0.1.0` vs. `v1.0.0` communicates
- [ ] **Exercise:** refactor `gc_content()` into `compbio_utils.sequence` with a clean API; confirm all existing tests pass after the move

---

## Part 2 — NumPy (Weeks 2–3)

### Notebook 04 — NumPy Fundamentals

`notebooks/04_numpy_fundamentals.ipynb`

- [ ] Understand the `ndarray` mental model: why it is not a Python list
- [ ] Practice array creation: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `np.eye`
- [ ] Practice indexing and slicing: 1D, 2D, multi-dimensional, boolean indexing
- [ ] Understand universal functions (`ufuncs`) and why they outperform Python loops
- [ ] Apply biological framing: DNA sequence as array, expression matrix as 2D float array
- [ ] **Exercise:** represent a 5-gene × 10-sample expression matrix as a NumPy array; compute per-gene mean, standard deviation, and coefficient of variation — no loops, no Pandas

### Notebook 05 — Broadcasting and Vectorization

`notebooks/05_broadcasting_vectorization.ipynb`

- [ ] Understand the broadcasting shape-compatibility rule precisely
- [ ] Benchmark: Python loop vs. NumPy ufunc on a biological-scale array
- [ ] Implement a pairwise Euclidean distance matrix using broadcasting — no loops
- [ ] Apply biological framing: pairwise sequence identity from binary-encoded arrays
- [ ] **Exercise:** implement L2 pairwise distance between expression profiles using broadcasting only — no `scipy.spatial.distance`, no `np.linalg.norm` loop

### Notebook 06 — NumPy Linear Algebra Operations

`notebooks/06_numpy_linear_algebra.ipynb`

- [ ] Practice `np.linalg`: `@`, `inv`, `det`, `eig`, `svd`, `solve`
- [ ] Understand covariance matrix: `np.cov` and its relationship to SVD
- [ ] Understand why SVD is numerically preferred over `eig` for PCA
- [ ] Apply biological framing: covariance matrix of expression data; eigenvalues as explained variance
- [ ] **Exercise:** compute the covariance matrix of a 5-gene × 20-sample toy expression matrix; find the top-2 eigenvectors using SVD; plot the projection; explain why SVD and `eig` give the same result

### Notebook 07 — Random Numbers and Reproducible Seeding

`notebooks/07_random_numbers_reproducibility.ipynb`

- [ ] Understand `np.random.default_rng(seed)` — why `np.random.seed()` is deprecated
- [ ] Practice common distributions: uniform, normal, binomial, Poisson
- [ ] Apply biological framing: read counts as Poisson; allele frequencies under drift
- [ ] Apply the reproducibility rule: every notebook using randomness documents its seed as a top-level constant
- [ ] **Exercise:** simulate 1,000 coin flips; verify convergence to 0.5; fix the seed and confirm two independent runs produce identical sequences

---

## Part 3 — Pandas (Weeks 3–4)

### Notebook 08 — Pandas Fundamentals

`notebooks/08_pandas_fundamentals.ipynb`

- [ ] Understand `Series` and `DataFrame` mental models — why they are not spreadsheets
- [ ] Practice reading: `pd.read_csv`, `pd.read_table`, biological flat-file formats
- [ ] Practice indexing: `.loc`, `.iloc`, boolean filtering
- [ ] Practice `groupby`, `merge`, `concat`
- [ ] Apply biological framing: GEO sample metadata table, gene annotation table, expression count matrix
- [ ] **Exercise:** load a small GEO metadata CSV; filter to one condition; compute per-condition mean expression for 5 genes

### Notebook 09 — Data Cleaning for Biological Data

`notebooks/09_data_cleaning_biological.ipynb`

- [ ] Understand why missing values appear in biological data (failed assays, detection limits, censoring)
- [ ] Know the three strategies: drop, impute, flag — and when each is scientifically justified
- [ ] Practice duplicate sample detection
- [ ] Identify data type coercion pitfalls common in biological tables
- [ ] Apply biological framing: clean a real GEO clinical metadata table
- [ ] **Exercise:** given the messy metadata table in `exercises/`, produce a clean version with every decision documented inline

---

## Part 4 — Visualization (Week 4)

### Notebook 10 — Matplotlib and Seaborn Scientific Plotting

`notebooks/10_matplotlib_seaborn_plotting.ipynb`

- [ ] Understand Matplotlib figure/axes object model
- [ ] Build multi-panel figures with `plt.subplots`
- [ ] Apply publication-quality defaults: DPI, font sizes, colorblind-safe palettes
- [ ] Practice Seaborn: `stripplot`, `boxplot`, `violinplot`, `heatmap`, `clustermap`, `pairplot`
- [ ] Apply biological framing: expression heatmap, volcano plot scaffold, PCA scatter
- [ ] **Exercise:** produce a three-panel publication-quality figure (heatmap, boxplot, PCA scatter) from an earlier notebook's expression dataset

---

## Part 5 — SciPy (Weeks 4–5)

### Notebook 11 — SciPy: Optimization

`notebooks/11_scipy_optimization.ipynb`

- [ ] Understand `scipy.optimize.minimize`: interface, solver options, convergence
- [ ] Practice `scipy.optimize.curve_fit`: fitting a parametric model to noisy data
- [ ] Practice root finding: `scipy.optimize.brentq`
- [ ] Apply biological framing: logistic growth curve fitting; gene expression equilibrium
- [ ] **Exercise:** fit a logistic growth model to a simulated bacterial growth curve; plot fit vs. data; report estimated parameters and 95% confidence intervals

### Notebook 12 — SciPy: ODE Solvers and Numerical Integration

`notebooks/12_scipy_odes_integration.ipynb`

- [ ] Understand `scipy.integrate.solve_ivp`: interface, RK45 vs. LSODA, `dense_output`
- [ ] Understand stiff vs. non-stiff systems and why solver choice matters
- [ ] Practice `scipy.integrate.quad` for definite integrals
- [ ] Apply biological framing: mRNA production-degradation ODE; two-variable precursor to Lotka-Volterra
- [ ] **Exercise:** solve and plot mRNA concentration over time; perturb the degradation rate 2× and overlay both trajectories

---

## Part 6 — Software Engineering for Science (Week 5)

### Notebook 13 — Writing Reusable Scientific Code

`notebooks/13_reusable_scientific_code.ipynb`

- [ ] Understand the function → module → package progression
- [ ] Know what makes scientific code reusable vs. a one-off script
- [ ] Practice one-line docstrings — understand why multi-paragraph docstrings are usually a symptom of unclear code
- [ ] Practice type hints in scientific code — where they add value, where they add noise
- [ ] **Practical:** refactor one function from an earlier notebook into `compbio_utils` with a clean, testable public API

### Notebook 14 — Testing Scientific Code with pytest

`notebooks/14_testing_with_pytest.ipynb`

- [ ] Understand why testing scientific code is hard: floating-point, stochasticity, biological edge cases
- [ ] Practice `pytest` fundamentals: discovery, plain `assert`, fixtures, `parametrize`
- [ ] Use `np.testing.assert_allclose` for floating-point assertions — never `==` for floats
- [ ] Know what to test: properties and invariants, not unknowable exact outputs
- [ ] **Practical:** write a test suite for `compbio_utils.sequence.gc_content` covering: empty string, all-A, all-GC, mixed case, non-ACGT characters
- [ ] **Exercise:** write a `parametrize`-based test verifying GC content is always in `[0.0, 1.0]` for any valid uppercase DNA string

### Notebook 15 — Packaging with pyproject.toml

`notebooks/15_packaging_pyproject.ipynb`

- [ ] Read and understand `pyproject.toml` anatomy: `[project]`, `[build-system]`, `[tool.ruff]`, `[tool.pytest.ini_options]`
- [ ] Build a wheel with `python -m build`
- [ ] Understand `pip install .` vs. `pip install -e .`
- [ ] Understand semantic versioning: `0.1.0` vs. `1.0.0`
- [ ] Add a `CITATION.cff` stub to `compbio_utils`
- [ ] **Exercise:** build a wheel, install it in a fresh environment, import `compbio_utils.sequence.gc_content`, verify the version string

---

## Part 7 — Biopython and Unix (Week 6)

### Notebook 16 — Biopython Fundamentals

`notebooks/16_biopython_fundamentals.ipynb`

- [ ] Understand `SeqRecord` and `Seq` — the two objects used everywhere
- [ ] Practice reading FASTA and FASTQ with `SeqIO.parse`
- [ ] Practice writing sequences with `SeqIO.write`
- [ ] Practice basic sequence operations: slicing, complement, reverse complement, translation
- [ ] Fetch a real gene mRNA sequence from NCBI via `Entrez` (with rate-limiting and email set)
- [ ] Compute GC content on the fetched sequence using `compbio_utils.sequence`
- [ ] **Exercise:** parse the multi-FASTA in `datasets/`; filter sequences longer than 500 bp; compute GC content for each; output a TSV summary

### Notebook 17 — Unix Command Line for Bioinformatics

`notebooks/17_unix_cli_bioinformatics.ipynb`

- [ ] Understand why Unix literacy is interview-tested at every Track A role
- [ ] Practice core commands: `ls`, `cd`, `cat`, `head`, `tail`, `grep`, `cut`, `sort`, `uniq`, `wc -l`
- [ ] Practice pipes and redirection: `|`, `>`, `>>`, `<`
- [ ] Practice `awk` for column extraction on biological flat files
- [ ] Write a `for` loop in Bash iterating over files
- [ ] Write a pipeline: FASTA → count sequences → filter by length → output summary
- [ ] **Exercise A:** write a Bash one-liner counting sequences in a FASTA file
- [ ] **Exercise B:** write a Bash pipeline extracting all headers from a FASTA, sorted, written to a file

---

## Part 8 — Integration and Assessment (Week 6)

### Notebook 18 — Mini Project: `compbio_utils` v0

`notebooks/18_mini_project_compbio_utils_v0.ipynb`

- [ ] Collect all utility functions from Notebooks 03–17 into `compbio_utils` v0
- [ ] Confirm `pip install -e utilities/compbio_utils` works in a clean environment
- [ ] Run full `pytest` suite — all tests pass, zero failures
- [ ] Write `utilities/compbio_utils/README.md`: install instructions, minimal usage example
- [ ] Apply Wilson et al. (2017) checklist to `compbio_utils` v0 — document every gap honestly
- [ ] Tag `v0.1.0` in Git with an annotated tag

### Notebook 19 — Research Paper Reading Session

`notebooks/19_paper_reading_session.ipynb`

- [ ] Select one paper from `papers.md` (Harris/NumPy 2020 or Cock/Biopython 2009)
- [ ] Complete Pass 1 — skim: title, abstract, figures, conclusion
- [ ] Complete Pass 2 — intent: read in order, note method and evidence
- [ ] Complete Pass 3 — reconstruct: re-explain core method with paper closed
- [ ] Log Pass-3 result in `paper-notes/`
- [ ] Write reflection: after Wilson et al. and this paper, what does good scientific Python code look like?

### Notebook 20 — Module Assessment and Track A Mock Interview

`notebooks/20_module_assessment_mock_interview.ipynb`

- [ ] **Unix section (5 min):** answer 3 command-line questions without reference material
- [ ] **NumPy section (5 min):** explain broadcasting with a concrete array shape example; implement a vectorized operation from scratch
- [ ] **Pandas section (5 min):** describe how to clean a messy metadata table — narrated, not just coded
- [ ] **Live-coding warm-up (5 min):** given a list of DNA sequences, return those with GC content > 60%, sorted by length descending — without notes
- [ ] Self-score against the Track A rubric in `Learning_Progress.md` §13
- [ ] Write reflection paragraph: what is understood and what is still fuzzy after this module

---

## Assignments

### Assignment A01 — Expression Matrix Pipeline

`assignments/A01_expression_matrix_pipeline.ipynb`

- [ ] Download a small public GEO expression dataset (document accession in `datasets/README.md`)
- [ ] Clean the metadata table
- [ ] Normalize expression values to CPM
- [ ] Produce a labeled heatmap
- [ ] Produce a PCA scatter plot
- [ ] Verify the notebook runs top-to-bottom from a clean clone

### Assignment A02 — `compbio_utils` v0 Audit

`assignments/A02_compbio_utils_v0_audit.ipynb`

- [ ] Apply all 24 Wilson et al. (2017) practices to `compbio_utils` v0
- [ ] Document every pass and every failure honestly
- [ ] Fix at least three failures found in the audit

---

## Module Completion Checklist

- [ ] All 20 notebooks completed and executed without errors
- [ ] `compbio_utils` v0 installs cleanly and all `pytest` tests pass
- [ ] Assignment A01 runs reproducibly from a clean clone
- [ ] Assignment A02 completed with ≥3 fixes applied
- [ ] Pass-3 reconstruction logged in `paper-notes/`
- [ ] `v0.1.0` tagged in Git
- [ ] Mock interview drill (Notebook 20) completed and self-scored
- [ ] Progress log updated in `progress/`

---

*See also: [README.md](README.md) — [references.md](references.md) — [papers.md](papers.md) — [Learning_Progress.md](../../Learning_Progress.md) §4 Module 01*
