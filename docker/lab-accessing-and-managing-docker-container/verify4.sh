#!/bin/bash
if history | grep -Eq 'docker logs my-shell-container'; then
  exit 0
else
  exit 1
fi
if docker ps -a | grep -Eq my-shell-container; then
  exit 1
else
  exit 0
fi