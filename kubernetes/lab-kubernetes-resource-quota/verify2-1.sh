#!/bin/zsh

minikube kubectl -- get namespaces | grep example-namespace
