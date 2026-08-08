import streamlit as st
from src.utils import load_css

load_css()


st.title("ℹ️ About AI Data Analyst")


st.markdown(
    """
## 🤖 AI Data Analyst

AI Data Analyst is a beginner-friendly
Generative AI application that helps users
analyze CSV datasets using natural language.

### Features

- 📂 Dataset Upload
- 📊 Dataset Overview
- 🧹 Automatic Data Cleaning
- 📈 Interactive Visualizations
- 🤖 AI Dataset Assistant
- 💡 Business Insights
- 📥 Downloadable Reports

### Technology Stack

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Groq LLM
- Git & GitHub

### Generative AI Concepts

This project demonstrates:

- LLM API integration
- Prompt Engineering
- Dataset Context
- Context Injection
- AI-powered Data Analysis

### Purpose

This project demonstrates practical skills
in Python, Data Science, Streamlit,
and Generative AI development.
"""
)