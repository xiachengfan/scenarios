#!/bin/zsh

minikube kubectl -- get sa -n kubernetes-dashboard | grep admin-user
minikube kubectl -- get ClusterRoleBinding | grep admin-user
