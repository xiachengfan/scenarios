#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep  -Eq create
kubectl get secrets -n mynamespace| grep myconfigmap