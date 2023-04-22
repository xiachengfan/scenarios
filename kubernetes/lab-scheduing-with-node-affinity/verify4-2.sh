#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 
minikube kubectl -- describe pods pod-with-node-affinity-and-selector |grep web |grep type |grep nodeSelector