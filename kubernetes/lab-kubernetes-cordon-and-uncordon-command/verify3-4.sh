#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube
minikube kubectl -- get pods nginx-deployment |grep Runnig
