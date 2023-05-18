#!/bin/zsh

sudo cp /var/lib/docker/volumes/myvolume/_data/hello.txt /home/labex/hello.txt
FILE=/home/labex/hello.txt
[ -f "$FILE" ]
