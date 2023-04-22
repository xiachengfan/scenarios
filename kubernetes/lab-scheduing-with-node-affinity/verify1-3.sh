#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep nodes|grep show-labels
cat /dev/null >  ~/.zsh_history