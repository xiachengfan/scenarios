#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep uncordon|grep org=labex
if minikube kubectl -- describe node | grep SchedulingDisabled; then
  exit 1
else
  echo 0
fi