"""

Utility functions for cleaning and preparing the Netflix dataset.
These functions are imported and used inside Notebook 1.

The goal is to keep the notebook clean and move repeated logic here.

cleaning_utils.py

"""
import re
import logging
import pandas as pd
import numpy as np

# basic logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def clean_text_column(series):
    """
    Clean a text column by:
    - converting to string
    - trimming whitespace
    - removing zero-width unicode characters
    - converting empty strings to NaN
    """
    logger.info(f"Cleaning text column: {series.name}")

    series = series.astype(str)
    series = series.str.strip()
    series = series.str.replace(r"[\u200b-\u200f\u202a-\u202e]", "", regex=True)
    series = series.replace({"": np.nan, "nan": np.nan})

    return series


def clean_dataframe(df):
    """
    Apply all cleaning steps to the Netflix dataset.
    Returns a cleaned DataFrame.
    """
    logger.info("Starting dataframe cleaning...")
    df = df.copy()

    # Clean text columns
    text_cols = ["title", "director", "cast", "country", "description", "genre"]
    for col in text_cols:
        df[col] = clean_text_column(df[col])

    # Parse date_added
    logger.info("Parsing date_added column")
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year

    # Duration handling (integer column)
    logger.info("Splitting duration into numeric + type")

    # numeric duration
    df["duration_int"] = df["duration"].astype(int)

    # duration type based on show type
    df["duration_type"] = np.where(
        df["type"] == "Movie",
        "min",
        "Seasons"
    )

    # Fill missing values
    logger.info("Filling missing values for director and country")
    df["director"] = df["director"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")

    # Create decade column
    logger.info("Creating decade column")
    df["decade"] = (df["release_year"] // 10) * 10

    logger.info("Dataframe cleaning complete.")
    return df
