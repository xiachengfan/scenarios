#!/bin/zsh

minikube kubectl -- get deployments | grep selector-deployment
