#!/bin/bash

minikube kubectl -- describe deployment containerprobe-deployment |grep -q "Readiness"

cat /dev/null >  ~/.zsh_history