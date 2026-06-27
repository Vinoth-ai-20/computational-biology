# Exercises — Notebook 13: Reproducible Research Checklist

---

## Exercise 1 — Wilson et al. audit gaps

From Notebook 13 Cell 6.1, list every ✗ item:

| Failed practice | Concrete fix plan | Target date |
|----------------|-------------------|-------------|
| | | |
| | | |

---

## Exercise 2 — Bootstrap test

In a temporary directory, test the one-command bootstrap:

```bash
cd /tmp
git clone https://github.com/Vinoth-ai-20/computational-biology test-clone
cd test-clone
pip install -r requirements.txt
pip install -e utilities/compbio_utils
python scripts/verify_environment.py
```

**Every step that required manual intervention (be specific):**

1.
2.
3.

**Overall result:** works / fails (describe failure)

---

## Exercise 3 — Module 00 sign-off

Check each item in Notebook 13 Cell 6.3 (completion gate) and confirm it is done.

- [ ] `scripts/verify_environment.py` passes all checks
- [ ] First commit pushed to public repository
- [ ] Jupytext pairing confirmed working
- [ ] nbstripout confirmed working
- [ ] Pass-3 of Wilson et al. logged in `paper-notes/`
- [ ] First weekly log written in `progress/`
- [ ] 13-step lesson sequence can be recited unprompted
- [ ] One-command bootstrap tested from scratch

**After all 8 are checked:**
1. Update `roadmap.md` completion checklist
2. Update `Learning_Progress.md` §4 Module 00 status to `✓ Complete`
3. Commit and push

**Date Module 00 completed:**
