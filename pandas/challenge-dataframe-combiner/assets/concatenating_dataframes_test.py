import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
from unittest.mock import patch

from create_dataframe import create_dataframe
from concatenating_dataframes import concatenating_dataframes


class TestDataframeCombining(unittest.TestCase):
    def test_concatenating_dataframes(self):
        with patch(
            "concatenating_dataframes.create_dataframe",
            return_value=create_dataframe(["A", "B", "C"], 5),
        ):
            df_concat = concatenating_dataframes()
            self.assertEqual(df_concat.shape, (10, 3))
            self.assertTrue(set(df_concat.columns) == {"A", "B", "C"})


if __name__ == "__main__":
    unittest.main()
