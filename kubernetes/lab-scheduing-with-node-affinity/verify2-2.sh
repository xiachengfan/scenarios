#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
minikube kubectl -- describe pod-with-node-affinity |grep affinity |grep matchExpressions |grep In