#!/bin/bash

minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'

cat /dev/null >  ~/.zsh_history