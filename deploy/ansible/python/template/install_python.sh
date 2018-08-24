#!/bin/bash

#1、安装python
cd /tmp/Python-3.6.2/
./configure --prefix=/usr/local/python-3.6.2/
make -j 2
make install

cd /tmp/mysql-connector
/usr/local/python-3.6.2/bin/pip3 install six-1.11.0-py2.py3-none-any.whl
/usr/local/python-3.6.2/bin/pip3 install protobuf-3.6.0-cp36-cp36m-manylinux1_x86_64.whl
/usr/local/python-3.6.2/bin/pip3 install mysql_connector_python-8.0.11-cp36-cp36m-manylinux1_x86_64.whl



