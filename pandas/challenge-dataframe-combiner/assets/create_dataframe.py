import pandas as pd
import numpy as np


def create_dataframe(columns: list, rows: int) -> pd.DataFrame:
    """
    Create a DataFrame with the specified columns and rows filled with random integer values between 0 and 100.

    :param columns: List of column names for the DataFrame.
    :param rows: Number of rows in the DataFrame.
    :return: DataFrame with the specified columns and rows.
    """

    # TODO

    return


if __name__ == "__main__":
    columns = ["E", "X", "A", "M", "P", "L", "E"]
    rows = 3
    print(create_dataframe(columns, rows))
