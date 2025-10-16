import pandas as pd

def dataframe_summary(df: pd.DataFrame):

    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing": df.isna().sum().to_dict()
    }