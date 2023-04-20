#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
if minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+true';then
exit 0
        minikube kubectl -- delete deployment nginx-deployment
        exit 1
fi
# minikube kubectl -- get pods | grep nginx 
# if $(minikube kubectl -- get pods | grep nginx | awk '{print $3}') -eq "Pending";then
#         exit 0
# esle
#         minikube kubectl -- delete deployment nginx-deployment
#         exit 1
# fi
