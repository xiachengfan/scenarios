#!/bin/zsh

test -z "$(docker images | grep my-web-server)"
