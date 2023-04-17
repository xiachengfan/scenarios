#!/bin/bash

minikube kubectl -- get pod | grep "nginx"|grep "MY_VAR=my-value"