"""
Utility functions for the incremental pipeline.
Shared helpers for Bronze, Silver, and Gold layers.
"""

import os
from datetime import datetime, UTC
from pathlib import Path


# -----------------------------
# Date Helpers
# -----------------------------
def today_str() -> str:
    """Return today's date as YYYY-MM-DD."""
    return datetime.now(UTC).date().isoformat()


# -----------------------------
# File Discovery Helpers
# -----------------------------
def list_files_with_prefix(directory: str, prefix: str, extension=".json"):
    """
    Return all files in a directory that start with a given prefix.
    Useful for loading today's Bronze files.
    """
    return [
        f for f in os.listdir(directory)
        if f.startswith(prefix) and f.endswith(extension)
    ]


def list_all_json(directory: str):
    """Return all JSON files in a directory."""
    return [
        f for f in os.listdir(directory)
        if f.endswith(".json")
    ]


# -----------------------------
# Folder Helpers
# -----------------------------
def ensure_folder(path: str):
    """Create folder if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


# -----------------------------
# Logging Helpers
# -----------------------------
def log_info(message: str):
    print(f"[INFO] {message}")


def log_warning(message: str):
    print(f"[WARNING] {message}")


def log_success(message: str):
    print(f"[SUCCESS] {message}")