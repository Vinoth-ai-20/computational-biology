# Module 19 — Datasets

This module does not use biological datasets directly. The "data" of this module is the literature itself.

## What goes here

If you download any supplementary data from a paper you are reading (e.g., a paper that releases a benchmark dataset alongside its results), store it here with a corresponding README.

## Convention

```
datasets/
└── raw/
    └── [paper_shortname]_[year]/
        ├── README.md   ← source paper, DOI, download date, license
        └── data/       ← actual downloaded files (check .gitignore — large files go here)
```

## .gitignore note

Large files (> 50 MB) must not be committed to the repository. Use Git LFS or a download script (`scripts/fetch_[dataset].sh`) and document the fetch procedure in the dataset's README.

## Current datasets

None — populated as papers are read and their supplementary data is used.
