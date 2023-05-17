#!/bin/zsh

minikube kubectl -- describe pod my-pod3 | grep -E 'MY_ENV_VAR.*Hello\s+World!'
