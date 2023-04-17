#!/bin/bash

cat ~/.zsh_history |grep kubectl | grep pod | grep nginx | grep  -Eq exec