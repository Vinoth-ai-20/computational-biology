# Module 16 — Exercises

One exercise file per notebook. Attempt each exercise before reading the next notebook.

- **E01** — `01_package_structure.md`: Reorganise a flat script into a proper package with `src/` layout. Add `__version__` and verify the import works.
- **E02** — `02_testing_with_pytest.md`: Write 10 parametrized tests for a `complement(base: str) -> str` function. Include at least two `pytest.raises` cases and one fixture.
- **E03** — `03_documentation_sphinx.md`: Write a fully documented `melting_temperature(seq: str) -> float` function with NumPy-style docstring (Parameters, Returns, Raises, Examples sections). Add a doctest that passes.
- **E04** — `04_cli_tools_click.md`: Add a `compbio tm --sequence ATCGATCG` command to the CLI that computes melting temperature. Test it with `CliRunner`.
- **E05** — `05_github_actions_ci.md`: Write a GitHub Actions workflow that runs your test suite on Python 3.10 and 3.12, uploads a coverage report, and fails if coverage drops below 80%.
- **E06** — `06_code_quality_tools.md`: Take a provided "bad" function (deliberately missing type hints, docstring, and using mutable default arguments) and refactor it until it passes mypy strict mode and ruff with no warnings.
- **E07** — `07_profiling_optimization.md`: Profile a naive GC-content-over-sliding-window implementation. Identify the bottleneck, optimise it, and document the speedup.
- **E08** — `08_compbio_utils_sequence.md`: Implement `find_orfs` using only the tools covered so far (no Biopython). Write 5 tests covering: empty sequence, no ORFs, overlapping ORFs, ORF at position 0, ORF spanning end of sequence.
- **E09** — `09_compbio_utils_statistics.md`: Use `bootstrap_ci` to estimate the 95% CI of the mean GC content across 100 randomly generated DNA sequences of length 1000. Plot the bootstrap distribution.
- **E10** — `10_compbio_utils_io.md`: Write a FASTQ round-trip test: generate 50 synthetic reads, write them to a file with `write_fastq`, read them back with `read_fastq`, and assert every field matches.
- **E11** — `11_packaging_publishing.md`: Write a minimal `pyproject.toml` for a package called `seqtools` with one dependency (`numpy>=1.24`) and one CLI entry point. Verify it with `python -m build --sdist`.
- **E12** — `12_mini_project_and_assessment.md`: See the assessment notebook. Implement all 5 stubs without looking at the reference implementations.
