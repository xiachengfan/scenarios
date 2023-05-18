#!/bin/zsh

docker ps | grep my-container
docker inspect my-container | grep myvolume
docker inspect my-container | grep "/app/data"
