# Module 17 — References

## Books and Documentation

### Rust

- **The Rust Programming Language** ("The Book") — https://doc.rust-lang.org/book/
  - Free, official, comprehensive. Chapters 1–10 cover everything needed for this module.
  - Chapter 4 (Ownership), Chapter 5 (Structs), Chapter 6 (Enums), Chapter 8 (Collections)
- **Rust by Example** — https://doc.rust-lang.org/rust-by-example/
  - Companion to The Book; shorter, code-first. Good for quick reference.
- **Programming Rust** (Blandy, Orendorff, Tindall) — O'Reilly, 2nd ed. 2021
  - Best book for deep understanding of the ownership model and performance implications.

### PyO3 and Maturin

- **PyO3 User Guide** — https://pyo3.rs/
  - Definitive reference for writing Python extensions in Rust.
- **Maturin** — https://www.maturin.rs/
  - Build tool for PyO3 projects; handles Cargo + Python packaging together.

### NumPy / Numba / Cython

- **NumPy broadcasting docs** — https://numpy.org/doc/stable/user/basics.broadcasting.html
- **Numba docs** — https://numba.readthedocs.io/en/stable/
  - `@jit`, `@vectorize`, `@cuda.jit`; the "5-minute guide" is the right starting point.
- **Cython docs** — https://cython.readthedocs.io/en/latest/
  - Tutorials → Working with NumPy → Typed Memoryviews is the critical section.

### Parallel Python

- **Python `multiprocessing` docs** — https://docs.python.org/3/library/multiprocessing.html
- **joblib docs** — https://joblib.readthedocs.io/en/latest/
  - `Parallel`, `delayed`, `Memory` — the three things worth knowing deeply.
- **Dask docs** — https://docs.dask.org/en/stable/
  - Array API, Dataframe API, Distributed scheduler. Start with Array.

### HPC / SLURM / Snakemake

- **SLURM documentation** — https://slurm.schedmd.com/documentation.html
  - `sbatch`, `squeue`, `scancel`, `sacct` — the four commands to know cold.
- **Snakemake docs** — https://snakemake.readthedocs.io/en/stable/
  - "Getting started" tutorial covers 80% of real-world use.
- **SLURM quick-start guide** (many universities publish these — e.g. Harvard FAS, UCL Myriad)
  - Practical `#SBATCH` directive checklists.

## Rust Bioinformatics Ecosystem

- **noodles** — https://github.com/zaeleus/noodles
  - Rust library for reading/writing BAM, CRAM, VCF, BCF, GFF, FASTQ, FASTA.
  - Used in production at Sanger Institute and other large genomics centres.
- **needletail** — https://github.com/onecodex/needletail
  - Fast FASTA/FASTQ parser in Rust, with Python bindings via PyO3.
  - Example of a real PyO3 crate used in bioinformatics.
- **rust-bio** — https://rust-bio.github.io/
  - Bioinformatics algorithms in Rust: Smith-Waterman, BWT, suffix arrays.
- **bio-seq** — https://github.com/jeff-k/bio-seq
  - Bit-packed sequence types; example of Rust's type system for biology.

## Key Labs and Research Groups

- **Wellcome Sanger Institute** — https://www.sanger.ac.uk/ — heavy Rust and HPC user
- **EMBL European Bioinformatics Institute (EBI)** — https://www.ebi.ac.uk/ — large-scale genomics infrastructure
- **Broad Institute** — https://www.broadinstitute.org/ — GATK, Terra platform (HPC/cloud)
- **One Codex** — https://www.onecodex.com/ — needletail, Rust bioinformatics tools

## Key Researchers

- **Luiz Irber** — Rust bioinformatics, sourmash, MinHash
- **Nick Greenfield** — One Codex, needletail author
- **Michael Lin (noodles)** — Rust CRAM/BAM/VCF parsing at Sanger
- **Lam et al.** — Numba (Anaconda / NVIDIA)
- **Stefan Behnel** — Cython core developer
