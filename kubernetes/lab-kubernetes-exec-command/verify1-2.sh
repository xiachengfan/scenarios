#!/bin/bash
cat ~/.zsh_history |grep kubectl | grep apply 
cat ~/.zsh_history |grep kubectl | grep pod | grep nginx |grep v | grep  -Eq exec