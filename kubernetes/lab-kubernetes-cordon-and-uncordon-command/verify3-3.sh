#!/bin/bash

cat ~/.zsh_history | grep kubectl |grep apply
sleep 60
if $(kubectl get pods | grep nginx | awk '{print $3}') == "Pending";then
        exit 0
esle
        exit 2
fi