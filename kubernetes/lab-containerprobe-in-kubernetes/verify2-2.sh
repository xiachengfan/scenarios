#!/bin/bash

minikube kubectl -- describe deployment containerprobe-deployment | grep "Liveness"
