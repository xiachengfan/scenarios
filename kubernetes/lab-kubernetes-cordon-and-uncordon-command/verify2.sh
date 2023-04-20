#!/bin/bash

minikube kubectl -- describe nodes | grep -E 'Unschedulable:[[:space:]]+false'

sudo history -c