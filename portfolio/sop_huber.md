# SOP Draft — EMBL Heidelberg: Wolfgang Huber Lab

**Verified paper referenced (most recent):** Ahlmann-Eltze C, Huber W. "Analysis of
multi-condition single-cell data with latent embedding multivariate regression."
*Nature Genetics* 57, 2025.
DOI: [10.1038/s41588-024-01996-0](https://doi.org/10.1038/s41588-024-01996-0)
(LEMUR — moves beyond discrete cluster-based differential expression toward a
continuous latent-space model that predicts per-cell expression changes as a function
of condition.)

**Also verifiable, still relevant to your Module 09 work:** Love M.I., Huber W.,
Anders S. (2014), "Moderated estimation of fold change and dispersion for RNA-seq data
with DESeq2," *Genome Biology*.
DOI: [10.1186/s13059-014-0550-8](https://doi.org/10.1186/s13059-014-0550-8)

**Rules for filling this in:** every `[bracketed]` item must be something you have
actually built — see the note in `sop_theis.md`. Do not claim a specific GEO
accession or pydeseq2 run unless you have actually done it.

---

I first encountered your group's work not through a paper but through a tool:
[if true — pydeseq2 or DESeq2, and name the actual dataset/notebook you ran it on;
otherwise describe how you actually encountered the DESeq2 model, e.g. through Module
03/09]. Understanding why DESeq2's shrinkage estimator outperforms naive fold-change
ranking required me to work through the negative binomial model, the dispersion
estimation procedure, and the moderated t-statistic derivation — all from your 2014
*Genome Biology* paper. Your group's more recent LEMUR method (2025, *Nature
Genetics*) reframes the same underlying problem — how do you attribute expression
change to condition reliably — for continuous, multi-condition single-cell data
instead of discrete bulk comparisons, which is the direction I find most interesting
to work in next.

My computational background is in [your actual prior engineering background — name it
honestly]. For the past [N] months I have been systematically rebuilding toward
computational genomics: statistics at Tier 1 depth (implemented and tested from
scratch: t-tests, FDR via Benjamini-Hochberg, bootstrap, Bayesian inference — Module
03), [name your actual NGS/DE artifact if one exists], and reproducible scientific
software (Jupytext pairing, nbstripout, pytest, pyproject.toml packaging — all live in
my public repository at [GitHub URL]).

What attracts me specifically to your group is the Bioconductor philosophy: software
infrastructure that makes correct statistical practice easier than incorrect practice.
I want to contribute to that kind of principled tooling, and I want to do it for
Python-native workflows where the infrastructure is less mature than in the R
ecosystem.
