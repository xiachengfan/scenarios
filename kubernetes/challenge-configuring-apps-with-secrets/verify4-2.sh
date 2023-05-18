#!/bin/zsh

minikube kubectl -- describe pod secret-pod | grep my-secret
