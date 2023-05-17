import re
from typing import Dict


def parse_config_file(config_contents: str) -> Dict[str, Dict[str, str]]:
    """
    Parse a configuration file and return the extracted key-value pairs as a dictionary.

    :param config_contents: A string representing the contents of a configuration file.
    :return: A dictionary containing the extracted key-value pairs.
    """
    # TODO: Write your code here
    # Note: Do not change the existing code


if __name__ == "__main__":
    sample_config = """
    [Application]
    name = MyApplication
    version = 2.0.1

    [Database]
    host = localhost
    port = 3306
    username = dbadmin
    password = mysecretpassword
    database = mydatabase
                    """
    print(parse_config_file(sample_config))
