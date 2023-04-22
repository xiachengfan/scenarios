#!/bin/bash

minikube kubectl -- logs nginx-busybox -c nginx | grep "19001"

