# Duplicate File Finder

In this sub-challenge, you will create a duplicate file finder that scans a specified directory for duplicate files. The finder should compare files based on their content, not their names. It should display a list of duplicate files with their paths.

## TODO:

1.Complete the `find_duplicate_files` and `delete_files` functions in `/home/labex/project/find_duplicate_finder.py` and implement a duplicate file finder using the `os` module. 2. Scans for duplicate files in a specified directory, compares them based on content, and removes the duplicates (leaving the original files intact).

## Example Usage

The path `test_example/find_duplicate_finder_example` has three files, `1.txt` and `2.txt` have exactly the same content with "1", and `3.txt` has "2".

When you have finished the experiment, run the script to obtain the following results:

```python
python find_duplicate_finder.py
```

Output:

```python
test_example/find_duplicate_finder_example/1.txt
test_example/find_duplicate_finder_example/2.txt
```

The `delete_files` function does not return a value, but directly modifies the file system to delete the specified file.
