#!/bin/bash
if cat ~/.zsh_history | grep kubectl | grep top | grep nodes && minikube kubectl top nodes; then
  exit 0
else
  exit 1
fi
