
---

## 📌 Contents

### **1. raw/netflix_data.csv**
- This is the **original dataset** loaded into Notebook 1.
- It contains the unmodified Netflix titles data, including:
  - show_id  
  - type  
  - title  
  - director  
  - cast  
  - country  
  - date_added  
  - release_year  
  - duration  
  - description  
  - genre  
- No cleaning, formatting, or preprocessing has been applied.

---

### **2. processed/netflix_cleaned.csv**
This file is generated after running **Notebook 1 — Data Cleaning & Preparation**.

It includes:

- Cleaned column names (lowercase, underscores)
- Corrected data types:
  - `date_added` → datetime  
  - `release_year` → integer  
  - `duration` → numeric  
- Missing values handled:
  - `country`, `director`, `cast` filled with `"Unknown"`
  - Rows with missing `duration` removed
- No duplicates
- Ready for analysis in Notebook 2 and Notebook 3

This is the **only cleaned dataset** produced by the project.

---

## 🔒 Notes
- Do **not** modify files in `raw/`.  
- All transformations should be done in notebooks or scripts and saved into `processed/`.

---

## 📬 Contact
For questions about the dataset or cleaning process, refer to Notebook 1 or contact the project author.