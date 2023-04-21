#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube

minikube kubectl -- get pods nginx |grep Running

cat /dev/null >  ~/.zsh_history