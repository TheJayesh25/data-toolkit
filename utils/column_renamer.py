import pandas as pd

def standardize_columns(df: pd.DataFrame):

    df = df.copy()

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df