# Batch File Renamer

In this sub-challenge, you will create a batch file renamer that scans a specified directory (not including its subdirectories) and renames all files with a specified extension to have a new extension. The batch file renamer should be case-insensitive when matching file extensions.

## TODO:

1. Complete the `batch_rename_files` function in `/home/labex/project/batch_file_renamer.py` and implement a batch file renamer using the `os` module.
2. Scan the specified directory (excluding its subdirectories) for files with the specified extension (case-insensitive).
3. Rename all matching files to have the new extension.

## Example Usage

The path `test_example/batch_file_renamer_example` contains a file named `1.txt`.

The old extension is ".txt" and the new extension is ".pdf".

When you have finished the experiment, run the script to obtain the following results:

```python
python batch_file_renamer.py
```

Output:

```python
Renamed 1 files:
test_example/batch_file_renamer_example/1.pdf
```
