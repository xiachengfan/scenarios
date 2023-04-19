#!/bin/bash

cat ~/.zsh_history | grep kubectl | |grep run|grep nginx-deployment
minikube kubectl -- get deployment |grep nginx-deployment