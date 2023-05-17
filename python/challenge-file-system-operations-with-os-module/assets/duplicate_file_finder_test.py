import sys

sys.path.append("/home/labex/project")

import os
import unittest
from duplicate_file_finder import find_duplicate_files, delete_files


class TestDuplicateFileFinder(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir)

        self.file_1 = os.path.join(self.test_dir, "file1.txt")
        self.file_2 = os.path.join(self.test_dir, "file2.txt")
        self.file_3 = os.path.join(self.test_dir, "file3.txt")

        with open(self.file_1, "w") as f:
            f.write("This is a test file.")

        with open(self.file_2, "w") as f:
            f.write("This is a test file.")

        with open(self.file_3, "w") as f:
            f.write("This is another test file.")

    def tearDown(self):
        if os.path.exists(self.file_1):
            os.remove(self.file_1)
        if os.path.exists(self.file_2):
            os.remove(self.file_2)
        if os.path.exists(self.file_3):
            os.remove(self.file_3)
        os.rmdir(self.test_dir)

    def test_find_and_delete_duplicate_files(self):
        duplicates = find_duplicate_files(self.test_dir)
        file_paths = list(duplicates.values())[0]
        self.assertEqual(len(file_paths), 2)
        delete_files(file_paths)
        self.assertFalse(os.path.exists(self.file_1))
        self.assertFalse(os.path.exists(self.file_2))


if __name__ == "__main__":
    unittest.main()
