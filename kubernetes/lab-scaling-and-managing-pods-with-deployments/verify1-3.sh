#!/bin/bash
REPLICAS_DESIRED=3

cat ~/.zsh_history | grep kubectl |grep deployment|grep get