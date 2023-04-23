#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep describe|grep pod |grep containerprobe-deployment
