import re
import json
from urllib.parse import urljoin
from datetime import datetime


# -----------------------------
# Price Cleaning
# -----------------------------
def clean_price(price):
    """Convert price like '£51.77' or 51.77 into float."""
    if price is None:
        return None
    try:
        return float(str(price).replace("£", "").strip())
    except:
        return None


# -----------------------------
# Availability Cleaning
# -----------------------------
def clean_availability(text):
    """Extract number from 'In stock (11 available)'."""
    if not text:
        return 0
    match = re.search(r"\((\d+)\s+available\)", text)
    return int(match.group(1)) if match else 0


# -----------------------------
# Rating Cleaning
# -----------------------------
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def clean_rating(text):
    """Convert rating word into integer."""
    if not text:
        return None
    return RATING_MAP.get(text.strip(), None)


# -----------------------------
# Image URL Cleaning
# -----------------------------
BASE_URL = "https://books.toscrape.com/"

def clean_image_url(url):
    """Convert relative image URL to absolute."""
    if not url:
        return None
    return urljoin(BASE_URL, url.replace("../", ""))


# -----------------------------
# Description Cleaning
# -----------------------------
def clean_description(text):
    """Remove HTML tags and normalize whitespace."""
    if not text:
        return None
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("\n", " ").strip()
    return text if text else None


# -----------------------------
# Category Cleaning
# -----------------------------
def clean_category(cat):
    """Standardize category casing."""
    if not cat:
        return None
    return cat.strip().title()


# -----------------------------
# Timestamp
# -----------------------------
def add_timestamp():
    """Return UTC timestamp."""
    return datetime.utcnow().isoformat()


# -----------------------------
# Full Record Cleaner
# -----------------------------
def clean_record(record):
    """Apply all cleaning functions to a Bronze record."""
    return {
        "title": record.get("title"),
        "price": clean_price(record.get("price")),
        "availability": clean_availability(record.get("availability")),
        "rating": clean_rating(record.get("rating")),
        "image_url": clean_image_url(record.get("image_url")),
        "category": clean_category(record.get("category")),
        "description": clean_description(record.get("description")),
        "product_page_url": record.get("product_page_url"),
        "scraped_at": add_timestamp()
    }