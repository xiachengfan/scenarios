#!/bin/zsh

docker inspect my-nginx2 | grep "\"80/tcp\""
