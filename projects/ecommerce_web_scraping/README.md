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
- **incremental data processing (new)**

It is designed as a portfolio‑ready showcase of modern data engineering skills.

---

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

---

## Features

✔ **Automated Category Discovery**  
✔ **Full‑Site Web Scraper**  
✔ **Bronze Layer** — raw structured JSON  
✔ **Silver Layer** — cleaned analytics‑ready dataset  
✔ **Gold Layer** — dimensional warehouse (star schema)  
✔ **EDA + Visuals**  
✔ **Incremental Pipeline (new)**  
Processes daily snapshots without overwriting existing data.

---

## Tech Stack

- Python  
- Requests / BeautifulSoup  
- Pandas  
- PyTest  
- Jupyter Notebook  
- Matplotlib / Seaborn  
- Medallion Architecture  
- Dimensional Modeling (Kimball)

---

## Repository Structure

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
├── src_incremental/          ← NEW
│   ├── bronze_incremental.py
│   ├── silver_incremental.py
│   ├── gold_incremental.py
│   ├── utils.py
│   └── __init__.py
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

---

# 🆕 **Incremental Pipeline (New Addition)**

The project now includes a **fully incremental Bronze → Silver → Gold pipeline** that processes **daily snapshots** without overwriting existing data.

### 🥉 Incremental Bronze  
- Saves raw JSON files with a date prefix  
- Preserves historical raw scrapes  
- Example: `2026-06-18_all_products.json`

### 🥈 Incremental Silver  
- Processes **only today's Bronze files**  
- Cleans and deduplicates within the day  
- Saves a daily Silver snapshot  
- Example: `2026-06-18_all_books.json`

### 🥇 Incremental Gold  
- Loads **all Silver snapshots**  
- Upserts dimensions (book, category, rating, date)  
- Appends new fact rows for each day  
- Maintains a historical warehouse

This enables:

- price trend analysis  
- availability trends  
- category evolution  
- historical reporting  
- time‑series analytics  

---

## How the Pipeline Works

🔍 **Category Discovery**  
🕷️ **Crawler**  
🥉 **Bronze Layer**  
🥈 **Silver Layer**  
🥇 **Gold Layer**  
📊 **EDA**

(See original README for full details.)

---

## How to Run the Full Pipeline

### **Original Full‑Refresh Pipeline**
1. Install dependencies  
```
pip install -r requirements.txt
```

2. Run full scraper  
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

---

# 🆕 **How to Run the Incremental Pipeline**

### 1. Run Incremental Bronze  
```
python src_incremental/bronze_incremental.py
```

### 2. Run Incremental Silver  
```
python src_incremental/silver_incremental.py
```

### 3. Run Incremental Gold  
```
python src_incremental/gold_incremental.py
```

This produces daily historical snapshots across all layers.

---

## Future Enhancements

- Incremental scraping (done)  
- Historical fact tables (done)  
- SCD Type 2 for dim_book  
- Multi‑site scraping  
- Power BI dashboard  
- ML model for price prediction  

---

## AI Collaboration Notice

Portions of this project were developed with the assistance of AI tools, specifically for improving documentation quality, refining code structure, and aligning scripts for consistency. All core engineering decisions, data modeling logic, and final code reviews were performed manually.

---

⭐ **Author**  
Olayinka Ogunneye  
Analytics Engineer
