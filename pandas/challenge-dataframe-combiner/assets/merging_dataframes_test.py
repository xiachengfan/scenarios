import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch

from create_dataframe import create_dataframe
from merging_dataframes import merging_dataframes


class TestDataframeCombining(unittest.TestCase):
    def test_merging_dataframes(self):
        with patch(
            "joining_dataframes.create_dataframe",
            return_value=create_dataframe(["A", "B", "C"], 5),
        ):
            df_merge = merging_dataframes()
            self.assertEqual(df_merge.shape, (5, 7))
            self.assertTrue(
                set(df_merge.columns)
                == {"Key", "A_x", "B_x", "C_x", "A_y", "B_y", "C_y"}
            )


if __name__ == "__main__":
    unittest.main()
