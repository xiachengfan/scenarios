!/bin/bash

data=$(minikube kubectl -- get configmap my-configmap -o jsonpath='{.data}')

if echo "$data" | grep -q "postgres://newuser:newpassword@newhost:newport/newdbname"; then
  exit 0
else
  exit 1
fi