# Module 16 — References

## Books

- **The Pragmatic Programmer** — Hunt & Thomas (2019, 20th Anniversary Edition). Chapters on DRY, orthogonality, and automation are directly applicable to this module.
- **Clean Code** — Robert C. Martin (2008). Core principles on naming, functions, and tests; read alongside actual Python examples since the book is Java-centric.
- **Python Packages** — Devenish, Sochat, Kaszynska et al. (open access, https://py-pkgs.org/). The modern reference for pyproject.toml-based Python packaging with hatchling.
- **Architecture Patterns with Python** — Percival & Gregory (2020, O'Reilly). Domain-driven design and hexagonal architecture applied to Python; relevant for compbio_utils design.

## Key Software

- **pytest** — https://docs.pytest.org/ — Test framework; parametrize, fixtures, conftest, coverage plugin.
- **Sphinx** — https://www.sphinx-doc.org/ — Documentation generator; autodoc and napoleon extensions for NumPy-style docstrings.
- **Click** — https://click.palletsprojects.com/ — CLI framework; decorator-based, testable via CliRunner.
- **ruff** — https://docs.astral.sh/ruff/ — Fast Python linter and formatter (replaces flake8, isort, pyupgrade in one tool).
- **black** — https://black.readthedocs.io/ — Opinionated code formatter.
- **mypy** — https://mypy.readthedocs.io/ — Static type checker; strict mode enforces full annotation coverage.
- **GitHub Actions** — https://docs.github.com/en/actions — CI/CD platform; YAML-based workflows.
- **hatchling / hatch** — https://hatch.pypa.io/ — Modern Python build backend and project manager.
- **pyproject.toml** — PEP 517/518/621 — The modern standard for Python project configuration.
- **Zenodo** — https://zenodo.org/ — DOI minting for software; integration with GitHub releases for citable software artifacts.
- **pre-commit** — https://pre-commit.com/ — Git hook framework; runs ruff, black, nbstripout, mypy before every commit.
- **coverage.py** — https://coverage.readthedocs.io/ — Code coverage measurement.

## Key Researchers and Labs

- **Greg Wilson** — Software Carpentry founder; author of the "Best Practices" and "Good Enough Practices" papers. https://third-bit.com/
- **The Turing Way** — https://the-turing-way.netlify.app/ — Community handbook for reproducible, ethical, and collaborative data science.
- **SSI (Software Sustainability Institute)** — https://www.software.ac.uk/ — UK institute for RSE best practices; runs the RSE conference series.
- **rOpenSci** — https://ropensci.org/ — Peer-review process for scientific software; the review checklist is language-agnostic and worth reading even for Python code.
