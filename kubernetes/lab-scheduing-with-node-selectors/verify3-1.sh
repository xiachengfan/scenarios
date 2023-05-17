#!/bin/zsh

minikube kubectl -- describe node minikube | grep resigon=labex
minikube kubectl -- describe node minikube | grep gpu=true
