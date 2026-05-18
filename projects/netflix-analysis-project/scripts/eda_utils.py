"""
eda_utils.py

A small collection of helper functions for exploratory analysis
on the cleaned Netflix dataset. These functions are used mainly
in Notebook 2 (1990s analysis) and Notebook 3 (global trends).

The idea is to keep the notebooks tidy and move repeated logic here.
"""

import pandas as pd


# ---------------------------------------------------------
# Filtering helpers
# ---------------------------------------------------------

def filter_movies(df):
    """Return only rows where type == 'Movie'."""
    return df[df["type"] == "Movie"].copy()


def filter_tv_shows(df):
    """Return only rows where type == 'TV Show'."""
    return df[df["type"] == "TV Show"].copy()


def filter_1990s(df):
    """Return movies released between 1990 and 1999."""
    return df[(df["release_year"] >= 1990) & (df["release_year"] <= 1999)].copy()


# ---------------------------------------------------------
# Basic aggregations
# ---------------------------------------------------------

def movies_per_year(df):
    """
    Count how many movies were released each year.
    Works for any subset (e.g., 1990s movies).
    """
    return (
        df.groupby("release_year")
          .size()
          .reset_index(name="count")
          .sort_values("release_year")
    )


def top_genres(df, n=10):
    """
    Return the top N genres by frequency.
    Assumes the 'genre' column contains a single genre per row.
    """
    return (
        df["genre"]
        .str.split(", ")
        .explode()
        .value_counts()
        .head(n)
        .reset_index(name="count")
        .rename(columns={"index": "genre"})
    )


def avg_duration_by_genre(df):
    """
    Compute the average duration (in minutes) for each genre.
    Only applies to movies.
    """
    return (
        df.groupby("genre")["duration"]
          .mean()
          .reset_index()
          .sort_values("duration", ascending=False)
    )


def country_counts(df, n=10):
    """
    Return the top N countries by number of titles.
    If a row contains multiple countries, only the first is used.
    """
    return (
        df["country"]
        .fillna("Unknown")
        .str.split(", ")
        .explode()
        .value_counts()
        .head(n)
        .reset_index(name="count")
        .rename(columns={"index": "country"})
    )


def top_directors(df, n=10):
    """
    Return the most frequent directors in the dataset.
    Rows with 'Unknown' are ignored.
    """
    temp = df[df["director"] != "Unknown"]["director"]
    return (
        temp.value_counts()
            .reset_index()
            .rename(columns={"index": "director", "director": "count"})
            .head(n)
    )


# ---------------------------------------------------------
# Duration statistics
# ---------------------------------------------------------

def duration_distribution(df):
    """
    Return basic statistics for movie durations.
    Useful for plotting histograms or boxplots.
    """
    return df["duration"].describe()

# ---------------------------------------------------------
#  comparing 1990s movies to other movies
# --------------------------------------------------------- 

def filter_non_1990s(df):
    """Return movies NOT released between 1990 and 1999."""
    return df[(df["release_year"] < 1990) | (df["release_year"] > 1999)].copy()


def compare_avg_duration(df_1990s, df_other):
    """Return a simple comparison of average duration."""
    return {
        "1990s_avg_duration": df_1990s["duration"].mean(),
        "other_avg_duration": df_other["duration"].mean()
    }


def compare_genre_distribution(df_1990s, df_other, n=10):
    """Return top genres for both groups."""
    top_90s = df_1990s["genre"].value_counts().head(n)
    top_other = df_other["genre"].value_counts().head(n)
    return top_90s, top_other
