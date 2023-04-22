#!/bin/bash

cat ~/.zsh_history | grep kubectl | |grep port-forward |grep "19443:443" |grep "19080:80"
