# Module 11 — Structural Biology Roadmap

**Tier:** 3 — Survey  
**Total notebooks:** 8  
**Approach:** Implement lightweight versions of key algorithms from scratch to build
genuine understanding; use Biopython for validation and convenience where appropriate.

## Part 1 — Structure Fundamentals (NB01–NB02)

1. `01_protein_structure_hierarchy.ipynb`  
   Primary → secondary → tertiary → quaternary; amino acid chemistry review;
   the backbone dihedral angles (φ, ψ, ω); protein folding problem framing.

2. `02_experimental_structure_determination.ipynb`  
   Survey: X-ray crystallography (diffraction, phase problem, electron density maps);
   cryo-EM (single-particle, resolution revolution); NMR (solution structures);
   comparison table; PDB deposition statistics over time.

## Part 2 — PDB and Structure Analysis (NB03–NB05)

3. `03_pdb_format_parsing.ipynb`  
   PDB file format (ATOM/HETATM records, chain IDs, residue numbers, B-factors);
   mmCIF format; parse PDB from scratch; extract Cα coordinates; visualize
   a protein in 3D (matplotlib); Biopython validation.

4. `04_secondary_structure_and_ramachandran.ipynb`  
   φ/ψ dihedral angle calculation from Cα/N/C/O coordinates; Ramachandran plot
   from scratch; DSSP algorithm concept (hydrogen bond energy criterion); helix,
   sheet, loop regions; secondary structure composition analysis.

5. `05_contact_maps_and_distance_geometry.ipynb`  
   Residue contact map (Cβ distance matrix, threshold 8 Å); contact map from scratch;
   contact conservation and co-evolution (survey); distance geometry and constraints;
   contact-guided structure prediction (pre-AlphaFold context).

## Part 3 — AlphaFold and Applications (NB06–NB07)

6. `06_alphafold2_and_protein_folding.ipynb`  
   Protein folding problem history (Levinthal's paradox, CASP); AlphaFold2 architecture
   survey (Evoformer, structure module, multiple sequence alignments, pLDDT); what
   changed after AlphaFold2; limitations (disordered regions, complexes, dynamics);
   pLDDT score interpretation.

7. `07_structure_comparison_and_drug_design.ipynb`  
   RMSD calculation from scratch; pairwise Cα RMSD alignment; structural databases
   survey (SCOP, CATH, ECOD); structure-based drug design survey (binding sites,
   docking concept, virtual screening); key tools (AutoDock, Glide, AlphaFold-DB).

## Part 4 — Assessment (NB08)

8. `08_module_assessment.ipynb`  
   Conceptual questions (20 pts) + implementation tasks (30 pts):
   PDB parser, φ/ψ dihedral calculation, RMSD, contact map.
