import re
from collections import Counter
from typing import Dict


def count_word_occurrences(file_path: str) -> Dict[str, int]:
    """
    Count the occurrences of each word in the given text file.

    :param file_path: The path to the text file.
    :return: A dictionary containing the occurrences of each word, sorted in descending order of occurrence.
    """
    word_pattern = re.compile(r"\b\w+\b")

    with open(file_path, "r", encoding="utf-8") as text_file:
        text = text_file.read()

    words = [word_match.group(0).lower() for word_match in word_pattern.finditer(text)]
    word_occurrences = dict(Counter(words).most_common())

    return word_occurrences


if __name__ == "__main__":
    print(count_word_occurrences("sample_text.txt"))
