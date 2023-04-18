#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep  -Eq apply
kubectl get deployments -n mynamespace| grep mydeployment