"""
Incremental Bronze Pipeline
---------------------------
This script performs a daily incremental Bronze load.

Instead of overwriting bronze files, it saves new files
with a date prefix so that each day's raw scrape is preserved.

Output examples:
    data/bronze/2026-06-17_travel.json
    data/bronze/2026-06-17_mystery.json
    data/bronze/2026-06-17_all_products.json
"""

import json
from pathlib import Path
from datetime import datetime, UTC

from src.category_discovery import CategoryDiscovery
from src.crawler import Crawler
from src.config import BRONZE_DATA_DIR


def save_json(data, filename):
    """Save Python data as JSON inside the Bronze folder."""
    path = Path(BRONZE_DATA_DIR) / filename
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"[BRONZE] Saved: {path}")


def run_bronze_incremental():
    print("\n=== Running Incremental Bronze Pipeline ===\n")

    # Ensure bronze folder exists
    Path(BRONZE_DATA_DIR).mkdir(parents=True, exist_ok=True)

    # Today's date prefix
    today = datetime.now(UTC).date().isoformat()

    # Step 1 — Discover categories
    cd = CategoryDiscovery()
    categories = cd.discover()

    if not categories:
        print("[ERROR] No categories found. Exiting.")
        return

    crawler = Crawler()
    all_products = []

    # Step 2 — Scrape each category
    for name, url in categories.items():
        print(f"\n[SCRAPE] Category: {name}")

        products = crawler.crawl_category(url)

        # Safe filename
        safe_name = name.lower().replace(" ", "_")
        filename = f"{today}_{safe_name}.json"

        # Save category-level Bronze file
        save_json(products, filename)

        all_products.extend(products)

    # Step 3 — Save combined Bronze file
    combined_filename = f"{today}_all_products.json"
    save_json(all_products, combined_filename)

    print("\n=== Incremental Bronze Pipeline Complete ===\n")


if __name__ == "__main__":
    run_bronze_incremental()