#!/bin/zsh

minikube kubectl -- get deployments | grep multi-selector-deployment
