import streamlit as st

from src.utils import require_dataset
from src.utils import load_css

load_css()

from src.visualization import (
    create_bar_chart,
    create_box_plot,
    create_correlation_heatmap,
    create_histogram,
    create_line_chart,
    create_pie_chart,
    create_scatter_plot,
    get_categorical_columns,
    get_numeric_columns,
)


st.title("📈 Interactive Visualizations")


# Check dataset
df = require_dataset()


# Use cleaned dataset if available
if (
    "cleaned_df" in st.session_state
    and st.session_state.cleaned_df is not None
):

    visualization_df = (
        st.session_state.cleaned_df
    )

    st.info(
        "Using the cleaned dataset."
    )

else:

    visualization_df = df

    st.info(
        "Using the original dataset."
    )


# Get column types
numeric_columns = get_numeric_columns(
    visualization_df
)

categorical_columns = get_categorical_columns(
    visualization_df
)


chart_type = st.selectbox(
    "Select Visualization",
    [
        "Histogram",
        "Box Plot",
        "Scatter Plot",
        "Correlation Heatmap",
        "Bar Chart",
        "Pie Chart",
        "Line Chart",
    ],
)


# --------------------------------------------------
# Histogram
# --------------------------------------------------

if chart_type == "Histogram":

    if numeric_columns:

        column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
        )

        fig = create_histogram(
            visualization_df,
            column,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "No numerical columns available."
        )


# --------------------------------------------------
# Box Plot
# --------------------------------------------------

elif chart_type == "Box Plot":

    if numeric_columns:

        column = st.selectbox(
            "Select Numerical Column",
            numeric_columns,
        )

        fig = create_box_plot(
            visualization_df,
            column,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "No numerical columns available."
        )


# --------------------------------------------------
# Scatter Plot
# --------------------------------------------------

elif chart_type == "Scatter Plot":

    if len(numeric_columns) >= 2:

        col1, col2 = st.columns(2)

        with col1:

            x_column = st.selectbox(
                "X-axis",
                numeric_columns,
            )

        with col2:

            y_column = st.selectbox(
                "Y-axis",
                numeric_columns,
                index=1,
            )

        fig = create_scatter_plot(
            visualization_df,
            x_column,
            y_column,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "At least two numerical columns "
            "are required."
        )


# --------------------------------------------------
# Correlation Heatmap
# --------------------------------------------------

elif chart_type == "Correlation Heatmap":

    if len(numeric_columns) >= 2:

        fig = create_correlation_heatmap(
            visualization_df
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "At least two numerical columns "
            "are required."
        )


# --------------------------------------------------
# Bar Chart
# --------------------------------------------------

elif chart_type == "Bar Chart":

    if categorical_columns:

        column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
        )

        fig = create_bar_chart(
            visualization_df,
            column,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "No categorical columns available."
        )


# --------------------------------------------------
# Pie Chart
# --------------------------------------------------

elif chart_type == "Pie Chart":

    if categorical_columns:

        column = st.selectbox(
            "Select Categorical Column",
            categorical_columns,
        )

        unique_values = (
            visualization_df[column].nunique()
        )

        if unique_values <= 10:

            fig = create_pie_chart(
                visualization_df,
                column,
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
            )

        else:

            st.warning(
                "Pie charts work best with "
                "10 or fewer categories."
            )

    else:

        st.warning(
            "No categorical columns available."
        )


# --------------------------------------------------
# Line Chart
# --------------------------------------------------

elif chart_type == "Line Chart":

    if numeric_columns:

        col1, col2 = st.columns(2)

        with col1:

            x_column = st.selectbox(
                "X-axis",
                visualization_df.columns.tolist(),
            )

        with col2:

            y_column = st.selectbox(
                "Y-axis",
                numeric_columns,
            )

        fig = create_line_chart(
            visualization_df,
            x_column,
            y_column,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    else:

        st.warning(
            "No numerical columns available."
        )