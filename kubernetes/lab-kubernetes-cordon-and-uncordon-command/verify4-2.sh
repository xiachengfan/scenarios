#!/bin/bash


cat ~/.zsh_history | grep kubectl |grep 'l' |grep cordon|grep org=labex 
minikube kubectl -- describe node | grep SchedulingDisabled