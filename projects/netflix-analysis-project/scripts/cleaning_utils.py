
"""
cleaning_utils.py

This module contains reusable helper functions for cleaning datasets.
These functions are intentionally generic so they can be used across
multiple notebooks and projects.

They DO NOT perform full cleaning pipelines — they only handle small,
reusable cleaning tasks such as renaming columns, converting types,
and filling missing values.
"""

import pandas as pd


def clean_column_names(df):
    """
    Standardize column names by:
    - stripping whitespace
    - converting to lowercase
    - replacing spaces with underscores

    This ensures consistent naming across the project.

    Parameters:
        df (pd.DataFrame): Input dataframe

    Returns:
        pd.DataFrame: Dataframe with cleaned column names
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df


def convert_to_datetime(df, col):
    """
    Convert a column to datetime format.

    Parameters:
        df (pd.DataFrame): Input dataframe
        col (str): Column name to convert

    Returns:
        pd.DataFrame: Updated dataframe with datetime column
    """
    df[col] = pd.to_datetime(df[col], errors='coerce')
    return df


def convert_to_numeric(df, col):
    """
    Convert a column to numeric values.

    Non-numeric values become NaN.

    Parameters:
        df (pd.DataFrame)
        col (str)

    Returns:
        pd.DataFrame
    """
    df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def fill_missing(df, col, value="Unknown"):
    """
    Fill missing values in a column with a default value.

    Useful for categorical fields like country, director, cast.

    Parameters:
        df (pd.DataFrame)
        col (str)
        value (str): Replacement value

    Returns:
        pd.DataFrame
    """
    df[col] = df[col].fillna(value)
    return df
