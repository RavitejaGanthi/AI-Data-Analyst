from groq import Groq

from src.utils import get_api_key
from src.ai_assistant import create_dataset_context


client = Groq(
    api_key=get_api_key()
)


def generate_business_insights(df):
    """
    Generate business insights from the uploaded dataset.
    """

    if df.empty:
        return "The uploaded dataset is empty."

    dataset_context = create_dataset_context(df)

    prompt = f"""
You are an experienced Business Analyst.

Using ONLY the dataset information below,
generate a professional report.

The report must contain:

# Executive Summary

# Key Findings

# Trends

# Data Quality Issues

# Recommendations

Rules:

- Never invent information.
- Keep explanations beginner-friendly.
- Use bullet points.
- Base every conclusion only on the dataset.

Dataset

{dataset_context}
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            temperature=0.3,

            max_tokens=1200,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Business Intelligence Analyst."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response.choices[0].message.content

    except Exception as error:

        return f"Error: {error}"