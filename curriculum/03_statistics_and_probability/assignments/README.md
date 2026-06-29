# Assignments — Module 03: Statistics and Probability

Module 03 (Tier 1) has one assignment, delivered through NB17.

## A01 — Full Statistical Analysis Report (Portfolio Artifact)

**Deliverable:** A polished, reproducible statistical analysis notebook on a public GEO dataset with:
- Data loading and QC (missing values, outlier samples)
- Normalization (log2-CPM or quantile normalisation)
- Differential expression testing: t-test + Wilcoxon side-by-side
- Multiple-testing correction: Bonferroni AND Benjamini-Hochberg
- Volcano plot (log2 fold-change vs. -log10 FDR-adjusted p)
- QQ-plot of p-values under the null
- Bootstrapped confidence intervals on the top 10 effect sizes
- 300-word methods narrative (written, not code comments)

**Portfolio outputs:**
- `portfolio/module03_statistical_analysis_report.png` (4-panel figure)
- `portfolio/module03_methods_narrative.md` (written summary)

**Completion criteria:**
- [ ] Notebook runs top-to-bottom on a clean clone
- [ ] BH correction implemented from scratch (not only statsmodels)
- [ ] Volcano plot publication-quality (axis labels, significance threshold line, top genes annotated)
- [ ] QQ-plot included and interpreted in text
- [ ] Oral exam self-test: "walk me through your analysis" answered in ≤ 5 minutes
