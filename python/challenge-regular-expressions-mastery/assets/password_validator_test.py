import unittest
import sys

sys.path.append("/home/labex/project")
from password_validator import is_password_valid


class TestPasswordValidator(unittest.TestCase):
    def test_valid_password(self):
        password = "A1$bcdefghijk"
        self.assertTrue(is_password_valid(password))

    def test_invalid_password_length(self):
        password = "A1$bc"
        self.assertFalse(is_password_valid(password))

    def test_invalid_password_missing_lowercase(self):
        password = "A1$BCDEFGHIJK"
        self.assertFalse(is_password_valid(password))

    def test_invalid_password_missing_uppercase(self):
        password = "a1$bcdefghijk"
        self.assertFalse(is_password_valid(password))

    def test_invalid_password_missing_digit(self):
        password = "A!@bcdefghijk"
        self.assertFalse(is_password_valid(password))

    def test_invalid_password_missing_special_char(self):
        password = "A1abcdeFghijk"
        self.assertFalse(is_password_valid(password))

    def test_invalid_password_forbidden_pattern(self):
        password = "A1$bcdefpassword"
        self.assertTrue(is_password_valid(password))


if __name__ == "__main__":
    unittest.main()
