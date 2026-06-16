import os
import json
import pandas as pd


SILVER_DIR = "data/silver"
GOLD_DIR = "data/gold"


# -----------------------------
# Helpers
# -----------------------------
def ensure_gold_folder():
    if not os.path.exists(GOLD_DIR):
        os.makedirs(GOLD_DIR)
        print(f"[INFO] Created folder: {GOLD_DIR}")


def load_silver_data():
    """Load and concatenate all Silver JSON files into a single DataFrame."""
    records = []
    for filename in os.listdir(SILVER_DIR):
        if filename.endswith(".json"):
            path = os.path.join(SILVER_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                records.extend(data)
            print(f"[SILVER] Loaded {filename} ({len(data)} records)")
    if not records:
        print("[WARNING] No Silver data found.")
        return pd.DataFrame()
    return pd.DataFrame(records)


# -----------------------------
# Dimension builders
# -----------------------------

def create_dim_book(df: pd.DataFrame) -> pd.DataFrame:
    # Drop rows where product_page_url is missing
    df = df.dropna(subset=['product_page_url'])

    # Deduplicate using the true natural key
    dim_book = df[['product_page_url', 'title', 'description', 'image_url']].drop_duplicates(
        subset=['product_page_url']
    )

    dim_book = dim_book.reset_index(drop=True)
    dim_book['book_id'] = dim_book.index + 1

    return dim_book[['book_id', 'product_page_url', 'title', 'description', 'image_url']]


def create_dim_category(df: pd.DataFrame) -> pd.DataFrame:
    dim_category = df[['category']].drop_duplicates()
    dim_category = dim_category.rename(columns={'category': 'category_name'})
    dim_category = dim_category.reset_index(drop=True)
    dim_category['category_id'] = dim_category.index + 1
    return dim_category[['category_id', 'category_name']]


def create_dim_rating(df: pd.DataFrame) -> pd.DataFrame:
    dim_rating = df[['rating']].drop_duplicates().dropna()
    dim_rating = dim_rating.rename(columns={'rating': 'rating_value'})

    rating_labels = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
    dim_rating['rating_label'] = dim_rating['rating_value'].map(rating_labels)

    dim_rating = dim_rating.reset_index(drop=True)
    dim_rating['rating_id'] = dim_rating.index + 1

    return dim_rating[['rating_id', 'rating_value', 'rating_label']]


def create_dim_date(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['scraped_date'] = pd.to_datetime(df['scraped_at']).dt.date

    dim_date = pd.DataFrame(df['scraped_date'].drop_duplicates())
    dim_date = dim_date.rename(columns={'scraped_date': 'date'})

    dim_date['year'] = pd.to_datetime(dim_date['date']).dt.year
    dim_date['month'] = pd.to_datetime(dim_date['date']).dt.month
    dim_date['day'] = pd.to_datetime(dim_date['date']).dt.day

    dim_date = dim_date.reset_index(drop=True)
    dim_date['date_id'] = dim_date.index + 1

    return dim_date[['date_id', 'date', 'year', 'month', 'day']]


# -----------------------------
# Fact builder
# -----------------------------
    
def create_fact_book_metrics(df, dim_book, dim_category, dim_rating, dim_date):
    df = df.copy()
    df['scraped_date'] = pd.to_datetime(df['scraped_at']).dt.date

    # Join to dim_book using ONLY the natural key
    fact = df.merge(
        dim_book[['book_id', 'product_page_url']],
        on='product_page_url',
        how='left'
    )

    # Join to dim_category
    fact = fact.merge(
        dim_category,
        left_on='category',
        right_on='category_name',
        how='left'
    )

    # Join to dim_rating
    fact = fact.merge(
        dim_rating,
        left_on='rating',
        right_on='rating_value',
        how='left'
    )

    # Join to dim_date
    fact = fact.merge(
        dim_date,
        left_on='scraped_date',
        right_on='date',
        how='left'
    )

    fact_book_metrics = fact[[
        'book_id',
        'category_id',
        'rating_id',
        'date_id',
        'price',
        'availability'
    ]]

    return fact_book_metrics

# -----------------------------
# Save helpers
# -----------------------------
def save_table(df: pd.DataFrame, name: str):
    path = os.path.join(GOLD_DIR, f"{name}.csv")
    df.to_csv(path, index=False)
    print(f"[GOLD] Saved {name} → {path}")


# -----------------------------
# Main pipeline
# -----------------------------
def run_gold_pipeline():
    print("\n=== Running Silver → Gold Warehouse Pipeline ===\n")

    ensure_gold_folder()

    silver_df = load_silver_data()
    if silver_df.empty:
        print("[ERROR] No Silver data to process.")
        return

    # Build dimensions
    dim_book = create_dim_book(silver_df)
    dim_category = create_dim_category(silver_df)
    dim_rating = create_dim_rating(silver_df)
    dim_date = create_dim_date(silver_df)

    # Build fact
    fact_book_metrics = create_fact_book_metrics(
        silver_df, dim_book, dim_category, dim_rating, dim_date
    )

    # Save all
    save_table(dim_book, "dim_book")
    save_table(dim_category, "dim_category")
    save_table(dim_rating, "dim_rating")
    save_table(dim_date, "dim_date")
    save_table(fact_book_metrics, "fact_book_metrics")

    print("\n=== Gold Warehouse Build Complete ===\n")


if __name__ == "__main__":
    run_gold_pipeline()