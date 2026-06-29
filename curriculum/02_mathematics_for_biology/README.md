# Module 02 — Mathematics for Biology

**Depth tier:** Tier 2 — Working competence  
**Week budget:** Weeks 1–8 (parallel with Modules 01, 03, 05)  
**Notebooks:** 12  
**Status:** ⏳ Not started — 0 / 12 notebooks

---

## Motivation

Mathematics is the language biology is learning to speak. A computational biologist
who cannot follow the derivation of a growth model, read an ODE system in a paper,
or understand why gradient descent converges is dependent on black-box tools. This
module builds working fluency — not research-level mastery — in the specific
mathematics that appears in biological modelling, population genetics, and systems
biology.

Tier 2 means: use the methods correctly, explain what they do and why, recognize when
something looks wrong. It does not mean: derive from first principles, prove
convergence theorems, or specialize deeply. The quarterly checkpoint at Month 3 is
the explicit moment to reassess whether this module should be promoted to Tier 1 based
on real signal (a lab opening in mathematical biology, sustained personal interest).

---

## Learning Objectives

By the end of this module you will be able to:

1. Explain exponential and logistic growth models and fit them to data
2. Set up and interpret a system of ODEs from a biological description
3. Implement Euler integration and RK4 from scratch in NumPy
4. Simulate and visualize the Lotka-Volterra predator-prey system
5. Explain fixed points and stability qualitatively (no eigenvalue analysis required)
6. Use gradient descent as a computational optimization method
7. Apply discrete mathematics vocabulary (graphs, degree, path) to biological networks
8. Read and follow a mathematical biology paper's modelling section

---

## Track A Relevance

**Occasional.** Growth-curve/kinetics modelling appears in some RA postings
(pharmacokinetics, microbial growth, dose-response curves). The ODE literacy built
here directly supports Module 12 (Systems & Network Biology) and Module 15
(Simulation & ABM), which have higher Track A relevance.

## Track B Relevance

**Required.** Following systems-biology and population-genetics reasoning in papers
and interviews requires this vocabulary. A PhD applicant who cannot read an ODE system
in a paper is visibly limited. This module removes that limitation.

---

## Portfolio Artifact

**Lotka-Volterra solver with phase-portrait visualization** — a polished notebook
showing: the biological motivation, the ODE system, fixed-point analysis (by
intuition, not calculation), numerical solution with both Euler and RK4, phase
portrait, and parameter sensitivity analysis.

---

## Prerequisites

- Module 01 Notebooks 11–12 (SciPy optimization and ODEs) — this module assumes
  `solve_ivp` is familiar and adds the mathematical understanding underneath it
- High-school calculus (derivatives, integrals) at recall level — this module
  reviews and extends, not introduces from zero

---

## Subtopics

See [`roadmap.md`](roadmap.md) for the full ordered notebook breakdown.

- **Calculus refresher:** derivatives, integrals, area-under-curve intuition
- **Growth models:** exponential, logistic, difference equations
- **ODEs:** separable first-order, geometric intuition, fixed points
- **Numerical methods:** Euler, RK4 — implemented from scratch
- **Systems of ODEs:** Lotka-Volterra, phase portraits
- **Discrete mathematics:** graphs, combinatorics for sequence analysis
- **Optimization:** gradient descent by hand and in code

---

## References

See [`references.md`](references.md).

## Papers

See [`papers.md`](papers.md).

---

*Runs in parallel with Modules 01, 03, and 05 from Week 1.*

*See also: [CLAUDE.md](../../CLAUDE.md) — [Learning_Progress.md](../../Learning_Progress.md) §4 Module 02*
