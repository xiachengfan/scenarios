#!/bin/zsh

test ! -z "$(docker exec my_container ls /tmp/ | grep file.txt)"
