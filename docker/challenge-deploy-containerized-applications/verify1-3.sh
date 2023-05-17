#!/bin/zsh

docker images | grep hello-world
docker inspect hello-world | grep Hello
