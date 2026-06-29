# Module 02 — Mathematics for Biology: Roadmap

Track progress by checking boxes as each item is completed. Each notebook must satisfy
the 13-step teaching sequence in [CLAUDE.md](../../CLAUDE.md) §4.1 before being marked done.

**Started:** __________  
**Completed:** __________

---

## Part 1 — Motivation and Calculus Refresher (Weeks 1–2)

### Notebook 01 — Why Mathematics for Biology

`notebooks/01_why_math_for_biology.ipynb`

- [ ] State 5 concrete biological questions that require mathematics to answer
- [ ] Distinguish descriptive from mechanistic models
- [ ] Preview all 12 notebooks: what question does each answer?
- [ ] Set up the recurring biological case studies: bacterial growth, predator-prey, gene expression

### Notebook 02 — Functions, Limits, and Derivatives

`notebooks/02_derivatives_and_limits.ipynb`

- [ ] Explain a derivative as an instantaneous rate of change — no formal limit notation required
- [ ] Compute derivatives of `e^x`, `ln(x)`, `x^n` by hand for small examples
- [ ] Implement numerical differentiation (central difference) in NumPy
- [ ] Apply biological framing: rate of bacterial growth, rate of mRNA production
- [ ] **Exercise:** implement `numerical_derivative(f, x, h)` and verify against `sympy.diff` on 3 functions

### Notebook 03 — Integrals and Area Under a Curve

`notebooks/03_integrals_and_auc.ipynb`

- [ ] Explain an integral as accumulated change / area under a curve
- [ ] Implement Riemann sum integration (left, right, midpoint) in NumPy
- [ ] Use `scipy.integrate.quad` and verify against the Riemann sum
- [ ] Apply biological framing: total drug exposure (AUC in PK), cumulative growth
- [ ] **Exercise:** compute the AUC of a simulated drug concentration curve; compare trapezoid vs. `quad`

---

## Part 2 — Growth Models (Weeks 2–3)

### Notebook 04 — Exponential and Logistic Growth

`notebooks/04_exponential_logistic_growth.ipynb`

- [ ] Derive the exponential growth ODE: `dN/dt = rN` → `N(t) = N₀ e^(rt)`
- [ ] Derive the logistic growth ODE: `dN/dt = rN(1 - N/K)` and explain `K`
- [ ] Fit both models to simulated bacterial growth data using `scipy.optimize.curve_fit`
- [ ] Visualize: data, exponential fit, logistic fit on the same axes
- [ ] Apply biological framing: tumour growth, bacterial culture, epidemic early phase
- [ ] **Exercise:** generate noisy logistic data; fit; report K, r, and 95% CIs; interpret biologically

### Notebook 05 — Difference Equations vs Differential Equations

`notebooks/05_difference_vs_differential_equations.ipynb`

- [ ] Explain the difference: discrete time steps (difference) vs. continuous time (differential)
- [ ] Implement the discrete logistic map: `N_{t+1} = r * N_t * (1 - N_t/K)`
- [ ] Show that the continuous logistic ODE is the limit as step size → 0
- [ ] Demonstrate the discrete logistic map's period-doubling route to chaos
- [ ] Apply biological framing: seasonal reproduction (discrete) vs. continuous reproduction
- [ ] **Exercise:** implement the logistic map, plot N vs. r for r ∈ [2, 4], observe bifurcations

---

## Part 3 — ODEs (Weeks 3–4)

### Notebook 06 — First-Order ODEs: Separable Equations

`notebooks/06_first_order_odes_separable.ipynb`

- [ ] Identify a separable ODE and solve it analytically (by hand for simple cases)
- [ ] Solve `dN/dt = rN` analytically and verify against `solve_ivp`
- [ ] Understand fixed points: where `dN/dt = 0`
- [ ] Understand stability intuitively: is the fixed point attracting or repelling?
- [ ] Apply biological framing: mRNA degradation, radioactive decay, drug clearance
- [ ] **Exercise:** solve 3 separable ODEs analytically; verify each with `solve_ivp`

### Notebook 07 — Numerical ODE Solving: Euler Method

`notebooks/07_euler_method.ipynb`

