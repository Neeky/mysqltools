#!/bin/bash
cd /tmp/sysbench/

./autogen.sh && \
./configure --prefix=/usr/local/sysbench/ --with-mysql --with-mysql-includes=/usr/local/mysql/include --with-mysql-libs=/usr/local/mysql/lib && \
make && \
make install