#!/bin/zsh
echo '127.0.0.1 - - [10/May/2023:00:00:00 +0000] "GET /about.html HTTP/1.1" 200 2048 "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"' > project/sample_log.txt
echo '127.0.0.2 - - [10/May/2023:00:00:01 +0000] "POST /register HTTP/1.1" 500 4096 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"' >> project/sample_log.txt
echo 'This is a short text.' > project/sample_text.txt
