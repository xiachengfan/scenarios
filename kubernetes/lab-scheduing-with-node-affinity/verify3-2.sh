#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
minikube kubectl -- describe pods pod-with-node-affinity |grep affinity |grep matchExpressions |grep NotIn
