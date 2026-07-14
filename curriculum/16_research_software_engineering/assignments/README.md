# Module 16 — Assignments

## A01: Complete compbio_utils Package

**Goal:** Deliver a production-quality `compbio_utils` package with 100% test coverage and Sphinx documentation.

**Requirements:**
1. All three submodules implemented: `sequence.py`, `stats.py`, `io.py` — with every function from NB08–NB10.
2. Test suite: `pytest --cov=compbio_utils --cov-report=term-missing` must show 100% coverage.
3. All functions have NumPy-style docstrings with working doctests.
4. Sphinx docs build without warnings: `sphinx-build -W docs/ docs/_build/`.
5. `pyproject.toml` is complete and `python -m build` produces a valid sdist and wheel.
6. `ruff check .` and `mypy compbio_utils/ --strict` both pass with zero errors.

**Deliverable:** A git tag `v0.1.0` on the `utilities/compbio_utils/` directory, plus a screenshot of the Sphinx-generated HTML in `assignments/A01_screenshot.png`.

---

## A02: CLI k-mer Search Tool

**Goal:** Build a CLI tool that performs a BLAST-inspired k-mer exact search between a query and a database of sequences.

**Requirements:**
1. CLI entry point: `compbio-search --query ATCGATCG --db sequences.fasta --k 7 --min-hits 2`
2. Algorithm: index all k-mers in the database sequences; report any database sequence sharing ≥ `min-hits` k-mers with the query.
3. Output: tab-separated table with columns `db_sequence_id`, `shared_kmers`, `query_coverage_pct`.
4. Tested with `CliRunner`: ≥ 8 tests covering normal cases, empty database, query shorter than k, and the `--help` flag.
5. Type-annotated, ruff-clean, documented with a NumPy-style docstring on every function.

**Deliverable:** `assignments/A02_kmer_search.py` plus `assignments/A02_test_kmer_search.py` with the full test suite.
