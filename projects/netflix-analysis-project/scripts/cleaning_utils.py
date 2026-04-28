"""
Utility functions for cleaning the Netflix dataset.

This file contains a few helper functions I use in Notebook 1
to clean text fields, parse dates, extract duration info, and
apply some basic feature engineering.

The goal is to keep the notebook clean and move repeated logic here.
"""

import re
import logging
import pandas as pd

# basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Text cleaning
# ---------------------------------------------------------

def clean_text(value):
    """
    Remove weird unicode characters and trim whitespace.
    Some titles in the dataset contain zero‑width characters,
    so this helps normalize them.
    """
    if not isinstance(value, str):
        return value

    # remove zero‑width unicode characters
    value = re.sub(r"[\u200b-\u200f\u202a-\u202e]", "", value)

    return value.strip()


# ---------------------------------------------------------
# Date parsing
# ---------------------------------------------------------

def parse_date(date_str):
    """
    Convert the 'date_added' column into a proper datetime.
    If parsing fails, return NaT instead of crashing.
    """
    try:
        return pd.to_datetime(date_str, errors="coerce")
    except Exception as e:
        logger.warning(f"Could not parse date: {date_str} ({e})")
        return pd.NaT


# ---------------------------------------------------------
# Duration parsing
# ---------------------------------------------------------

def parse_duration(raw_value):
    """
    Split the duration column into a numeric value and a type.
    Examples:
        '93 min' -> (93, 'min')
        '2 Seasons' -> (2, 'Seasons')
    """
    if not isinstance(raw_value, str):
        return None, None

    num = re.findall(r"\d+", raw_value)
    typ = re.findall(r"[A-Za-z]+", raw_value)

    duration_num = int(num[0]) if num else None
    duration_type = typ[0] if typ else None

    return duration_num, duration_type


# ---------------------------------------------------------
# Main cleaning pipeline
# ---------------------------------------------------------

def clean_dataframe(df):
    """
    Apply the full cleaning pipeline to the Netflix dataset.

    Steps:
    - clean text fields
    - parse dates
    - split duration into numeric + type
    - fill missing values
    - add year_added and decade columns
    """

    logger.info("Starting cleaning process...")

    # clean text columns
    text_columns = ["title", "director", "cast", "country", "description", "genre"]
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].apply(clean_text)

    # parse date_added
    if "date_added" in df.columns:
        df["date_added"] = df["date_added"].apply(parse_date)

    # parse duration
    if "duration" in df.columns:
        parsed = df["duration"].apply(parse_duration)
        df["duration_int"] = parsed.apply(lambda x: x[0])
        df["duration_type"] = parsed.apply(lambda x: x[1])

    # fill missing values
    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")

    # if date is missing, set to a placeholder
    df["date_added"] = df["date_added"].fillna(pd.Timestamp("1900-01-01"))

    # feature engineering
    if "date_added" in df.columns:
        df["year_added"] = df["date_added"].dt.year

    if "release_year" in df.columns:
        df["decade"] = (df["release_year"] // 10) * 10

    logger.info("Cleaning completed.")

    return df
