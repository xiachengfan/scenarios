# Extracting URLs from web page

## Problem Statement

In this sub-challenge, you will create a Python function to extract all the URLs from an HTML web page. The function should return a list of unique URLs found on the web page. You will use regex to identify the URLs in the input HTML string.

## Requirements

1. Complete the `extract_urls` function in `extracting_url.py`, which takes an HTML string as input and returns a list of unique URLs found in the web page.
2. Use regex to identify URLs in the input HTML string.
3. Filter out duplicate URLs.
4. Test the function with a sample HTML string containing multiple URLs in various HTML tags.

## Example

If you complete the `extract_urls` function, open the terminal and input:

```shell
python extracting_url.py
```

Output:

```python
[
    'https://www.google.com/',
    'https://www.apple.com/',
    'https://www.amazon.com/'
]
```
