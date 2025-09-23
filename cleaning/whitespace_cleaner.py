import pandas as pd

def strip_whitespace(df: pd.DataFrame):

    df = df.copy()

    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    return df