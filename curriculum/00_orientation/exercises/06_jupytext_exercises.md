# Exercises — Notebook 06: Jupyter and Jupytext Workflow

---

## Exercise 1 — Pair a new notebook

In JupyterLab, create `curriculum/00_orientation/notebooks/test_pairing.ipynb` with:

- One markdown cell: `## Test Pairing`
- One code cell: `print("jupytext pairing works")`

Run in terminal:

```bash
jupytext --set-formats ipynb,py:percent curriculum/00_orientation/notebooks/test_pairing.ipynb
```

Open `test_pairing.py` in VS Code.

**Does it match the notebook content?** yes / no

Add a new markdown cell to `test_pairing.py`:

```python
# %% [markdown]
# ## New Cell Added in .py File
```

Then run:

```bash
jupytext --sync curriculum/00_orientation/notebooks/test_pairing.ipynb
```

Open `test_pairing.ipynb` in JupyterLab. Does it have the new cell?

**Result:**

---

## Exercise 2 — Verify the pre-commit hook

Add some output to `test_pairing.ipynb` by running the code cell. Then:

```bash
git add curriculum/00_orientation/notebooks/test_pairing.ipynb
git commit -m "test: verify nbstripout hook fires"
```

**What happened during the commit?**

Run `git diff --staged` after the hook fires.

**What does the diff show?**

---

## Exercise 3 — Clean up

```bash
git rm curriculum/00_orientation/notebooks/test_pairing.ipynb
git rm curriculum/00_orientation/notebooks/test_pairing.py
git commit -m "module-00: remove test pairing file"
```

**Confirmed deleted:** yes / no
