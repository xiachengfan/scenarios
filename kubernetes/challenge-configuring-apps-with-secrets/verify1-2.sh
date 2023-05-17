#!/bin/zsh

minikube kubectl -- get secrets | grep my-secret | grep Opaque
