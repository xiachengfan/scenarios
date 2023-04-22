#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 
minikube kubectl -- describe deployment containerprobe-deployment |grep containerprobe
cat /dev/null >  ~/.zsh_history