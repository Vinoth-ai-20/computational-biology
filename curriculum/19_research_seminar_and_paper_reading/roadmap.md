# Module 19 — Roadmap

**Tier:** Ongoing/Cross-cutting
**Total notebooks:** 12
**Sequence:** Work through NB01–NB03 in Weeks 1–2 to establish the practice framework. Then use the remaining notebooks as needed — NB06 before your first journal club, NB07 before writing a review, NB10 before any interview. NB12 is maintained throughout the year.

## Notebook sequence

1. `01_three_pass_method.ipynb` — The Three-Pass Method and paper-notes/ protocol: skim (5–10 min), read (45–90 min), reconstruct (1–2 hrs). Build the PaperLog class. Establish the logging habit from Week 1.

2. `02_reading_methods_critically.ipynb` — What a methods section must contain vs. what it typically contains. The replication gap. Red flags in methods sections. Build a MethodsChecker that flags missing software versions, random seeds, statistical tests, and accession numbers.

3. `03_evaluating_statistical_claims.ipynb` — Common statistical errors in computational biology: NHST misinterpretation, p-value fishing, underpowered studies. Power analysis formula. Cohen's d, odds ratio, relative risk. Simulate p-hacking. Demonstrate FDR vs Bonferroni.

4. `04_reading_benchmarks.ipynb` — What makes a computational biology benchmark valid: held-out data, correct baselines, consistent metrics, multiple datasets. Common flaws. Implement an 8-criteria benchmark scoring rubric. Simulate fair vs biased benchmark.

5. `05_single_cell_transcriptomics_papers.ipynb` — How to read a single-cell RNA-seq paper: filtering thresholds, normalization, dimensionality reduction, clustering, marker genes. Key papers: Seurat, Scanpy, Harmony. Simulate a scRNA-seq analysis pipeline on synthetic data.

6. `06_journal_club_presentation.ipynb` — Journal club structure (15–20 min, 8–12 slides). Slide-by-slide breakdown. Build a PresentationAudit class. Audit a complete slide outline for a synthetic paper.

7. `07_writing_literature_reviews.ipynb` — Narrative vs systematic vs scoping review. Scope definition, search strategy, synthesis. Build a LiteratureMap class tracking papers by (year, topic, method, dataset). Populate with 20 synthetic papers.

8. `08_citation_management.ipynb` — Zotero workflow and BibTeX anatomy. DOI-to-BibTeX simulation. Build a BibTeXManager: parse BibTeX, validate required fields, detect duplicates, format citations in APA and Nature styles.

9. `09_identifying_research_gaps.ipynb` — Gap identification framework: map what exists, find where methods fail, where data is missing, where biological questions are unanswered. Gap radar chart. Build a gap-scoring function ranking open questions by opportunity.

10. `10_cold_paper_explanation.ipynb` — The interview task: "Here's an abstract — 5 minutes, then explain it back to me." Three-step cold explanation. Build a ColdExplanationTimer. Practice on 5 real abstract texts with difficulty ratings. Jargon adjustment for different audiences.

11. `11_building_a_reading_list.ipynb` — Paper tier system (foundational / landmark / survey). Build a ReadingList managing papers across all 20 modules. Priority-sort algorithm: score = Track A relevance × 2 + Track B relevance + pass3_gap_penalty. Reading coverage heatmap.

12. `12_assessment_and_paper_reading_log.ipynb` — Annual reading log (52 weeks × 1 paper). Assessment stubs: pass3_success_rate, gap sentence detector, age distribution, citation formatter, cold explanation scorer. Test harness. Full 52-row tracking table.

## Weekly habit (runs in parallel with all other modules)

| Week | Activity |
|------|----------|
| 1 | Complete NB01, log first paper |
| 2 | Complete NB02–NB03, log second paper |
| 3+ | 1 paper/week: Pass 1 + Pass 2 + Pass 3 attempt + log entry |
| Monthly | Full journal club walkthrough of one paper (NB06) |
| Quarterly | Review Pass-3 success rate trend; adjust reading list priorities |
