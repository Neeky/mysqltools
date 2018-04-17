#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install --isolated bs4-0.0.1.tar.gz