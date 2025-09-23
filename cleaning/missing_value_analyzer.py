import pandas as pd

def missing_summary(df: pd.DataFrame):

    missing = df.isna().sum()

    return pd.DataFrame({
        "missing_count": missing
    })