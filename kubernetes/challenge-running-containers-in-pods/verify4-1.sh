#!/bin/zsh

minikube kubectl -- get configmaps | grep my-config
