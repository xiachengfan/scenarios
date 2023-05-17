import os
from collections import defaultdict
from typing import Dict, List


def find_duplicate_files(path: str) -> Dict[str, List[str]]:
    """Finds duplicate files in the given directory based on content.

    Args:
        path (str): The path of the directory.

    Returns:
        Dict[str, List[str]]: A dictionary with the hash of file content as keys and a list of file paths as values.
    """
    file_map = defaultdict(list)

    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            with open(file_path, "rb") as f:
                file_content = f.read()
            file_map[file_content].append(file_path)

    return {
        file_content: paths
        for file_content, paths in file_map.items()
        if len(paths) > 1
    }


def delete_files(file_paths: List[str]):
    """Deletes the files at the given paths.

    Args:
        file_paths (List[str]): A list of file paths to delete.
    """
    for path in file_paths:
        if os.path.exists(path):
            os.remove(path)


if __name__ == "__main__":
    directory_to_search = "test_example/find_duplicate_finder_example"
    duplicates = find_duplicate_files(directory_to_search)

    for _, file_paths in duplicates.items():
        for file_path in file_paths:
            print(f"{file_path}")
