import pandas as pd
import pytest
import os

GOLD_DIR = "data/gold"
SILVER_DIR = "data/silver"


# -----------------------------
# Helpers
# -----------------------------
def load_silver():
    records = []
    for file in os.listdir(SILVER_DIR):
        if file.endswith(".json"):
            df = pd.read_json(os.path.join(SILVER_DIR, file))
            records.extend(df.to_dict(orient="records"))
    return pd.DataFrame(records)


def load_gold(name):
    return pd.read_csv(os.path.join(GOLD_DIR, f"{name}.csv"))


# -----------------------------
# 1. Row Count Consistency
# -----------------------------
def test_fact_row_count_matches_silver():
    silver = load_silver()
    fact = load_gold("fact_book_metrics")

    assert len(silver) == len(fact), \
        f"Row mismatch: Silver={len(silver)}, Fact={len(fact)}"


# -----------------------------
# 2. Dimension Uniqueness
# -----------------------------
def test_dim_book_unique_keys():
    dim = load_gold("dim_book")
    assert dim["book_id"].is_unique, "book_id must be unique"
    assert dim[["title", "product_page_url"]].duplicated().sum() == 0, \
        "Duplicate natural keys found in dim_book"


def test_dim_category_unique_keys():
    dim = load_gold("dim_category")
    assert dim["category_id"].is_unique, "category_id must be unique"
    assert dim["category_name"].is_unique, "category_name must be unique"


def test_dim_rating_unique_keys():
    dim = load_gold("dim_rating")
    assert dim["rating_id"].is_unique, "rating_id must be unique"
    assert dim["rating_value"].is_unique, "rating_value must be unique"


def test_dim_date_unique_keys():
    dim = load_gold("dim_date")
    assert dim["date_id"].is_unique, "date_id must be unique"
    assert dim["date"].is_unique, "date must be unique"


# -----------------------------
# 3. Foreign Key Integrity
# -----------------------------
def test_fact_foreign_keys_exist():
    fact = load_gold("fact_book_metrics")

    dim_book = load_gold("dim_book")
    dim_category = load_gold("dim_category")
    dim_rating = load_gold("dim_rating")
    dim_date = load_gold("dim_date")

    assert fact["book_id"].isin(dim_book["book_id"]).all(), "Invalid book_id in fact table"
    assert fact["category_id"].isin(dim_category["category_id"]).all(), "Invalid category_id"
    assert fact["rating_id"].isin(dim_rating["rating_id"]).all(), "Invalid rating_id"
    assert fact["date_id"].isin(dim_date["date_id"]).all(), "Invalid date_id"


# -----------------------------
# 4. Fact Table Grain
# -----------------------------
def test_fact_grain_unique():
    fact = load_gold("fact_book_metrics")
    duplicates = fact.duplicated(subset=["book_id", "date_id"]).sum()
    assert duplicates == 0, f"Fact table grain violated: {duplicates} duplicates found"


# -----------------------------
# 5. Measure Sanity Checks
# -----------------------------
def test_price_and_availability_valid():
    fact = load_gold("fact_book_metrics")

    assert fact["price"].notnull().all(), "Null price found"
    assert (fact["price"] > 0).all(), "Invalid price detected"

    assert fact["availability"].notnull().all(), "Null availability found"
    assert (fact["availability"] >= 0).all(), "Invalid availability detected"