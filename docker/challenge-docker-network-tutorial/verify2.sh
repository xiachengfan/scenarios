#!/bin/zsh

docker ps | grep container1
docker ps | grep container2

docker inspect container1 | grep my-network
docker inspect container2 | grep my-network
