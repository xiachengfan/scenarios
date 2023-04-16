#!/bin/zsh

minikube kubectl -- logs nginx| grep "This is a test log"