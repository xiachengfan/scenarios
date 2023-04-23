#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep top|grep pods  |grep namespace=kube-system

cat ~/.zsh_history | grep kubectl |grep top|grep nodes

minikube kubectl top nodes