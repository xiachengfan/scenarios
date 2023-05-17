#!/bin/zsh

cat ~/.zsh_history | grep -E "docker\s+exec\s+-it\s+alpine-container2\s+ping\s+nginx-container2"
