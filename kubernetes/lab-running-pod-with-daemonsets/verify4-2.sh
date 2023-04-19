#!/bin/bash

minikube kubectl -- describe daemonset myapp-daemonset |grep busybox