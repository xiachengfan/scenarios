#!/bin/zsh

docker inspect my-nginx4 | grep "\"/var/www:/usr/share/nginx/html\""
