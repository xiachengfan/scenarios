#!/bin/zsh

cat ~/.zsh_history | grep -E "docker\s+exec\s+-it\s+alpine-container\s+ping\s+nginx-container"
