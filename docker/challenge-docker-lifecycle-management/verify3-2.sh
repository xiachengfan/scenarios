#!/bin/zsh

cat ~/.zsh_history | grep "docker.*stop"

test -z "$(docker ps | grep 'my-web-server.*8080.*my-web')"
