#!/bin/bash

minikube kubectl -- describe daemonset myapp-daemonset |grep busybox
cat ~/.zsh_history | grep kubectl |grep pod|grep app=myapp 

cat /dev/null >  ~/.zsh_history