#!/bin/bash

minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'

history -c