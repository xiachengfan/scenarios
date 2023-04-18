#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep  -Eq apply
kubectl get services -n mynamespace| grep myservices