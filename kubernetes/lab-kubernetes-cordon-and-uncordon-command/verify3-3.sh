#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply

POD=$(kubectl get pods -l app=nginx -o jsonpath='{.items[0].metadata.name}')

if kubectl wait --for=condition=ready pod/$POD --timeout=2m; then
  exit 1
else
  echo 0
fi