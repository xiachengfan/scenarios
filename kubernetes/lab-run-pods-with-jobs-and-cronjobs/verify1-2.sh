#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply 
minikube kubectl -- describe jobs hello-job 