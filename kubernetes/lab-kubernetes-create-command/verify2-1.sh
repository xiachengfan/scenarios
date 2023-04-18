#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep  -Eq create
kubectl get deployments -n mynamespace| grep mydeployment