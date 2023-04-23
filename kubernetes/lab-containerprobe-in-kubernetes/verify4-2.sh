#!/bin/bash

minikube kubectl -- describe deployment containerprobe-deployment |grep minikube kubectl -- describe deployment containerprobe-deployment |grep grep -q "Readiness:[[:space:]]+http-get[[:space:]]+http://:80/[[:space:]]+delay=0s[[:space:]]+timeout=1s[[:space:]]+period=10s[[:space:]]+#success=1[[:space:]]+#failure=3
