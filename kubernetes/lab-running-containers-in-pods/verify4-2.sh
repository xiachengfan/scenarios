#!/bin/zsh
minikube kubectl -- exec -it my-pod-4 -- env | grep labex
