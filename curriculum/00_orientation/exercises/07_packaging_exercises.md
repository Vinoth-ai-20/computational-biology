# Exercises — Notebook 07: Python Environment and Packaging Basics

---

## Exercise 1 — Uninstall and restore

```bash
pip uninstall seaborn -y
```

Re-run Notebook 07 Cell 6.2. Confirm seaborn is gone.

```bash
pip install seaborn
```

Confirm it returns.

**seaborn version after restore:**

---

## Exercise 2 — Editable install

If not already done:
```bash
pip install -e utilities/compbio_utils
```

In a Python cell, run:
```python
import compbio_utils
print(compbio_utils.__version__)
```

**Version string:**

---

## Exercise 3 — Editable vs regular install

In your own words, what is the difference between:
- `pip install seaborn`
- `pip install -e utilities/compbio_utils`

**Your explanation (2–3 sentences, no jargon):**
