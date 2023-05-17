#!/bin/zsh

docker images | grep python-volume
docker inspect python-volume | grep /data
