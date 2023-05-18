#!/bin/zsh

minikube kubectl -- describe deployment my-app | grep DATABASE_PASSWORD | grep my-secret
