#!/bin/zsh

docker ps | grep nginx-container
docker inspect nginx-container | grep my-network
