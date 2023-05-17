#!/bin/zsh
cat ~/.zsh_history | grep kubectl | grep apply
minikube kubectl -- get pod | grep "my-pod"
