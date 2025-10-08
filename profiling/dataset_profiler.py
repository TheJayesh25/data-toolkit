import pandas as pd

def profile_dataset(df: pd.DataFrame):

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict()
    }

    return profile