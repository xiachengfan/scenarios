#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube

sleep 120
if $(minikube kubectl -- get pods | grep nginx | awk '{print $3}') != "Pending";then
        exit 0
esle
        exit 1
fi