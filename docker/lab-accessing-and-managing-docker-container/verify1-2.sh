#!/bin/bash
# Check if the my-container log has been viewed
if history | grep -Eq 'docker logs my-container'; then
  exit 0
else
  exit 1
fi