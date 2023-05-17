#!/bin/zsh

docker ps | grep container3
docker ps | grep container4

docker inspect container3 | grep host
docker inspect container4 | grep host
