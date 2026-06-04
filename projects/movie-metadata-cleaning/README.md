# 🎬 Movies Metadata Cleaning Pipeline

A professional, modular data‑engineering project for ingesting, cleaning, and preparing  
a Movies Metadata dataset for analysis, visualization, and downstream modeling.

---

## 📁 Project Structure

```

movie-metadata-cleaning/
├─ data/
│   ├─ raw/
│   └─ cleaned/
├─ notebooks/
│   └─ 01_exploration.ipynb
├─ src/
│   ├─ ingestion/
│   ├─ cleaning/
│   └─ utils/
├─ docs/
├─ reports/
└─ requirements.txt

```

---


## 🚀 Pipeline Overview

### **1. Ingestion**
📍 *Location:* `src/ingestion/ingest_movies_metadata.py`

The ingestion module:

- Loads the raw CSV file  
- Validates file structure and column names  
- Standardizes column naming  
- Passes the DataFrame into the cleaning pipeline  
- Saves the cleaned dataset as a Parquet file in `data/cleaned/`  

---

### **2. Cleaning**
📍 *Location:* `src/cleaning/clean_movies_metadata.py`

The cleaning pipeline performs:

- Data type corrections  
- Normalization of list‑like columns (genres, cast, production companies, production countries)  
- Text cleaning and whitespace normalization  
- Duplicate removal  
- Missing value handling  
- Validation of numeric fields (budget, revenue, runtime)  

Full details documented in:

`docs/cleaning_steps.md`


---

## 📊 Notebooks

📍 *Location:* `notebooks/01_exploration.ipynb`

The notebook is used for:

- Validating the cleaned dataset  
- Exploratory data analysis (EDA)  
- Visualizing distributions, correlations, and categorical patterns  
- Exporting charts to the `reports/` directory  

---

## 📚 Documentation

- `docs/cleaning_steps.md` — Detailed cleaning pipeline  
- `docs/data_dictionary.md` — Column definitions and metadata  
- `docs/README.md` — Project overview and methodology
- `docs/insights_summary` - Detailed insights  

---

## 🧪 Requirements

Install all dependencies:


pip install -r requirements.txt


---

## 📝 Author
Olayinka Ogunneye  
Analytics Engineer & Analytics Consultant  