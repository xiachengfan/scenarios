#!/bin/bash

pod_name=$(minikube kubectl -- get pods -l app=containerprobe -o jsonpath='{.items[0].metadata.name}')
cat ~/.zsh_history | grep kubectl | grep describe | grep pod | grep ${pod_name}
