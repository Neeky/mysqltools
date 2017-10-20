#!/bin/bash
#注意要用root用户运行这个脚本

#1、安装python相关的依赖
sudo yum -y install gcc gcc-c++ libffi libffi-devel zlib zlib-devel openssl openssl-devel libyaml sqlite-devel libxml2 libxslt-devel libxml2-devel

#2、安装python
pythondir=`dirname $0`
cd $pythondir
tar -xvf python-3.6.2.tar.xz -C /tmp/
cd /tmp/Python-3.6.2/
./configure --prefix=/usr/local/python-3.6.2/
make -j 2
make install
cd /usr/local/
ln -s /usr/local/python-3.6.2  python
echo 'export PATH=/usr/local/python/bin/:$PATH' >> /etc/profile
source /etc/profile


