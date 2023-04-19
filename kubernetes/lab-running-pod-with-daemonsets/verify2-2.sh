#!/bin/bash

minikube kubectl -- get daemonset | grep "myapp-daemonset"