# ENVIRONMENT.md

# Computational Biology Research Notebook

This document describes how to set up a complete, reproducible development environment for the **Computational Biology Research Notebook** repository.

The goal is to ensure that every notebook, script, and project in this repository can be executed consistently across different systems.

---

# System Requirements

## Supported Operating Systems

* Windows 11 (Primary Development Environment)
* Ubuntu 22.04+ (Supported)
* macOS 14+ (Supported)

---

# Hardware Recommendations

## Minimum

* 4 CPU cores
* 16 GB RAM
* 20 GB free storage

## Recommended

* 8+ CPU cores
* 32 GB RAM
* NVIDIA GPU (optional)
* 100 GB SSD

---

# Software Requirements

Install the following software before working with this repository.

| Software           | Version |
| ------------------ | ------- |
| Python             | 3.12+   |
| Git                | Latest  |
| GitHub CLI         | Latest  |
| Visual Studio Code | Latest  |
| JupyterLab         | Latest  |

---

# Clone the Repository

```bash
git clone https://github.com/<your-username>/computational-biology.git

cd computational-biology
```

---

# Create a Virtual Environment

## Windows

```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1
```

## Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

If the repository is still under development:

```bash
pip install \
jupyterlab \
notebook \
numpy \
scipy \
pandas \
matplotlib \
seaborn \
scikit-learn \
scikit-image \
biopython \
networkx \
scikit-bio \
pytest \
jupytext \
nbstripout \
papermill \
rich \
tqdm
```

---

# Save Dependencies

Whenever packages are added:

```bash
pip freeze > requirements.txt
```

---

# Launch JupyterLab

```bash
jupyter lab
```

---

# Visual Studio Code

Recommended Extensions

* Python
* Pylance
* Jupyter
* GitLens
* Markdown All in One
* Error Lens
* Ruff
* YAML
* Docker (optional)

---

# Git Configuration

Configure Git once.

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

Verify:

```bash
git config --list
```

---

# GitHub CLI

Login

```bash
gh auth login
```

Verify

```bash
gh auth status
```

---

# Recommended Folder Workflow

```text
Repository
        │
        ├── Read README.md
        │
        ├── Open Learning_Progress.md
        │
        ├── Choose current module
        │
        ├── Read roadmap.md
        │
        ├── Open notebook
        │
        ├── Complete exercises
        │
        ├── Complete assignment
        │
        ├── Read papers
        │
        └── Commit progress
```

---

# Notebook Workflow

Every lesson should be completed in the following order.

1. Read README.md

2. Read roadmap.md

3. Open notebook

4. Study theory

5. Run code

6. Complete exercises

7. Complete assignment

8. Read recommended papers

9. Write reflection

10. Commit changes

---

# Git Workflow

Check status

```bash
git status
```

Stage files

```bash
git add .
```

Commit

```bash
git commit -m "Complete Module 01 Lesson 03"
```

Push

```bash
git push
```

---

# Repository Maintenance

Update dependencies

```bash
pip install --upgrade -r requirements.txt
```

Generate a new requirements file

```bash
pip freeze > requirements.txt
```

---

# Project Structure

```text
computational-biology/
│
├── CLAUDE.md
├── Learning_Progress.md
├── README.md
├── ENVIRONMENT.md
│
├── curriculum/
├── portfolio/
├── paper-notes/
├── progress/
├── scripts/
└── utilities/
```

---

# Reproducibility Guidelines

* Always use a virtual environment.
* Commit notebooks frequently.
* Keep code modular.
* Document every experiment.
* Record package versions.
* Avoid hard-coded paths.
* Store reusable code inside `utilities/`.
* Keep datasets organized.
* Use descriptive commit messages.

---

# Troubleshooting

## Virtual environment activation fails

Windows:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## Jupyter does not start

```bash
python -m pip install --upgrade notebook jupyterlab
```

---

## Package installation errors

Upgrade pip first.

```bash
python -m pip install --upgrade pip
```

Then reinstall requirements.

---

## GitHub authentication issues

Re-authenticate.

```bash
gh auth login
```

---

# Future Tools

These tools may be introduced in later curriculum modules.

* Docker
* Podman
* Snakemake
* Nextflow
* Conda
* Mamba
* Rust
* CUDA
* PyTorch
* BLAST+
* SAMtools
* BWA
* HISAT2
* STAR
* GATK

---

# Repository Principles

* Learn by implementing.
* Prefer reproducible workflows.
* Build reusable scientific software.
* Read research papers regularly.
* Maintain a public portfolio.
* Track progress continuously.
* Focus on understanding rather than memorization.

---

**Last Updated:** June 2026
**Repository:** Computational Biology Research Notebook
**Status:** Active Development
