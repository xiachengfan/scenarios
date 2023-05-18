#!/bin/zsh

test -z "$(docker inspect my-network | grep container2)"
