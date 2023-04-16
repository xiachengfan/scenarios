#!/bin/bash

cat ~/.zsh_history |grep kubectl | grep nginx|grep '-f' | grep  -Eq logs 