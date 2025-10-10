import pandas as pd

def validate_schema(df: pd.DataFrame, expected_schema: dict):

    issues = []

    for col, dtype in expected_schema.items():

        if col not in df.columns:
            issues.append(f"Missing column: {col}")
            continue

        if str(df[col].dtype) != dtype:
            issues.append(
                f"{col} expected {dtype} but got {df[col].dtype}"
            )

    return issues