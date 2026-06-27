# Exercises — Notebook 08: Scientific Computing Workflow

---

## Exercise 1 — Wilson et al. audit on existing code

Take any piece of code from a personal project. Paste it below (or summarize it).  
Apply the 10-item audit from Notebook 08 Cell 6.2.

**Code description:**

| Practice | Pass (✓/✗) | Notes |
|----------|-----------|-------|
| Version controlled | | |
| Clear function name | | |
| Docstring | | |
| Type hints | | |
| Magic numbers removed | | |
| Edge case handled | | |
| Tests written | | |
| No global state | | |
| Readable without comments | | |
| Module-level (not notebook-only) | | |

**Score: __ / 10**

**Failures — what specifically needs fixing:**

---

## Exercise 2 — Explain every line

Copy `normalize_counts` from Notebook 08 Cell 6.3 here and write a line-by-line plain English explanation:

```python
def normalize_counts(counts, pseudocount: float = 0.5):
    import math
    total = sum(counts) + pseudocount * len(counts)
    return [math.log2((c + pseudocount) / total * 1e6) for c in counts]
```

**Line-by-line explanation:**

1. `def normalize_counts(counts, pseudocount: float = 0.5):` —
2. `import math` —
3. `total = sum(counts) + pseudocount * len(counts)` —
4. `return [math.log2((c + pseudocount) / total * 1e6) for c in counts]` —

**Answer (before looking it up):**  
Why pseudocount?  
What does 1e6 represent?  
What does log2 do to the scale?

---

## Exercise 3 — Refactor the BAD function

Rewrite this function without looking at Notebook 08 Cell 6.1's GOOD version:

```python
# BAD version
def process(x):
    r = []
    for i in x:
        if i > 0.5:
            r.append(i)
    return sum(r)/len(r)
```

**Your refactored version:**

```python
# Write here
```
