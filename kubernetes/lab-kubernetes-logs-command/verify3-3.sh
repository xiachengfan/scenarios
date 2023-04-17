#!/bin/zsh

minikube kubectl -- logs nginx| grep "127.0.0.1"