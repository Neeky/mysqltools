#!/bin/bash
source /etc/profile
basedir=`dirname $0`
echo $basedir
cd $basedir

pip3 install --isolated uwsgi-2.0.17.tar.gz

cd /www/uwsgi
if [ ! -d "/www/uwsgi/leorg" ];then
    django-admin startproject leorg
fi
