#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube
minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'