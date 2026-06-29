# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Notebook 01 — Welcome and Repository Orientation
#
# **Module:** 00 — Orientation
# **Notebook:** 01 of 13
# **Paired file:** `notebooks/00_welcome_and_repository_orientation.py` ↔ `.ipynb`
# **Prerequisites:** None — this is your first notebook.
# **Time estimate:** 60–90 minutes
#
# ---
#
# > **How to read this notebook.**
# > Every notebook in this program follows the same 13-step sequence:
# > Motivation → Intuition → Biological Background → Mathematical Explanation →
# > Computational Explanation → Python Implementation → Visualization →
# > Exercises (posed only) → Quiz → Reflection → Papers → References → Future Work.
# >
# > This notebook *is* the sample format. Every notebook you write afterward
# > will have this exact structure. Pay attention to it, not just the content.

# %% [markdown]
# ---
# ## Step 1 — Motivation
#
# **Why does this notebook exist? What problem does it solve?**
#
# This repository is a 12-month Research Accelerator — a structured, portfolio-driven
# program for becoming a competitive computational biologist. The problem is that a
# repository without a map is just a pile of files. This notebook is the map.
#
# Three things this notebook will make permanently clear:
#
# 1. **What every folder is for** — so you never wonder "where does this go?"
# 2. **What the non-negotiable rules are** — the 13-step lesson sequence, the
#    Three-Pass paper reading method, the "no code ships that you can't explain" rule.
#    These are not suggestions; they are the structural load-bearing elements of the program.
# 3. **The 12-month shape** — which modules run in parallel, what the Month 6 and
#    Month 12 checkpoints actually require, and why depth-tiering is the mechanism that
#    makes this achievable in a fixed time window.
#
# If you finish this notebook having understood these three things, everything else
# in the repository will make sense. If you skip it, later notebooks will feel arbitrary.

# %% [markdown]
# ---
# ## Step 2 — Intuition
#
# **Plain language, concrete analogy.**
#
# Think of this repository as a **research lab notebook** — the kind a working scientist
# keeps on their bench.
#
# A real lab notebook is not a diary. It is a structured, reproducible record:
# - Every experiment is dated and indexed.
# - Every reagent is named and sourced.
# - Every result is recorded exactly as observed — even failures.
# - A stranger should be able to reproduce any experiment from the notes alone.
#
# This repository works the same way:
#
# | Lab notebook concept | This repository equivalent |
# |---|---|
# | Indexed experiment entries | `notebooks/` — one per topic, in order |
# | Materials and methods | `ENVIRONMENT.md` — exact toolchain, pinned versions |
# | Raw data storage | `datasets/raw/` (gitignored, fetch scripts provided) |
# | Results and figures | notebook outputs + `portfolio/` for the polished ones |
# | Literature references | `paper-notes/` — Three-Pass logs per paper |
# | Lab meeting presentations | `portfolio/` — defensible, polished artifacts |
# | Audit trail | Git history — every change, who made it, why |
#
# The one thing a lab notebook cannot do that this repository can: **reproduce itself
# from a clean clone** on any machine, at any time, with one command.
# That is what the reproducibility toolchain (Jupytext, nbstripout, pre-commit, `uv`) buys.

# %% [markdown]
# ---
# ## Step 3 — Biological Background
#
# *This step is not applicable to Module 00 — orientation is a meta-module, not a
# biology module. Biological content begins in Module 05 (Biology Fundamentals),
# which runs in parallel from Week 1.*
#
# **Why the step is still listed:** Every notebook in every module has this heading.
# Its presence here, even when it says "N/A," is deliberate — it ensures you never
# accidentally skip the biological framing in a module where it does apply.

# %% [markdown]
# ---
# ## Step 4 — Mathematical Explanation
#
# *Not applicable to this orientation notebook. Mathematical content begins in
# Module 02 (Mathematics for Biology) and Module 03 (Statistics), both of which
# run in parallel from Week 1–2.*

