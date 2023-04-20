#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep cordon |grep minikube
minikube kubectl -- get nodes | grep SchedulingDisabled