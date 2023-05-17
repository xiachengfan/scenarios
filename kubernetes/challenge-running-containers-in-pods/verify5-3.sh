#!/bin/zsh

minikube kubectl -- describe pod my-pod5 | grep /mnt/data
minikube kubectl -- describe pod my-pod5 | grep my-pvc
