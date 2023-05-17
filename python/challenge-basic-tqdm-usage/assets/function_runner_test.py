import unittest
import time
import sys

sys.path.append("/home/labex/project")

from function_runner import function_runner
from unittest.mock import patch
from io import StringIO


class TestProgressBarSolutions(unittest.TestCase):
    def test_function_runner(self):
        def func1():
            time.sleep(0.5)

        def func2():
            time.sleep(0.8)

        with patch("sys.stderr", new=StringIO()) as captured_output:
            function_runner([func1, func2])
            output = captured_output.getvalue()
        self.assertIn("100%", output)


if __name__ == "__main__":
    unittest.main()
