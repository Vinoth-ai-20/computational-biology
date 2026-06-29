# Module 05 — Biology Fundamentals: Roadmap

**Tier 1 — Master | 18 notebooks**

## Part 1 — The Cell (NB01–NB04)

- [ ] **NB01** `01_why_this_module_is_not_optional.ipynb`
  Honest framing of starting from zero. The biology vocabulary gap. What "literate"
  means for a computational biologist vs. a bench scientist. The 12-month learning contract.

- [ ] **NB02** `02_cell_structure_and_function.ipynb`
  Prokaryote vs. eukaryote. Organelles and their functions. The plasma membrane.
  Cell cycle overview. Why cell biology is the foundation of everything downstream.
  Visualize a simplified cell diagram in Matplotlib.

- [ ] **NB03** `03_central_dogma_dna_rna_protein.ipynb`
  DNA structure: double helix, base pairing (A-T, G-C). Transcription: DNA → mRNA.
  Translation: mRNA → protein (genetic code table). Why RNA-seq measures transcription.
  Implement the genetic code lookup table. Translate a synthetic mRNA sequence.

- [ ] **NB04** `04_chromosomes_genes_genome_scale.ipynb`
  Chromosomes, ploidy, loci, alleles. Genome size and gene count across organisms.
  Coding vs. non-coding DNA. Gene structure: exons, introns, promoters, UTRs.
  Compute nucleotide composition and GC content. Visualize genome scale.

## Part 2 — Genetics (NB05–NB08)

- [ ] **NB05** `05_mendelian_genetics_punnett_squares.ipynb`
  Dominant/recessive. Homozygous/heterozygous. Punnett square from scratch.
  Monohybrid and dihybrid crosses. Probability of genotypes. Cystic fibrosis example.
  Implement `punnett_square(parent1, parent2)` as a Python function.

- [ ] **NB06** `06_population_genetics_hardy_weinberg.ipynb`
  Population vs. individual thinking. Allele frequencies p and q. The five HWE
  assumptions. Hardy-Weinberg principle: p² + 2pq + q² = 1. Chi-square test for
  HWE deviation. Compute HWE expectations and test real population data.

- [ ] **NB07** `07_genetic_drift_mutation_migration.ipynb`
  Genetic drift: random sampling in finite populations. Wright-Fisher model simulation.
  Effect of population size on drift. Mutation: adding rare alleles. Migration: gene flow.
  Implement `wright_fisher_simulation(N, p0, n_gen, n_trials)` from scratch.

- [ ] **NB08** `08_natural_selection_fitness_models.ipynb`
  Fitness, selection coefficient s, relative fitness w. Selection on allele frequency:
  Δp per generation formula. Directional, stabilizing, disruptive selection.
  Simulate allele frequency trajectories under selection + drift. Antibiotic resistance model.

## Part 3 — Evolutionary and Ecological Thinking (NB09–NB11)

- [ ] **NB09** `09_speciation_and_phylogenetics.ipynb`
  Species concept. Allopatric vs. sympatric speciation. Phylogenetic trees: nodes,
  branches, clades, outgroup. Reading Newick format. Distance-based tree (UPGMA) from scratch.
  Interpret a real phylogenetic figure from a paper.

- [ ] **NB10** `10_cell_signaling_and_gene_regulation.ipynb`
  Signal transduction: receptor → second messenger → transcription factor → gene.
  MAPK cascade (Ras → Raf → MEK → ERK). Wnt pathway overview. Gene regulatory networks:
  activators and repressors. Implement a simple Boolean gene regulation model.

- [ ] **NB11** `11_ecology_population_biology.ipynb`
  Populations, communities, ecosystems. Exponential and logistic growth (connects to Module 02).
  Carrying capacity K. Trophic levels and food webs as graphs. Species interactions:
  competition, predation, mutualism. Implement a simple food web adjacency matrix.

## Part 4 — Applied Biology and Literacy (NB12–NB16)

- [ ] **NB12** `12_human_genetics_and_disease.ipynb`
  Mendelian disease (autosomal dominant/recessive, X-linked). Complex disease: GWAS concept.
  Carrier frequency calculations. Cancer as somatic mutation accumulation.
  Oncogenes vs. tumor suppressors. Implement carrier risk calculator.

- [ ] **NB13** `13_reading_biology_figures.ipynb`
  How to read a western blot, gel image, flow cytometry plot, expression heatmap,
  phylogenetic tree, and GWAS Manhattan plot. What to look for. Common visualisation
  conventions and how to replicate them in Matplotlib.

- [ ] **NB14** `14_biology_vocabulary_50_terms.ipynb`
  The 50 terms that appear in nearly every computational biology paper you will read
  this year. Grouped by domain. Active recall flashcard format. Test yourself.
  Reference to use when encountering an unknown term in downstream modules.

- [ ] **NB15** `15_mini_project_hw_drift_simulator.ipynb`
  **Portfolio artifact 1.** Hardy-Weinberg + genetic drift simulator from scratch.
  Full pipeline: set p₀, N, s → simulate n_gen generations → plot allele frequency
  trajectories. Compare drift alone vs. drift + selection. Saved to `portfolio/`.

- [ ] **NB16** `16_mini_project_biology_for_cs.ipynb`
  **Portfolio artifact 2.** A polished explainer notebook titled "Biology for Computer
  Scientists." Audience: someone with strong CS but zero biology. Covers central dogma,
  genome organization, and why sequence data looks like it does. Teaching-ability artifact.

## Part 5 — Integration (NB17–NB18)

- [ ] **NB17** `17_paper_reading_session.ipynb`
  Three-Pass reading of one foundational paper (see `papers.md`). Structured template:
  Pass 1 notes, Pass 2 notes, Pass 3 reconstruction attempt, vocabulary log.

- [ ] **NB18** `18_module_assessment_mock_interview.ipynb`
  **Pass gate: ≥48/60 (80%).**
  Section A: vocabulary (12 pts). Section B: genetics calculations (20 pts).
  Section C: implementation (20 pts) — HW simulator, Punnett square.
  Section D: mock interview (8 pts) — explain central dogma + HWE without notes.
