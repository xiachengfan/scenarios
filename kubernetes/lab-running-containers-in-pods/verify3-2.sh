#!/bin/zsh
minikube kubectl -- exec -it my-pod-3 -- env | grep Hello | grep World
