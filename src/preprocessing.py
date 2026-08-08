import pandas as pd


def clean_dataset(df: pd.DataFrame):
    """
    Clean the dataset and return:
    - Cleaned DataFrame
    - Cleaning Summary
    """

    cleaned_df = df.copy()

    original_rows = len(cleaned_df)

    # Remove duplicate rows
    duplicates_removed = cleaned_df.duplicated().sum()
    cleaned_df = cleaned_df.drop_duplicates()

    # Detect column types
    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = cleaned_df.select_dtypes(exclude=["number"]).columns.tolist()

    # Convert object columns to numeric where possible
    for column in categorical_columns:
        try:
            cleaned_df[column] = pd.to_numeric(cleaned_df[column])
        except Exception:
            pass

    # Refresh column lists after conversion
    numeric_columns = cleaned_df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = cleaned_df.select_dtypes(exclude=["number"]).columns.tolist()

    # Fill missing values
    for column in numeric_columns:
        cleaned_df[column] = cleaned_df[column].fillna(
            cleaned_df[column].median()
        )

    for column in categorical_columns:
        mode = cleaned_df[column].mode()

        if not mode.empty:
            cleaned_df[column] = cleaned_df[column].fillna(mode[0])
        else:
            cleaned_df[column] = cleaned_df[column].fillna("Unknown")

    summary = {
        "Original Rows": original_rows,
        "Final Rows": len(cleaned_df),
        "Duplicates Removed": duplicates_removed,
        "Numeric Columns": numeric_columns,
        "Categorical Columns": categorical_columns,
    }

    return cleaned_df, summary