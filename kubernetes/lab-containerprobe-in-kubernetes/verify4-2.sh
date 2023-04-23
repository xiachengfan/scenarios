#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply

if minikube kubectl -- describe deployment containerprobe-deployment |grep -q "Readiness";then
  history -c
  exit 0
else
  exit 1
  fi