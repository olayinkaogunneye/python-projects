# 🎬 Final Project Report — Movies Metadata Cleaning & Exploratory Analysis

## 1. Project Overview
This project focuses on building a reproducible **data ingestion and cleaning pipeline**, followed by a structured **exploratory data analysis (EDA)** of a movies metadata dataset. The objective is to transform raw, inconsistent movie information into a clean, analysis‑ready dataset and extract meaningful insights about movie characteristics, performance, and audience engagement.

The project demonstrates:

- Data ingestion and pipeline design  
- Data cleaning and transformation  
- Exploratory data analysis  
- Visualization and insight generation  
- Documentation and reporting  
- Responsible use of AI assistance to accelerate development  

---

## 2. Dataset Description
The dataset contains metadata for a collection of movies, including:

- Title  
- Release date  
- Genres  
- Budget  
- Revenue  
- Runtime  
- Popularity  
- Vote metrics  
- Cast  
- Production companies  
- Production countries  

The raw dataset required cleaning due to inconsistent formats, missing values, nested fields, incorrect data types, and invalid numeric values.

---

## 3. Methodology

### 3.1 Ingestion
The ingestion step:

- Loads the raw CSV file  
- Validates structure and column names  
- Standardizes column naming  
- Stores the raw file under `data/raw/`  

---

### 3.2 Cleaning
The cleaning pipeline:

- Converts columns to appropriate data types  
- Parses list‑like fields (genres, cast, production companies, production countries)  
- Handles missing values  
- Cleans numeric fields such as budget, revenue, and runtime  
- Removes invalid or inconsistent records  
- Saves the cleaned dataset as a Parquet file  

The cleaned dataset is stored at:

`data/cleaned/movies_metadata_clean.parquet`


---

### 3.3 Exploratory Data Analysis
The EDA notebook includes:

- Dataset validation  
- Descriptive statistics  
- Distribution analysis  
- Genre and cast frequency analysis  
- Correlation analysis  
- Outlier detection  
- Export of visualizations to the `reports/` folder  

---

## 4. Use of AI Assistance
AI tools were used responsibly to support and accelerate the project in the following areas:

- Drafting boilerplate code for ingestion, cleaning, and visualization  
- Generating structured EDA workflows and notebook templates  
- Providing explanations of statistical concepts and best practices  
- Assisting with Markdown documentation structure  
- Helping refine insights based on visual outputs  
- Ensuring consistent formatting across project files  

All AI‑generated content was reviewed and validated manually to ensure correctness and alignment with project goals.

---

## 5. Key Findings and Insights

### 5.1 Runtime Insights
- Most movies fall between **100 and 130 minutes**, with a median around **120 minutes**.  
- A single extreme outlier (~20 minutes) suggests a short film or data anomaly.  
- Runtime shows **weak correlation** with revenue, popularity, and vote metrics.  

---

### 5.2 Genre Insights
- **Action, Comedy, Thriller, and Drama** are the most frequent genres.  
- **Documentary** and **Music** genres appear only a few times.  
- Genre imbalance means mainstream genres drive most patterns.  

---

### 5.3 Budget Insights
- *The Electric State* is the highest‑budget film at **$320M**.  
- Budget distribution is **right‑skewed**.  
- High‑budget outliers distort averages and should be treated separately.  

---

### 5.4 Revenue Insights
- *Despicable Me 2* is the top revenue outlier at **$970.7M**.  
- Revenue is heavily **right‑skewed**, driven by blockbuster films.  
- Franchise films dominate the upper tail of revenue.  

---

### 5.5 Popularity Insights
- Popularity scores are **right‑skewed**.  
- Most movies have moderate popularity; a few achieve very high scores.  
- Popularity correlates moderately with **vote_count** and **revenue**.  

---

### 5.6 Correlation Insights
- **vote_count ↔ revenue**: strongest correlation (**0.69**)  
- **budget ↔ revenue**: moderate correlation (**0.44**)  
- **vote_average** shows very weak correlation with revenue or popularity  
- **runtime** has weak correlations with all numeric variables  

---

### 5.7 Cast Insights
- A few actors (e.g., **Tom Cruise**, **Ving Rhames**, **Sofia Carson**) appear multiple times.  
- Most actors appear only once or twice.  
- Recurring actors reflect franchise‑driven patterns.  

---

## 6. Limitations
- Dataset size is relatively small (**42 movies**).  
- Genre and cast fields vary in completeness.  
- Budget and revenue figures may not be inflation‑adjusted.  
- Popularity is platform‑specific and not industry‑standard.  

---

## 7. Recommendations
- Perform ROI analysis across genres and production types.  
- Build predictive models for revenue or popularity.  
- Enrich the dataset with external data sources.  
- Expand the dataset with more movies and time periods.  

---

## 8. Future Work
- Feature engineering for modeling  
- Dashboard development (Power BI or Streamlit)  
- Revenue or popularity forecasting  
- Automated reporting pipeline  

---

## 9. Conclusion
This project demonstrates a complete workflow from raw movies metadata to a cleaned, analysis‑ready dataset and a structured exploratory analysis. The findings highlight the importance of audience engagement (**vote_count**), the skewed nature of revenue and popularity, and the influence of genre and franchise patterns. The project is reproducible, extendable, and provides a strong foundation for further modeling or dashboarding.