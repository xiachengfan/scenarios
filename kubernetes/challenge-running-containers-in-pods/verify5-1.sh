#!/bin/zsh

minikube kubectl -- describe pv my-pv | grep Path | grep /mnt/data
