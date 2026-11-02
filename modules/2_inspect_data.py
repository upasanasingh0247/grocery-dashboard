
from pathlib import Path

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# These are the folders containing our datasets
DATASET_FOLDERS = [
    PROJECT_DIR / "data" / "raw" / "bigbasket",
    PROJECT_DIR / "data" / "raw" / "dunnhumby",
]

# Inspect each dataset folder
for folder in DATASET_FOLDERS:
    print(f"\nChecking folder: {folder.name}")
    print("-" * 40)

    if not folder.exists():
        print("Folder does not exist!")
        continue

    files = list(folder.rglob("*"))

    if not files:
        print("Folder is empty!")
        continue

    for file in files:
        if file.is_file():
            size_mb = file.stat().st_size / (1024 * 1024)

            print(f"File: {file.name}")
            print(f"Size: {size_mb:.2f} MB")
            print("-" * 20)
