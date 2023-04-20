#!/bin/bash

# minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+true'

if minikube kubectl -- get pods nginx-deployment |grep Pending;then
    exit 0
else
    minikube kubectl -- delete deployment nginx-deployment
    exit 1
  fi