import sys

sys.path.append("/home/labex/project")

import os
import unittest
from file_search_engine import search_files_with_keyword


class TestFileSearchEngine(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir)

        self.file_1 = os.path.join(self.test_dir, "file1.txt")
        self.file_2 = os.path.join(self.test_dir, "file2.txt")
        self.file_3 = os.path.join(self.test_dir, "file3.txt")

        with open(self.file_1, "w") as f:
            f.write("This is a test file with the keyword Apple.")

        with open(self.file_2, "w") as f:
            f.write("This is another test file without any keyword.")

        with open(self.file_3, "w") as f:
            f.write("This file also contains the keyword apple.")

    def tearDown(self):
        os.remove(self.file_1)
        os.remove(self.file_2)
        os.remove(self.file_3)
        os.rmdir(self.test_dir)

    def test_search_files_with_keyword(self):
        keyword = "apple"
        matching_files = search_files_with_keyword(self.test_dir, keyword)
        expected_files = [self.file_1, self.file_3]
        self.assertEqual(set(matching_files), set(expected_files))


if __name__ == "__main__":
    unittest.main()
