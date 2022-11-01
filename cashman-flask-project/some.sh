#!/bin/sh
set -x

echo "Param $1"
echo "Param $2"
echo "Param $3"

/usr/local/bin/kasa --type $1 --host $2 $3

echo "Run from script"
