# Project Overview — BooksToScrape Data Engineering Pipeline

This project is an end‑to‑end data engineering pipeline built using the BooksToScrape website — a mock e‑commerce bookstore commonly used for training and testing scraping workflows.
The goal is to demonstrate a complete, production‑style data engineering lifecycle:

- automated category discovery

- scalable web scraping

- structured Bronze ingestion

- cleaned and unified Silver layer

- dimensional Gold warehouse

- analytics and insights

- documentation and testing


This project showcases practical skills in web scraping, ETL, data modeling, analytics engineering, and pipeline design.

### Project Objectives

- Build a fully automated scraper that discovers and extracts all book data

- Implement a Bronze → Silver → Gold medallion architecture

- Clean, normalize, and deduplicate scraped data

- Design a Kimball‑style star schema for analytics

- Generate insights through EDA and visualizations

- Produce professional documentation suitable for a portfolio

### Architecture Summary

The pipeline follows a modern medallion architecture:

```
                ┌──────────────────────────┐
                │   Category Discovery     │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │         Crawler          │
                │  (Scraper + Parser)      │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │        Bronze Layer      │
                │  Raw structured JSON     │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │        Silver Layer      │
                │ Cleaned, unified dataset │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │         Gold Layer       │
                │  Fact + Dimension tables │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │            EDA           │
                │   Visuals + Insights     │
                └──────────────────────────┘

```
## Pipeline Components


### Category Discovery

The pipeline begins by visiting the homepage and extracting:

- category names

- category URLs

- This enables automatic full‑site scraping without hardcoding URLs.

### Crawler

The crawler coordinates:

- fetching HTML

- parsing book details

- iterating through pages

- collecting all books in each category

- It produces Bronze JSON files.

### Bronze → Silver Cleaning

The Silver pipeline:

- cleans prices

- extracts availability

- maps ratings

- fixes image URLs

- normalizes categories

- removes duplicates

unifies all books into one dataset

Output:
`data/silver/all_books.json`

### Gold Layer — Dimensional Model

A proper Kimball star schema:

**Dimensions**

dim_book

dim_category

dim_rating

dim_date

**Fact Table**

fact_book_metrics

book_id

category_id

rating_id

date_id

price

availability

This structure is warehouse‑ready and supports scalable analytics.

### EDA + Visuals

Using the Gold tables, the notebook explores:

- price distribution

- rating distribution

- category patterns

- availability insights

- top expensive books

Visuals are exported to:

`reports/visuals/`


### Key Insights (From EDA)

- Prices are mostly between £20–£60

- Ratings cluster around 3–4 stars

- Some categories have very low stock

- A few categories contain premium books

- Category popularity varies widely

These insights demonstrate the value of the pipeline.

### Project Folder Structure

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
│   └── category_analysis.ipynb
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

### Future Work

- Incremental scraping

- SCD Type 2 for dim_book

- Multi‑site scraping

- Power BI dashboard

- ML model for price prediction

7. Conclusion

This project demonstrates a full, production‑grade data engineering workflow:

- automated scraping

- medallion architecture

- dimensional modeling

- analytics engineering

- testing

- documentation

