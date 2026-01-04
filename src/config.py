from pathlib import Path

# ======================
# Project paths
# ======================

# This file lives in: src/config.py
# parents[1] means "go up two levels" to project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data" / "sample"
IMG_DIR = DATA_DIR / "images"
LABELS_PATH = DATA_DIR / "sample_labels.csv"

# ======================
# Reproducibility
# ======================

RANDOM_SEED = 19

# ======================
# Image settings
# ======================

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

# ======================
# Labels
# ======================

PATHOLOGY_LABELS = [
    "Atelectasis",
    "Cardiomegaly",
    "Effusion",
    "Infiltration",
    "Mass",
    "Nodule",
    "Pneumonia",
    "Pneumothorax",
    "Consolidation",
    "Edema",
    "Emphysema",
    "Fibrosis",
    "Pleural_Thickening",
    "Hernia",
]
