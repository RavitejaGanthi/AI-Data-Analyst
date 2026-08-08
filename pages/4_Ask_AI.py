import streamlit as st

from src.ai_assistant import ask_ai
from src.utils import require_dataset
from src.utils import load_css

load_css()


st.title("🤖 Ask AI")


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


st.subheader("💡 Try asking")


st.info(
    """
• Summarize this dataset.

• Explain the important columns.

• Are there missing values?

• What trends do you observe?

• Which variables appear related?

• Explain this dataset like I'm a beginner.

• What business insights can you provide?
"""
)


user_question = st.text_area(
    "Enter your question",
    placeholder="Example: Summarize this dataset.",
)


if st.button("🤖 Ask AI"):

    if not user_question.strip():

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner(
                "🤖 AI is analyzing your dataset..."
            ):

                response = ask_ai(
                    analysis_df,
                    user_question,
                )

            st.subheader("📋 AI Analysis")

            st.markdown(response)

        except Exception as error:

            st.error(
                f"❌ Error: {error}"
            )