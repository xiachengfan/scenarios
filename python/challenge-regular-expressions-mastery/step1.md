# Web Log Analysis

## Problem Statement

In this sub-challenge, you will analyze a web server log file to extract useful information about the visitors and their activities. You will use regex to parse the log entries and extract specific information.

## Requirements

1. Complete the `parse_log_file` function in `web_log_analysis.py`, which parses the log file into a list of strings, where each string represents a log entry.
2. Use regex to extract the following information from each log entry:
   a. IP address
   b. Timestamp
   c. HTTP method (GET, POST, etc.)
   d. Requested resource (URL)
   e. HTTP response status code
   f. User agent string
3. Complete the `analyze_log_entries` function in `web_log_analysis.py`, which stores the extracted information in dictionary.
4. Calculate and display the following statistics:
   a. Number of unique IP addresses
   b. Most common HTTP methods
   c. Most requested resources
   d. Distribution of response status codes
   e. Top user agents

## Example

We have a `sample_log.txt` file for you:

```txt
127.0.0.1 - - [10/May/2023:00:00:00 +0000] "GET /about.html HTTP/1.1" 200 2048 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"',
127.0.0.2 - - [10/May/2023:00:00:01 +0000] "POST /register HTTP/1.1" 500 4096 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

If you complete these two functions, open the terminal and input:

```shell
python web_log_analysis.py
```

Output:

```python
step1 = [
   '127.0.0.1 - - [10/May/2023:00:00:00 +0000] "GET /about.html HTTP/1.1" 200 2048 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"\n',
   '127.0.0.2 - - [10/May/2023:00:00:00 +0000] "POST /register HTTP/1.1" 500 4096 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"\n'
        ]

step2 = {
   'unique_ips': 2,
   'http_methods':
      {
         'GET': 1,
         'POST': 1
      },
   'requested_resources':
      {
         '/about.html': 1,
         '/register': 1
      },
   'status_codes':
      {
      '200': 1, '500': 1
      },
   'user_agents':
      {
         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko 20100101 Firefox/71.0': 1, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36': 1
      }
   }
```
