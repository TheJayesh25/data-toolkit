import pandas as pd

def validate_schema(df: pd.DataFrame, expected_columns):

    missing = []

    for col in expected_columns:
        if col not in df.columns:
            missing.append(col)

    return missing