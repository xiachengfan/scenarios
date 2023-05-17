# Extracting Information from Configuration File

## Problem Statement

In this sub-challenge, you will create a Python function to extract key-value pairs from a configuration file. The configuration file uses the INI file format, with sections and key-value pairs separated by an equals sign. You will use regex to parse the configuration file and return the extracted information in dictionary.

## Requirements

1. Complete the `parse_config_file` function in `extracting_information.py`, which takes a string representing the contents of a configuration file and returns a dictionary containing the extracted key-value pairs.
2. Use `regex` to identify sections, keys, and values in the input string.
3. Store the extracted information in `dictionary`.
4. Test the function with a sample configuration file containing multiple sections and key-value pairs.

## Example

If you complete the `parse_config_file` function, open the terminal and input:

```shell
python extracting_information.py
```

Output:

```python
{
    'Application':
        {
        'name': 'MyApplication',
        'version': '2.0.1'
        },
    'Database':
        {'host': 'localhost', 'port': '3306', 'username': 'dbadmin', 'password': 'mysecretpassword', 'database': 'mydatabase'
        }
}
```
