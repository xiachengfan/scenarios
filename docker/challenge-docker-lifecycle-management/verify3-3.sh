#!/bin/zsh

cat ~/.zsh_history | grep "docker.*rm"

test -z "$(docker ps -a | grep 'my-web-server.*my-web')"
