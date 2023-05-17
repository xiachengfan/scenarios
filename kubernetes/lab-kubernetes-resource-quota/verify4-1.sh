#!/bin/zsh

minikube kubectl -- describe resourcequota example-resourcequota | grep "cpu.*2"
minikube kubectl -- describe resourcequota example-resourcequota | grep "memory.*2Gi"
