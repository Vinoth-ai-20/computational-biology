# Module 01 — Python & Scientific Computing: References

---

## Books

### Primary

| Book | Authors | Access | Notes |
|------|---------|--------|-------|
| *Python Data Science Handbook* | Jake VanderPlas | Free at jakevdp.github.io/PythonDataScienceHandbook | Primary reference for NumPy, Pandas, and Matplotlib in this module. Use as a reference, not cover-to-cover. The NumPy and Pandas chapters are the most relevant. |
| *Scientific Python Lectures* | Gaël Varoquaux, Emmanuelle Gouillart et al. | Free at lectures.scientific-python.org | Complements VanderPlas with more depth on SciPy. Particularly useful for the optimization and ODE chapters. |

### Secondary

| Book | Authors | Notes |
|------|---------|-------|
| *Python for Data Analysis* (3rd ed.) | Wes McKinney | Authoritative Pandas reference, written by Pandas' creator. Pull the DataFrame internals and `groupby` chapters when the fundamentals notebooks feel thin. |
| *Elegant SciPy* | Nunez-Iglesias, van der Walt, Dashnow | Free at elegant-scipy.org. Bridges scientific Python to real biological and imaging problems. Worth reading alongside the SciPy notebooks. |

---

## Official Documentation — Bookmark These

| Resource | URL | When to consult |
|----------|-----|----------------|
| NumPy documentation | https://numpy.org/doc/ | Continuously — especially the user guide for broadcasting |
| SciPy documentation | https://docs.scipy.org/doc/scipy/ | Notebooks 11–12 and whenever a SciPy function's behavior is unclear |
| Pandas documentation | https://pandas.pydata.org/docs/ | Notebooks 08–09; the "User Guide" section is more useful than the API reference for learning |
| Matplotlib documentation | https://matplotlib.org/stable/ | Notebook 10; the gallery is the fastest way to find a plot type |
| Seaborn documentation | https://seaborn.pydata.org/ | Notebook 10 |
| Biopython Tutorial and Cookbook | https://biopython.org/DIST/docs/tutorial/Tutorial.html | Notebooks 16 and throughout Modules 08–09 |
| scikit-bio documentation | http://scikit-bio.org/docs/latest/ | Supplementary to Biopython |

---

## Online Tutorials and Courses

| Resource | URL | Notes |
|----------|-----|-------|
| Software Carpentry: Programming with Python | https://swcarpentry.github.io/python-novice-inflammation/ | A good baseline check — skip if the Notebook 02 diagnostic passes cleanly |
| Software Carpentry: The Unix Shell | https://swcarpentry.github.io/shell-novice/ | Required companion for Notebook 17 (Unix CLI). Work through it before or alongside that notebook. |
| NumPy for Absolute Beginners | https://numpy.org/doc/stable/user/absolute_beginners.html | Best first read for NumPy if Notebook 04 reveals unexpected gaps |
| Real Python | https://realpython.com | Targeted lookup for specific Python patterns — not a course to follow serially |

---

## Key Software — Pinned Versions

| Package | Version | Purpose | Install |
|---------|---------|---------|---------|
| NumPy | ≥ 1.26 | Core array operations | `pip install numpy` |
| SciPy | ≥ 1.12 | Optimization, integration, ODE solvers | `pip install scipy` |
| Pandas | ≥ 2.2 | Tabular biological data | `pip install pandas` |
| Matplotlib | ≥ 3.8 | Base plotting | `pip install matplotlib` |
| Seaborn | ≥ 0.13 | Statistical visualization | `pip install seaborn` |
| Biopython | ≥ 1.83 | Sequence data, NCBI access | `pip install biopython` |
| scikit-bio | ≥ 0.6 | Bioinformatics-specific utilities | `pip install scikit-bio` |
| pytest | ≥ 8.0 | Testing | `pip install pytest` |
| ruff | ≥ 0.4 | Linting and formatting | `pip install ruff` |
| mypy | ≥ 1.9 | Static type checking | `pip install mypy` |
| build | current | Wheel building for `compbio_utils` | `pip install build` |
| maturin | current | Python–Rust bridge (Module 17) | `pip install maturin` |

---

## Key Researchers and Labs

| Name | Affiliation | Relevance |
|------|-------------|-----------|
| Jake VanderPlas | Google | Author of the Python Data Science Handbook; major contributor to the scientific Python ecosystem |
| Wes McKinney | Posit (formerly RStudio) | Creator of Pandas — understanding his design decisions explains Pandas' API choices |
| Travis Oliphant | NumFOCUS | Creator of NumPy and SciPy; his writings on array programming are worth reading |
| Biopython core developers | biopython.org | The Biopython codebase is itself an example of scientific Python packaging — worth reading as a model |
| Software Carpentry instructors | carpentries.org | The Carpentries' Unix and Python lessons are the template for Notebooks 17 and several earlier notebooks |

---

## Biological Datasets Used in This Module

| Dataset | Accession | Source | Notebooks | Notes |
|---------|-----------|--------|-----------|-------|
| Small GEO expression dataset (6–12 samples) — to be selected | GSE (TBD) | NCBI GEO | 08, 09, 10, A01 | Choose any small RNA-seq or microarray dataset with a clean metadata table. Document the accession in `datasets/README.md` after selection. |
| Gene family FASTA — to be fetched programmatically | NCBI Entrez | NCBI | 16, 17 | Write the fetch script in `scripts/fetch_gene_family_fasta.py`. Do not commit the raw FASTA to the repository. |

*Raw data files go in `datasets/raw/` (gitignored per `.gitignore`). Processed small files go in `datasets/processed/` and are committed. Always document the accession number and license in `datasets/README.md` before using a dataset.*

---

## NCBI Access Etiquette (for Notebook 16)

When using Biopython's `Entrez` to fetch sequences programmatically:

- Always set `Entrez.email` to a valid email address before making any request
- Do not make more than 3 requests per second (use `time.sleep(0.34)` between requests)
- For large batches, use `efetch` with `rettype="fasta"` and `retmax` set to the actual number needed
- Cache results locally — never re-fetch something already downloaded

---

*See also: [roadmap.md](roadmap.md) — [papers.md](papers.md) — [ENVIRONMENT.md](../../ENVIRONMENT.md)*
