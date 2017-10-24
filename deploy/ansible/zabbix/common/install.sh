#!/bin/bash
cd /tmp/zabbix-3.4.3/
./configure --enable-server --enable-agent --with-mysql=/usr/local/mysql/bin/mysql_config --with-net-snmp --with-libcurl --with-libxml2 --with-unixodbc --prefix=/usr/local/zabbix-3.4.3
make install 