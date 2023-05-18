#!/bin/zsh

cat ~/.zsh_history | grep -E "kubectl\s+describe\s+pod\s+example-pod"
