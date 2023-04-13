#!/bin/bash
history | grep "docker rm my-shell-container"
if docker ps -a | grep -q my-shell-container; then
  exit 1
else
  exit 0
fi