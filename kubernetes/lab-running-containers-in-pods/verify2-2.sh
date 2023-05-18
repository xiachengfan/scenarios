#!/bin/zsh
minikube kubectl -- get pod | grep "my-pod-2" | grep 2/2
