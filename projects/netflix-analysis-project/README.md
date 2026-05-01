# 📊 Netflix Content Analysis Project

A data cleaning, exploratory analysis, and global trends study of Netflix titles

---

# 📌 Project Overview

This project explores the evolution of Netflix content using a structured analytics workflow.
The goal is to understand:

how Netflix’s catalog has changed over time

what made the 1990s unique

which genres dominate different eras

how movie durations and storytelling styles have shifted

how countries contribute to Netflix’s global library

The project is organized using a clean, analytics‑engineering‑style structure with reusable scripts, modular notebooks, and exported visuals.

---

# 🗂️ Project Structure

netflix-analysis-project/
│
├── data/
│   ├── raw/                     # Original dataset
│   └── processed/               # Cleaned dataset (output of Notebook 1)
│
├── scripts/
│   ├── cleaning_utils.py        # Data cleaning functions
│   ├── eda_utils.py             # EDA helper functions
│   └── visualization_utils.py   # Plotting utilities
│
├── notebooks/
│   ├── Notebook_1_Data_Cleaning.ipynb
│   ├── Notebook_2_1990s_Analysis.ipynb
│   └── Notebook_3_Global_Trends.ipynb
│
├── docs/
│   ├── project_overview.md      # High-level description of the project
│   ├── methodology.md           # Detailed workflow and approach
│   ├── insights_summary.md      # Key findings from all notebooks
│   └── future_work.md           # Ideas for extending the project
│
├── visuals/                     # Exported charts and figures
│
├── README.md                    # Main project documentation
└── requirements.txt             # Python dependencies

---

# 🧹 Notebook 1 — Data Cleaning & Preparation

Notebook 1 loads the raw dataset and applies a full cleaning pipeline using functions from cleaning_utils.py.

Key steps include:

removing invisible unicode characters

standardizing text fields

parsing date_added

splitting duration into numeric + type

filling missing values

adding year_added and decade features

exporting a clean dataset for analysis

The cleaned file is saved to: `data/processed/netflix_cleaned.csv`

---

# 🎬 Notebook 2 — 1990s Movies Deep Dive

This notebook focuses on movies released between 1990 and 1999.

Analyses include:

number of movies released each year

top genres of the decade

average duration by genre

top contributing countries

most frequent directors

duration distribution

## 🔥 Additional Comparison

The notebook also compares:

1990s movies vs. all other movies, including:

genre differences

duration differences

country contributions

director patterns

This section highlights what made the 1990s distinct.

# 🌍 Notebook 3 — Global Trends & Evolution

This notebook zooms out to analyze the entire Netflix catalog.

Key insights include:

growth of movies and TV shows over time

shifts in genre popularity

duration trends across decades

country diversification

movies vs TV shows comparison

This notebook ties the whole project together and provides a global perspective.

# 🛠️ Technologies & Skills Demonstrated

This project showcases practical skills in:

## Data Engineering & Analytics

Modular Python scripting

Clean project structuring

Reusable utilities for cleaning, EDA, and visualization

Feature engineering

Exploratory data analysis

## Visualization

Seaborn & Matplotlib

Trend analysis

Comparative charts

Distribution analysis

## Professional Workflow

Separation of concerns (scripts vs notebooks)

Reproducible analysis

Clear documentation

Portfolio‑ready storytelling

# 📈 Key Insights (High‑Level)

Netflix’s content library has grown significantly over time, especially after 2010.

Certain genres dominate the catalog, but newer years show diversification.

Movie durations vary by decade, reflecting changes in storytelling style.

A handful of countries contribute a large share of the catalog.

The 1990s have distinct genre and duration patterns compared to other decades.

# 📥 Dataset Source

The dataset used in this project is the publicly available Netflix Titles dataset, commonly used for exploratory analysis and educational projects.

# 👤 Author

Olayinka Ogunneye
  
Data Analyst / Data Engineer

This project reflects my approach to building clean, modular, analytics‑engineering‑style workflows using Python, reusable scripts, and structured notebooks.