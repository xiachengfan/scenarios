#!/bin/zsh

cat ~/.zsh_history | grep "kubectl.*delete"

test -z "$(minikube kubectl -- get deployments | grep my-deployment)"
