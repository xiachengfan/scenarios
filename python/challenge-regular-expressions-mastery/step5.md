# Counting Occurrences of Words in Text File

## Problem Statement

In this sub-challenge, you will create a Python function to count the occurrences of each word in a given text file. The function should be case-insensitive and ignore punctuation marks. The output should be a dictionary with words as keys and their occurrences as values, sorted in descending order of occurrence.

## Requirements

1. Complete the `count_word_occurrences` function in `counting_occurrences.py`, which takes a file path as input and returns a dictionary containing the occurrences of each word in the text file.
2. Use `regex` to identify words in the input text file.
3. Count the occurrences of each word in a case-insensitive manner and ignore punctuation marks.
4. Sort the output dictionary in `descending order` of occurrence.
5. Test the function with a sample text file containing multiple lines and varying capitalization.

## Example

We have a `sample_text.txt` file for you:

```txt
This is a short text.
```

If you complete the `count_word_occurrences` function, open the terminal and input:

```shell
python counting_occurrences.py
```

Output:

```python
{
    'this': 1,
    'is': 1,
    'a': 1,
    'short': 1,
    'text': 1
}
```
