#!/bin/bash

POD_NAME=$(kubectl get pods -o jsonpath='{.items[*].metadata.name}')
minikube kubectl -- logs $POD_NAME | grep "19080"
minikube kubectl -- logs $POD_NAME | grep "19443"