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

from src.category_discovery import CategoryDiscovery
from src.crawler import Crawler
from src.config import BRONZE_DATA_DIR

# ⭐ Import utils
from src_incremental.utils import (
    today_str,
    ensure_folder,
    log_info,
    log_success,
    log_warning
)


def save_json(data, filename):
    """Save Python data as JSON inside the Bronze folder."""
    path = Path(BRONZE_DATA_DIR) / filename
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    log_success(f"Saved: {path}")


def run_bronze_incremental():
    log_info("=== Running Incremental Bronze Pipeline ===")

    # ⭐ Ensure bronze folder exists (using utils)
    ensure_folder(BRONZE_DATA_DIR)

    # ⭐ Today's date prefix (using utils)
    today = today_str()

    # Step 1 — Discover categories
    cd = CategoryDiscovery()
    categories = cd.discover()

    if not categories:
        log_warning("No categories found. Exiting.")
        return

    crawler = Crawler()
    all_products = []

    # Step 2 — Scrape each category
    for name, url in categories.items():
        log_info(f"Scraping category: {name}")

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

    log_success("=== Incremental Bronze Pipeline Complete ===")


if __name__ == "__main__":
    run_bronze_incremental()