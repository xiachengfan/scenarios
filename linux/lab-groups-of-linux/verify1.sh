#!/bin/zsh

cat ~/.zsh_history | grep -i "groups"
result=$?

if [ $result -eq 0 ]; then
  exit 0
else
  exit 1
fi
