#!/bin/zsh

minikube kubectl -- get pvc | grep my-pvc | grep 1Gi
