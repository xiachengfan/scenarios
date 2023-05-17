#!/bin/zsh

test ! -z "$(docker exec my_container2 ls /tmp/labex/ | grep file1)"
test ! -z "$(docker exec my_container2 ls /tmp/labex/ | grep file2)"
