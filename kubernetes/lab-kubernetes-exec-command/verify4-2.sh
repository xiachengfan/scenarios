#!/bin/bash
minikube kubectl -- get describe pod nginx-env |grep MY_VAR |grep my-value
cat ~/.zsh_history |grep kubectl | grep pod | grep nginx-env| grep c | grep  -Eq exec