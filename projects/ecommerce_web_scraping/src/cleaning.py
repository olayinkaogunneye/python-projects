import re
from urllib.parse import urljoin
from datetime import datetime

BASE_URL = "https://books.toscrape.com/"

# -----------------------------
# Fix UTF-8 mojibake
# -----------------------------
def fix_mojibake(text):
    if not text:
        return text
    try:
        return text.encode("latin1").decode("utf8")
    except:
        return text

# -----------------------------
# Price Cleaning
# -----------------------------
def clean_price(price):
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
    if not text:
        return 0
    match = re.search(r"\((\d+)\s+available\)", text)
    return int(match.group(1)) if match else 0

# -----------------------------
# Rating Cleaning
# -----------------------------
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def clean_rating(text):
    if not text:
        return None
    return RATING_MAP.get(text.strip(), None)

# -----------------------------
# Image URL Cleaning
# -----------------------------
def clean_image_url(url):
    if not url:
        return None
    url = url.replace("../../", "").replace("../", "")
    return urljoin(BASE_URL, url)

# -----------------------------
# Description Cleaning
# -----------------------------
def clean_description(text):
    if not text:
        return None
    text = fix_mojibake(text)
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("\n", " ").strip()
    return text if text else None

# -----------------------------
# Category Cleaning
# -----------------------------
def clean_category(cat):
    if not cat:
        return None
    return cat.strip().title()

# -----------------------------
# Product URL Cleaning
# -----------------------------
def clean_product_url(url):
    if not url or not isinstance(url, str):
        return None
    return url.strip()

# -----------------------------
# Timestamp
# -----------------------------
def add_timestamp():
    return datetime.utcnow().isoformat()

# -----------------------------
# Full Record Cleaner
# -----------------------------
def clean_record(record):
    return {
        "title": record.get("title"),
        "price": clean_price(record.get("price")),
        "availability": clean_availability(record.get("availability")),
        "rating": clean_rating(record.get("rating")),
        "image_url": clean_image_url(record.get("image_url")),
        "category": clean_category(record.get("category")),
        "description": clean_description(record.get("description")),
        "product_page_url": clean_product_url(record.get("product_page_url")),
        "scraped_at": add_timestamp()
    }
