# Module 12 — Datasets

## DS01 — Synthetic PPI Network (generated in notebooks)
- **Format:** Edge list (CSV), node attribute table
- **Size:** ~300 nodes, ~800 edges, 4 planted modules
- **Used in:** NB02–NB07, NB12
- **Source:** Generated in Python (Barabási-Albert + planted partition)

## DS02 — Human PPI Subnetwork (STRING, optional real data)
- **Format:** Tab-separated edge list
- **Size:** ~1000 nodes, ~5000 edges (filtered to high-confidence interactions)
- **Used in:** NB07 (optional real-data exercise)
- **Fetch:**
  ```bash
  # Download human STRING network (filtered to score ≥ 700)
  wget https://stringdb-downloads.org/download/protein.links.v12.0/9606.protein.links.v12.0.txt.gz
  ```
- **License:** STRING is free for academic use

## DS03 — Synthetic Gene Expression Data for GRN (generated in notebooks)
- **Format:** Gene × sample matrix (CSV)
- **Size:** 20 genes × 100 conditions
- **Used in:** NB08
- **Source:** Simulated from known Boolean network attractors

## DS04 — Toy Metabolic Model (generated in notebooks)
- **Format:** Stoichiometric matrix + reaction bounds (numpy)
- **Size:** 10 metabolites × 12 reactions
- **Used in:** NB10
- **Source:** Simplified E. coli central carbon metabolism (glycolysis skeleton)

## DS05 — Disease Gene List (generated/referenced in notebooks)
- **Format:** CSV (gene name, disease, source)
- **Used in:** NB11
- **Source:** Simplified subset from DisGeNET public data (or simulated)
