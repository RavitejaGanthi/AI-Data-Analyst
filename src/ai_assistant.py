from groq import Groq

from src.utils import get_api_key


client = Groq(
    api_key=get_api_key()
)


def create_dataset_context(df):
    """
    Create a compact summary of the uploaded dataset.
    """

    context = f"""
DATASET OVERVIEW

Shape:
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes.to_string()}

Missing Values:
{df.isnull().sum().to_string()}

Summary Statistics:
{df.describe(include='all').to_string()}

Sample Data:
{df.head(10).to_string(index=False)}
"""

    return context


def ask_ai(df, question):
    """
    Ask the AI questions about the uploaded dataset.
    """

    dataset_context = create_dataset_context(df)

    prompt = f"""

You are an experienced Data Analyst and Business Intelligence Expert.

You must answer ONLY using the uploaded dataset information provided below.

Rules:

1. Never invent information.
2. Never guess missing values.
3. If information is unavailable, reply:
   "I cannot determine that from the uploaded dataset."
4. Keep answers beginner-friendly.
5. Use bullet points whenever appropriate.
6. Explain technical terms in simple language.
7. Mention important trends if they are visible.
8. Mention data quality issues if present.
9. Suggest business insights only when supported by the dataset.

-------------------------
DATASET INFORMATION
-------------------------

{dataset_context}

-------------------------
USER QUESTION
-------------------------

{question}

Provide a clear, structured answer.
"""

    try:

        response = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            temperature=0.3,

            max_tokens=1000,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Data Analyst."
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