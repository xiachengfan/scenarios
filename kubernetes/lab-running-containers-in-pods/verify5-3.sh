#!/bin/zsh
minikube kubectl -- exec -it my-pod-5 -- df | grep /mnt/data
