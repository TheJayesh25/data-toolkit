import pandas as pd

def validate_range(df: pd.DataFrame, column, min_val=None, max_val=None):

    df = df.copy()

    if min_val is not None:
        df = df[df[column] >= min_val]

    if max_val is not None:
        df = df[df[column] <= max_val]

    return df