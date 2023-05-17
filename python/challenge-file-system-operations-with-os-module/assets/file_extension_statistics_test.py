import sys

sys.path.append("/home/labex/project")

import os
import unittest
from file_extension_statistics import generate_file_extension_statistics


class TestFileExtensionStatistics(unittest.TestCase):
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
        os.remove(self.file_1)
        os.remove(self.file_2)
        os.remove(self.file_3)
        os.rmdir(self.test_dir)

    def test_generate_file_extension_statistics(self):
        extension_statistics = generate_file_extension_statistics(self.test_dir)
        expected_statistics = {".txt": 2, ".pdf": 1}
        self.assertEqual(extension_statistics, expected_statistics)


if __name__ == "__main__":
    unittest.main()
