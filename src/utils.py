import os

import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path

import streamlit as st


def load_css():
    """Load the application's custom CSS."""

    css_path = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "style.css"
    )

    try:

        with open(
            css_path,
            "r",
            encoding="utf-8",
        ) as css_file:

            st.markdown(
                f"<style>{css_file.read()}</style>",
                unsafe_allow_html=True,
            )

    except FileNotFoundError:

        st.warning(
            "Custom CSS file was not found."
        )





def get_api_key():
    """Load the Groq API key from the .env file."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env file."
        )

    return api_key


def require_dataset():
    """
    Check whether a dataset has been uploaded.

    Stops the current page if no dataset is available.
    """

    if (
        "df" not in st.session_state
        or st.session_state.df is None
    ):
        st.warning(
            "📂 Please upload a dataset to continue."
        )

        st.info(
            "Go to '1_Upload_Dataset' from the sidebar "
            "and upload a CSV file."
        )

        st.stop()

    return st.session_state.df