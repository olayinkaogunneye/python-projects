"""
Incremental Gold Pipeline
-------------------------
This script performs an incremental load into the Gold warehouse.

It:
- Loads existing Gold tables (if present)
- Loads ALL Silver daily snapshots
- Updates dimensions without losing surrogate keys
- Appends new fact rows for each day's snapshot
- Preserves full historical data

Output:
    data/gold/dim_book.csv
    data/gold/dim_category.csv
    data/gold/dim_rating.csv
    data/gold/dim_date.csv
    data/gold/fact_book_metrics.csv
"""

import os
import json
import pandas as pd
from pathlib import Path

SILVER_DIR = "data/silver"
GOLD_DIR = "data/gold"


# -----------------------------
# Helpers
# -----------------------------
def ensure_gold_folder():
    Path(GOLD_DIR).mkdir(parents=True, exist_ok=True)


def load_silver_snapshots():
    """Load ALL Silver daily files into a single DataFrame."""
    records = []
    for filename in os.listdir(SILVER_DIR):
        if filename.endswith(".json"):
            path = os.path.join(SILVER_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                records.extend(data)
            print(f"[SILVER] Loaded {filename} ({len(data)} records)")
    return pd.DataFrame(records)


def load_existing_table(name: str) -> pd.DataFrame:
    """Load existing Gold table if it exists, else return empty DataFrame."""
    path = os.path.join(GOLD_DIR, f"{name}.csv")
    if os.path.exists(path):
        print(f"[GOLD] Loaded existing {name}")
        return pd.read_csv(path)
    print(f"[GOLD] No existing {name}, creating new one")
    return pd.DataFrame()


def save_table(df: pd.DataFrame, name: str):
    path = os.path.join(GOLD_DIR, f"{name}.csv")
    df.to_csv(path, index=False)
    print(f"[GOLD] Saved {name} → {path}")


# -----------------------------
# Dimension Upsert Logic
# -----------------------------
def upsert_dim_book(df_silver, dim_book):
    new_books = df_silver[['product_page_url', 'title', 'description', 'image_url']].drop_duplicates()

    if dim_book.empty:
        new_books = new_books.reset_index(drop=True)
        new_books['book_id'] = new_books.index + 1
        return new_books

    existing_urls = set(dim_book['product_page_url'])
    incoming_new = new_books[~new_books['product_page_url'].isin(existing_urls)]

    if incoming_new.empty:
        return dim_book

    incoming_new = incoming_new.reset_index(drop=True)
    incoming_new['book_id'] = dim_book['book_id'].max() + incoming_new.index + 1

    return pd.concat([dim_book, incoming_new], ignore_index=True)


def upsert_dim_category(df_silver, dim_category):
    new_cats = df_silver[['category']].drop_duplicates().rename(columns={'category': 'category_name'})

    if dim_category.empty:
        new_cats = new_cats.reset_index(drop=True)
        new_cats['category_id'] = new_cats.index + 1
        return new_cats

    existing = set(dim_category['category_name'])
    incoming_new = new_cats[~new_cats['category_name'].isin(existing)]

    if incoming_new.empty:
        return dim_category

    incoming_new = incoming_new.reset_index(drop=True)
    incoming_new['category_id'] = dim_category['category_id'].max() + incoming_new.index + 1

    return pd.concat([dim_category, incoming_new], ignore_index=True)


def upsert_dim_rating(df_silver, dim_rating):
    new_ratings = df_silver[['rating']].drop_duplicates().dropna().rename(columns={'rating': 'rating_value'})
    new_ratings['rating_label'] = new_ratings['rating_value'].map({1:"One",2:"Two",3:"Three",4:"Four",5:"Five"})

    if dim_rating.empty:
        new_ratings = new_ratings.reset_index(drop=True)
        new_ratings['rating_id'] = new_ratings.index + 1
        return new_ratings

    existing = set(dim_rating['rating_value'])
    incoming_new = new_ratings[~new_ratings['rating_value'].isin(existing)]

    if incoming_new.empty:
        return dim_rating

    incoming_new = incoming_new.reset_index(drop=True)
    incoming_new['rating_id'] = dim_rating['rating_id'].max() + incoming_new.index + 1

    return pd.concat([dim_rating, incoming_new], ignore_index=True)


def upsert_dim_date(df_silver, dim_date):
    df_silver = df_silver.copy()
    df_silver['scraped_date'] = pd.to_datetime(df_silver['scraped_at']).dt.date

    new_dates = pd.DataFrame(df_silver['scraped_date'].drop_duplicates())
    new_dates = new_dates.rename(columns={'scraped_date': 'date'})
    new_dates['year'] = pd.to_datetime(new_dates['date']).dt.year
    new_dates['month'] = pd.to_datetime(new_dates['date']).dt.month
    new_dates['day'] = pd.to_datetime(new_dates['date']).dt.day

    if dim_date.empty:
        new_dates = new_dates.reset_index(drop=True)
        new_dates['date_id'] = new_dates.index + 1
        return new_dates

    existing = set(dim_date['date'])
    incoming_new = new_dates[~new_dates['date'].isin(existing)]

    if incoming_new.empty:
        return dim_date

    incoming_new = incoming_new.reset_index(drop=True)
    incoming_new['date_id'] = dim_date['date_id'].max() + incoming_new.index + 1

    return pd.concat([dim_date, incoming_new], ignore_index=True)


# -----------------------------
# Fact Table Incremental Append
# -----------------------------
def build_fact(df_silver, dim_book, dim_category, dim_rating, dim_date):
    df = df_silver.copy()
    df['scraped_date'] = pd.to_datetime(df['scraped_at']).dt.date

    fact = df.merge(dim_book[['book_id', 'product_page_url']], on='product_page_url', how='left')
    fact = fact.merge(dim_category, left_on='category', right_on='category_name', how='left')
    fact = fact.merge(dim_rating, left_on='rating', right_on='rating_value', how='left')
    fact = fact.merge(dim_date, left_on='scraped_date', right_on='date', how='left')

    return fact[['book_id', 'category_id', 'rating_id', 'date_id', 'price', 'availability']]


# -----------------------------
# Main Incremental Pipeline
# -----------------------------
def run_gold_incremental():
    print("\n=== Running Incremental Gold Pipeline ===\n")

    ensure_gold_folder()

    # Load all Silver snapshots
    silver_df = load_silver_snapshots()
    if silver_df.empty:
        print("[ERROR] No Silver data found.")
        return

    # Load existing Gold tables
    dim_book = load_existing_table("dim_book")
    dim_category = load_existing_table("dim_category")
    dim_rating = load_existing_table("dim_rating")
    dim_date = load_existing_table("dim_date")
    fact_book_metrics = load_existing_table("fact_book_metrics")

    # Upsert dimensions
    dim_book = upsert_dim_book(silver_df, dim_book)
    dim_category = upsert_dim_category(silver_df, dim_category)
    dim_rating = upsert_dim_rating(silver_df, dim_rating)
    dim_date = upsert_dim_date(silver_df, dim_date)

    # Build today's fact rows
    new_fact_rows = build_fact(silver_df, dim_book, dim_category, dim_rating, dim_date)

    # Append to existing fact table
    fact_book_metrics = pd.concat([fact_book_metrics, new_fact_rows], ignore_index=True)

    # Save updated Gold tables
    save_table(dim_book, "dim_book")
    save_table(dim_category, "dim_category")
    save_table(dim_rating, "dim_rating")
    save_table(dim_date, "dim_date")
    save_table(fact_book_metrics, "fact_book_metrics")

    print("\n=== Incremental Gold Pipeline Complete ===\n")


if __name__ == "__main__":
    run_gold_incremental()