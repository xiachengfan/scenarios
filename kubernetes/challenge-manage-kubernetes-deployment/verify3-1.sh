#!/bin/zsh

cat ~/.zsh_history | grep "kubectl.*edit"

minikube kubectl -- describe deployment my-deployment | grep "nginx:1.19"
