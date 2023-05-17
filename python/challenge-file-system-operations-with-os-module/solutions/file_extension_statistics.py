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
    extension_counter = Counter()

    for _, _, filenames in os.walk(path):
        for filename in filenames:
            _, extension = os.path.splitext(filename)
            extension_counter[extension.lower()] += 1

    return dict(extension_counter)


if __name__ == "__main__":
    directory_to_scan = "test_example/file_extension_statistics_example"
    extension_statistics = generate_file_extension_statistics(directory_to_scan)

    for extension, count in extension_statistics.items():
        print(f"{extension}: {count}")
