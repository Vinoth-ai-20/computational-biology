# Module 03 — Statistics and Probability

**Depth tier:** Tier 1 — Master  
**Week budget:** Weeks 2–10 (parallel with Modules 04 and 05)  
**Notebooks:** 18  
**Status:** ⏳ Not started

---

## Motivation

Statistics is **the single most-tested non-coding skill** in Track A bioinformatics interviews.
Direct, cold questions on t-tests, p-value interpretation, and multiple-testing correction
appear in nearly every research associate and junior bioinformatics engineer interview documented
in the research underlying this curriculum. This module builds that knowledge from first principles
to implementation to critical reading of published methods.

---

## Track A relevance (India RA / JRF / Bioinformatics Engineer)

The typical interview pattern:
1. "What is a t-test? When would you use a paired vs. unpaired test?" (asked cold, not as a hint)
2. "You have 20,000 genes and you've computed a p-value for each. What do you do with them?"
3. "What is FDR? How is it different from the family-wise error rate?"
4. "Your p-value is 0.049. Is the result significant? What else do you need to know?"

All four of these are answered rigorously by NB05, NB06, NB11, and NB10 respectively.

---

## Track B relevance (European PhD applications)

- Every genomics, transcriptomics, or clinical data paper uses statistical testing
- FDR correction (NB11) is required to read Methods sections critically
- Bayesian inference (NB13) is the statistical framework of many European computational
  biology groups (EMBL-EBI, IMPRS, Wellcome Sanger)
- Power analysis (NB12) shows you can design experiments, not just analyse existing data

---

## Portfolio artifact

**A full statistical analysis report** on a public gene expression dataset (GEO):
- Differential expression testing (t-test / Wilcoxon)
- Multiple-testing correction (Benjamini-Hochberg FDR)
- Volcano plot, MA plot, QQ-plot
- Bootstrapped confidence intervals on effect sizes
- Written as a reproducible notebook suitable for direct portfolio inclusion

Delivered in NB17. Saved to `portfolio/module03_statistical_analysis_report.png`.

---

## Prerequisites

- Module 01 complete (NumPy, Pandas, Matplotlib, SciPy basics)
- Module 02 NB02–NB03 (derivatives, integrals — needed for likelihood)
