import streamlit as st

from src.data_loader import load_dataset
from src.preprocessing import clean_dataset
from src.utils import load_css

load_css()


st.title("📂 Upload Dataset")

st.write(
    "Upload a CSV file to begin analyzing your data."
)


uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"],
)


if uploaded_file is not None:

    try:

        df = load_dataset(uploaded_file)

        # Store uploaded dataset
        st.session_state.df = df

        # Reset previous cleaned dataset
        st.session_state.cleaned_df = None

        st.success(
            "✅ Dataset uploaded successfully!"
        )

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(),
            use_container_width=True,
        )

        st.divider()

        st.subheader("🧹 Automatic Data Cleaning")

        if st.button("Clean Dataset"):

            cleaned_df, summary = clean_dataset(df)

            # Store cleaned dataset
            st.session_state.cleaned_df = cleaned_df

            st.success(
                "✅ Dataset cleaned successfully!"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Original Rows",
                    summary["Original Rows"],
                )

            with col2:
                st.metric(
                    "Final Rows",
                    summary["Final Rows"],
                )

            with col3:
                st.metric(
                    "Duplicates Removed",
                    summary["Duplicates Removed"],
                )

            st.subheader("Numerical Columns")

            st.write(
                summary["Numeric Columns"]
            )

            st.subheader("Categorical Columns")

            st.write(
                summary["Categorical Columns"]
            )

            st.subheader(
                "Cleaned Dataset Preview"
            )

            st.dataframe(
                cleaned_df.head(),
                use_container_width=True,
            )

            cleaned_csv = cleaned_df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="Download Cleaned Dataset",
                data=cleaned_csv,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
            )

    except Exception as error:

        st.error(
            f"❌ Error loading dataset: {error}"
        )