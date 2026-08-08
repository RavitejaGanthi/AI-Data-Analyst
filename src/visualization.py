import pandas as pd
import plotly.express as px




def get_numeric_columns(df: pd.DataFrame) -> list:
    """Return numerical column names."""
    return df.select_dtypes(include="number").columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> list:
    """Return categorical column names."""
    return df.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()


def create_histogram(df: pd.DataFrame, column: str):
    """Create a histogram for a numerical column."""

    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )

    return fig


def create_box_plot(df: pd.DataFrame, column: str):
    """Create a box plot for a numerical column."""

    fig = px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )

    return fig


def create_scatter_plot(
    df: pd.DataFrame,
    x_column: str,
    y_column: str
):
    """Create a scatter plot."""

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{x_column} vs {y_column}"
    )

    return fig


def create_bar_chart(
    df: pd.DataFrame,
    categorical_column: str
):
    """Create a bar chart showing category counts."""

    counts = (
        df[categorical_column]
        .value_counts()
        .head(20)
        .reset_index()
    )

    counts.columns = [categorical_column, "Count"]

    fig = px.bar(
        counts,
        x=categorical_column,
        y="Count",
        title=f"Top Categories in {categorical_column}"
    )

    return fig


def create_pie_chart(
    df: pd.DataFrame,
    categorical_column: str
):
    """Create a pie chart showing category distribution."""

    counts = (
        df[categorical_column]
        .value_counts()
        .head(10)
        .reset_index()
    )

    counts.columns = [categorical_column, "Count"]

    fig = px.pie(
        counts,
        names=categorical_column,
        values="Count",
        title=f"Distribution of {categorical_column}"
    )

    return fig


def create_line_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str
):
    """Create a line chart."""

    plot_df = df[[x_column, y_column]].dropna()

    fig = px.line(
        plot_df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    return fig


def create_correlation_heatmap(df: pd.DataFrame):
    """Create a correlation heatmap."""

    numeric_df = df.select_dtypes(include="number")

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig