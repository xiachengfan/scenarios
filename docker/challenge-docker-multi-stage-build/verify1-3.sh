#!/bin/zsh

test -f "/home/labex/myapp/Dockerfile"
cat /home/labex/myapp/Dockerfile | grep node:14-alpine
cat /home/labex/myapp/Dockerfile | grep RUN
cat /home/labex/myapp/Dockerfile | grep COPY
cat /home/labex/myapp/Dockerfile | grep 3000
cat /home/labex/myapp/Dockerfile | grep WORKDIR
cat /home/labex/myapp/Dockerfile | grep EXPOSE
cat /home/labex/myapp/Dockerfile | grep CMD
