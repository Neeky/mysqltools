#!/bin/bash
#注意要用root用户运行这个脚本

#1、安装python相关的依赖
sudo yum -y install gcc gcc-c++ libffi libyaml-devel libffi-devel zlib zlib-devel openssl openssl-devel libyaml sqlite-devel libxml2 libxslt-devel libxml2-devel

#2、安装python
pythondir=`dirname $0`
cd $pythondir

if [ ! -d '/tmp/mysql-connector' ]; then
    cp -rf mysql-connector /tmp/
fi

if [ ! -d '/tmp/mysqltools-python' ]; then
    cp -rf mysqltools-python /tmp/
fi 

tar -xvf python-3.6.2.tar.xz -C /tmp/
cd /tmp/Python-3.6.2/
./configure --prefix=/usr/local/python-3.6.2/
make -j $(nproc)
make install
cd /usr/local/
ln -s /usr/local/python-3.6.2  python


echo 'export PATH=/usr/local/python/bin/:$PATH' >> /etc/profile

export PATH=/usr/local/python/bin/:$PATH

cd /tmp/
cd mysql-connector
pip3 install six-1.11.0-py2.py3-none-any.whl
pip3 install protobuf-3.6.0-cp36-cp36m-manylinux1_x86_64.whl
pip3 install mysql_connector_python-8.0.12-cp36-cp36m-manylinux1_x86_64.whl

cd /tmp/mysqltools-python
pip3 install mysqltools-python-2.18.11.24.tar.gz

rm -rf /tmp/Python-3.6.2
rm -rf /tmp/mysql-connector
rm -rf /tmp/mysqltools-python

if [ -f /tmp/python-3.6.2.tar.xz ];then
   rm -rf /tmp/python-3.6.2.tar.xz
fi


