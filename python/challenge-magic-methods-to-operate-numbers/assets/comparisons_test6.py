import unittest
import sys

sys.path.append("/home/labex/project")

from comparisons import MathExpression


class TestMathExpression(unittest.TestCase):
    def test_ge(self):
        a = MathExpression(5)
        b = MathExpression(5)
        c = MathExpression(3)
        self.assertTrue(a >= b)
        self.assertTrue(a >= c)


if __name__ == "__main__":
    unittest.main()
