#!/bin/zsh

cat ~/.zsh_history | grep -E "kubectl\s+describe\s+limitrange\s+example-limitrange"
