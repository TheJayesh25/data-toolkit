import pandas as pd

def memory_usage(df: pd.DataFrame):

    usage = df.memory_usage(deep=True)

    return usage.sort_values(ascending=False)