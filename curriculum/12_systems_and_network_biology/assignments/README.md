# Module 12 — Assignments

## A01 — Real PPI Network Analysis

1. Download the human STRING PPI network (score ≥ 700, DS02) or use BioGRID data
2. Extract the largest connected component
3. Compute: degree distribution (log-log plot), clustering coefficient, average path length
4. Identify the top 10 hub proteins by degree; look up their biological function
5. Apply Louvain community detection; how many modules? What biological pathways do they correspond to?
6. Compare your network's properties to an Erdős-Rényi random graph with the same N and E

Submit: notebook + 4 figures + 1-paragraph biological interpretation per analysis.

## A02 — ODE Model: Repressilator

Implement the repressilator (Elowitz & Leibler 2000) from scratch using scipy.

Model: 3 genes (lacI, tetR, cI) mutually repressing each other + their protein products.
$$\dot{m}_i = -m_i + \frac{\alpha}{1 + p_j^n} + \alpha_0$$
$$\dot{p}_i = -\beta(p_i - m_i)$$

1. Implement the ODE system
2. Show that the system oscillates for appropriate parameter values
3. Vary n (Hill coefficient) and show the transition from damped to sustained oscillations
4. Plot the time series and phase portrait

Submit: notebook + oscillation plot + 1-paragraph explanation of why mutual repression leads to oscillation.
