import pandas as pd

def column_summary(df: pd.DataFrame):

    summary = []

    for col in df.columns:
        summary.append({
            "column": col,
            "dtype": str(df[col].dtype),
            "missing": int(df[col].isna().sum()),
            "unique": int(df[col].nunique())
        })

    return pd.DataFrame(summary)