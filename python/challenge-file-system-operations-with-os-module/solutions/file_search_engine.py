import os
from typing import List


def search_files_with_keyword(path: str, keyword: str) -> List[str]:
    """Searches files containing the given keyword in the specified directory and its subdirectories.

    Args:
        path (str): The path of the directory.
        keyword (str): The keyword to search for.

    Returns:
        List[str]: A list of matching file paths.
    """
    matching_files = []

    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "r", errors="ignore") as file:
                content = file.read().lower()
                if keyword.lower() in content:
                    matching_files.append(file_path)

    return matching_files


if __name__ == "__main__":
    directory_to_search = "test_example/file_search_engine_example"
    search_keyword = "people"
    matching_files = search_files_with_keyword(directory_to_search, search_keyword)

    for file_path in matching_files:
        print(file_path)
