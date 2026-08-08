import streamlit as st

from src.utils import require_dataset
from src.utils import load_css

load_css()


st.title("📊 Dataset Overview")


# Check whether dataset exists
df = require_dataset()


st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True,
)


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Rows",
        df.shape[0],
    )


with col2:

    st.metric(
        "Columns",
        df.shape[1],
    )


with col3:

    st.metric(
        "Duplicate Rows",
        df.duplicated().sum(),
    )


st.divider()


st.subheader("📋 Column Names")

st.write(
    list(df.columns)
)


st.subheader("🔤 Data Types")

st.dataframe(
    df.dtypes.astype(str),
)


st.subheader("❓ Missing Values")

st.dataframe(
    df.isnull().sum().rename(
        "Missing Values"
    )
)


st.subheader("📈 Summary Statistics")

st.dataframe(
    df.describe(include="all"),
)


csv = df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="dataset.csv",
    mime="text/csv",
)