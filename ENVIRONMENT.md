# ENVIRONMENT.md — Environment Setup & Repository Bootstrap

This document is the single source of truth for setting up and reproducing the computational environment for this repository. Anyone, including future Vinoth, should be able to reproduce any notebook's output from a clean clone using only these instructions.

**Last verified:** June 2026
**Python version:** 3.12 (recommended), 3.11 (minimum)
**Primary platform:** Windows 11

---

## Table of Contents

1. [Supported Operating Systems](#1-supported-operating-systems)
2. [Hardware Recommendations](#2-hardware-recommendations)
3. [Prerequisites: Core Tools](#3-prerequisites-core-tools)
4. [Python Environment Setup](#4-python-environment-setup)
5. [Package Installation](#5-package-installation)
6. [JupyterLab Configuration](#6-jupyterlab-configuration)
7. [VS Code Configuration](#7-vs-code-configuration)
8. [Git Configuration](#8-git-configuration)
9. [GitHub CLI](#9-github-cli)
10. [Pre-commit Hooks](#10-pre-commit-hooks)
11. [Rust Toolchain](#11-rust-toolchain)
12. [Optional: Docker](#12-optional-docker)
13. [One-Command Bootstrap](#13-one-command-bootstrap)
14. [Verifying the Setup](#14-verifying-the-setup)
15. [Troubleshooting](#15-troubleshooting)

---

## 1. Supported Operating Systems

| OS | Status | Notes |
|----|--------|-------|
| Windows 11 (primary) | Fully supported | Use Windows Terminal + PowerShell 7 |
| macOS 13+ | Fully supported | Use iTerm2 or built-in Terminal |
| Ubuntu 22.04 / Debian 12 | Fully supported | Standard Linux setup |

**Windows users:** Modules 08 and 09 use Unix-native bioinformatics tools (BWA, STAR, SAMtools). Install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) for those modules. All other modules work natively on Windows.

---

## 2. Hardware Recommendations

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4 cores | 8+ cores |
| RAM | 16 GB | 32 GB |
| Storage | 20 GB free | 100 GB SSD |
| GPU | — | NVIDIA (optional, for Module 13–14 GPU notebooks only) |

---

## 3. Prerequisites: Core Tools

Install these before setting up the Python environment.

### Git

```bash
# Verify (need 2.40+)
git --version

# Install on Ubuntu/Debian
sudo apt-get install git

# Install on macOS
brew install git

# Install on Windows
# Download from https://git-scm.com/download/win
# Or via winget:
winget install --id Git.Git
```

### GitHub CLI

```bash
# Verify (need 2.40+)
gh --version

# Install on Ubuntu/Debian
sudo apt install gh

# Install on macOS
brew install gh

# Install on Windows
winget install --id GitHub.cli

# Authenticate (run once)
gh auth login
```

### Recommended Terminal

| Platform | Recommendation |
|----------|---------------|
| Windows | Windows Terminal (Microsoft Store) + PowerShell 7 |
| macOS | iTerm2 or built-in Terminal |
| Linux | Any modern terminal emulator |

---

## 4. Python Environment Setup

**Python 3.12 recommended; 3.11 minimum.** Choose one environment manager — do not mix them in the same session.

### Option A: uv (Recommended — fastest)

[uv](https://github.com/astral-sh/uv) is a modern, fast Python package and project manager written in Rust.

```bash
# Install uv
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Verify
uv --version

# Create virtual environment (from repo root)
uv venv --python 3.12 .venv

# Activate
# macOS / Linux
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Install all dependencies
uv pip install -r requirements.txt
```

### Option B: conda / mamba (Alternative — better for complex bioinformatics deps)

```bash
# Install Miniforge (recommended over Miniconda)
# https://github.com/conda-forge/miniforge

# Create environment from spec
conda env create -f environment.yml

# Activate
conda activate compbio

# Verify
python --version
```

---

## 5. Package Installation

### Core scientific stack

```bash
pip install numpy scipy pandas matplotlib seaborn scikit-learn
```

### Bioinformatics

```bash
pip install biopython scikit-bio pydeseq2
```

### Notebook reproducibility toolchain

```bash
pip install jupyterlab jupytext nbstripout papermill
```

### Testing and packaging

```bash
pip install pytest pytest-cov coverage build
```

### Machine learning (Modules 13–14)

```bash
# CPU-only PyTorch (sufficient for all modules except the GPU acceleration notebook)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# For GPU support, follow https://pytorch.org/get-started/locally/
```

### Single-cell and network biology (Modules 10, 12)

```bash
pip install scanpy networkx cobra
```

### Agent-based modeling (Module 15)

```bash
pip install mesa
```

### Code quality

```bash
pip install pre-commit ruff mypy
```

### Full install (preferred)

```bash
# Using pip
pip install -r requirements.txt

# Using conda
conda env create -f environment.yml
```

---

## 6. JupyterLab Configuration

### Install and launch

```bash
pip install jupyterlab
jupyter lab
```

### Recommended extensions

```bash
pip install jupyterlab-git                         # Git integration
pip install jupyterlab-lsp python-lsp-server[all]  # Code completion
```

### Jupytext — the notebook pairing workflow

Every notebook in `notebooks/` is paired with a `.py` file (Jupytext percent format). The `.py` file is what gets diffed and reviewed in git; the `.ipynb` is regenerated from it.

```bash
# Sync a notebook pair manually
jupytext --sync notebooks/your_notebook.ipynb

# Convert .py → .ipynb for running
jupytext --to notebook notebooks/your_notebook.py

# Convert .ipynb → .py for editing
jupytext --to py:percent notebooks/your_notebook.ipynb
```

Jupytext is configured in `pyproject.toml`. The pairing happens automatically after `pre-commit install`.

### nbstripout — strip outputs before commit

nbstripout is wired into the pre-commit hooks. It strips output cells automatically on every `git commit`, keeping diffs readable and the repository lean.

```bash
# Strip outputs manually
nbstripout notebooks/your_notebook.ipynb

# Check which notebooks would be stripped
nbstripout --dry-run notebooks/*.ipynb
```

### papermill — parametric re-execution

Used when a notebook needs to be re-run on a new dataset without hand-editing outputs.

```bash
# Re-execute a notebook with a parameter override
papermill notebooks/09_differential_expression.ipynb \
          outputs/09_executed.ipynb \
          -p dataset_accession GSE123456
```

---

## 7. VS Code Configuration

### Required extensions

| Extension | Extension ID | Purpose |
|-----------|-------------|---------|
| Python | `ms-python.python` | Python language support |
| Pylance | `ms-python.vscode-pylance` | Type checking and IntelliSense |
| Jupyter | `ms-toolsai.jupyter` | Notebook editing |
| Ruff | `charliermarsh.ruff` | Fast linting and formatting |
| GitLens | `eamodio.gitlens` | Enhanced Git integration |
| Markdown All in One | `yzhang.markdown-all-in-one` | Markdown editing |
| Even Better TOML | `tamasfe.even-better-toml` | TOML support |
| rust-analyzer | `rust-lang.rust-analyzer` | Rust (Modules 16–17) |
| Error Lens | `usernamehw.errorlens` | Inline error display |

### Recommended workspace settings (`settings.json`)

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "jupyter.notebookFileRoot": "${workspaceFolder}",
  "files.autoSave": "onFocusChange"
}
```

---

## 8. Git Configuration

```bash
# Set identity (required before first commit)
git config --global user.name "Vinoth Murugan"
git config --global user.email "vinoth.ac.in@gmail.com"

# Set default branch name
git config --global init.defaultBranch main

# Line-ending handling
# Windows
git config --global core.autocrlf true
# macOS / Linux
git config --global core.autocrlf input

# Useful aliases
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.st "status -sb"

# Verify
git config --list
```

---

## 9. GitHub CLI

```bash
# Authenticate (run once)
gh auth login

# Verify
gh auth status

# Clone this repository
gh repo clone Vinoth-ai-20/computational-biology

# View repository info
gh repo view
```

---

## 10. Pre-commit Hooks

Pre-commit runs Jupytext sync and nbstripout automatically on every `git commit`. Install it once after cloning.

```bash
# Install pre-commit
pip install pre-commit

# Install hooks (run from repo root — do this once)
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

The hook configuration lives in `.pre-commit-config.yaml` at the repo root.

---

## 11. Rust Toolchain

Required for Modules 16 (`compbio_utils` HPC extensions) and 17 (HPC, Parallel & Rust).

```bash
# Install rustup
# macOS / Linux
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Windows: download rustup-init.exe from https://rustup.rs

# Verify (need rustc 1.77+)
rustc --version
cargo --version

# Install maturin (Python–Rust bridge)
pip install maturin

# Verify
maturin --version
```

---

## 12. Optional: Docker

Docker provides the strongest reproducibility guarantee. Use it when you need results to match exactly across machines.

### Install

Download Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/).

### Build the project image

```bash
docker build -t compbio-env:latest .
```

### Run JupyterLab inside the container

```bash
# macOS / Linux
docker run -p 8888:8888 -v $(pwd):/workspace compbio-env:latest \
  jupyter lab --ip=0.0.0.0 --no-browser

# Windows PowerShell
docker run -p 8888:8888 -v ${PWD}:/workspace compbio-env:latest `
  jupyter lab --ip=0.0.0.0 --no-browser
```

*A `Dockerfile` and `docker-compose.yml` will be added when the containerization notebook in Module 16 is completed.*

---

## 13. One-Command Bootstrap

Clone and set up the full environment in one sequence:

```bash
# 1. Clone
git clone https://github.com/Vinoth-ai-20/computational-biology.git
cd computational-biology

# 2a. Using uv (recommended)
uv venv --python 3.12 .venv
source .venv/bin/activate          # macOS / Linux
# .venv\Scripts\Activate.ps1       # Windows PowerShell
uv pip install -r requirements.txt

# 2b. Using conda (alternative)
# conda env create -f environment.yml && conda activate compbio

# 3. Install pre-commit hooks
pre-commit install

# 4. Verify
python scripts/verify_environment.py
```

---

## 14. Verifying the Setup

```bash
python scripts/verify_environment.py
```

Expected output:

```
Python 3.12.x        ✓
NumPy 1.26.x         ✓
SciPy 1.12.x         ✓
Pandas 2.2.x         ✓
Matplotlib 3.8.x     ✓
Seaborn 0.13.x       ✓
scikit-learn 1.4.x   ✓
Biopython 1.83+      ✓
JupyterLab 4.x       ✓
Jupytext 1.16.x      ✓
nbstripout 0.7.x     ✓
pytest 8.x           ✓
pre-commit hooks     ✓
```

*Note: `scripts/verify_environment.py` is created in the Module 01 environment-setup notebook.*

---

## 15. Troubleshooting

### `ModuleNotFoundError` after activating the environment

Confirm you activated the correct environment before launching JupyterLab:

```bash
which python    # macOS / Linux — should point inside .venv
where python    # Windows
```

### JupyterLab does not show the `.venv` kernel

Register the kernel manually:

```bash
pip install ipykernel
python -m ipykernel install --user --name compbio --display-name "Python (compbio)"
```

### nbstripout not running on commit

```bash
pre-commit install   # re-run if hooks appear missing
pre-commit run --all-files
```

### Rust compilation errors in Module 17

Ensure both `maturin` and the Rust toolchain are installed, and that you are inside the activated Python environment when running `maturin develop`.

### PowerShell execution policy error when activating `.venv`

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### conda and uv conflict in the same session

Use one, not both. If conda is initialized in the session, run `conda deactivate` before activating a uv-managed `.venv`.

### Package installation fails behind a corporate proxy

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

---

*See also: [README.md](README.md) — [CLAUDE.md](CLAUDE.md) §7.2 (reproducibility toolchain)*
