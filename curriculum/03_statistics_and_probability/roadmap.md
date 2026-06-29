# Module 03 Roadmap — Statistics and Probability

**18 notebooks | Tier 1 | Weeks 2–10**

---

## Part 1 — Foundations (NB01–NB04)

- [ ] **NB01** `01_why_statistics_for_biology.ipynb`
  - The interview reality: what is actually asked in Track A
  - Descriptive vs. inferential statistics
  - The role of statistics in genomics and systems biology
  - Module dependency map

- [ ] **NB02** `02_descriptive_statistics_distributions.ipynb`
  - Mean, median, mode, variance, standard deviation, IQR
  - Empirical distributions: histograms, kernel density estimates
  - Box plots, violin plots — when to use each
  - Biological example: GC content distribution across genes

- [ ] **NB03** `03_probability_fundamentals.ipynb`
  - Sample space, events, probability axioms
  - Conditional probability: $P(A|B) = P(A \cap B) / P(B)$
  - Independence: $P(A \cap B) = P(A) \cdot P(B)$
  - Bayes' theorem: derivation and intuition
  - Biological example: diagnostic test sensitivity / specificity

- [ ] **NB04** `04_distributions_normal_and_clt.ipynb`
  - The Normal distribution: PDF, CDF, Z-scores
  - The Central Limit Theorem: simulation from scratch
  - Common biological distributions: Poisson, Binomial, Negative Binomial
  - When to assume normality — and when not to

---

## Part 2 — Hypothesis Testing (NB05–NB09)

- [ ] **NB05** `05_hypothesis_testing_fundamentals.ipynb`
  - Null and alternative hypotheses
  - Type I error (α), Type II error (β), power
  - p-value: the correct definition and the three most common misinterpretations
  - One-tailed vs. two-tailed tests

- [ ] **NB06** `06_t_tests.ipynb`
  - One-sample t-test: is this mean different from μ₀?
  - Independent two-sample t-test: equal and unequal variance (Welch's)
  - Paired t-test: before/after measurements
  - Biological example: gene expression difference between two conditions
  - Implementing from scratch using t-statistic formula and scipy validation

- [ ] **NB07** `07_anova_basics.ipynb`
  - One-way ANOVA: comparing means across ≥ 3 groups
  - F-statistic: between-group vs. within-group variance
  - Post-hoc tests: Tukey's HSD
  - Biological example: expression across three tissue types

- [ ] **NB08** `08_nonparametric_tests.ipynb`
  - When normality fails: rank-based tests
  - Mann-Whitney U test (independent samples)
  - Wilcoxon signed-rank test (paired)
  - Kruskal-Wallis test (non-parametric ANOVA)
  - Biological example: comparing two NGS coverage distributions

- [ ] **NB09** `09_correlation.ipynb`
  - Pearson correlation: linearity assumption, sensitivity to outliers
  - Spearman rank correlation: robust, monotone relationships
  - Correlation vs. causation — worked counterexamples
  - Biological example: co-expression analysis between two genes

---

## Part 3 — Advanced Testing and Correction (NB10–NB12)

- [ ] **NB10** `10_pvalues_and_misinterpretations.ipynb`
  - The correct definition of a p-value (from first principles)
  - Five common misinterpretations — each refuted concretely
  - Effect size: Cohen's d, fold change
  - Ioannidis (2005): why most published findings are false — worked through
  - Publication bias and the file drawer problem

- [ ] **NB11** `11_multiple_testing_correction.ipynb`
  - The multiple testing problem: why 20,000 t-tests at α=0.05 gives 1,000 false positives
  - Bonferroni correction: FWER control — conservative, when to use
  - Benjamini-Hochberg procedure: FDR control — the genomics standard
  - Implementing BH from scratch (sort, rank, step-up procedure)
  - Validating against `statsmodels.stats.multitest.multipletests`
  - Q-Q plot interpretation

- [ ] **NB12** `12_power_analysis.ipynb`
  - Statistical power: $1 - \beta$
  - Four quantities: α, power, effect size, sample size — any three determine the fourth
  - Power curves: visualizing the tradeoff
  - Sample size calculation for a t-test from scratch
  - Biological example: how many replicates do I need for RNA-seq?

---

## Part 4 — Probabilistic Methods (NB13–NB15)

- [ ] **NB13** `13_bayesian_statistics_intuition.ipynb`
  - Frequentist vs. Bayesian framing — not a philosophical debate, a practical choice
  - Prior, likelihood, posterior — Bayes' theorem as an update rule
  - Conjugate priors: Beta-Binomial for allele frequencies
  - MCMC intuition (no implementation — pointer to Module 13's autodiff)
  - Biological example: estimating SNP allele frequency from sequencing data

- [ ] **NB14** `14_resampling_bootstrap_permutation.ipynb`
  - Bootstrap: resample with replacement to quantify uncertainty
  - Bootstrapped confidence intervals: percentile and BCa methods
  - Permutation test: reshuffle labels to build a null distribution
  - When to use bootstrap vs. t-test — a decision framework
  - `compbio_utils.stats.bootstrap_ci` audit and extension

- [ ] **NB15** `15_regression_linear_and_logistic.ipynb`
  - Linear regression: OLS derivation, residuals, R²
  - Implementing OLS from scratch (Normal equations: $\hat{\beta} = (X^T X)^{-1} X^T y$)
  - Logistic regression: log-odds, sigmoid, MLE
  - Biological example: predicting gene length from GC content (linear);
    predicting essential vs. non-essential gene from expression (logistic)

---

## Part 5 — Integration and Assessment (NB16–NB18)

- [ ] **NB16** `16_statistics_on_expression_data.ipynb`
  - End-to-end: take a toy expression matrix and apply the full statistical toolkit
  - QC plots, normalization, t-tests, FDR correction, volcano plot
  - "Tell me what's significant and why" — practice running the interview scenario
  - All previous notebook functions composed into a mini pipeline

- [ ] **NB17** `17_mini_project_statistical_report.ipynb`
  - Real GEO dataset (public, fetched by script)
  - Full statistical analysis: normalization → testing → correction → reporting
  - Portfolio figure: volcano plot + QQ-plot saved to `portfolio/`
  - Written narrative: 300-word methods description (practice for Track B writing)

- [ ] **NB18** `18_module_assessment_mock_interview.ipynb`
  - Oral exam self-test: 60 points, ≥ 80% pass gate
  - Mock interview scenario: "walk me through testing whether gene X is differentially expressed"
  - Sections: A (probability), B (hypothesis testing), C (multiple testing), D (Bayesian), E (regression)
  - Readiness scorecard update

---

## Module Completion Checklist

- [ ] All 18 notebooks run top-to-bottom without errors
- [ ] `compbio_utils.stats.bootstrap_ci` reviewed and extended (NB14)
- [ ] BH correction implemented from scratch and validated (NB11)
- [ ] Portfolio figure saved: `portfolio/module03_statistical_analysis_report.png`
- [ ] Oral exam ≥ 80% (NB18)
- [ ] Papers: Benjamini & Hochberg (1995) Pass 2 complete; Ioannidis (2005) Pass 3 complete
- [ ] Progress tracker updated
