#!/bin/bash

cat ~/.zsh_history |grep kubectl | grep pod | grep nginx-busybox |grep 'ls'| grep  -Eq exec
