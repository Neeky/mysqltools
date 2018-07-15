#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install mysqlclient-1.3.13.tar.gz
pip3 install six-1.11.0-py2.py3-none-any.whl
pip3 install protobuf-3.6.0-cp36-cp36m-manylinux1_x86_64.whl
pip3 install mysql_connector_python-8.0.11-cp36-cp36m-manylinux1_x86_64.whl

#pip3 install mysql_connector_python-8.0.6-cp36-cp36m-manylinux1_x86_64.whl
