import unittest
import time
import sys

sys.path.append("/home/labex/project")

from range_progress import range_progress
from unittest.mock import patch
from io import StringIO


class TestProgressBarSolutions(unittest.TestCase):
    def test_range_progress(self):
        with patch("sys.stderr", new=StringIO()) as captured_output:
            range_progress(5)
            output = captured_output.getvalue()
        self.assertIn("100%", output)


if __name__ == "__main__":
    unittest.main()
