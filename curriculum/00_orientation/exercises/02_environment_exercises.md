# Exercises — Notebook 02: Environment Setup and Verification

---

## Exercise 1 — Deliberate package removal and restoration

Run in terminal:

```bash
pip uninstall seaborn -y
```

Re-run Cell 6.2. Record what you see:

**Output when seaborn is missing:**

Re-install:

```bash
pip install seaborn
```

Re-run Cell 6.2. Confirm seaborn returns. Record the version:

**seaborn version after re-install:**

---

## Exercise 2 — ModuleNotFoundError diagnosis

In a new notebook cell, run:

```python
import compbio_utils_typo
```

**Full error message:**

**Your diagnosis (what caused this error):**

---

## Exercise 3 — Jupytext round-trip

In terminal:

```bash
jupytext --to notebook curriculum/00_orientation/notebooks/01_environment_setup_and_verification.ipynb
```

Confirm the `.ipynb` cells match the source. Then:

```bash
nbstripout curriculum/00_orientation/notebooks/01_environment_setup_and_verification.ipynb
```

**What happened to the outputs after nbstripout ran?**

**What does `git diff` show after nbstripout?**
