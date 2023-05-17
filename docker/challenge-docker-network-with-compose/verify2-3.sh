#!/bin/zsh

docker ps | grep nginx-container2
docker inspect nginx-container2 | grep my-network2
