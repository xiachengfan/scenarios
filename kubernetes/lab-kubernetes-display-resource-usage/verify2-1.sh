#!/bin/bash

minikube kubectl -- get pods -n kube-system|grep metrics-server |grep Running