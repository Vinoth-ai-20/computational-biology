# Module 15 — Simulation and Agent-Based Modeling

**Depth tier:** Tier 2 — Working competence  
**Week budget:** 5 weeks  
**Notebooks:** 12  

## Motivation

Biological systems are rarely at equilibrium. Populations fluctuate, cells move,
pathogens spread, and genomes drift. Simulation is how we study dynamics that
can't be reduced to a closed-form equation: stochastic gene expression, spatial
pattern formation, emergent collective behaviour, and multi-scale interactions
between individual cells and tissue-level outcomes. This module builds the core
toolkit — deterministic ODEs, stochastic simulation, cellular automata, and
agent-based models — used across systems biology, computational ecology, and
computational epidemiology.

## Depth-tier rationale (Tier 2)

Full Tier 1 mastery (implementing every numerical solver variant, full ABM
framework internals, complete MCMC inference) would require 15–20 notebooks.
Tier 2 gives working competence: you can build, run, visualize, and interpret
standard models; fit parameters to data; and explain the method's assumptions
and limitations in an interview. Note: prior Mesa/ABM familiarity (noted in
project constitution) accelerates NB05–NB08; port existing artefacts rather
than redoing them from scratch.

## Track A relevance

**Why this helps Track A (India RA/JRF/Bioinformatics Engineer):**
Epidemic modelling (SIR), ODE-based systems biology, and basic stochastic
simulation appear in computational biology PhD interviews and JRF written
tests. NetworkX-based network analysis is standard in bioinformatics pipelines.
Parameter estimation (NB09) is directly tested in data-science research roles.

## Track B relevance

**Why this helps Track B (European PhD):**
Systems biology programmes (EMBL, Wageningen, CSH Vienna) weight simulation
and dynamical modelling heavily. ABM is the primary method in computational
ecology, epidemiology, and artificial life — all explicitly open target
sub-fields. A working multiscale model (NB11) is a strong portfolio artefact
for these applications.

## Prerequisites

- Module 02 (Mathematics for Biology): ODEs, linear algebra
- Module 03 (Statistics): probability, basic stochastic processes
- Module 05 (Biology Fundamentals): population ecology, gene regulation
- Python: NumPy, SciPy, Matplotlib (all used throughout)

## Notebook sequence

See `roadmap.md` for the full ordered list.
