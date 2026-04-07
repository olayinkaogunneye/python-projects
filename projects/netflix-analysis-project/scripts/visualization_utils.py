"""
visualization_utils.py

This module contains reusable plotting functions for common chart types.
These functions help keep notebooks clean by abstracting away repetitive
plotting code.

They are intentionally simple and customizable.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def plot_line(series, title, xlabel, ylabel, color='blue'):
    """
    Plot a simple line chart.

    Parameters:
        series (pd.Series): Index → x-axis, Values → y-axis
        title (str)
        xlabel (str)
        ylabel (str)
        color (str)
    """
    plt.figure(figsize=(10, 4))
    plt.plot(series.index, series.values, marker='o', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


def plot_bar(series, title, xlabel, ylabel, color='purple'):
    """
    Plot a bar chart from a pandas Series.

    Parameters:
        series (pd.Series)
        title (str)
        xlabel (str)
        ylabel (str)
        color (str)
    """
    plt.figure(figsize=(10, 4))
    series.plot(kind='bar', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def plot_hist(df, col, bins=20, color='skyblue'):
    """
    Plot a histogram for a numeric column.

    Parameters:
        df (pd.DataFrame)
        col (str)
        bins (int)
        color (str)
    """
    plt.figure(figsize=(8, 4))
    plt.hist(df[col], bins=bins, color=color, edgecolor='black')
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()


def plot_box(df, col, color='orange'):
    """
    Plot a boxplot for a numeric column.

    Parameters:
        df (pd.DataFrame)
        col (str)
        color (str)
    """
    plt.figure(figsize=(8, 2))
    sns.boxplot(x=df[col], color=color)
    plt.title(f"{col} Spread")
    plt.show()