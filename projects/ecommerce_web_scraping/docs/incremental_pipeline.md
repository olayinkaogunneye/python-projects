# 📘 Incremental Pipeline Documentation

Daily Bronze → Silver → Gold Snapshot Architecture
This document explains the incremental data pipeline implemented in the src_incremental/ folder.
It describes how daily scrapes are ingested, cleaned, modeled, and appended into a historical warehouse using the Medallion Architecture.

### 🧱 1. Overview of the Incremental Architecture
The incremental pipeline processes new data only, while preserving all historical data.

```
Daily Scrape
     ↓
Incremental Bronze (raw daily files)
     ↓
Incremental Silver (cleaned daily snapshot)
     ↓
Incremental Gold (historical warehouse)

```
Each layer stores daily snapshots, enabling trend analysis and historical reporting.

### 🥉 2. Incremental Bronze Layer
Purpose

The Bronze layer stores raw, unmodified JSON from the scraper.
Unlike the original pipeline, the incremental version never overwrites previous scrapes.

Behavior
Each scrape produces new Bronze files with a date prefix.

All raw data is preserved for lineage, debugging, and reproducibility.

File Naming Convention

```
data/bronze/YYYY-MM-DD_category.json
data/bronze/YYYY-MM-DD_all_products.json

```
Example:

```
2026-06-17_travel.json
2026-06-17_all_products.json

```
**Key Benefits**

- Full historical raw data

- Perfect for reprocessing

- Supports daily incremental Silver loads

Explore the script:

- bronze_incremental.py

### 🥈 3. Incremental Silver Layer

Purpose

The Silver layer produces a cleaned, deduplicated snapshot for today only.

**Behavior**

- Loads only Bronze files matching today’s date prefix

- Cleans and normalizes fields

- Deduplicates within today only

- Saves a daily Silver snapshot

**File Naming Convention**

```
data/silver/YYYY-MM-DD_all_books.json

```
Example

```
2026-06-17_all_books.json

```
Why Deduplicate Only Within Today?

- Because duplicates across days are not duplicates — they are snapshots.

- Explore the script:

- silver_incremental.py

### 🥇 4. Incremental Gold Layer

Purpose

The Gold layer is a historical data warehouse.

It maintains:

- Slowly growing dimensions

- A snapshot fact table

- One fact row per book per day

Behavior

- Loads existing Gold tables (if present)

- Loads all Silver snapshots

- Upserts dimensions (book, category, rating, date)

- Appends new fact rows

- Preserves full history

**Snapshot Fact Table Grain**

The fact table uses the grain:

(**book_id**, **date_id**)

This means:

Scraping the same book tomorrow is not a duplicate

It is a new historical record

Example:

book_id	date_id	price	availability
101	1	£51.77	22
101	2	£49.99	18


**This enables:**

- price trend analysis

- availability trend analysis

- ating changes

- catalog evolution

- Explore the script:

gold_incremental.py

### 🧩 5. Dimension Upsert Logic

Each dimension table grows only when new values appear.

**dim_book**

Natural key: product_page_url

New books → new book_id

Existing books → keep existing ID

**dim_category**

Natural key: category_name

New categories → new category_id

**dim_rating**

Natural key: rating_value

Rarely changes

**dim_date**

Natural key: date

One row per scrape date

This ensures stable surrogate keys across the warehouse.

### 📊 6. Fact Table Append Logic

The fact table stores one row per book per day.

Fields:

- book_id

- category_id

- rating_id

- date_id

- price

- availability

Rows are never overwritten.

New daily rows are appended.

This is the foundation of a historical analytical warehouse.

### 🗂️ 7. Folder Structure

```
src_incremental/
│
├── bronze_incremental.py
├── silver_incremental.py
├── gold_incremental.py
└── utils.py

```

```
data/
│
├── bronze/
│   ├── 2026-06-16_all_products.json
│   ├── 2026-06-17_all_products.json
│
├── silver/
│   ├── 2026-06-16_all_books.json
│   ├── 2026-06-17_all_books.json
│
└── gold/
    ├── dim_book.csv
    ├── dim_category.csv
    ├── dim_rating.csv
    ├── dim_date.csv
    └── fact_book_metrics.csv

```


### 🚀 8. How to Run the Incremental Pipeline

Step 1 — Run Bronze Incremental

```
python src_incremental/bronze_incremental.py

```
### Step 2 — Run Silver Incremental

```
python src_incremental/silver_incremental.py

```
### Step 3 — Run Gold Incremental

```
python src_incremental/gold_incremental.py

```

### 🧠 9. Why Incremental Pipelines Matter

- Incremental pipelines allow you to:

- Track price changes

- Track availability changes

- Detect new books

- Detect removed books

- Build time‑series analytics

- Scale to daily or hourly scrapes

- Avoid reprocessing entire datasets