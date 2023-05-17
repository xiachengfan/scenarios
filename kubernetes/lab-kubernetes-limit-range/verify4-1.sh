#!/bin/zsh

minikube kubectl -- describe limitrange example-limitrange | grep -E "cpu\s+200m\s+2\s+1"
minikube kubectl -- describe limitrange example-limitrange | grep -E "memory\s+200Mi\s+2Gi\s+1Gi"
