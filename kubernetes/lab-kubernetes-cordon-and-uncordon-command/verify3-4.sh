#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube

POD=$(minikube kubectl --  get pods -l app=nginx -o jsonpath='{.items[0].metadata.name}')
echo "Pod名称：$POD"
if minikube kubectl --  wait --for=condition=ready pod/$POD --timeout=3m; then
  exit 0
else
  echo 1
fi