import streamlit as st

from src.insights import generate_business_insights
from src.utils import require_dataset
from src.utils import load_css

load_css()


st.title("💡 Business Insights")


# Check dataset
df = require_dataset()


# Use cleaned dataset if available
if (
    "cleaned_df" in st.session_state
    and st.session_state.cleaned_df is not None
):

    analysis_df = (
        st.session_state.cleaned_df
    )

else:

    analysis_df = df


st.write(
    """
Generate an AI-powered business report
from your uploaded dataset.
"""
)


if st.button(
    "💡 Generate Business Insights"
):

    try:

        with st.spinner(
            "🤖 Generating business insights..."
        ):

            insights = generate_business_insights(
                analysis_df
            )

        st.success(
            "✅ Business report generated!"
        )

        st.markdown(insights)

        st.download_button(
            label="📥 Download Business Report",
            data=insights,
            file_name="business_insights.txt",
            mime="text/plain",
        )

    except Exception as error:

        st.error(
            f"❌ Error: {error}"
        )