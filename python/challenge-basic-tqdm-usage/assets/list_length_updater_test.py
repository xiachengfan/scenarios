import unittest
import time
import sys

sys.path.append("/home/labex/project")

from list_length_updater import list_length_updater
from unittest.mock import patch
from io import StringIO


class TestProgressBarSolutions(unittest.TestCase):
    def test_list_length_updater(self):
        lst = [[1, 2], [3, 4], [5, 6, 7, 8, 9]]

        with patch("sys.stderr", new=StringIO()) as captured_output:
            list_length_updater(lst, 9)
            output = captured_output.getvalue()
        self.assertIn("9/9", output)
        self.assertIn("100%", output)


if __name__ == "__main__":
    unittest.main()
