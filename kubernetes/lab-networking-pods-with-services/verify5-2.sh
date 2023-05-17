#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep label | grep "app=busybox"
