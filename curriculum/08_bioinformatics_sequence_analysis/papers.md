# Module 08 — Papers

Tier 1 module — all five papers below are Pass-2 or Pass-3 targets.
The BLAST paper is the single most important paper to read in this module.

---

| Paper | Type | Why | When | Difficulty | Prereqs | Pass target |
|-------|------|-----|------|-----------|---------|-------------|
| Needleman & Wunsch (1970), *A general method applicable to the search for similarities in the amino acid sequence of two proteins*, J. Mol. Biol. | Foundational | The global alignment algorithm from the source | Week 10–11, with NB04 | Easy–Moderate | None | Pass 3 — derive from memory |
| Smith & Waterman (1981), *Identification of common molecular subsequences*, J. Mol. Biol. | Foundational | The local alignment algorithm, 2 pages only | Week 11, with NB05 | Easy | NW (NB04) | Pass 3 — derive from memory |
| Altschul et al. (1990), *Basic local alignment search tool*, J. Mol. Biol. | Foundational, interview-critical | The BLAST paper — the one paper you must be able to explain cold | Week 12–13, with NB08 | Moderate | SW (NB05), statistics basics | Pass 2 minimum; Pass 3 the k-mer/heuristic section |
| Henikoff & Henikoff (1992), *Amino acid substitution matrices from protein blocks*, PNAS | Classic | How BLOSUM matrices are derived from observed substitutions | Week 11–12, with NB06 | Moderate | None | Pass 2 |
| Saitou & Nei (1987), *The neighbor-joining method: a new method for reconstructing phylogenetic trees*, Mol. Biol. Evol. | Foundational | The NJ paper — connect to NB12 | Week 14–15, with NB12 | Moderate | Distance matrices | Pass 2 |

---

## Pass-3 reconstruction targets

1. **NW algorithm:** given two sequences, set up the DP matrix from scratch with
   gap penalty −2. Fill row by row. Traceback diagonal (match/mismatch), left (gap in
   seq2), or up (gap in seq1). This must be doable from memory before Track A interviews.

2. **SW algorithm:** same as NW but (a) no negative values in the matrix, and (b)
   traceback starts at the maximum cell, not at the bottom-right corner. State the
   difference clearly, then implement.

3. **BLAST k-mer seeding:** given a query sequence of length L and word size W,
   how many k-mers are generated? How is the neighbourhood extended? What is the
   ungapped extension threshold T? Be able to explain this step-by-step without notes.
