#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply

if $(minikube kubectl -- get pods | grep nginx | awk '{print $3}') -eq "Pending";then
        exit 0
esle
        minikube kubectl -- delete deployment nginx-deployment
        exit 1
fi
