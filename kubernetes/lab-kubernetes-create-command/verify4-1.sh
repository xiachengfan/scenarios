#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep  -Eq apply
kubectl get secrets -n mynamespace| grep mysecret