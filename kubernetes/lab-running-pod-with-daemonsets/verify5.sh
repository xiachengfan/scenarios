#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep pods |grep app=myapp 
