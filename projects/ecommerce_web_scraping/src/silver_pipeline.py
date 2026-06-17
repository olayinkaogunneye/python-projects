import os
import json
from src.cleaning import clean_record

BRONZE_DIR = "data/bronze"
SILVER_DIR = "data/silver"
SILVER_FILE = "all_books.json"


def ensure_silver_folder():
    if not os.path.exists(SILVER_DIR):
        os.makedirs(SILVER_DIR)
        print(f"[INFO] Created folder: {SILVER_DIR}")


def load_bronze_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_silver_file(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[SILVER] Saved unified cleaned file → {output_path}")


def run_silver_pipeline():
    """Unify ALL bronze files into ONE cleaned Silver dataset."""
    print("\n=== Running Unified Bronze → Silver Cleaning Pipeline ===\n")

    ensure_silver_folder()

    bronze_files = [
        f for f in os.listdir(BRONZE_DIR)
        if f.endswith(".json")
    ]

    if not bronze_files:
        print("[WARNING] No bronze files found.")
        return

    all_records = []

    # 1) Load all bronze files
    for filename in bronze_files:
        input_path = os.path.join(BRONZE_DIR, filename)
        print(f"[BRONZE] Loading {filename}...")
        bronze_data = load_bronze_file(input_path)
        all_records.extend(bronze_data)

    print(f"[INFO] Total raw records from bronze: {len(all_records)}")

    # 2) Clean all records
    cleaned = [clean_record(rec) for rec in all_records]

    # 3) Deduplicate by product_page_url
    deduped_by_url = {
        rec["product_page_url"]: rec
        for rec in cleaned
        if rec.get("product_page_url")
    }
    unified_silver = list(deduped_by_url.values())

    print(f"[INFO] Unified cleaned records after dedupe: {len(unified_silver)}")

    # 4) Save ONE unified Silver file
    output_path = os.path.join(SILVER_DIR, SILVER_FILE)
    save_silver_file(unified_silver, output_path)

    print("\n=== Unified Silver Pipeline Complete ===\n")


if __name__ == "__main__":
    run_silver_pipeline()