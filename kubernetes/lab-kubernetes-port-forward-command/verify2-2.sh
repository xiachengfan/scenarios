#!/bin/bash

minikube kubectl -- describe daemonset myapp-daemonset |grep busybox
cat ~/.zsh_history | grep kubectl | |grep pod|grep app=myapp 
sudo test -f /home/labex/myapp-daemonset-update.yaml
minikube start