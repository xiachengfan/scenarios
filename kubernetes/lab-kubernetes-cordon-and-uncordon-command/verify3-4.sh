#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube

sleep 120
minikube kubectl -- get pods | grep nginx |grep  Running