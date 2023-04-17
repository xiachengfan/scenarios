#!/bin/bash

cat ~/.zsh_history |grep kubectl | grep pod | grep nginx-busybox |grep 'it'| grep  -Eq exec