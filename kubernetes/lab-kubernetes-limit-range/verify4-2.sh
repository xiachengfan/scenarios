#!/bin/zsh

cat ~/.zsh_history | grep -E "kubectl\s+describe\s+limitranges\s+example-limitrange"
