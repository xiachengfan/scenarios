#!/bin/zsh

cat ~/.zsh_history | grep "kubectl.*rollout.*undo"

minikube kubectl -- describe deployment my-deployment | grep "nginx:latest"
