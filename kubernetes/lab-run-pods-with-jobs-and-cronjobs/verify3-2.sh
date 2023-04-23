#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply | grep 'cronjob.yaml'

minikube kubectl -- describe jobs download-job 