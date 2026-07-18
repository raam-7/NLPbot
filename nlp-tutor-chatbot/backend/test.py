import pickle
from pathlib import Path

metadata_path = Path("vector-db/practical/metadata.pkl")

with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)

print("Total chunks:", len(metadata))

titles = sorted(set(item["title"] for item in metadata))

print("\nTitles:\n")

for t in titles:
    print("-", t)