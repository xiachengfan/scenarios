#!/bin/zsh

cat ~/.zsh_history | grep -E "kubectl\s+describe\s+resourcequotas\s+example-resourcequota"
