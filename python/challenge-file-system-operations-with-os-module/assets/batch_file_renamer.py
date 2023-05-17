import os
from typing import Tuple
from typing import List


def batch_rename_files(path: str, old_ext: str, new_ext: str) -> Tuple[int, List[str]]:
    """Renames all files with the specified extension in the given directory to have a new extension.

    Args:
        path (str): The path of the directory.
        old_ext (str): The old file extension.
        new_ext (str): The new file extension.

    Returns:
        Tuple[int, List[str]]: The number of renamed files and a list of new file paths.
    """

    # TODO: implement this function
    # Note: Do not change the existing code


if __name__ == "__main__":
    directory_to_rename = "test_example/batch_file_renamer_example"
    old_extension = ".txt"
    new_extension = ".pdf"

    renamed_count, new_file_paths = batch_rename_files(
        directory_to_rename, old_extension, new_extension
    )

    print(f"Renamed {renamed_count} files:")
    for file_path in new_file_paths:
        print(file_path)
