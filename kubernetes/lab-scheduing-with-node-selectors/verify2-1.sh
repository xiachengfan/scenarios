#!/bin/zsh

minikube kubectl -- describe node minikube | grep disk=ssd
