#!/bin/bash

cat ~/.zsh_history | grep kubectl | grep get | grep pods | grep app=containerprobe
