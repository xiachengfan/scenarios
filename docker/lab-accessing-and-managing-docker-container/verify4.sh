#!/bin/bash
docker ps -a |grep my-shell-container || echo "ok"