# %% [markdown]
# ---
# ## Step 5 — Computational Explanation
#
# **The directory tree as a computational system.**
#
# Every folder in the repository has a defined purpose. This is not aesthetic —
# it is the interface contract between modules. When Module 09 expects a cleaned
# CSV in `datasets/processed/`, that expectation is reliable because the architecture
# enforces where processed data lives.
#
# ```
# computational-biology/
# ├── README.md                    ← front door; 12-month plan at a glance
# ├── ENVIRONMENT.md               ← exact setup; one-command bootstrap
# ├── CLAUDE.md                    ← project constitution; rules that never bend
# ├── Learning_Progress.md         ← live tracker; update when notebooks complete
# ├── requirements.txt / environment.yml / pyproject.toml
# ├── .pre-commit-config.yaml      ← Jupytext + nbstripout hooks (auto-run on commit)
# │
# ├── curriculum/                  ← one folder per module
# │   ├── 00_orientation/          ← this module
# │   ├── 01_python_scientific_computing/
# │   └── ... (20 modules total)
# │
# │   Each module contains:
# │   ├── README.md       ← objectives, tier, week budget, Track A/B relevance
# │   ├── roadmap.md      ← ordered checklist of notebooks (track progress here)
# │   ├── references.md   ← books, docs, key labs, key software
# │   ├── papers.md       ← reading list with Pass-3 guidance
# │   ├── notebooks/      ← the lecture-equivalent content (YOU ARE HERE)
# │   ├── exercises/      ← exercise files, posed but not solved
# │   ├── assignments/    ← larger, less-scaffolded work
# │   ├── mini_projects/  ← Tier 1/2 modules only
# │   └── datasets/       ← raw/ (gitignored) + processed/
# │
# ├── portfolio/           ← polished subset; what gets linked in applications
# ├── paper-notes/         ← one file per paper read; Three-Pass log
# ├── progress/            ← weekly/monthly review logs
# ├── scripts/             ← reusable CLI tools (data fetchers, batch runners)
# └── utilities/compbio_utils/  ← the shared, tested Python utility library
# ```
#
# **The two source-of-truth files you must never modify arbitrarily:**
#
# - `CLAUDE.md` — the project constitution. Version-controlled. Only bump the version
#   at quarterly checkpoints or structural changes.
# - `Learning_Progress.md` — the live tracker. Update the module status and checklist
#   whenever a notebook completes. This is how you measure progress.

# %% [markdown]
# ---
# ## Step 6 — Python Implementation
#
# **Walk through the repository structure programmatically.**
# Run each cell, read the output, then move on.

# %%
# Cell 6.1 — Verify Python version and basic imports
import sys
import os
import pathlib

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current working directory: {os.getcwd()}")

# Navigate to the repo root (two levels up from this notebook's location)
repo_root = pathlib.Path(__file__).resolve().parent.parent.parent
print(f"\nRepository root: {repo_root}")
print(f"Root exists: {repo_root.exists()}")


# %%
# Cell 6.2 — Print the repository top-level structure
def print_tree(
    root: pathlib.Path, prefix: str = "", max_depth: int = 2, depth: int = 0
) -> None:
    """Print a directory tree up to max_depth levels."""
    if depth > max_depth:
        return
    try:
        items = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name))
    except PermissionError:
        return
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        connector = "└── " if is_last else "├── "
        marker = "/" if item.is_dir() else ""
        print(f"{prefix}{connector}{item.name}{marker}")
        if item.is_dir() and depth < max_depth:
            extension = "    " if is_last else "│   "
            print_tree(item, prefix + extension, max_depth, depth + 1)


print(f"Repository structure (depth 2):\n{'=' * 45}")
print_tree(repo_root, max_depth=2)

# %%
# Cell 6.3 — Verify that the 20 curriculum module folders exist (or are planned)
curriculum_dir = repo_root / "curriculum"
expected_modules = [
    "00_orientation",
    "01_python_scientific_computing",
    "02_mathematics_for_biology",
    "03_statistics_and_probability",
    "04_linear_algebra",
    "05_biology_fundamentals",
    "06_genetics_and_evolution",
    "07_biochemistry_and_molecular_biology",
    "08_bioinformatics_sequence_analysis",
    "09_genomics_and_ngs",
    "10_transcriptomics_and_proteomics",
    "11_structural_biology",
    "12_systems_and_network_biology",
    "13_machine_learning_for_biology",
    "14_deep_learning_and_gnns",
    "15_simulation_and_agent_based_modeling",
    "16_research_software_engineering",
    "17_hpc_parallel_and_rust",
    "18_scientific_writing_and_open_science",
    "19_research_seminar_and_paper_reading",
    "20_capstone_projects",
]

print(f"Curriculum module check:\n{'=' * 45}")
present_count = 0
for module in expected_modules:
    path = curriculum_dir / module
    status = "✓ exists" if path.exists() else "○ not yet created"
    if path.exists():
        present_count += 1
    print(f"  {status:15s}  {module}")

print(f"\n{present_count}/{len(expected_modules)} module folders present")

