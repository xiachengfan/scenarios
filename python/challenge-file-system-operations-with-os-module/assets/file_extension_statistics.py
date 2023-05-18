import os
from collections import Counter
from typing import Dict


def generate_file_extension_statistics(path: str) -> Dict[str, int]:
    """Generates file extension statistics for the given directory.

    Args:
        path (str): The path of the directory.

    Returns:
        Dict[str, int]: A dictionary with file extensions as keys and their counts as values.
    """

    # TODO: implement this function
    # Note: Do not change the existing code


if __name__ == "__main__":
    directory_to_scan = "test_example/file_extension_statistics_example"
    extension_statistics = generate_file_extension_statistics(directory_to_scan)

    for extension, count in extension_statistics.most_common():
        print(f"{extension}: {count}")
