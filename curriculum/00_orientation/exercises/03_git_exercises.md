# Exercises — Notebook 03: Git Fundamentals

---

## Exercise 1 — Read the commit graph

Run in terminal:
```bash
git log --oneline --graph --all
```

**What does the output tell you?**

If no commits exist yet: make the first commit (add `README.md` and `ENVIRONMENT.md`). Record the commit hash:

**First commit hash:**
**Commit message used:**

---

## Exercise 2 — Branch practice

Run these commands and record what each one did:

```bash
git checkout -b module-00/orientation
# [make a small edit to any file in curriculum/00_orientation/]
git add curriculum/00_orientation/<filename>
git commit -m "<your message here>"
git push -u origin module-00/orientation
git checkout main
git merge module-00/orientation
```

**Commands run (with output summaries):**

**What did the merge produce in `git log --oneline`?**

---

## Exercise 3 — Commit message practice

Write a commit message for this hypothetical change, without looking at Notebook 03's examples:

> "I added a function called `reverse_complement` to `compbio_utils/sequence.py` and wrote two pytest tests for it."

**Your commit message:**

---

*After writing your message, compare it to the convention in Notebook 03 Cell 6.4. What would you change?*
