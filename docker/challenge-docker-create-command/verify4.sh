#!/bin/zsh

docker inspect my-nginx3 | grep "\"NGINX_HOST=example.com\","
