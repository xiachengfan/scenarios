#!/bin/zsh

cat /home/labex/.zsh_history | grep -E "docker search --filter ('is-official=true'|\"is-official=true\") nginx"
