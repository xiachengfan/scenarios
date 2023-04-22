#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep nodes|grep label
minikube kubectl -- get nodes --show-labels=true |grep disk-type=ssd