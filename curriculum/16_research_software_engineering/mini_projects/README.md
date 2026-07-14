# Module 16 — Mini Projects

## MP01: Build and Publish compbio_utils to TestPyPI; Integrate into Module 13

**Goal:** Close the loop — package the library built across NB08–NB10, publish it to TestPyPI, and demonstrate it works as an installed dependency inside a Module 13 notebook.

### Phase 1: Finalize and tag the package

1. Ensure all three submodules pass `pytest --cov=compbio_utils` with ≥ 95% coverage.
2. Bump version to `0.1.0` in `pyproject.toml` and `compbio_utils/__init__.py`.
3. Write `CHANGELOG.md` with a single `[0.1.0]` entry listing all public functions.
4. Tag the commit: `git tag v0.1.0`.

### Phase 2: Build and publish

1. `python -m build` — verify the `dist/` directory contains both `.tar.gz` and `.whl`.
2. `twine check dist/*` — must pass with no errors.
3. `twine upload --repository testpypi dist/*` — publish to https://test.pypi.org.
4. In a fresh virtual environment: `pip install --index-url https://test.pypi.org/simple/ compbio_utils` — verify import works.

### Phase 3: Integrate into Module 13

1. Open the Module 13 (Machine Learning for Biology) notebook of your choice.
2. Add a cell at the top: `from compbio_utils.sequence import gc_content, kmer_frequencies`.
3. Use `gc_content` on the biological sequences already present in that notebook.
4. Add a markdown cell explaining which compbio_utils version is being used and why.

### Deliverable

- TestPyPI package URL (e.g. `https://test.pypi.org/project/compbio-utils/0.1.0/`)
- Screenshot of `pip install` succeeding in a fresh venv: `mini_projects/MP01_install_screenshot.png`
- The modified Module 13 notebook with compbio_utils import cells added.
