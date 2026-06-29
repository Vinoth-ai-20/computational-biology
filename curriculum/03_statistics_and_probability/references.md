# Module 03 References — Statistics and Probability

## Core Textbooks

| Resource | Why this module | Coverage |
|----------|----------------|----------|
| Wasserman, *All of Statistics* (Springer, 2004) | Rigorous but compact — the right depth for this module | Probability, estimation, testing, regression, bootstrap |
| Motulsky, *Intuitive Biostatistics* (Oxford, 4th ed.) | Biology-framed, unusually clear on p-value misuse | Descriptive stats, testing, regression, Bayesian intro |
| Rice, *Mathematical Statistics and Data Analysis* | Reference for theory — open when a derivation needs unpacking | Full probability and statistics |
| Diez, Barr & Çetinkaya-Rundel, *OpenIntro Statistics* (free PDF) | Open access, worked examples | Hypothesis testing, regression, ANOVA |

## Applied Bioinformatics Statistics

| Resource | Why |
|----------|-----|
| Holmes & Huber, *Modern Statistics for Modern Biology* (Cambridge, free online) | Exactly this module's content, in R — convert worked examples to Python |
| Gentleman et al., *Bioinformatics and Computational Biology Solutions Using R and Bioconductor* | Context for how statistics actually appears in genomics pipelines |
| Quackenbush (2002), *Microarray data normalization and transformation*, Nat. Genet. | The normalization-before-testing requirement, explained for gene expression |

## Python Libraries

| Library | Role in this module |
|---------|---------------------|
| `scipy.stats` | t-tests, Mann-Whitney, Pearson/Spearman, distributions — primary tool |
| `statsmodels` | OLS regression, ANOVA, `multipletests` for BH/Bonferroni |
| `numpy.random.default_rng` | Reproducible sampling, bootstrap, permutation tests |
| `pingouin` | Clean, pandas-friendly statistical testing library |
| `seaborn` | Distribution plots, regression plots, QQ-plots |

## Key Researchers

| Researcher | Contribution relevant here |
|-----------|---------------------------|
| Yoav Benjamini | FDR / Benjamini-Hochberg procedure (NB11) |
| Bradley Efron | Bootstrap theory; empirical Bayes in genomics |
| John Ioannidis | Multiple testing, reproducibility crisis (NB10) |
| Terry Speed | Bioinformatics statistics; microarray normalization |
| Wolfgang Huber | Statistical methods in R/Bioconductor; *Modern Statistics for Modern Biology* |

## Key Concepts Indexed to Notebooks

| Concept | Notebook |
|---------|---------|
| Bayes' theorem | NB03 |
| Central Limit Theorem | NB04 |
| t-test (all variants) | NB06 |
| p-value misinterpretations | NB10 |
| Benjamini-Hochberg FDR | NB11 |
| Bootstrap CI | NB14 |
| OLS / logistic regression | NB15 |
