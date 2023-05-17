import re
from typing import List


def is_password_valid(password: str) -> bool:
    """
    Check if the given password is valid according to the defined criteria.

    :param password: The input password to be checked.
    :return: A boolean value indicating if the password is valid or not.
    """
    if len(password) < 12:
        return False

    lowercase = re.compile(r"[a-z]")
    uppercase = re.compile(r"[A-Z]")
    digit = re.compile(r"\d")
    special_char = re.compile(r"[!@#$%^&*()]")

    if not (
        lowercase.search(password)
        and uppercase.search(password)
        and digit.search(password)
        and special_char.search(password)
    ):
        return False

    return True


if __name__ == "__main__":
    password_1 = "MyPassword123!"
    password_2 = "mypassword"

    print(is_password_valid(password_1))
    print(is_password_valid(password_2))
