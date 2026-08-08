import streamlit as st
from pathlib import Path
from src.utils import load_css



# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="wide",
    

)

load_css()


# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

if "df" not in st.session_state:
    st.session_state.df = None

if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None


# --------------------------------------------------
# Home Page
# --------------------------------------------------

st.title("🤖 AI Data Analyst")

st.subheader(
    "Your AI-powered data analysis assistant"
)

st.write(
    """
Welcome to **AI Data Analyst**.

Upload any CSV dataset, explore your data,
create interactive visualizations, ask questions
using Generative AI, and generate business insights.
"""
)

st.divider()


# --------------------------------------------------
# Main Features
# --------------------------------------------------

st.subheader("🚀 What Can You Do?")


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown("### 📂 Upload")

    st.write(
        """
        Upload any CSV dataset and
        automatically understand its structure.
        """
    )


with col2:

    st.markdown("### 📊 Analyze")

    st.write(
        """
        Clean your data and create
        interactive visualizations.
        """
    )


with col3:

    st.markdown("### 🤖 Ask AI")

    st.write(
        """
        Ask natural-language questions
        about your uploaded dataset.
        """
    )


st.divider()


# --------------------------------------------------
# Features
# --------------------------------------------------

st.subheader("✨ Features")


features = [
    "📂 CSV Dataset Upload",
    "📊 Dataset Overview",
    "🧹 Automatic Data Cleaning",
    "📈 Interactive Visualizations",
    "🤖 AI Dataset Assistant",
    "💡 Business Insights",
    "📥 Download Reports",
]


for feature in features:

    st.write(f"• {feature}")


st.divider()


# --------------------------------------------------
# Technology Stack
# --------------------------------------------------

st.subheader("🛠️ Technology Stack")


st.markdown(
    """
**Python** · **Streamlit** · **Pandas** · **NumPy** ·
**Plotly** · **Groq LLM** · **Git & GitHub**
"""
)


st.divider()


# --------------------------------------------------
# Getting Started
# --------------------------------------------------

st.subheader("🚀 Getting Started")


st.info(
    """
Use the sidebar to navigate through the application.

**Recommended workflow:**

1. 📂 Upload your CSV
2. 📊 Explore the dataset
3. 🧹 Clean the data
4. 📈 Create visualizations
5. 🤖 Ask AI questions
6. 💡 Generate business insights
"""
)