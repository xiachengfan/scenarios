#!/bin/bash
# Check if the my-container log has been viewed
history | grep -Eq 'docker logs my-container'