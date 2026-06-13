from pathlib import Path
import json

from src.category_discovery import CategoryDiscovery
from src.crawler import Crawler
from src.config import BRONZE_DATA_DIR


def save_json(data, filename):
    """Save Python data as a JSON file inside bronze/."""
    path = Path(BRONZE_DATA_DIR) / filename
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Saved: {path}")


def main():
    # Step 1 — Discover all categories
    cd = CategoryDiscovery()
    categories = cd.discover()

    if not categories:
        print("No categories found. Exiting.")
        return

    crawler = Crawler()
    all_products = []

    # Step 2 — Loop through each category
    for name, url in categories.items():
        print(f"\nScraping category: {name}")
        products = crawler.crawl_category(url)

        # Save category-level bronze file
        filename = f"{name.lower().replace(' ', '_')}.json"
        save_json(products, filename)

        all_products.extend(products)

    # Step 3 — Save combined bronze dataset
    save_json(all_products, "all_products.json")
    print("\nScraping complete.")


if __name__ == "__main__":
    main()