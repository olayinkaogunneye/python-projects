# BooksToScrape — End‑to‑End Data Engineering Pipeline

A complete, production‑style data engineering project built on the BooksToScrape website.

This pipeline demonstrates:

- automated category discovery

- scalable web scraping

- medallion architecture (Bronze → Silver → Gold)

- dimensional modeling (Kimball)

- analytics engineering

- testing

- documentation

- EDA + visuals

It is designed as a portfolio‑ready showcase of modern data engineering skills.

## Project Architecture
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
```

### Features

✔ **Automated Category Discovery**
Extracts all category names and URLs from the homepage.

✔ **Full‑Site Web Scraper**
Scrapes every book across all categories and pages.

✔ **Bronze Layer**
Stores raw structured JSON extracted from HTML.

✔ **Silver Layer**
Cleans and unifies all books into a single analytics‑ready dataset.

✔ **Gold Layer (Dimensional Model)**
Warehouse‑ready star schema:

    **dim_book**

    **dim_category**

    **dim_rating**

    **dim_date**

    **fact_book_metrics**

✔ EDA + Visuals

Explores:

    price distribution

    rating distribution

    category patterns

    availability insights

    top expensive books

### Tech Stack

- Python

- Requests / BeautifulSoup

- Pandas

- PyTest

- Jupyter Notebook

- Matplotlib / Seaborn

- Medallion Architecture

- Dimensional Modeling (Kimball)

### Repository Structure

```
books_pipeline/
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

### How the Pipeline Works

🔍 **Category Discovery**

Automatically extracts all category names and URLs.

🕷️ **Crawler**

Scrapes:

- title

- price

- rating

- availability

- description

- image URL

- product URL

🥉 **Bronze Layer**

Stores raw structured JSON.

🥈 **Silver Layer**

Cleans and unifies all books into:

`data/silver/all_books.json`

🥇 **Gold Layer**

Dimensional model:

- dim_book

- dim_category

- dim_rating

- dim_date

- fact_book_metrics

📊 **EDA**

Visuals include:

- price distribution

- rating distribution

- category counts

- availability patterns

- top expensive books

### Key Insights

- Most books are priced between £20–£60

- Ratings cluster around 3–4 stars

- Some categories have very low availability

- A few categories contain premium books

- Category popularity varies significantly

### How to Run the Pipeline

1. Install dependencies
```
pip install -r requirements.txt

```
2. Run the full scraper

```
python src/main.py

```
3. Run Silver pipeline

```
python src/silver_pipeline.py

```
4. Run Gold pipeline

```
python src/gold_pipeline.py

```
5. Open the EDA notebook

```
notebooks/eda.ipynb

```
### Future Enhancements

Incremental scraping

Historical fact tables

SCD Type 2 for dim_book

Multi‑site scraping

Power BI dashboard

ML model for price prediction


### AI Collaboration Notice
Portions of this project were developed with the assistance of AI tools, specifically for improving documentation quality, refining code structure, and aligning scripts for consistency. All core engineering decisions, data modeling logic, and final code reviews were performed manually.


⭐ Author

Olayinka Ogunneye

Analytics Engineer