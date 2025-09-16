import pandas as pd

def profile_dataset(df: pd.DataFrame):

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "dtypes": df.dtypes.astype(str).to_dict()
    }