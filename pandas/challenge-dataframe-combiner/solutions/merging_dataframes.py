import pandas as pd

from create_dataframe import create_dataframe


def merging_dataframes() -> pd.DataFrame:
    """
    Outer merge of two DataFrames by key.

    :return: Returns the DataFrame that was outer merged.
    """
    key = ["K1", "K2", "K3", "K4", "K5"]
    df3 = create_dataframe(["A", "B", "C"], 5)
    df4 = create_dataframe(["A", "B", "C"], 5)
    df3["Key"] = key
    df4["Key"] = key
    return pd.merge(df3, df4, on="Key")


if __name__ == "__main__":
    print(merging_dataframes())
