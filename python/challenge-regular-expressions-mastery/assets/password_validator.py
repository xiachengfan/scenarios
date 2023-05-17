import re
from typing import List


def is_password_valid(password: str) -> bool:
    """
    Check if the given password is valid according to the defined criteria.

    :param password: The input password to be checked.
    :return: A boolean value indicating if the password is valid or not.
    """
    # TODO: Write your code here
    # Note: Do not change the existing code


if __name__ == "__main__":
    password_1 = "MyPassword123!"
    password_2 = "mypassword"

    print(is_password_valid(password_1))
    print(is_password_valid(password_2))
