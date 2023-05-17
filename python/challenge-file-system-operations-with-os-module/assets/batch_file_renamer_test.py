import sys

sys.path.append("/home/labex/project")

import os
import unittest
from batch_file_renamer import batch_rename_files


class TestBatchFileRenamer(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir)

        self.file_1 = os.path.join(self.test_dir, "file1.txt")
        self.file_2 = os.path.join(self.test_dir, "file2.txt")
        self.file_3 = os.path.join(self.test_dir, "file3.pdf")

        with open(self.file_1, "w") as f:
            f.write("This is a test file.")

        with open(self.file_2, "w") as f:
            f.write("This is another test file.")

        with open(self.file_3, "w") as f:
            f.write("This is a PDF file.")

    def tearDown(self):
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)

    def test_batch_rename_files(self):
        old_ext = ".txt"
        new_ext = ".md"
        renamed_count, new_file_paths = batch_rename_files(
            self.test_dir, old_ext, new_ext
        )

        expected_files = [
            os.path.join(self.test_dir, "file1.md"),
            os.path.join(self.test_dir, "file2.md"),
        ]
        self.assertEqual(renamed_count, 2)
        self.assertEqual(set(new_file_paths), set(expected_files))


if __name__ == "__main__":
    unittest.main()
