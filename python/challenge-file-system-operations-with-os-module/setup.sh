#!/bin/zsh

mkdir -p /home/labex/project/test_example/disk_space_analyzer_example
mkdir -p /home/labex/project/test_example/find_duplicate_finder_example
mkdir -p /home/labex/project/test_example/file_extension_statistics_example
mkdir -p /home/labex/project/test_example/file_search_engine_example
mkdir -p /home/labex/project/test_example/batch_file_renamer_example

cd /home/labex/project/test_example/disk_space_analyzer_example
truncate -s 100M 1.txt
truncate -s 200M 2.txt
truncate -s 300M 3.txt

cd /home/labex/project/test_example/find_duplicate_finder_example
echo "1" > 1.txt
echo "1" > 2.txt
echo "2" > 3.txt

cd /home/labex/project/test_example/file_extension_statistics_example
echo "This is a test file." > 1.txt
touch 2.pdf

cd /home/labex/project/test_example/file_search_engine_example
echo "people" > 1.txt
echo "PEOPLE" > 2.txt
echo "woman" > 3.txt

cd /home/labex/project/test_example/batch_file_renamer_example
touch 1.txt
