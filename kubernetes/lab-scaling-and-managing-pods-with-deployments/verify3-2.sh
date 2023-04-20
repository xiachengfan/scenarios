#!/bin/bash

IMAGE=nginx:1.19

# 获取实际镜像版本
IMAGE_CURRENT=$(minikube kubectl -- get deployment my-deployment -o=jsonpath='{.spec.template.spec.containers[0].image}')

if [ "$IMAGE" -eq "$IMAGE_CURRENT" ]; then
  exit 0
else
  exit 1
fi

cat ~/.zsh_history | grep kubectl |grep rollout |grep status