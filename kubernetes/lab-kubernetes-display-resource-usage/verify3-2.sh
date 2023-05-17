#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep apply && minikube kubectl -- describe pods myapp-pod | grep myapp-container > /dev/null; then
  exit 0
else
  exit 1
fi
