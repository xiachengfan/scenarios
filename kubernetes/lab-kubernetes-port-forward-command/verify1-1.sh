#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep create >/dev/null && minikube kubectl -- get pods | grep nginx; then
  exit 0
else
  exit 1
fi
