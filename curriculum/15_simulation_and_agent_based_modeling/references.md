# Module 15 — References

## Core textbooks

| Title | Authors | Why |
|-------|---------|-----|
| *An Introduction to Systems Biology* (2nd ed.) | Uri Alon | ODE-based biological circuits, bifurcations, bistability — the standard text for systems biology modelling |
| *Modeling Infectious Diseases in Humans and Animals* | Keeling & Rohani | SIR and network epidemic models; parameter estimation; covers stochastic versions |
| *The Art of Agent-Based Modeling* | Wilenski & Rand | Conceptual foundations, NetLogo-based but principles apply; emergent behaviour theory |
| *Stochastic Methods* | Gardiner | Fokker-Planck, Langevin, SSA rigorous derivations — for deeper stochastic theory |
| *Mathematical Biology I & II* | Murray | Phase planes, reaction-diffusion, Turing instability — the canonical reference |

## Key software

| Tool | Role |
|------|------|
| [Mesa](https://mesa.readthedocs.io/) | Python ABM framework — Agent, Model, Scheduler, DataCollector classes |
| [SciPy `integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) | ODE integration (Dormand-Prince RK45, LSODA) |
| [NetworkX](https://networkx.org/) | Graph construction and analysis for network epidemic models |
| [Tellurium](https://tellurium.readthedocs.io/) | SBML-based ODE modelling for systems biology — Antimony model language |
| [GillesPy2](https://gillespy2.readthedocs.io/) | Stochastic simulation (Gillespie, tau-leaping) with SBML support |
| [SALib](https://salib.readthedocs.io/) | Sensitivity analysis: Sobol, Morris, FAST methods |
| [emcee](https://emcee.readthedocs.io/) | Affine-invariant ensemble MCMC for parameter estimation |

## Key researchers and labs

| Person / Lab | Institution | Focus |
|-------------|-------------|-------|
| Uri Alon | Weizmann Institute | Systems biology, network motifs, ODE models |
| Matt Keeling | University of Warwick | Epidemic network models |
| Christophe Dessimoz | University of Lausanne | Comparative genomics; evolutionary simulation |
| Paulien Hogeweg | Utrecht University | Pioneer of ABM in biology (Potts model, development) |
| Santa Fe Institute | — | Complexity science, ABM, adaptive systems |
| BioMASS (Okada lab) | Osaka University | ODE parameter estimation for signalling networks |

## Online resources

- [SHODOR Interactivate](https://www.shodor.org/interactivate/) — visual epidemic and ecology models
- [OpenABM](https://www.openabm.org/) — curated ABM repository
- [EMBL-EBI BioModels Database](https://www.ebi.ac.uk/biomodels/) — curated SBML ODE models for reuse
- Uri Alon's [Systems Biology lectures (YouTube)](https://www.youtube.com/c/UriAlonSystemsBiology) — rigorous, free
