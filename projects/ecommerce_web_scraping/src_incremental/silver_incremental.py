"""
Incremental Silver Pipeline
---------------------------
This script processes ONLY today's Bronze files and produces
a cleaned Silver dataset for today.

Output example:
    data/silver/2026-06-17_all_books.json

This preserves daily snapshots and enables historical Gold fact tables.
"""

import os
import json
from datetime import datetime, UTC
from pathlib import Path

from src.cleaning import clean_record

BRONZE_DIR = "data/bronze"
SILVER_DIR = "data/silver"


def ensure_silver_folder():
    Path(SILVER_DIR).mkdir(parents=True, exist_ok=True)


def load_bronze_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_silver_file(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[SILVER] Saved cleaned file → {output_path}")


def run_silver_incremental():
    print("\n=== Running Incremental Silver Pipeline ===\n")

    ensure_silver_folder()

    # Today's date prefix
    today = datetime.now(UTC).date().isoformat()

    # Load ONLY today's Bronze files
    bronze_files = [
        f for f in os.listdir(BRONZE_DIR)
        if f.startswith(today) and f.endswith(".json")
    ]

    if not bronze_files:
        print(f"[WARNING] No Bronze files found for {today}.")
        return

    all_records = []

    # Load today's Bronze files
    for filename in bronze_files:
        input_path = os.path.join(BRONZE_DIR, filename)
        print(f"[BRONZE] Loading {filename}...")
        bronze_data = load_bronze_file(input_path)
        all_records.extend(bronze_data)

    print(f"[INFO] Total raw records from today's Bronze: {len(all_records)}")

    # Clean records
    cleaned = [clean_record(rec) for rec in all_records]

    # Deduplicate within today only
    deduped_by_url = {
        rec["product_page_url"]: rec
        for rec in cleaned
        if rec.get("product_page_url")
    }
    unified_silver = list(deduped_by_url.values())

    print(f"[INFO] Cleaned records after dedupe: {len(unified_silver)}")

    # Save today's Silver file
    output_path = os.path.join(SILVER_DIR, f"{today}_all_books.json")
    save_silver_file(unified_silver, output_path)

    print("\n=== Incremental Silver Pipeline Complete ===\n")


if __name__ == "__main__":
    run_silver_incremental()