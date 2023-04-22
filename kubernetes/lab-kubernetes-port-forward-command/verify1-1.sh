#!/bin/bash

cat ~/.zsh_history | grep kubectl|grep create
minikube kubectl -- get pods |grep nginx