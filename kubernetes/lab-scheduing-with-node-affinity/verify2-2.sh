#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply |grep pod-with-node-affinity.yaml
