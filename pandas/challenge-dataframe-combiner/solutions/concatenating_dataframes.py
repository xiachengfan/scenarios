import pandas as pd
from create_dataframe import create_dataframe


def concatenating_dataframes() -> pd.DataFrame:
    """
    Concatenate two DataFrame with 3 columns `('A', 'B', 'C')` and `5` rows of random integers.

    :return: The DataFrame after being concatenated.
    """
    columns = ["A", "B", "C"]
    df1 = create_dataframe(columns, 5)
    df2 = create_dataframe(columns, 5)
    return pd.concat([df1, df2], axis=0)


if __name__ == "__main__":
    print(concatenating_dataframes())
