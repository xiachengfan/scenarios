#!/bin/bash

minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'

sudo cat /dev/null > .zsh_history