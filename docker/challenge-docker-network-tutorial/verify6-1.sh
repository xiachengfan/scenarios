#!/bin/zsh

test -z "$(docker network ls | grep my-network2)"
