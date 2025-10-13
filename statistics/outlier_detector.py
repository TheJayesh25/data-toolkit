import pandas as pd
import numpy as np

def detect_outliers(df: pd.DataFrame, column, method="iqr"):

    if method == "iqr":

        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        return df[(df[column] < lower) | (df[column] > upper)]

    if method == "zscore":

        z = np.abs((df[column] - df[column].mean()) / df[column].std())
        return df[z > 3]