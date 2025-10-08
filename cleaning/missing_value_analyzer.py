import pandas as pd

def missing_summary(df: pd.DataFrame):

    missing = df.isna().sum()
    percent = (missing / len(df)) * 100

    return pd.DataFrame({
        "missing_count": missing,
        "missing_percent": percent
    }).sort_values("missing_percent", ascending=False)