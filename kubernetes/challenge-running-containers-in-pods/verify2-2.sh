#!/bin/zsh

minikube kubectl -- describe pod my-pod2 | grep my-container
minikube kubectl -- describe pod my-pod2 | grep my-sidecar
