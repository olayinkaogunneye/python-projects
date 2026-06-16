import os
import json
from src.cleaning import clean_record


BRONZE_DIR = "data/bronze"
SILVER_DIR = "data/silver"


def ensure_silver_folder():
    """Create silver folder if it doesn't exist."""
    if not os.path.exists(SILVER_DIR):
        os.makedirs(SILVER_DIR)
        print(f"[INFO] Created folder: {SILVER_DIR}")


def load_bronze_file(path):
    """Load a bronze JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_silver_file(data, output_path):
    """Save cleaned silver JSON file."""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[SILVER] Saved cleaned file → {output_path}")


def process_bronze_file(filename):
    """Clean a single bronze file and save to silver."""
    input_path = os.path.join(BRONZE_DIR, filename)
    output_path = os.path.join(SILVER_DIR, filename)

    print(f"[BRONZE] Processing {filename}...")

    bronze_data = load_bronze_file(input_path)
    silver_data = [clean_record(item) for item in bronze_data]

    save_silver_file(silver_data, output_path)


def run_silver_pipeline():
    """Main runner for Bronze → Silver transformation."""
    print("\n=== Running Bronze → Silver Cleaning Pipeline ===\n")

    ensure_silver_folder()

    bronze_files = [
        f for f in os.listdir(BRONZE_DIR)
        if f.endswith(".json")
    ]

    if not bronze_files:
        print("[WARNING] No bronze files found.")
        return

    for filename in bronze_files:
        process_bronze_file(filename)

    print("\n=== Silver Pipeline Complete ===\n")


if __name__ == "__main__":
    run_silver_pipeline()