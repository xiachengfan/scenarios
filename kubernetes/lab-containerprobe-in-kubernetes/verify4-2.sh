#!/bin/bash


if cat ~/.zsh_history | grep kubectl |grep apply > /dev/null&& minikube kubectl -- describe deployment containerprobe-deployment |grep -q "Readiness";then
  history -c
  exit 0
else
  exit 1
  fi