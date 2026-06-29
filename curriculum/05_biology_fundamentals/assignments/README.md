# Module 05 — Assignments

## A01 — Population Genetics Audit

**Linked to:** NB06–NB08  
**Due:** Before NB15 (mini-project)

Implement a complete population genetics calculator with three functions:

1. `hardy_weinberg_freqs(p)` → `(p², 2pq, q²)` — genotype frequencies under HWE
2. `hw_chi_square(obs_AA, obs_Aa, obs_aa)` → `(chi2_stat, p_value)` — test for deviation
3. `delta_p_selection(p, s, h=0.5)` → `Δp` per generation — allele frequency change under selection

All three must be implemented from scratch, validated against analytical expectations,
and accompanied by one test dataset (real or synthetic) showing the functions work.

**Deliverable:** A runnable notebook cell with all three functions and a brief worked
example explaining what each output means biologically.

## A02 — Biology Vocabulary Self-Assessment

**Linked to:** NB14  
**Due:** Before NB18 (assessment)

Write a one-sentence definition for each of the 50 vocabulary terms in NB14, **without
looking at the notebook**. Score yourself. Any term scoring < 4/5 on your own rubric
gets a second attempt — write an analogy or example that makes it stick.

**Deliverable:** A plain text or markdown file in `exercises/` with 50 definitions and
self-scores.
