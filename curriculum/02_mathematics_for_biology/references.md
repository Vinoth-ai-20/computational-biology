# References — Module 02: Mathematics for Biology

## Core Books

| Title | Author(s) | Why | When to use |
|-------|-----------|-----|------------|
| *Nonlinear Dynamics and Chaos* | Steven Strogatz (2nd ed.) | The standard reference — readable, biology-grounded, intuition-first | Read §1–§3 during this module; §4–§6 before Module 12 |
| *Mathematical Biology I: An Introduction* | J.D. Murray (3rd ed.) | Comprehensive reference; use selectively (Lotka-Volterra, logistic, epidemic models) | Reference chapters only; not cover-to-cover |
| *Mathematics for the Life Sciences* | Bodine, Lenhart, Gross | Undergraduate-level, directly biology-framed calculus and ODEs | Supplement Strogatz; exercises are good |

## Video Resources

| Resource | Why | URL |
|----------|-----|-----|
| 3Blue1Brown — *Essence of Calculus* (12 videos) | Best intuition-first treatment of derivatives and integrals; watch before reading | youtube.com/3blue1brown |
| 3Blue1Brown — *Differential equations* series | Geometric intuition for ODEs and phase portraits | youtube.com/3blue1brown |
| *Stochastic Processes in Biology* (MIT OpenCourseWare 7.91J) | Context for where this module's deterministic models break down | ocw.mit.edu |

## Key Software

| Library | Purpose | Version |
|---------|---------|---------|
| `scipy.integrate.solve_ivp` | ODE solving — production use | SciPy ≥ 1.12 |
| `scipy.optimize.curve_fit` | Model fitting | SciPy ≥ 1.12 |
| `networkx` | Graph construction and analysis | ≥ 3.0 |
| `sympy` | Symbolic differentiation (for exercise verification) | ≥ 1.12 |

## Key Researchers

| Name | Contribution | Why relevant |
|------|-------------|--------------|
| Steven Strogatz | Nonlinear dynamics, coupled oscillators | His book is the canonical entry point |
| J.D. Murray | Mathematical biology | Murray (2002) is the reference for biological ODEs |
| Alfred Lotka / Vito Volterra | Predator-prey equations | The founding model of mathematical ecology |

## Online Resources

- [NRICH Mathematics — Differential Equations](https://nrich.maths.org) — worked examples
- [PhET Simulations — Predator-Prey](https://phet.colorado.edu) — interactive intuition
- [Khan Academy — Differential Equations](https://khanacademy.org) — calculus refresher
