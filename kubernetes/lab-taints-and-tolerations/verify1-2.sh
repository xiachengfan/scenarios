#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep nodes|grep taint

minikube kubectl -- describe  nodes  |grep 