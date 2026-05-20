# Data Dictionary — Cleaned Movies Metadata

This document describes each column in the cleaned dataset  
(`movies_metadata_clean.parquet`), including type and meaning.

---

## Core Metadata

| Column | Type | Description |
|--------|------|-------------|
| **id** | string | Unique movie identifier |
| **title** | string | Movie title (cleaned text) |
| **overview** | string | Short plot summary |
| **release_date** | datetime | Official release date |
| **original_language** | string | ISO language code (e.g., "en") |

---

## Numeric Fields

| Column | Type | Description |
|--------|------|-------------|
| **budget** | float | Production budget in USD |
| **revenue** | float | Worldwide box office revenue |
| **runtime** | float | Duration in minutes |
| **vote_average** | float | Average user rating |
| **vote_count** | float | Number of votes |
| **popularity** | float | Popularity score from TMDB |

---

## List‑Like Metadata

| Column | Type | Description |
|--------|------|-------------|
| **genres** | list[string] | Movie genres (cleaned list) |
| **cast** | list[string] | Main cast members |
| **production_companies** | list[string] | Companies involved in production |
| **production_countries** | list[string] | Countries where production occurred |

---

## Notes
- All list columns contain **clean Python lists**, not strings.  
- Missing text fields are filled with `"Unknown"`.  
- Missing numeric fields are filled with `0` (except runtime → median).  
- Missing dates are represented as `NaT`.  