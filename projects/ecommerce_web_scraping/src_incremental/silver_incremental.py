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
from pathlib import Path

from src.cleaning import clean_record

# ⭐ Import utils
from src_incremental.utils import (
    today_str,
    list_files_with_prefix,
    ensure_folder,
    log_info,
    log_warning,
    log_success
)

BRONZE_DIR = "data/bronze"
SILVER_DIR = "data/silver"


def load_bronze_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_silver_file(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    log_success(f"Saved cleaned file → {output_path}")


def run_silver_incremental():
    log_info("=== Running Incremental Silver Pipeline ===")

    # ⭐ Ensure Silver folder exists
    ensure_folder(SILVER_DIR)

    # ⭐ Today's date prefix
    today = today_str()

    # ⭐ Load ONLY today's Bronze files using utils
    bronze_files = list_files_with_prefix(BRONZE_DIR, today)

    if not bronze_files:
        log_warning(f"No Bronze files found for {today}.")
        return

    all_records = []

    # Load today's Bronze files
    for filename in bronze_files:
        input_path = os.path.join(BRONZE_DIR, filename)
        log_info(f"Loading Bronze file: {filename}")
        bronze_data = load_bronze_file(input_path)
        all_records.extend(bronze_data)

    log_info(f"Total raw records from today's Bronze: {len(all_records)}")

    # Clean records
    cleaned = [clean_record(rec) for rec in all_records]

    # Deduplicate within today only
    deduped_by_url = {
        rec["product_page_url"]: rec
        for rec in cleaned
        if rec.get("product_page_url")
    }
    unified_silver = list(deduped_by_url.values())

    log_info(f"Cleaned records after dedupe: {len(unified_silver)}")

    # Save today's Silver file
    output_path = os.path.join(SILVER_DIR, f"{today}_all_books.json")
    save_silver_file(unified_silver, output_path)

    log_success("=== Incremental Silver Pipeline Complete ===")


if __name__ == "__main__":
    run_silver_incremental()
