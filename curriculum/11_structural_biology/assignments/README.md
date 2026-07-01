# Module 11 — Assignments

## A01 — PDB Analysis Pipeline (real structure)

Download lysozyme (1HEL.pdb) from the RCSB PDB.

1. Parse all ATOM records and extract: chain, residue number, residue name, atom name, (x, y, z)
2. Compute the Cα distance matrix and plot as a contact map (threshold = 8 Å)
3. Compute φ/ψ angles for all residues and produce a Ramachandran plot
4. Identify which residues fall outside the allowed Ramachandran regions
5. Compute the radius of gyration of the protein

Submit: working notebook + Ramachandran plot + contact map + 1-paragraph interpretation.

## A02 — AlphaFold2 Paper Summary

Read Jumper et al. 2021 (AlphaFold2) using the Three-Pass method (see §8 of CLAUDE.md).

Write a `paper-notes/jumper2021_alphafold2.md` entry with:
- Pass 1 summary (5 sentences)
- Pass 2: key architectural components (Evoformer, structure module) described in plain English
- Pass 3: explain from memory — what is pLDDT and how is it used to assess prediction confidence?
- One question the paper leaves open

Submit: paper-notes entry.
