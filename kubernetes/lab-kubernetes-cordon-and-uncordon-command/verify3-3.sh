#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
sleep 60
minikube kubectl -- get pods | grep nginx | grep "Pending"
