# Module 07 — Assignments

Larger, less-scaffolded work. Attempt after completing all notebooks.

---

## A01 — Enzyme Kinetics Data Analysis

**Prompt:** You are given a CSV file with substrate concentration [S] and reaction
velocity v measurements for an unknown enzyme under three conditions:
no inhibitor, Inhibitor A (suspected competitive), Inhibitor B (suspected
non-competitive). Using `scipy.optimize.curve_fit`, fit the appropriate MM model
to each condition and:
1. Report Km and Vmax for each condition with 95% confidence intervals
2. Produce a Lineweaver-Burk plot for all three conditions on one axes
3. Confirm or refute the inhibition type hypothesis from the data
4. Calculate the Ki for each inhibitor

Data: use the synthetic dataset in `datasets/` or generate your own using the
`michaelis_menten()` and `competitive_inhibition()` functions from NB03.

---

## A02 — Biochemistry Assay Data Types Report

**Prompt:** For each of the following assay types, write a 2-paragraph explanation
(in a Jupyter notebook) of (a) what it measures and (b) what the data shape looks
like and how to interpret it quantitatively:
- Western blot (band intensity vs. protein expression)
- ELISA (absorbance vs. analyte concentration)
- Flow cytometry (forward scatter / side scatter)
- LC-MS/MS (retention time, m/z, intensity)

For the ELISA entry, fit a 4-parameter logistic (4PL) model to simulated data and
extract the EC50. For the LC-MS/MS entry, annotate a simulated spectrum with
5 manually assigned peaks.
