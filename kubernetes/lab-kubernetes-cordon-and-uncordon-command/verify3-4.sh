#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon |grep minikube

cat /dev/null >  ~/.zsh_history