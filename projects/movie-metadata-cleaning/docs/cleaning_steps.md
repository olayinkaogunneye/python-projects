# Cleaning Steps — Movies Metadata Project

This document describes the full data‑cleaning pipeline applied to the raw `movies_metadata.csv` dataset.  
The cleaning logic is implemented in `src/clean_movies_metadata.py`.

---

## 1. Fix Data Types
Several columns in the raw dataset contain incorrect or inconsistent data types.  
The pipeline corrects them as follows:

- **release_date** → converted to datetime using `pd.to_datetime(errors="coerce")`
- **budget, revenue, runtime, vote_average, vote_count, popularity** → converted to numeric
- **id** → cast to string to avoid integer overflow and preserve formatting

---

## 2. Normalize List‑Like Columns
Some metadata fields contain multiple values stored as comma‑separated strings.  
These are normalized into clean Python lists.

Columns:
- `genres`
- `cast`
- `production_companies`
- `production_countries`

Rules applied:
- If value is a list → strip whitespace from each item  
- If value is a string → split by comma → strip whitespace  
- Otherwise → return an empty list `[]`

---

## 3. Clean Text Columns
Text fields often contain:
- extra spaces  
- newline characters  
- inconsistent formatting  

Cleaning steps:
- Trim leading/trailing whitespace  
- Collapse multiple spaces into one using regex (`\s+`)  
- Convert non‑string values to `"Unknown"`  
- Apply the same cleaning to items inside list columns

Columns cleaned:
- `title`
- `overview`
- `director`
- `original_language`
- plus all list‑column items

---

## 4. Remove Duplicates Inside Lists
List columns may contain repeated values.  
Duplicates are removed while preserving order using:

`list(dict.fromkeys(x))`

Example:
`["Comedy", "Drama", "Comedy"]` → `["Comedy", "Drama"]`

---

## 5. Handle Missing Values
Missing values are handled according to column type:

### Text Columns
- Filled with `"Unknown"`

### List Columns
- Converted to empty lists `[]`

### Runtime
- Missing values replaced with the median runtime

### Numeric Columns
- Filled with `0` (interpreted as “not reported”)

### release_date
- Missing values set to `NaT`

---

## 6. Output
The cleaned dataset is saved as:

`data/cleaned/movies_metadata_clean.parquet`

Parquet is used because it:
- preserves data types  
- supports nested structures (lists)  
- loads faster  
- compresses efficiently  

---

## Pipeline Summary
1. Fix data types  
2. Normalize list columns  
3. Clean text  
4. Remove list duplicates  
5. Handle missing values  
6. Save cleaned dataset  