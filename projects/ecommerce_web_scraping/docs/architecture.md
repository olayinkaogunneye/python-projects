# Architecture — BooksToScrape Data Engineering Pipeline

This document describes the full architecture of the BooksToScrape data engineering pipeline, built using a modern Medallion Architecture (Bronze → Silver → Gold) and a Kimball‑style dimensional model.

The pipeline is designed to be modular, testable, scalable, and analytics‑ready.

### High‑Level Architecture

```
Category Discovery
        ↓
Crawler (Scraper + Parser)
        ↓
Bronze Layer (Raw Structured JSON)
        ↓
Silver Layer (Cleaned, Unified Dataset)
        ↓
Gold Layer (Fact + Dimensions)
        ↓
EDA + Visuals
Each layer has a clear purpose and responsibility, ensuring clean separation of concerns.

```

### Components Overview

🔍 Category Discovery

File: `src/category_discovery.py`

Purpose:

- Visit homepage

- Extract all category names

- Extract all category URLs

- Return a dictionary of categories

This enables automatic full‑site scraping without hardcoding URLs.

🕷️ Crawler

Files:

`src/scraper.py`

`src/parser.py`

`src/crawler.py`

The crawler orchestrates:

- fetching HTML

- parsing book details

- handling pagination

- collecting all books in each category

Output: Bronze JSON files.

### Bronze Layer

Folder: `data/bronze/ `

Script: `src/main.py`

The Bronze layer stores raw structured JSON extracted from HTML.

Characteristics:

- minimally processed

- one file per category

- preserves original scraped values

- includes timestamps

This layer acts as the source of truth for all downstream transformations.

### Silver Layer

**Folder:** `data/silver/`

**Script:** `src/silver_pipeline.py`

**Cleaning Logic:** `src/cleaning.py`

The Silver layer transforms Bronze into a clean, unified dataset.

- Transformations include:

- price normalization

- availability extraction

- rating mapping

- image URL fixing

- category standardization

- description cleaning

- deduplication

- timestamp normalization

Output:

`data/silver/all_books.json`

This is the analytics‑ready dataset used to build the warehouse.

### Gold Layer — Dimensional Model

**Folder:**  `data/gold/`

**Script:** `src/gold_pipeline.py`

The Gold layer implements a Kimball star schema, enabling scalable analytics and BI reporting.

### Dimension Tables

**dim_book**

Describes each book.

- book_id (surrogate key)

- title

- description

- product_page_url

- image_url

**dim_category**

Describes book categories.

- category_id

- category_name

**dim_rating**

Describes rating levels.

- rating_id

- rating_value (1–5)

rating_label (“One”, “Two”, etc.)

**dim_date**

Describes the scrape date.

- date_id

- date

- year

- month

- day

### Fact Table

**fact_book_metrics**

Stores measurable values for each book.

- book_id (FK)

- category_id (FK)

- rating_id (FK)

- date_id (FK)

- price

- availability

This table is the analytical engine of the warehouse.

### EDA + Visuals

**Notebook:** `notebooks/eda.ipynb`

**Visuals:** `reports/visuals/`

The EDA notebook loads the Gold tables and performs:

- price distribution analysis

- rating distribution

- category‑level insights

- availability patterns

- top expensive books

Visuals are exported for documentation and dashboards.

### Testing Architecture

Folder: tests/

Includes tests for:

- scraper

- parser

- crawler

- category discovery

- Gold validation

This ensures pipeline correctness and stability.

### Folder Structure

```
ecommerce_web_scraping/
│
├── data/
│   ├── raw/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── src/
│   ├── scraper.py
│   ├── parser.py
│   ├── crawler.py
│   ├── category_discovery.py
│   ├── cleaning.py
│   ├── silver_pipeline.py
│   ├── gold_pipeline.py
│   └── main.py
│
├── tests/
│   ├── test_scraper.py
│   ├── test_parser.py
│   ├── test_crawler.py
│   ├── test_category_discovery.py
│   └── test_gold_validation.py
│
├── notebooks/
│   ├── eda.ipynb
│   └── silver_transform.ipynb
│
├── reports/
│   └── visuals/
│
└── docs/
    ├── project_overview.md
    ├── architecture.md
    ├── insights_summary.md
    └── future_work.md

```

### Summary
This architecture demonstrates:

automated scraping

medallion architecture

dimensional modeling

analytics engineering

testing and validation

professional documentation

It is a complete, production‑style data engineering project suitable for your portfolio.

If you want, I can now generate: