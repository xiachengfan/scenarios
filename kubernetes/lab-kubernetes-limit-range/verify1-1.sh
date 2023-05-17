#!/bin/zsh

minikube kubectl -- get limitranges | grep example-limitrange
