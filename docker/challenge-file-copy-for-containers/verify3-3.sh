#!/bin/zsh

test ! -z "$(docker exec my_container3 ls /tmp/labexx/ | grep file1)"
test ! -z "$(docker exec my_container3 ls /tmp/labexx/ | grep file2)"
