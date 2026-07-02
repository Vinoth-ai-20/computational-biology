# Module 15 — Mini Projects

## MP01 — Epidemic model comparison: ODE vs. Network vs. ABM (NB12)

**Context:** The classic SIR ODE assumes perfect homogeneous mixing — every
individual contacts every other with equal probability. Real populations have
heterogeneous contact structures (household, workplace, age-structured networks).
This mini-project compares three levels of model complexity on the same epidemic
scenario, with the same β and γ, and asks: when does the simple ODE
approximation fail?

**Tasks:**
1. Implement three SIR variants:
   - **Deterministic ODE SIR** (scipy.integrate.solve_ivp)
   - **Stochastic network SIR** (agent on Barabási-Albert graph, NetworkX)
   - **Full ABM SIR** (agents with position, local contact radius, spatial spread)
2. Run each model with identical epidemic parameters (β=0.3, γ=0.1, N=500).
3. Compare: epidemic curves (I(t)), final epidemic size, epidemic peak time.
4. Quantify: how much variability does the stochastic model have across 20 runs?
   Plot the ODE solution on top of the stochastic ensemble.
5. Show a scenario where the network structure matters: introduce a "superspreader"
   hub (degree-100 node). How does the epidemic curve change?

**Portfolio value:** This is a directly presentable result — a 3-panel figure
comparing three modelling paradigms is exactly the kind of artefact that appears
in computational biology interview portfolios and Track B applications.

**Deliverable:** `mini_projects/MP01_epidemic_model_comparison.ipynb`
