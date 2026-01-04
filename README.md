Health Imaging – Chest X-ray Analysis (NIH Dataset)

This repository contains exploratory analysis and modelling experiments using a subsample of the NIH Chest X-ray dataset. The project is intended as a learning and research exercise, with emphasis on reproducibility, robust data handling, and understanding common pitfalls in medical imaging workflows.

Project structure

The repository is organised as follows:

README.md
Project overview, setup notes, and run instructions.

.gitignore
Excludes raw data and environment artefacts from version control.

notebooks/
Contains exploratory analysis and modelling notebooks.

Health Imaging Main.ipynb – primary working notebook.

src/
Reusable configuration and helper code.

init.py

config.py – centralised project configuration.

data/ (not tracked by git)
Raw dataset files used locally for analysis.

sample/

images/ – chest X-ray image files

sample_labels.csv – image-level metadata and labels

results/
Intended output directory for generated artefacts.

figures/

tables/

Dataset

This project uses a subsample of the NIH Chest X-ray dataset, which contains frontal chest radiographs with pathology labels derived from radiology reports.

Due to size and licensing considerations, the dataset is not included in this repository. Users must obtain the data separately and place it in the expected directory structure.

A sample version of the dataset is available via Kaggle:
https://www.kaggle.com/datasets/nih-chest-xrays/sample/data

Important setup notes & known challenges
1. Nested image folders in downloaded archives

Some distributed versions of the dataset (including subsamples) may contain duplicate nested folders after extraction.

For example, an archive may include:

an outer images/ directory

an additional inner sample/images/ directory

In this project, only one images directory is used. Any duplicated inner folders should be removed to avoid:

accidental duplication of images

incorrect dataset size estimates

potential data leakage during model training

The expected final location of image files is:

data/sample/images/

2. CSV files appearing in multiple locations

Depending on how the dataset archive is packaged or extracted, sample_labels.csv (or equivalent metadata files) may appear in more than one directory.

Only one authoritative CSV file is used in this project. Its expected location is:

data/sample/sample_labels.csv

All other copies should be ignored or removed to prevent confusion and inconsistency.

3. Data is read-only and excluded from version control

The data/ directory is treated as read-only and is excluded via .gitignore. All preprocessing, augmentation, and dataset splitting are performed dynamically within notebooks or code, rather than modifying raw files on disk.

This approach:

improves reproducibility

prevents accidental corruption of the original dataset

aligns with best practice for data-driven research projects

Configuration

Project-wide settings such as:

dataset paths

random seed

image size

batch size

list of pathology labels

are centralised in:

src/config.py

Notebooks import these values directly to ensure a single source of truth and to minimise duplication across files.

Current status

This project is a work in progress. Initial focus has been on:

robust project setup

data loading and sanity checks

resolving common dataset and environment pitfalls

Further analysis and modelling experiments will be added iteratively.

How to run
1. Clone the repository
git clone https://github.com/Lady-Beerus/health-imaging-classification.git
cd Health\ Imaging

2. Set up the Python environment

This project was developed using Python via Anaconda. Required packages include:

numpy

pandas

matplotlib

scikit-learn

tensorflow / keras

pillow

These can be installed via:

conda install numpy pandas matplotlib scikit-learn pillow
pip install tensorflow


Exact versions are not pinned; minor version warnings may appear but do not affect execution.

3. Obtain the dataset

Download a subsample of the NIH Chest X-ray dataset separately.

After extraction, ensure the data directory contains:

one images/ directory

a single sample_labels.csv file

⚠️ Remove any duplicated nested folders created during extraction.

4. Launch Jupyter Notebook

From the project root:

jupyter notebook


Then open:

notebooks/Health Imaging Main.ipynb

5. Run the notebook

Run the notebook from top to bottom, starting with:

Path bootstrap cell

Config import cell

Imports cell

These setup cells must be executed before any analysis.

6. Modify configuration (optional)

All project-wide settings (paths, image size, batch size, random seed, label list) are defined in:

src/config.py

To change dataset location or experiment parameters, modify this file rather than editing the notebook directly.

Notes on common issues

OneDrive-managed directories may interfere with Git or file access. If issues arise, ensure files are available locally or move the repository outside of OneDrive.

FutureWarnings from NumPy or TensorFlow may appear during import and can be safely ignored.

Notes

This repository prioritises clarity and learning over optimised or production-ready code. Decisions and challenges encountered during setup are documented intentionally, as these issues are common in real-world medical imaging workflows.