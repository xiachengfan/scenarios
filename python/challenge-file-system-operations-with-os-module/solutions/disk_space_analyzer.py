import os
from typing import Tuple


def get_directory_size_and_disk_usage(path: str) -> Tuple[int, float]:
    """Calculates the total size of all files in the directory and its disk usage percentage.

    Args:
        path (str): The path of the directory.

    Returns:
        Tuple[int, float]: A tuple containing the total size (in bytes) and the disk usage percentage.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    total_disk_space = os.statvfs(path).f_blocks * os.statvfs(path).f_frsize
    disk_usage_percentage = (total_size / total_disk_space) * 100

    return total_size, disk_usage_percentage


if __name__ == "__main__":
    directory_to_analyze = "test_example/disk_space_analyzer_example"
    size, usage = get_directory_size_and_disk_usage(directory_to_analyze)
    print(f"Total size: {size} bytes")
    print(f"Disk usage: {usage:.2f}%")
