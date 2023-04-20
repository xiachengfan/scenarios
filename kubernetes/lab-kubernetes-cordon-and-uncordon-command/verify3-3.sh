#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
minikube kubectl -- get pods | grep nginx | grep "Pending"
