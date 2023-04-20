#!/bin/bash

#为了保证verify3-2能通过
minikube kubectl -- cordon minikube
minikube kubectl -- uncordon minikube