# SOP Draft — IMPRS-ML Munich: Fabian Theis Lab

**Verified paper referenced:** Bahrami M, Richter T, Schmacke NA, Egea Lavandera A,
Theis FJ. "From modality-specific to compositional foundation models for cell
biology." *Cell Systems* 2026 Feb 18;17(2):101534.
DOI: [10.1016/j.cels.2026.101534](https://doi.org/10.1016/j.cels.2026.101534)

This replaces the earlier draft's citation, which had a placeholder DOI
(`10.1016/j.cels.2026.01.XXX`) and should not have been treated as verified.

**Rules for filling this in:** every `[bracketed]` item must be something you have
actually built and can point to in the repo — do not fill in a placeholder with
something aspirational. If a section has no real artifact yet, leave the bracket
rather than inventing content (CLAUDE.md §9.1, §9.6).

---

My route into computational biology is unusual: I am a software engineer with Python
proficiency at the level of building production ML systems — [your actual RAG/LLM/
agentic work — name the systems] — who taught myself the biology in parallel through a
structured 12-month research notebook program. I chose this approach because the
computational bottleneck in single-cell biology is not biology — it is the ability to
build and evaluate large-scale machine learning systems cleanly. Your group's February
2026 *Cell Systems* paper on compositional foundation models for cell biology argues
that modular, composable architectures — rather than monolithic ones — are the right
design for unifying modalities like chromatin accessibility, spatial transcriptomics,
and imaging into a shared representation of cellular behavior. That argument is
exactly the kind of architectural thinking I bring from language-model systems work,
applied to a domain I have spent the past year learning at depth.

My concrete starting point is [name the actual notebook/artifact — e.g. your Module 10
scanpy walkthrough or Module 13 ML-for-biology work — do not reference scGPT/Leiden
comparisons unless you have actually built them]. I have implemented PCA from
eigendecomposition [Module 04], the statistical model underlying differential
expression [Module 03/09], and [name any VAE/foundation-model work you have actually
done] — each from scratch in Python, with tests, before using library
implementations. The purpose was to be able to defend every design choice in exactly
the kind of interview your selection process uses.

What I want to pursue with your group is [name a specific, honest research direction —
do not claim a specific named project like "scooby" unless you have read and can
defend that specific paper]. The IMPRS-ML programme's structure — with lab rotations
before thesis commitment — is the environment where a candidate with strong
computational depth but recent biological breadth will land correctly rather than
accidentally.
