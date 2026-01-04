This project uses the NIH ChestX-ray14 dataset.



Raw image files are not included in this repository due to size and data-handling considerations.

Please download the dataset separately from Kaggle or the NIH source.
https://www.kaggle.com/datasets/nih-chest-xrays/sample/data?select=sample_labels.csv


# Health Imaging – Chest X-ray Analysis (NIH Dataset)

This repository contains exploratory analysis and modelling experiments
using a subsample of the NIH Chest X-ray dataset. The project is intended
as a learning and research exercise, with emphasis on reproducibility,
robust data handling, and understanding common pitfalls in medical
imaging workflows.

Health Imaging/
├── README.md
├── .gitignore
├── notebooks/
│ └── Health Imaging Main.ipynb
├── src/
│ ├── init.py
│ └── config.py
├── data/ (not tracked by git)
│ └── sample/
│ ├── images/
│ └── sample_labels.csv
└── results/
├── figures/
└── tables/

## Project structure

- `notebooks/` contains exploratory analysis and modelling notebooks  
- `src/` contains reusable configuration and helper code  
- `data/` contains raw dataset files and is excluded from version control  
- `results/` is intended for saved figures and tables  



## Dataset

This project uses a **subsample** of the NIH Chest X-ray dataset, which
contains frontal chest radiographs with pathology labels derived from
radiology reports.

Due to size and licensing considerations, the dataset is **not included**
in this repository. Users must obtain the data separately and place it
in the expected directory structure.



## Important setup notes & known challenges

### 1. Nested image folders in downloaded archives

Some distributed versions of the dataset (including subsamples) may
contain **duplicate nested folders**, for example:
sample/
├── images/
└── sample/
└── images/


In this project, only **one** `images/` directory is used.
Any duplicated inner folders should be removed to avoid accidental
duplication of images or data leakage during model training.

The final expected structure is:

data/sample/images/


containing image files directly.



### 2. CSV files appearing in multiple locations

Depending on how the dataset archive is packaged or extracted,
`sample_labels.csv` (or equivalent metadata files) may appear in more
than one directory.

Only **one authoritative CSV file** is used in this project.
Its expected location is:

data/sample/sample_labels.csv


All other copies should be ignored or removed to avoid confusion.



### 3. Data is read-only and excluded from version control

The `data/` directory is treated as **read-only** and is excluded via
`.gitignore`. All preprocessing, augmentation, and splitting are
performed dynamically within notebooks or code, rather than modifying
the raw files on disk.

This helps ensure reproducibility and prevents accidental corruption
of the original dataset.



## Configuration

Project-wide settings such as:

- dataset paths  
- random seed  
- image size  
- batch size  
- list of pathology labels  

are centralised in:
src/config.py


Notebooks import these values directly to ensure there is a single
source of truth and to reduce duplication.


## Current status

This project is a work in progress. Initial focus has been on:

- robust project setup
- data loading and sanity checks
- resolving common dataset and environment pitfalls

Further analysis and modelling experiments will be added iteratively.


## Notes

This repository prioritises **clarity and learning** over optimised or
production-ready code. Decisions and challenges encountered during
setup are documented intentionally, as these issues are common in
real-world medical imaging workflows.


