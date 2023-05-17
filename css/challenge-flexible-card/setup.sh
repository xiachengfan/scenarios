#!/bin/zsh

export PATH=$PATH:/usr/sbin/nodejs/bin >> ~/.bashrc
export NODE_PATH=/usr/sbin/nodejs/lib/node_modules >> ~/.bashrc
source ~/.bashrc

cd /tmp && npm i puppeteer@20.1.2
