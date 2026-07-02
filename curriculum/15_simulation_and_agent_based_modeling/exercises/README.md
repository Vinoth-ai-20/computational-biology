# Module 15 — Exercises

One exercise set per notebook. Attempt before reading the next notebook.

| Exercise | Paired notebook | Task |
|----------|----------------|------|
| E01 | NB01 — ODE biological models | Implement the SEIR model (add Exposed compartment to SIR). Derive the basic reproduction number R₀ algebraically. Plot the epidemic curve and show how it changes with different incubation rates. |
| E02 | NB02 — Gillespie SSA | Implement tau-leaping (approximate stochastic simulation) and compare its speed and accuracy against exact Gillespie on the birth-death process. At what tau does accuracy break down? |
| E03 | NB03 — Reaction-diffusion | Change the Gray-Scott feed and kill parameters to move from spot pattern to stripe pattern to worm pattern. Plot the (f, k) phase diagram with approximate boundaries. |
| E04 | NB04 — Cellular automata | Implement Conway's Game of Life and show: (a) a glider, (b) a still life, (c) a blinker. Count the total living cells at each step and show the long-run equilibrium. |
| E05 | NB05 — ABM fundamentals | Add a wealth-accumulation rule to the Schelling model: agents who have been satisfied for more than 10 steps gain 1 unit of "wealth." Show how segregation and wealth distribution co-evolve. |
| E06 | NB06 — Population dynamics | Implement the Moran model (another genetic drift model). Compare the fixation probability and fixation time to the Wright-Fisher model for the same population size N and initial allele frequency p. |
| E07 | NB07 — Network epidemic | Compare SIR epidemic spread on: (a) a random Erdős-Rényi graph, (b) a Barabási-Albert scale-free graph, (c) a grid lattice — all with the same average degree. Plot epidemic curves and final size. |
| E08 | NB08 — Spatial ABM | Implement a 2D random walk with reflecting boundary conditions. Show the mean squared displacement as a function of time and verify it scales linearly (characteristic of Brownian motion). |
| E09 | NB09 — Parameter estimation | Fit the Lotka-Volterra model to synthetic prey-predator time series data with added observation noise. Report the posterior distribution for all four parameters using Metropolis-Hastings MCMC. |
| E10 | NB10 — Bifurcation | Draw the bifurcation diagram for the logistic map x_{n+1} = rx_n(1-x_n) as r goes from 0 to 4. Identify the period-doubling bifurcations and the onset of chaos. |
| E11 | NB11 — Multiscale modeling | Add an apoptosis rule to the tumor growth model: cells with internal energy below a threshold trigger programmed death. Show how this changes the tumor growth curve. |
