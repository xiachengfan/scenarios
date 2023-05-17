#!/bin/zsh

cat ~/.zsh_history | grep "kubectl.*scale"

minikube kubectl -- get deployment my-deployment | grep 5
