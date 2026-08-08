import pandas as pd


def load_dataset(uploaded_file):
    """
    Load a CSV file into a Pandas DataFrame.

    Parameters:
        uploaded_file: Streamlit uploaded file object

    Returns:
        pd.DataFrame or None
    """

    try:
        df = pd.read_csv(uploaded_file)
        return df

    except Exception as error:
        raise ValueError(f"Error loading dataset: {error}")