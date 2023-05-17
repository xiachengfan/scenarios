import unittest
import sys

sys.path.append("/home/labex/project")
from counting_occurrences import count_word_occurrences


class TestWordOccurrences(unittest.TestCase):
    def test_count_word_occurrences(self):
        with open("sample_text.txt", "w", encoding="utf-8") as sample_file:
            sample_file.write("This is a sample text file.\n")
            sample_file.write("This file contains some words.\n")
            sample_file.write("Words are repeated in this file.\n")

        expected_output = {
            "a": 1,
            "are": 1,
            "contains": 1,
            "file": 3,
            "in": 1,
            "is": 1,
            "repeated": 1,
            "sample": 1,
            "some": 1,
            "text": 1,
            "this": 3,
            "words": 2,
        }

        word_occurrences = count_word_occurrences("sample_text.txt")
        self.assertEqual(word_occurrences, expected_output)

    def test_empty_file(self):
        with open("empty_file.txt", "w", encoding="utf-8") as empty_file:
            empty_file.write("")

        expected_output = {}

        word_occurrences = count_word_occurrences("empty_file.txt")
        self.assertEqual(word_occurrences, expected_output)


if __name__ == "__main__":
    unittest.main()
