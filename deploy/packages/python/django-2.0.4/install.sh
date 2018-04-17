#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install --isolated Django-2.0.4-py3-none-any.whl