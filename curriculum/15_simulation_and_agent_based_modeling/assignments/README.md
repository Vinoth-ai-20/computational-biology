# Module 15 — Assignments

## A01 — Network epidemic model analysis (Tier 2)

**Objective:** reproduce the core result of Pastor-Satorras & Vespignani (2001):
epidemic spreading behaves fundamentally differently on scale-free networks vs.
homogeneous networks.

**Tasks:**
1. Implement SIR on a Barabási-Albert (scale-free) graph and on an Erdős-Rényi
   (random) graph, both with N=1000 nodes and mean degree k=6.
2. Sweep the transmission rate β from 0.01 to 0.5 (recovery γ=0.1 fixed).
   Plot the final epidemic size (fraction infected) vs. β for both graphs.
3. Estimate the epidemic threshold β_c for each graph type from the simulations.
   Compare to the mean-field prediction β_c = γ/〈k〉 (random) and the
   scale-free prediction β_c → 0 (no threshold).
4. Write a 300-word methods section and a 200-word results section suitable for
   a scientific report.

**Deliverable:** `assignments/A01_network_epidemic.ipynb` + short report section.

---

## A02 — SIR parameter estimation from synthetic outbreak data (Tier 2)

**Objective:** fit SIR parameters to a synthetic incidence time series using
both deterministic least-squares and Bayesian (MCMC) inference.

**Tasks:**
1. Generate synthetic daily incidence data from a stochastic SIR model
   (Gillespie) with known β=0.3, γ=0.1, N=10,000 and add Poisson observation noise.
2. Fit β and γ using `scipy.optimize.minimize` (deterministic, least-squares on
   cumulative incidence).
3. Fit β and γ using Metropolis-Hastings MCMC (from scratch). Report the posterior
   mean, 95% credible interval, and effective sample size.
4. Plot: observed data, best-fit ODE curve, and 50 posterior predictive SIR curves
   (sampled from the MCMC chain).
5. Discuss: when does the deterministic fit fail, and what does the Bayesian
   posterior width tell you about parameter identifiability?

**Deliverable:** `assignments/A02_sir_parameter_estimation.ipynb`.
