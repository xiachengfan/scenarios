#!/bin/zsh

minikube kubectl -- get deployments | grep simple-deployment
