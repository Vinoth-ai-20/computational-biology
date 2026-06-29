# Module 07 — Mini Projects

---

## MP01 — Michaelis-Menten Kinetics Simulator

**Portfolio artifact:** `portfolio/module07_michaelis_menten_kinetics.png`

**Goal:** A single, self-contained, publication-ready 4-panel figure demonstrating
mastery of enzyme kinetics. Implemented entirely from memory.

**Panel specification:**

| Panel | Content |
|-------|---------|
| A | MM curve: v vs. [S] at different Vmax values; annotate Km and Vmax graphically |
| B | Lineweaver-Burk (double-reciprocal): 1/v vs. 1/[S], with linear fit; annotate intercepts |
| C | Three inhibition models: no inhibitor, competitive (Km↑), non-competitive (Vmax↓); same axes |
| D | Hill equation cooperativity: v vs. [S] for n=0.5, 1, 2, 4; annotate sigmoidal shape |

**Implementation rules:**
- All functions from scratch — no SciPy MM wrappers
- Parameters annotated directly on each panel with `ax.annotate()`
- All panels labelled A–D with bold text at top-left
- Saved at 150 dpi to `portfolio/`
- Written reflection: what would you add if this were for a manuscript?
