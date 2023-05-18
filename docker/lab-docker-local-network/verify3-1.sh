#!/bin/zsh

docker ps | grep container5

docker inspect container5 | grep "none"
