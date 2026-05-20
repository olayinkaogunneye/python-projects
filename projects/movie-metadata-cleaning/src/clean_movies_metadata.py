import pandas as pd
import logging
import re

# ============================================================
# LOGGING SETUP
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================
# 1. FIX DATA TYPES
# ============================================================

def fix_data_types(df):
    """Fix numeric, date, and ID column types."""
    logger.info("Fixing data types...")

    if 'release_date' in df.columns:
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

    numeric_cols = ['budget', 'revenue', 'runtime', 'vote_average',
                    'vote_count', 'popularity']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'id' in df.columns:
        df['id'] = df['id'].astype(str)

    return df


# ============================================================
# 2. NORMALIZE LIST-LIKE COLUMNS
# ============================================================

def clean_list_value(v):
    """Clean a single cell that should contain a list."""
    if isinstance(v, list):
        return [item.strip() for item in v]

    if isinstance(v, str):
        return [item.strip() for item in v.split(',')]

    return []


def normalize_list_column(series):
    """Apply list cleaning to one column."""
    return series.apply(clean_list_value)


def normalize_list_columns(df):
    """Normalize all list-like metadata columns."""
    logger.info("Normalizing list-like columns...")

    list_cols = ['genres', 'cast', 'production_companies', 'production_countries']

    for col in list_cols:
        if col in df.columns:
            df[col] = normalize_list_column(df[col])

    return df


# ============================================================
# 3. CLEAN TEXT COLUMNS
# ============================================================

def clean_text(text):
    """Clean a single text value using regex."""
    if not isinstance(text, str):
        return text

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def clean_text_columns(df):
    """Clean whitespace and formatting in text columns."""
    logger.info("Cleaning text columns...")

    text_cols = ['title', 'overview', 'director', 'original_language']

    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).apply(clean_text)

    # Clean text inside list columns
    list_cols = ['genres', 'cast', 'production_companies', 'production_countries']

    for col in list_cols:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda lst: [clean_text(item) for item in lst] if isinstance(lst, list) else []
            )

    return df


# ============================================================
# 4. REMOVE DUPLICATES INSIDE LISTS
# ============================================================

def remove_list_duplicates(df):
    """Ensure lists contain unique values while preserving order."""
    logger.info("Removing duplicates inside lists...")

    list_cols = ['genres', 'cast', 'production_companies', 'production_countries']

    for col in list_cols:
        if col in df.columns:
            df[col] = df[col].apply(
                lambda x: list(dict.fromkeys(x)) if isinstance(x, list) else []
            )

    return df


# ============================================================
# 5. HANDLE MISSING VALUES
# ============================================================

def handle_missing_values(df):
    """Column-specific missing value strategy."""
    logger.info("Handling missing values...")

    text_cols = ['title', 'overview', 'director', 'original_language']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    list_cols = ['genres', 'cast', 'production_companies', 'production_countries']
    for col in list_cols:
        if col in df.columns:
            df[col] = df[col].apply(clean_list_value)

    if 'runtime' in df.columns:
        df['runtime'] = df['runtime'].fillna(df['runtime'].median())

    numeric_zero_cols = ['budget', 'revenue', 'vote_average', 'vote_count', 'popularity']
    for col in numeric_zero_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    if 'release_date' in df.columns:
        df['release_date'] = df['release_date'].fillna(pd.NaT)

    return df


# ============================================================
# 6. MASTER CLEANING FUNCTION
# ============================================================

def clean_movies_metadata(df):
    """Run the full cleaning pipeline."""
    logger.info("Starting full cleaning pipeline...")

    df = fix_data_types(df)
    df = normalize_list_columns(df)
    df = clean_text_columns(df)
    df = remove_list_duplicates(df)
    df = handle_missing_values(df)

    logger.info("Cleaning pipeline completed.")
    return df
