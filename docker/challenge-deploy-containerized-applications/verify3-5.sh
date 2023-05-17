#!/bin/zsh

docker ps | grep python-volume
test -f "/home/labex/project/docker-volume/data/hello.txt"
