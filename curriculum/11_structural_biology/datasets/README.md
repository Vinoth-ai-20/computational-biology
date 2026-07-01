# Module 11 — Datasets

## DS01 — Synthetic PDB-like Structure (generated in notebooks)
- **Format:** PDB ATOM records (plain text)
- **Content:** Simulated helical and sheet peptides with known φ/ψ angles
- **Used in:** NB03–NB05
- **Source:** Generated in Python

## DS02 — Real PDB Structure (fetched on demand)
- **Protein:** Lysozyme (PDB ID: 1HEL) — a classic, small, well-characterized enzyme
- **Format:** PDB file (~100 KB)
- **Used in:** NB03–NB07 (optional real-data exercises)
- **Fetch:**
  ```bash
  wget https://files.rcsb.org/download/1HEL.pdb -O datasets/1HEL.pdb
  ```
  Or in Python:
  ```python
  import urllib.request
  urllib.request.urlretrieve('https://files.rcsb.org/download/1HEL.pdb', '1HEL.pdb')
  ```
- **License:** PDB data is freely available (CC0)

## DS03 — AlphaFold2 pLDDT Data (generated in notebooks)
- **Format:** NumPy array (residue × pLDDT score)
- **Content:** Simulated pLDDT profile with ordered and disordered regions
- **Used in:** NB06
- **Source:** Simulated in Python
