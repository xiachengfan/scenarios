import pandas as pd

from create_dataframe import create_dataframe


def joining_dataframes() -> pd.DataFrame:
    """
    Inner merge of two DataFrames by key.

    :return: Returns the DataFrame that was inner merged.
    """
    key = ["L1", "L2", "L3", "L4", "L5"]
    df5 = create_dataframe(["D", "E", "F"], 5)
    df6 = create_dataframe(["D", "E", "F"], 5)
    df5.index = key
    df6.index = key
    return df5.join(df6, lsuffix="_left", rsuffix="_right", how="outer")


if __name__ == "__main__":
    print(joining_dataframes())
