import sys

sys.path.append("/home/labex/project")
import unittest
from get_exchange_rate import get_exchange_rate


class TestGetExchangeRate(unittest.TestCase):
    def test_exchange_rate(self):
        self.assertAlmostEqual(
            get_exchange_rate("eur", "gbp"), 0.8853203819163821, delta=0.01
        )
        self.assertAlmostEqual(
            get_exchange_rate("eur", "cny"), 7.614026735873045, delta=0.01
        )

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            get_exchange_rate("ABC", "eur")

        with self.assertRaises(ValueError):
            get_exchange_rate("eur", "XYZ")


if __name__ == "__main__":
    unittest.main()
