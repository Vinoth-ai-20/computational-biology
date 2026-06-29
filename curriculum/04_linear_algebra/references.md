# Module 04 — References

## Books

| Title | Authors | Why | Tier relevance |
|-------|---------|-----|----------------|
| *Linear Algebra and Its Applications* (4th ed.) | Gilbert Strang | The standard reference; geometric intuition throughout | Core |
| *Introduction to Linear Algebra* (5th ed.) | Gilbert Strang | More accessible than Applications; great for intuition-building | Core |
| *Mathematics for Machine Learning* | Deisenroth, Faisal, Ong (free PDF) | Chapter 2 (linear algebra) and Chapter 10 (dimensionality reduction) are directly relevant | Supplementary |
| *Pattern Recognition and Machine Learning* | Bishop | Chapter 12: PCA and probabilistic PCA — reference for Module 13 bridge | Advanced reference |

## Video / Interactive Resources

| Resource | Why |
|----------|-----|
| 3Blue1Brown, *Essence of Linear Algebra* (YouTube) | Best available geometric intuition; watch before each notebook in NB01–NB06 |
| MIT 18.06 (Gilbert Strang, OCW) | Full lecture series if any topic needs reinforcement |
| Setosa.io interactive PCA | Excellent for building PCA intuition before NB05 |

## Key Software

| Tool | Role |
|------|------|
| `numpy.linalg` | `eig`, `svd`, `solve`, `lstsq`, `norm` — the core of this module |
| `scipy.linalg` | `qr`, `lu`, `cho_factor` — numerically stable alternatives |
| `sklearn.decomposition.PCA` | Validation target for scratch implementations |
| `networkx` | Graph adjacency and Laplacian matrix construction (NB07) |
| `matplotlib` / `seaborn` | Biplots, scree plots, heatmaps (NB05, NB09) |

## Key Researchers (Linear Algebra applied to Biology)

| Name | Contribution |
|------|-------------|
| Gilbert Strang | Canonical pedagogy; his geometric framing is the one used in this module |
| Matthew Stephens | Probabilistic PCA / FLASH for single-cell genomics |
| Lior Pachter | Algebraic genomics; genomic data structures as matrix problems |
| Aviv Regev | Pioneered PCA and matrix factorization approaches in single-cell biology |
