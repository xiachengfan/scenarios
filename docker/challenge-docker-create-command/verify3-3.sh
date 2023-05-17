#!/bin/zsh

docker inspect my-nginx2 | grep "\"HostPort\": \"8080\""