- [ ] Derive the Euler update rule from the definition of a derivative
- [ ] Implement `euler_solve(f, t_span, y0, h)` from scratch in NumPy
- [ ] Show Euler error vs. step size on logistic growth (plot error as a function of h)
- [ ] Compare to `solve_ivp(method='RK45')` on the same problem
- [ ] **Exercise:** implement Euler for the mRNA ODE; plot the solution and the error vs. `solve_ivp`

### Notebook 08 — Numerical ODE Solving: Runge-Kutta RK4

`notebooks/08_runge_kutta_rk4.ipynb`

- [ ] Derive the RK4 update rule (4 stages: k1, k2, k3, k4)
- [ ] Implement `rk4_solve(f, t_span, y0, h)` from scratch in NumPy
- [ ] Compare Euler, RK4, and `solve_ivp` on logistic growth: accuracy vs. n_steps
- [ ] Explain why RK4 is O(h⁴) accurate while Euler is O(h)
- [ ] **Exercise:** implement RK4; produce a convergence plot (log error vs. log h); confirm the expected slope

---

## Part 4 — Systems of ODEs (Weeks 4–5)

### Notebook 09 — Systems of ODEs: Lotka-Volterra Predator-Prey

`notebooks/09_lotka_volterra.ipynb`

- [ ] Write the Lotka-Volterra equations from biological description (no derivation required)
- [ ] Identify the four fixed points and their biological interpretation
- [ ] Implement and solve using `solve_ivp`
- [ ] Produce a phase portrait (N_prey vs. N_predator)
- [ ] Explore parameter sensitivity: what happens when α, β, γ, δ change?
- [ ] **Exercise (mini-project):** produce the polished Lotka-Volterra phase portrait that becomes the portfolio artifact

---

## Part 5 — Discrete Mathematics (Week 5)

### Notebook 10 — Graphs and Combinatorics for Biology

`notebooks/10_discrete_math_graphs_combinatorics.ipynb`

- [ ] Define a graph (nodes, edges, directed/undirected, weighted)
- [ ] Represent a small protein interaction network as an adjacency matrix and adjacency list
- [ ] Compute degree, shortest path, connected components using `networkx`
- [ ] Explain combinatorics applied to sequence counting: how many k-mers in a genome of length n?
- [ ] Apply: estimate the number of possible 20-amino-acid peptides; compare to known proteome
- [ ] **Exercise:** build a 6-node food-web graph; compute degree distribution; identify the top-degree node

---

## Part 6 — Optimization (Week 6)

### Notebook 11 — Optimization: Gradient Descent

`notebooks/11_optimization_gradient_descent.ipynb`

- [ ] Explain gradient descent geometrically: follow the slope downhill
- [ ] Implement vanilla gradient descent from scratch
- [ ] Visualize the optimization path on a 2D loss surface
- [ ] Show how learning rate affects convergence (too large → diverge; too small → slow)
- [ ] Connect to: `scipy.optimize.minimize`, neural network training
- [ ] **Exercise:** minimize the sum-of-squared-residuals for logistic growth manually with gradient descent; compare to `curve_fit`

---

## Part 7 — Integration and Assessment (Weeks 7–8)

### Notebook 12 — Mini Project and Assessment: Lotka-Volterra Portfolio

`notebooks/12_mini_project_assessment.ipynb`

- [ ] Produce the polished Lotka-Volterra phase portrait (portfolio artifact)
- [ ] Oral-exam style: explain every equation in the Lotka-Volterra system from memory
- [ ] Implement Euler and RK4 solvers from scratch; compare on the L-V system
- [ ] Mock interview: "Describe a biological system you'd model with ODEs and how you'd do it"
- [ ] Self-score the module assessment rubric
- [ ] Update `Learning_Progress.md` and `roadmap.md` checkboxes

---

## Module Completion Checklist

- [ ] All 12 notebooks completed and reflection filled in
- [ ] All exercises solved in `exercises/`
- [ ] Portfolio figure saved: `portfolio/module02_lotka_volterra_phase_portrait.png`
- [ ] Paper reading (Strogatz §1–§3 or equivalent) logged in `paper-notes/`
- [ ] Mock interview self-score ≥ 80%
- [ ] `roadmap.md` checkboxes all ticked

---

*See also: [README.md](README.md) — [references.md](references.md) — [papers.md](papers.md) — [Learning_Progress.md](../../Learning_Progress.md) §4 Module 02*
