#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 

minikube kubectl -- describe deployment nginx-deployment

# if minikube kubectl -- get pods nginx-deployment |grep Pending;then
#     exit 0
# else
#     minikube kubectl -- delete deployment nginx-deployment
#     exit 1
#   fi