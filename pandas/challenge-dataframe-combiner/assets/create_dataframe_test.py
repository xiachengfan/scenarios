import sys

sys.path.append("/home/labex/project")

import unittest
from pandas.testing import assert_frame_equal

from create_dataframe import create_dataframe


class TestDataframeCombining(unittest.TestCase):
    def test_create_dataframe(self):
        columns = ["A", "B", "C"]
        rows = 5
        df_a = create_dataframe(columns, rows)
        df_b = create_dataframe(columns, rows)

        self.assertEqual(list(df_a.columns), columns)
        self.assertEqual(df_a.shape, (rows, len(columns)))

        with self.assertRaises(AssertionError):
            assert_frame_equal(df_a, df_b)


if __name__ == "__main__":
    unittest.main()
