import os
import logging
import pandas as pd
from datetime import datetime

from src.clean_movies_metadata import clean_movies_metadata


# ============================================================
# LOGGING SETUP
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================
# INGESTION FUNCTION
# ============================================================

def ingest_movies_metadata(
    raw_path="data/raw/movies_metadata.csv",
    cleaned_path="data/cleaned/movies_metadata_clean.parquet"
):
    """
    Load raw movie metadata, clean it, and save cleaned output.
    """

    logger.info("Starting ingestion pipeline...")

    # --------------------------------------------------------
    # 1. CHECK RAW FILE EXISTS
    # --------------------------------------------------------
    if not os.path.exists(raw_path):
        logger.error(f"Raw file not found: {raw_path}")
        raise FileNotFoundError(f"Raw file not found: {raw_path}")

    logger.info(f"Loading raw dataset from: {raw_path}")

    # --------------------------------------------------------
    # 2. LOAD RAW DATA
    # --------------------------------------------------------
    try:
        df_raw = pd.read_csv(raw_path, low_memory=False)
        logger.info(f"Raw dataset loaded successfully. Shape: {df_raw.shape}")
    except Exception as e:
        logger.error(f"Failed to load raw CSV: {e}")
        raise

    # --------------------------------------------------------
    # 3. CLEAN DATA USING YOUR PIPELINE
    # --------------------------------------------------------
    logger.info("Cleaning dataset using cleaning pipeline...")
    df_clean = clean_movies_metadata(df_raw)
    logger.info(f"Cleaning completed. Cleaned shape: {df_clean.shape}")

    # --------------------------------------------------------
    # 4. ENSURE OUTPUT DIRECTORY EXISTS
    # --------------------------------------------------------
    os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)

    # --------------------------------------------------------
    # 5. SAVE CLEANED DATA
    # --------------------------------------------------------
    try:
        df_clean.to_parquet(cleaned_path, index=False)
        logger.info(f"Cleaned dataset saved to: {cleaned_path}")
    except Exception as e:
        logger.error(f"Failed to save cleaned dataset: {e}")
        raise

    logger.info("Ingestion pipeline completed successfully.")
    return df_clean


# ============================================================
# RUN SCRIPT DIRECTLY
# ============================================================

if __name__ == "__main__":
    ingest_movies_metadata()