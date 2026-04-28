"""
visualization_utils.py

A small set of helper functions for generating charts used in the
Netflix analysis notebooks. The goal is to avoid repeating the same
plotting code in multiple notebooks.

These functions use matplotlib and seaborn for simple, clean visuals.
"""

import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------
# Basic line and bar charts
# ---------------------------------------------------------

def plot_movies_per_year(df, title="Movies Released per Year", save_path=None):
    """
    Plot a simple line chart showing how many movies were released each year.
    Expects a dataframe with columns: release_year, count.
    """
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x="release_year", y="count", marker="o")
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel("Number of Movies")
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


def plot_top_genres(df, title="Top Genres", save_path=None):
    """
    Plot a horizontal bar chart of the top genres.
    Expects columns: genre, count.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="count", y="genre", palette="viridis")
    plt.title(title)
    plt.xlabel("Count")
    plt.ylabel("Genre")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


def plot_avg_duration(df, title="Average Duration by Genre", save_path=None):
    """
    Plot average movie duration by genre.
    Expects columns: genre, duration_int.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=df, x="duration_int", y="genre", palette="magma")
    plt.title(title)
    plt.xlabel("Average Duration (minutes)")
    plt.ylabel("Genre")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


# ---------------------------------------------------------
# Country charts
# ---------------------------------------------------------

def plot_country_counts(df, title="Top Countries by Number of Titles", save_path=None):
    """
    Plot a bar chart of the top countries.
    Expects columns: country, count.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x="count", y="country", palette="cubehelix")
    plt.title(title)
    plt.xlabel("Count")
    plt.ylabel("Country")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()


# ---------------------------------------------------------
# Duration distribution
# ---------------------------------------------------------

def plot_duration_distribution(df, title="Distribution of Movie Durations", save_path=None):
    """
    Plot a histogram of movie durations.
    Expects column: duration_int.
    """
    plt.figure(figsize=(10, 5))
    sns.histplot(df["duration_int"], bins=30, kde=True, color="steelblue")
    plt.title(title)
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Frequency")

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")

    plt.show()
