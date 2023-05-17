# Disk Space Analyzer

In this sub-challenge, you will create a disk space analyzer that scans a specified directory and calculates the total size of all files in that directory, including those in its subdirectories. The analyzer should also display the percentage of total disk space used by the specified directory.

## TODO:

1. Complete the `get_directory_size_and_disk_usage` function in `/home/labex/project/disk_space_analyzer.py` and implement a disk space analyser using the `os` module.
2. Calculate the total size of all files in the specified directory, including those in its subdirectories.

## Example Usage

There are files in the path `test_example/disk_space_analyzer_example`:

- `1.txt` 100MB,
- `2.txt` 200MB,
- `3.txt` 300MB.

When you have finished the experiment, run the script to obtain the following results:

```python
python disk_space_analyzer.py
```

Output:

```python
Total size: 629145600 bytes
Disk usage: 2.93%
```
