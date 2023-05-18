#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep top | grep myapp-pod | grep namespace=default | grep 'containers=true' && minikube kubectl -- top pod myapp-pod --namespace=default --containers=true > /dev/null; then
  exit 0
else
  exit 1
fi
