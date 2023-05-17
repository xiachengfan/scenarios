#!/bin/zsh

minikube kubectl -- get pods | grep my-pod
minikube kubectl -- describe pod my-pod | grep my-container
