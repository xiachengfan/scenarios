#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 
minikube kubectl -- describe pods pod-with-multiple-node-affinity |grep web |grep type |grep ssd |grep disktype