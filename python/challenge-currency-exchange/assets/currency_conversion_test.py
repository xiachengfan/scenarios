import sys

sys.path.append("/home/labex/project")
import unittest
from currency_conversion import currency_conversion


class TestCurrencyConverter(unittest.TestCase):
    def test_conversion(self):
        self.assertAlmostEqual(
            currency_conversion("eur", "gbp", 100), 88.532, delta=0.01
        )
        self.assertAlmostEqual(
            currency_conversion("eur", "cny", 100), 761.402, delta=0.01
        )

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            currency_conversion("ABC", "eur", 100)

        with self.assertRaises(ValueError):
            currency_conversion("eur", "XYZ", 100)


if __name__ == "__main__":
    unittest.main()
