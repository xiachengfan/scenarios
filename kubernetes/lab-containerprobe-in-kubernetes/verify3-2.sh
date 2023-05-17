#!/bin/bash

if cat ~/.zsh_history | grep kubectl | grep describe | grep pod > /dev/null; then
  exit 0
else
  exit 1
fi
