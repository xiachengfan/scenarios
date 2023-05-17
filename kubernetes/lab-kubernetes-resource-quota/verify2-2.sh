#!/bin/zsh

minikube kubectl -- describe namespace example-namespace | grep example-resourcequota
