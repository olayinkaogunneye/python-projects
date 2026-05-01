# Methodology

This project follows a structured analytics workflow inspired by
analytics engineering practices. The goal is to separate logic,
improve reusability, and maintain a clean project structure.

## 1. Data Cleaning

All cleaning logic is stored in `scripts/cleaning_utils.py`.  
Key steps include:

- removing invisible unicode characters
- trimming and standardizing text fields
- parsing `date_added` into a proper datetime
- splitting `duration` into numeric + type
- filling missing values in director, cast, and country
- engineering new features such as `year_added` and `decade`

The cleaned dataset is saved to `data/processed/netflix_cleaned.csv`.

## 2. Exploratory Data Analysis

EDA logic is stored in `scripts/eda_utils.py`.  
Functions include:

- filtering movies, TV shows, and 1990s content
- grouping by year, genre, and country
- computing duration statistics
- comparing 1990s movies with other decades

These functions keep the notebooks focused on insights rather than code.

## 3. Visualization

All charts are generated using functions in `scripts/visualization_utils.py`.  
This includes:

- line charts for content growth
- bar charts for genres and countries
- duration distributions
- comparison plots for 1990s vs other years

Visuals are exported to the `visuals/` folder.

## 4. Notebook Workflow

- **Notebook 1** prepares the data.
- **Notebook 2** performs decade‑specific analysis.
- **Notebook 3** analyzes global trends.

Each notebook imports the scripts and uses them as reusable tools.