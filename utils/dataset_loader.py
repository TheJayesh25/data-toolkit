import pandas as pd

def load_dataset(path):

    if path.endswith(".csv"):
        return pd.read_csv(path)

    if path.endswith(".parquet"):
        return pd.read_parquet(path)

    if path.endswith(".json"):
        return pd.read_json(path)

    raise ValueError("Unsupported file format")