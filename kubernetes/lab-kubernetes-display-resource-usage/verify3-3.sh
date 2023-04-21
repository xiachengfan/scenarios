#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep top|grep myapp-pod  |grep namespace=default | grep 'containers=true'
