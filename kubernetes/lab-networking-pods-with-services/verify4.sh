#!/bin/bash
minikube kubectl -- get endpoints/my-service | grep "none"
