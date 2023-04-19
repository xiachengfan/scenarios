#!/bin/bash

NODE_PORT=$(kubectl get svc hello-service -o jsonpath='{.spec.ports[0].nodePort}')

cat ~/.zsh_history |grep curl |grep $NODE_PORT