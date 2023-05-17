#!/bin/zsh

cat /home/labex/.zsh_history | grep -E "docker.*search.*--format.*table.*{{.Name}}.*{{.Description}}.*{{.StarCount}}.*--limit.*5.*nginx"
