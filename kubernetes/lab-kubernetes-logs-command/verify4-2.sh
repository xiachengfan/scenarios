#!/bin/bash

cat ~/.zsh_history |grep kubectl | grep fluentd| grep nginx-fluentd | grep  -Eq logs
cat ~/.zsh_history |grep kubectl | grep nginx  | grep nginx-fluentd | grep  -Eq logs