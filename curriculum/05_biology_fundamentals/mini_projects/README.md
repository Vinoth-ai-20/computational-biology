# Module 05 — Mini-Projects

## MP01 — Hardy-Weinberg + Genetic Drift Simulator (NB15)

**Portfolio artifact:** `portfolio/module05_hardy_weinberg_drift_simulator.png`

Implement a self-contained population genetics simulator from scratch:

- **HWE engine:** given allele frequency p and population size N, generate
  genotype counts under HWE
- **Wright-Fisher engine:** simulate allele frequency trajectories for n_gen
  generations with population size N and optional selection coefficient s
- **Visualization:** 4-panel figure showing:
  - Panel A: allele frequency trajectories (many trials) — drift alone
  - Panel B: allele frequency trajectories with directional selection (s=0.1)
  - Panel C: time to fixation vs. population size (N = 10, 50, 200, 1000)
  - Panel D: HWE expected vs. observed genotype frequencies with chi-square test

**Pass standard:** All 4 panels present. Each panel labeled with biological
interpretation. Chi-square test result stated explicitly.

---

## MP02 — Biology for Computer Scientists (NB16)

**Portfolio artifact:** `portfolio/module05_biology_for_computer_scientists.ipynb`
(publishable as a blog post or teaching resource)

Write a polished Jupyter notebook titled "Biology for Computer Scientists."
Audience: someone with strong Python and statistics but zero formal biology.

Required sections:
1. **The cell as a factory** — analogy-driven introduction
2. **The central dogma as a data pipeline** — DNA as source code, RNA as runtime,
   protein as executable
3. **The genome as a database** — organization, scale, indexing (genes, chromosomes)
4. **Mutation as bit-flip errors** — types, rates, detection
5. **Evolution as optimization without a loss function** — selection, drift, fitness
6. **One worked example** — a real biological question answered computationally

**Pass standard:** Can be shared publicly without embarrassment. No jargon without
definition. Every analogy is accurate (doesn't break down immediately). Includes
at least one runnable Python cell per section.
