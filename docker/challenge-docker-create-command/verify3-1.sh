#!/bin/zsh

docker inspect my-nginx2 && docker inspect my-nginx2 | grep -v "\"PortBindings\": {},"
