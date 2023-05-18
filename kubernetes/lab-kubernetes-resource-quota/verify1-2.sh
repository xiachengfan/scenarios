#!/bin/zsh

minikube kubectl -- describe resourcequota example-resourcequota | grep "cpu.*1"
minikube kubectl -- describe resourcequota example-resourcequota | grep "memory.*1Gi"
