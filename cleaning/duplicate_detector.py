import pandas as pd

def detect_duplicates(df: pd.DataFrame, subset=None):

    duplicates = df.duplicated(subset=subset)

    return df[duplicates]