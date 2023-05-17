#!/bin/bash

if grep -q "readinessProbe" "/home/labex/project/deployment.yaml"; then
  exit 0
else
  exit 1
fi
