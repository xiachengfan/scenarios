#!/bin/zsh

minikube kubectl -- get resourcequotas | grep example-resourcequota
