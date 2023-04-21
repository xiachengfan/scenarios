#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 

minikube kubectl -- describe pods myapp-pod |grep myapp-container

