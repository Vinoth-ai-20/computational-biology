# Module 06 — Mini-Projects

## MP01 — Wright-Fisher vs. Hardy-Weinberg (NB11)

**Portfolio artifact:** `portfolio/module06_wright_fisher_vs_hardy_weinberg.png`

Build a comprehensive comparison between the Wright-Fisher model and Hardy-Weinberg
expectations, implemented from memory (no referring to Module 05 code during the attempt).

**Required panels:**

- **Panel A:** Allele frequency trajectories (drift only, N=100, p0=0.5, 50 trials)
  with HWE equilibrium line overlaid. Label how many trials fix, lose, or remain.
- **Panel B:** HWE chi-square test over time — for each generation, compute chi2 from
  simulated genotype counts. Plot chi2 statistic vs. generation; show when HWE is
  first violated at p<0.05.
- **Panel C:** Fixation probability from simulation vs. Kimura's formula
  p_fix = (1 - e^{-2Ns p0}) / (1 - e^{-2Ns})
  for s ∈ {0, 0.01, 0.05, 0.1, 0.2}; N=200, p0=0.1.
- **Panel D:** Allele frequency variance over time — simulation variance vs.
  theoretical p(1-p)·(1 - (1-1/(2N))^t).

**Pass standard:**
- All 4 panels present with biological interpretation in title
- Kimura formula matches simulation to within sampling noise
- Figure saved to portfolio path
- Every function implemented independently (no copy from Module 05)
