import re
from typing import Dict


def parse_config_file(config_contents: str) -> Dict[str, Dict[str, str]]:
    """
    Parse a configuration file and return the extracted key-value pairs as a dictionary.

    :param config_contents: A string representing the contents of a configuration file.
    :return: A dictionary containing the extracted key-value pairs.
    """
    config = {}
    current_section = None

    section_pattern = re.compile(r"\[(.+)\]")
    key_value_pattern = re.compile(r"([^=]+)=(.+)")

    for line in config_contents.splitlines():
        section_match = section_pattern.match(line.strip())
        key_value_match = key_value_pattern.match(line.strip())

        if section_match:
            current_section = section_match.group(1)
            config[current_section] = {}
        elif key_value_match and current_section is not None:
            key = key_value_match.group(1).strip()
            value = key_value_match.group(2).strip()
            config[current_section][key] = value

    return config


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