# %%
# Cell 6.4 — Read and display the first 10 lines of CLAUDE.md (the project constitution)
claude_md = repo_root / "CLAUDE.md"
if claude_md.exists():
    lines = claude_md.read_text(encoding="utf-8").splitlines()
    print("First 10 lines of CLAUDE.md:")
    print("=" * 45)
    for line in lines[:10]:
        print(line)
    print(f"\n... ({len(lines)} lines total)")
else:
    print("CLAUDE.md not found — check the repo root path above.")

# %% [markdown]
# ---
# ## Step 7 — Visualization
#
# **The 12-month module dependency graph.**
#
# This text diagram shows which modules run in parallel and in what order.
# Study it until you can reproduce it from memory — the exercise below asks you to.
#
# ```
# MONTH  1   2   3   4   5   6   7   8   9  10  11  12
#
# 01 Python  [===========]
# 02 Math    [==================]
# 03 Stats   [============================]
# 04 LinAlg      [=======================]
# 05 Bio     [============================]
# 06 Genetics             [===========]
# 07 Biochem              [===========]
# 08 SeqAnal              [===========]
# 09 NGS              [===========]
# 10 Omics                    [=======]
# 11 Struct                       [===]    (Tier 3 sprint)
# 12 Systems             [===========]
# 13 ML                  [===========]
# 14 DL+GNN                          [=]  (Tier 3 sprint)
# 15 ABM                             [====]
# 16 RSE    [===================================]  (ongoing)
# 17 HPC                              [=======]
# 18 Writing [==========================================]  (weekly habit)
# 19 Seminar [==========================================]  (weekly habit)
# 20 Capstone                                    [=====]
#
# Track A bar: Month 6 ────────────────────────────▲
# Track B bar: Month 12 ──────────────────────────────────────▲
# ```
#
# Key observation: **Modules 01, 03, 05, and 16 all start in Month 1 and run in parallel.**
# A study session in Week 2 might touch NumPy (01), probability (03), and cell biology (05)
# in the same afternoon. This is the parallel-tracks design — it is not multitasking,
# it is deliberate interleaving to keep all three foundations moving.

# %%
# Cell 7.1 — Print the module overview table programmatically
modules = [
    (
        "01",
        "Python & Scientific Computing",
        "Tier 1",
        "Weeks 1–6",
        "Direct (baseline for every posting)",
    ),
    ("02", "Mathematics for Biology", "Tier 2", "Weeks 1–8", "Occasional"),
    (
        "03",
        "Statistics & Probability",
        "Tier 1",
        "Weeks 2–10",
        "Critical (most-tested non-coding skill)",
    ),
    ("04", "Linear Algebra", "Tier 2", "Weeks 3–9", "PCA on expression data"),
    ("05", "Biology Fundamentals", "Tier 1", "Weeks 1–10", "Baseline biology literacy"),
    ("06", "Genetics & Evolution", "Tier 2", "Weeks 8–14", "Genomics-adjacent roles"),
    (
        "07",
        "Biochemistry & Mol. Biology",
        "Tier 2",
        "Weeks 9–14",
        "Wet-lab-adjacent roles",
    ),
    (
        "08",
        "Bioinformatics: Seq. Analysis",
        "Tier 1",
        "Weeks 10–18",
        "Canonical interview module (BLAST)",
    ),
    (
        "09",
        "Genomics & NGS",
        "Tier 1",
        "Weeks 16–24",
        "Highest Track A posting relevance",
    ),
    (
        "10",
        "Transcriptomics & Proteomics",
        "Tier 2",
        "Weeks 20–26",
        "Single-cell skills",
    ),
    (
        "11",
        "Structural Biology",
        "Tier 3",
        "Weeks 24–28",
        "Survey depth (AlphaFold era)",
    ),
    (
        "12",
        "Systems & Network Biology",
        "Tier 2*",
        "Weeks 22–28",
        "Directly evidenced (IISER posting)",
    ),
    (
        "13",
        "Machine Learning for Biology",
        "Tier 1",
        "Weeks 14–22",
        "Named in EMBL/IMPRS themes",
    ),
    ("14", "Deep Learning & GNNs", "Tier 3", "Weeks 24–28", "Differentiator"),
    ("15", "Simulation & ABM", "Tier 2", "Weeks 26–32", "ALife/Ecology door"),
    (
        "16",
        "Research Software Engineering",
        "Tier 1",
        "Weeks 1–40",
        "Named target role (RSE)",
    ),
    (
        "17",
        "HPC, Parallel & Rust",
        "Tier 2",
        "Weeks 30–36",
        "Differentiator (existing Rust)",
    ),
    (
        "18",
        "Scientific Writing",
        "Ongoing",
        "Year-round",
        "Written communication tested",
    ),
    ("19", "Research Seminar", "Ongoing", "Year-round", "Pass-3 muscle for Track A"),
    (
        "20",
        "Capstone Projects",
        "T1 Synth",
        "Weeks 44–52",
        "Headline portfolio artifact",
    ),
]

