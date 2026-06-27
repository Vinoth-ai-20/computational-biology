# Exercises — Notebook 04: GitHub Workflow

---

## Exercise 1 — Make the repository public

Run:

```bash
gh repo edit --visibility public --yes
```

Visit the URL from Notebook 04 Cell 6.2 in a browser **without being logged in to GitHub**.

**Can you see the repository?** (yes/no)
**URL:**

---

## Exercise 2 — Push CI workflow and check status

After creating the `.github/workflows/ci.yml` in Notebook 04 Cell 6.3:

```bash
git add .github/workflows/ci.yml
git commit -m "module-00: add CI workflow (pytest + ruff)"
git push
```

Wait ~2 minutes. Check:

```bash
gh run list
```

**CI run status (green/red):**
**If red — what failed?**
**If red — what did you do to fix it?**

---

## Exercise 3 — Elevator pitch

Write a one-sentence elevator pitch for this repository in your own words.
Constraint: it must make sense to a PhD supervisor who has never heard of "depth-tiered curriculum."

**Your elevator pitch:**
