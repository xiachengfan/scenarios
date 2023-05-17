#!/bin/zsh

docker network ls | grep -E "my-network2\s+bridge"
