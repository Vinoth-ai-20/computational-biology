# SOP Draft — EMBL Heidelberg: Oliver Stegle Lab

**Verified paper referenced:** Dimitrov D, Schrod S, Rohbeck M, Stegle O.
"Interpretation, extrapolation and perturbation of single cells." *Nature Reviews
Genetics* 2026. DOI: [10.1038/s41576-025-00920-4](https://doi.org/10.1038/s41576-025-00920-4)

Older, also-verifiable foundational reference if useful for context: Argelaguet R.,
Stegle O. et al. (2020), "MOFA+: a statistical framework for comprehensive integration
of multi-modal single-cell data," *Genome Biology*.
DOI: [10.1186/s13059-020-02015-1](https://doi.org/10.1186/s13059-020-02015-1)

**Rules for filling this in:** every `[bracketed]` item must be something you have
actually built — see the note in `sop_theis.md`.

---

My application to EMBL's International PhD Programme stems from a specific technical
gap I want to close: I can implement the mathematics of latent variable models
[name what you've actually built — e.g. PCA from eigendecomposition, Module 04], but I
want to work at the scale and with the statistical rigor required to make those models
trustworthy for population-level genomic inference. Your group's 2026 *Nature Reviews
Genetics* piece on interpreting, extrapolating, and perturbing single cells frames
exactly the kind of principled, model-based approach my statistical training points
toward — moving from descriptive single-cell analysis toward models that can predict
the effect of interventions, not just characterize existing states.

My computational background before this year was in [your actual prior work — name it
honestly]. I have spent the past [N] months rebuilding my foundations specifically for
biological data: statistics at Tier 1 depth (multiple-testing correction through
Benjamini-Hochberg, bootstrap resampling, Bayesian inference — all implemented and
tested in Module 03), [name your actual RNA-seq/DE artifact if one exists — do not
claim pydeseq2 or a specific GEO accession unless you have actually run it], and
principal component analysis from the linear algebra up [Module 04]. Every notebook in
my repository follows a reproducible workflow: Jupytext-paired, nbstripout-committed,
papermill-compatible.

The EMBL programme specifically — not a national programme — matters because the
five-site rotation structure exists precisely for candidates like me: someone who can
contribute computationally from day one but whose biological intuition is still
developing. I want to land in the right project, not commit early to the wrong one.
