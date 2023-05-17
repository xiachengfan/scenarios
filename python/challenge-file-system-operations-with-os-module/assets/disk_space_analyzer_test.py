import sys

sys.path.append("/home/labex/project")

import os
import unittest
from disk_space_analyzer import get_directory_size_and_disk_usage


class TestDiskSpaceAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir)

        self.file_1 = os.path.join(self.test_dir, "file1.txt")
        self.file_2 = os.path.join(self.test_dir, "file2.txt")
        self.file_1_size = 100 * 1024 * 1024
        self.file_2_size = 300 * 1024 * 1024

        with open(self.file_1, "wb") as f:
            f.write(os.urandom(self.file_1_size))

        with open(self.file_2, "wb") as f:
            f.write(os.urandom(self.file_2_size))

    def tearDown(self):
        os.remove(self.file_1)
        os.remove(self.file_2)
        os.rmdir(self.test_dir)

    def test_get_directory_size_and_disk_usage(self):
        size, usage = get_directory_size_and_disk_usage(self.test_dir)
        expected_size = os.path.getsize(self.file_1) + os.path.getsize(self.file_2)
        total_disk_space = (
            os.statvfs(self.test_dir).f_blocks * os.statvfs(self.test_dir).f_frsize
        )
        expected_usage = (expected_size / total_disk_space) * 100
        self.assertAlmostEqual(usage, expected_usage, places=4)
        self.assertEqual(size, expected_size)


if __name__ == "__main__":
    unittest.main()
