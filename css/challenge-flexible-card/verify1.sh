export PATH=$PATH:/usr/sbin/nodejs/bin >> ~/.bashrc
export NODE_PATH=/usr/sbin/nodejs/lib/node_modules >> ~/.bashrc
source ~/.bashrc
cd /tmp && node test_flexible_card.js
