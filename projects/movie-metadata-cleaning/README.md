# 🎬 Movies Metadata Cleaning Pipeline

A professional, modular data‑engineering project for cleaning and preparing  
the TMDB Movies Metadata dataset.

---

## 📁 Project Structure

---

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

---


---

## 🚀 Pipeline Overview

### 1. Ingestion
Located in: `src/ingestion/ingest_movies_metadata.py`

- Loads raw CSV  
- Validates file  
- Sends DataFrame to cleaning pipeline  
- Saves cleaned dataset as Parquet  

### 2. Cleaning
Located in: `src/cleaning/clean_movies_metadata.py`

Cleaning steps include:
- fixing data types  
- normalizing list columns  
- cleaning text  
- removing duplicates  
- handling missing values  

Full details in: `docs/cleaning_steps.md`

---

## 📊 Notebooks
Located in: `notebooks/01_exploration.ipynb`

Used for:
- validating the cleaned dataset  
- exploratory data analysis  
- visualizations  
- exporting charts to `reports/`  

---

## 📚 Documentation
- `docs/cleaning_steps.md` — full cleaning pipeline  
- `docs/data_dictionary.md` — column definitions  
- `docs/README.md` — project overview  

---

## 🧪 Requirements
Install dependencies:

pip install -r requirements.txt


---

## 📝 Author
Olayinka Ogunneye  
Data Engineer & Analytics Consultant  