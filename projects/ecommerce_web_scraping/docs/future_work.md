# 🚀 Future Work — BooksToScrape Data Engineering Pipeline

This document outlines potential enhancements that can evolve the BooksToScrape pipeline into a more scalable, production‑grade data engineering system. These improvements reflect real‑world patterns used in enterprise data platforms.

## ⭐ 1. Incremental Scraping & Historical Tracking
The current pipeline performs a full scrape of all books. A natural next step is to support daily incremental scraping.

**Why Incremental Scraping Matters**

Websites change over time:

- prices fluctuate

- availability changes

- ratings update

- new books appear

- old books disappear

Capturing these changes requires daily snapshots, not deduplication across days.

**Snapshot Fact Table Grain**

The fact table should use the grain:

(product_page_url, scraped_date)

This ensures:

- Scraping the same book tomorrow is not a duplicate

- It is a new historical record

- You can track changes over time

Example:

book_id	date_id	price	availability
1	2026‑06‑16	£51.77	22
1	2026‑06‑17	£51.77	22


These are not duplicates — they are daily snapshots.

**How It Works**

Each day produces a new Silver file:
```
silver/all_books_2026-06-16.json
silver/all_books_2026-06-17.json

```

The Gold pipeline appends them into the fact table.

This enables:

- price trend analysis

- availability trend analysis

- category evolution

- rating changes

- catalog growth tracking

### ⭐ 2. SCD Type 2 for dim_book

Books may change over time:

- title corrections

- category reassignments

- updated descriptions

- new cover images

Implementing Slowly Changing Dimension Type 2 allows you to track these changes historically.

What SCD2 Would Add

- valid_from

- valid_to

- is_current

This is a strong demonstration of warehouse modeling expertise.

### ⭐ 3. Multi‑Site Scraping

Extend the pipeline to scrape multiple e‑commerce book sites:

- BooksToScrape

- OpenLibrary

- Gutenberg

- Other mock e‑commerce sites

- This requires:

- multi‑site category discovery

- unified Bronze schema

- cross‑site Silver normalization

- multi‑source Gold modeling

This turns the project into a real‑world data integration pipeline.

### ⭐ 4. Power BI / Tableau Dashboard

Build a dashboard using the Gold tables:

- category insights

- price distribution

- rating distribution

- availability trends

- top expensive books

- historical price changes

This adds a polished analytics layer to your portfolio.

### ⭐ 5. Airflow / Prefect Orchestration

Move from manual execution to orchestration:

- schedule daily scrapes

- run Silver and Gold pipelines automatically

- add monitoring and alerting

- track pipeline runs

- This transforms the project into a production‑ready data platform.

### ⭐ 6. Cloud Deployment

- Deploy the pipeline to:

- Azure Data Lake

- Azure Functions

- Azure Databricks

- AWS Lambda + S3

- GCP Cloud Run + Cloud Storage

This demonstrates cloud engineering skills.

### ⭐ 7. Machine Learning Extensions

- Use the Gold dataset to build ML models:

- price prediction

- rating prediction

- category classification

- availability forecasting

This adds a data science layer on top of your engineering work.

### ⭐ 8. API Layer for Real‑Time Access

Expose the Gold tables via:

- FastAPI

- Flask

- Azure API Management

This enables:

- real‑time book lookup

- category insights API

- price trend API

### ⭐ Summary

This future work roadmap shows how the project can evolve into:

- a historical data warehouse

- a multi‑site scraping platform

- a cloud‑native data pipeline

- a BI analytics system

- a machine learning dataset

- a real‑time API service

It demonstrates long‑term thinking and real‑world engineering maturity.