#!/bin/zsh

minikube kubectl -- describe pod my-pod4 | grep my-config
