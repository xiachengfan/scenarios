#!/bin/bash

if minikube kubectl -- get pods -n kube-system | grep metrics-server | grep Running > /dev/null && cat ~/.zsh_history | grep kubectl | grep top | grep pods | grep namespace=kube-system; then
  exit 0
else
  exit 1
fi
