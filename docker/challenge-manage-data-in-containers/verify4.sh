#!/bin/zsh

cat ~/.zsh_history | grep -E "docker\s+exec\s+my-container\s+cat\s+/app/data/hello.txt"