header = f"{'#':>3}  {'Module':<38} {'Tier':<10} {'Timeline':<14} {'Track A relevance'}"
print(header)
print("-" * len(header))
for num, name, tier, timeline, relevance in modules:
    print(f"{num:>3}  {name:<38} {tier:<10} {timeline:<14} {relevance}")

# %% [markdown]
# ---
# ## Step 8 — Exercises
#
# *Exercises are posed here. Your solution goes in the paired file:*
# *`exercises/01_welcome_exercises.md` → `exercises/solutions/01_welcome_solutions.md`*
#
# **Exercise 1 (conceptual — do it on paper, not in code):**
# Draw the module dependency graph from memory on a blank sheet of paper.
# Which modules are active in Month 1? In Month 6? Which module runs the entire year?
# Compare your drawing to Step 7's diagram above. Note every discrepancy — those are
# the parts you don't have solid yet.
#
# **Exercise 2:**
# Open `Learning_Progress.md` and find the readiness scorecards (§13).
# What is the current composite score for each of the three scorecards?
# What does the Month 6 composite target for Track A require in each dimension?
# Write the answers in `exercises/01_welcome_exercises.md`.
#
# **Exercise 3 (teach-back):**
# Explain the difference between "depth tiering" and "parallel tracks" in one plain
# sentence each. No jargon — as if explaining to a friend with no programming background.
# Write the sentences in `exercises/01_welcome_exercises.md`.

# %% [markdown]
# ---
# ## Quiz — Active Recall (answer before looking up)
#
# Answer these from memory. If you can't, go back and find the answer before continuing.
#
# 1. What are the two Track A and Track B deadlines (Month 6 and Month 12)?
# 2. Name the three Tier 1 modules that start in Month 1 alongside Module 01.
# 3. What does `nbstripout` do, and why does it matter for Git?
# 4. What does `pass3_unaided` mean in `paper-notes/`? Why is it the key metric?
# 5. What is the one rule that applies to every piece of code in this repository
#    without exception? (Hint: it involves explaining.)

# %% [markdown]
# ---
# ## Reflection
#
# *Write one paragraph here after completing this notebook. Plain English.
# What do you now understand clearly? What is still fuzzy?*
#
# **Date completed:** ____________________
#
# **Reflection:**
#
# > *[Write your reflection here — minimum 3 sentences. What was surprising?
# > What structure makes sense now that didn't before? What question does this notebook
# > leave open that you want to resolve in the next notebook?]*

# %% [markdown]
# ---
# ## Papers Referenced in This Notebook
#
# No papers are assigned in this notebook. The first paper reading session
# is Notebook 10 (Three-Pass Paper Reading), where you will apply all three passes
# to Wilson et al. (2017) — the paper that defines this program's code quality standard.
#
# **Upcoming (Notebook 10):**
# - Wilson et al. (2017), *Good enough practices in scientific computing*,
#   PLOS Computational Biology. DOI: 10.1371/journal.pcbi.1005510

# %% [markdown]
# ---
# ## References
#
# - [CLAUDE.md](../../../CLAUDE.md) — the project constitution; §1 (design philosophy),
#   §4.1 (13-step lesson sequence), §7.2 (reproducibility toolchain), §10 (Track A/B mapping)
# - [Learning_Progress.md](../../../Learning_Progress.md) — §2 (depth tiers),
#   §3 (12-month sprint calendar), §13 (readiness scorecards)
# - [README.md](../../../README.md) — front door; 12-month plan at a glance
# - [ENVIRONMENT.md](../../../ENVIRONMENT.md) — exact setup instructions

# %% [markdown]
# ---
# ## Future Work / Open Questions
#
# - After completing Module 00 orientation, revisit this notebook's module dependency
#   graph and verify it against the current `Learning_Progress.md` sprint calendar.
#   Do the timelines still feel right? If not, log the discrepancy.
# - The dependency graph above is approximate — it does not show which modules are
#   *prerequisites* for others vs. merely *concurrent*. Mapping the actual prerequisite
#   structure precisely is a useful exercise for the Month 3 quarterly checkpoint.
#
# ---
# *Next notebook: `01_environment_setup_and_verification.ipynb`*
# *See also: [roadmap.md](../roadmap.md) — [references.md](../references.md)*
