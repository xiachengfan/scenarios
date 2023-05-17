#!/bin/zsh

minikube kubectl -- describe limitrange example-limitrange | grep -E "cpu\s+100m\s+1\s+500m"
minikube kubectl -- describe limitrange example-limitrange | grep -E "memory\s+100Mi\s+1Gi\s+500Mi"
