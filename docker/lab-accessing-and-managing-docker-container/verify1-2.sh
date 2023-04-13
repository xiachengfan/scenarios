#!/bin/bash
# Check if the my-container log has been viewed
if history |grep docker | grep my-container | grep  -Eq logs; then
  exit 0
else
  exit 1
fi