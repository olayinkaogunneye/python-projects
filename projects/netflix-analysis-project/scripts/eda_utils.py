"""
eda_utils.py

This module contains helper functions for exploratory data analysis.
These functions perform common EDA tasks such as counting, grouping,
and filtering. They are intentionally generic so they can be reused
in Notebook 2, Notebook 3, or future projects.
"""


def count_by_year(df, year_col='release_year'):
    """
    Count number of records per year.

    Parameters:
        df (pd.DataFrame)
        year_col (str): Column representing the year

    Returns:
        pd.Series: Year → Count
    """
    return df[year_col].value_counts().sort_index()


def top_n(df, col, n=10):
    """
    Return the top N most frequent values in a column.

    Parameters:
        df (pd.DataFrame)
        col (str)
        n (int)

    Returns:
        pd.Series
    """
    return df[col].value_counts().head(n)


def average_by_group(df, group_col, value_col):
    """
    Compute the average of a numeric column grouped by another column.

    Example:
        Average duration by genre

    Parameters:
        df (pd.DataFrame)
        group_col (str)
        value_col (str)

    Returns:
        pd.Series
    """
    return df.groupby(group_col)[value_col].mean().sort_values(ascending=False)


def filter_decade(df, decade):
    """
    Filter rows belonging to a specific decade.

    Example:
        decade = 1990 → returns 1990–1999

    Parameters:
        df (pd.DataFrame)
        decade (int)

    Returns:
        pd.DataFrame
    """
    return df[df['release_year'].between(decade, decade + 9)]
