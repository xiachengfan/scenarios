#!/bin/zsh

docker ps | grep alpine-container2
docker inspect alpine-container2 | grep my-network2
