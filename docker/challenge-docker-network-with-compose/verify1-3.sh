#!/bin/zsh

docker ps | grep alpine-container
docker inspect alpine-container | grep my-network
