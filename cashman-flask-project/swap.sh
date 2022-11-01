#!/bin/bash
set -x

echo "Param $1"
echo "Param $2"

/usr/local/bin/kasa --type $1 --host $2 state > t.o
if [[ `cat t.o | grep 'Device state: OFF' | tr -d '\n'` == "" ]]; then
   echo "ON... turning OFF"
   /usr/local/bin/kasa --type $1 --host $2 off
else 
   echo "OFF... turning ON"
   /usr/local/bin/kasa --type $1 --host $2 on
fi
