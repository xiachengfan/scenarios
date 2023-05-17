#!/bin/bash
cat ~/.zsh_history | grep kubectl | grep exec | grep "test-pod-1"
