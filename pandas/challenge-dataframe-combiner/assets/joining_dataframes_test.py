import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch

from create_dataframe import create_dataframe
from joining_dataframes import joining_dataframes


class TestDataframeCombining(unittest.TestCase):
    def test_joining_dataframes(self):
        with patch(
            "joining_dataframes.create_dataframe",
            return_value=create_dataframe(["D", "E", "F"], 5),
        ):
            df_join = joining_dataframes()
            self.assertEqual(df_join.shape, (5, 6))
            self.assertTrue(
                set(df_join.columns)
                == {"D_left", "E_left", "F_left", "D_right", "E_right", "F_right"}
            )


if __name__ == "__main__":
    unittest.main()
