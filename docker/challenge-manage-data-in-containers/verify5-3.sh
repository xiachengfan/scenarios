#!/bin/zsh

sudo cp /var/lib/docker/volumes/mynewvolume/_data/hello.txt /home/labex/hello_new.txt
FILE2=/home/labex/hello_new.txt
[ -f "$FILE2" ]
