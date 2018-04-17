#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install --isolated ansible-2.5.0.tar.gz