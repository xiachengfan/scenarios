#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply

if minikube kubectl -- describe deployment containerprobe-deployment |grep -q "Readiness";then
  exit 0
  history -c
else
  exit 1
  fi