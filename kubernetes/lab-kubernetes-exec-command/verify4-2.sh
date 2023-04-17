#!/bin/bash
minikube kubectl -- get pod | grep "nginx"|grep "MY_VAR=my-value"
cat ~/.zsh_history |grep kubectl | grep pod | grep nginx | grep  -Eq exec