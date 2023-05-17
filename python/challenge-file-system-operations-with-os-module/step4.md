# File Search Engine

In this sub-challenge, you will create a file search engine that scans a specified directory and its subdirectories for files containing a given keyword. The search engine should be case-insensitive and display a list of matching files with their paths.

## TODO:

1. Complete the `search_files_with_keyword` function in `/home/labex/project/file_search_engine.py` and implement a file search engine using the `os` module.
2. Scan the specified directory and its subdirectories for files containing the given keyword (case-insensitive).

## Example Usage

The path `test_example/file_search_engine_example` contains the files `1.txt` containing "people", `2.txt` containing "PEOPLE" and `3.txt` containing "woman".

The key word is "people".

When you have finished the experiment, run the script to obtain the following results:

```python
python file_search_engine.py
```

Output:

```python
test_example/file_search_engine_example/1.txt
test_example/file_search_engine_example/2.txt
```
