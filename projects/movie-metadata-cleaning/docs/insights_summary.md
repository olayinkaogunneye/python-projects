# Insights Summary — Movies Metadata Project

This document summarizes the key insights derived from the exploratory data analysis (EDA) of the cleaned movies metadata dataset. The insights are based on visualizations and statistical exploration performed in the analysis notebook.

---

## 1. Runtime Insights
- Most movies fall between 100 and 130 minutes, with a median runtime around 120 minutes.
- A single extreme outlier (~20 minutes) indicates the presence of a short film or a data anomaly.
- Runtime shows weak correlation with revenue, popularity, and vote metrics, suggesting it is not a strong driver of commercial performance.

---

## 2. Genre Insights
- Action, Comedy, Thriller, and Drama dominate the dataset.
- Documentary and Music genres appear infrequently.
- Genre imbalance means mainstream genres drive most patterns in revenue and popularity.

---

## 3. Budget Insights
- “The Electric State” stands out as the highest-budget film at $320M.
- The budget distribution is right-skewed, with most films operating at significantly lower budgets.
- High-budget outliers can distort averages and should be treated separately in modeling.

---

## 4. Revenue Insights
- “Despicable Me 2” is the top revenue outlier at $970.7M.
- Revenue distribution is heavily right-skewed, driven by a small number of blockbuster films.
- Franchise films tend to dominate the upper tail of revenue.

---

## 5. Popularity Insights
- Popularity scores are right-skewed, with a few films achieving very high popularity.
- Most movies have moderate popularity levels.
- Popularity correlates moderately with vote_count and revenue.

---

## 6. Correlation Insights
- Vote Count has the strongest correlation with revenue (0.69), indicating audience engagement is a key driver of commercial success.
- Budget has a moderate positive correlation with revenue (0.44).
- Vote Average shows almost no correlation with revenue or popularity, suggesting high ratings do not guarantee financial success.

---

## 7. Cast Insights
- A few actors (e.g., Tom Cruise, Ving Rhames, Sofia Carson) appear frequently, reflecting franchise-driven patterns.
- Most actors appear only once or twice.
- Actor frequency may influence popularity and revenue in franchise-heavy datasets.

---

## 8. Overall Summary
The dataset is dominated by mainstream genres and feature-length films, with a few extreme outliers in budget and revenue that significantly influence distribution shapes. Audience engagement (vote count) is the strongest predictor of revenue, while runtime and ratings play minimal roles. Popularity and revenue are both right-skewed, driven by a small number of standout films. Franchise effects are visible in both cast frequency and revenue outliers.

