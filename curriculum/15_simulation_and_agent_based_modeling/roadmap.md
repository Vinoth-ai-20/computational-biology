# Module 15 — Roadmap

**Tier 2 | 12 notebooks | 5 weeks**

## Part 1 — Deterministic and Stochastic Dynamics (Weeks 1–2)

| # | Notebook | Key concepts |
|---|----------|-------------|
| 01 | `01_ode_biological_models.ipynb` | Euler method, RK4 from scratch; Lotka-Volterra predator-prey; SIR epidemic; phase portraits and nullclines |
| 02 | `02_stochastic_simulation_gillespie.ipynb` | Propensity functions; Gillespie SSA from scratch; tau-leaping; birth-death process; gene expression noise (intrinsic vs. extrinsic) |
| 03 | `03_reaction_diffusion_systems.ipynb` | Discretized PDE (finite differences); Turing pattern formation; Gray-Scott model (spots → stripes → worms); biological examples |
| 04 | `04_cellular_automata.ipynb` | 1D CA and Wolfram rules; Conway's Game of Life from scratch; excitable media (Greenberg-Hastings); forest fire CA |

## Part 2 — Agent-Based Modeling (Weeks 3–4)

| # | Notebook | Key concepts |
|---|----------|-------------|
| 05 | `05_abm_fundamentals.ipynb` | Agent/Model architecture; schedulers (random, simultaneous); Schelling segregation; Mesa or from-scratch implementation; emergent vs. designed behaviour |
| 06 | `06_population_dynamics_and_evolution.ipynb` | Hardy-Weinberg equilibrium; Wright-Fisher genetic drift from scratch; selection coefficients; fitness landscapes; mutation-selection balance |
| 07 | `07_network_epidemic_dynamics.ipynb` | SIR on Erdős-Rényi and scale-free networks (NetworkX); basic reproduction number R₀; herd immunity threshold; intervention strategies |
| 08 | `08_spatial_abm_movement.ipynb` | Random walk; biased walk (chemotaxis); Lévy flight; slime mold aggregation (Physarum); tissue-level emergent structure |

## Part 3 — Analysis and Multi-scale Modeling (Week 5)

| # | Notebook | Key concepts |
|---|----------|-------------|
| 09 | `09_parameter_estimation.ipynb` | Least-squares ODE fitting; Metropolis-Hastings MCMC from scratch; profile likelihood; practical: fit SIR parameters to synthetic incidence data |
| 10 | `10_sensitivity_analysis_bifurcation.ipynb` | Parameter sweep; bifurcation diagrams; fixed-point analysis; bistability in gene regulatory network; Morris elementary effects |
| 11 | `11_multiscale_modeling.ipynb` | Hybrid ODE + ABM; agents with internal ODE state; tumor growth model (cells with internal metabolism); coupling micro and macro scales |
| 12 | `12_mini_project_and_assessment.ipynb` | MP01: epidemic model comparison (ODE SIR vs. network SIR vs. ABM SIR); 50-point assessment |

## Completion criteria (Tier 2)

- Can implement Gillespie SSA from propensity functions without reference
- Can implement a 2D reaction-diffusion model with finite differences
- Can build a minimal ABM (agents, scheduler, data collector) from scratch
- Can fit ODE parameters to time-series data using MCMC
- Can read and explain a simulation paper (e.g., network epidemic on scale-free graphs) without preparation
- Can explain the difference between stochastic and deterministic regimes
