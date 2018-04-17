#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install --isolated mysqlclient-1.3.12.tar.gz
pip3 install --isolated mysql_connector_python-8.0.6-cp36-cp36m-manylinux1_x86_64.whl
