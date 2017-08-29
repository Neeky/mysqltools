#!/bin/bash

# 0001对整个实例进行备份
mysqlbackup --defaults-file=/etc/my.cnf --backup-dir=/tmp/ --with-timestamp \
  --host=127.0.0.1 --port=3306 --user=backupuser --password=1234567890 \
  --compress --skip-binlog --skip-relaylog --no-locking \
  --read-threads=4 --process-threads=8 --write-threads=4 --limit-memory=1024 \
  --backup-image=/tmp/$(date +'%F_%H-%M-%S').mbi \
  backup-to-image

# 0002对备份集进行校验
mysqlbackup --backup-image=/tmp/2017-04-16_17-32-30.mbi \
  validate


# 0003还原mysql备份
mysqlbackup --defaults-file=/etc/my.cnf --backup-dir=/tmp --datadir=/usr/local/data/3306/ \
  --uncompress --backup-image=/tmp/2017-04-16_17-32-30.mbi \
  --read-threads=4 --process-threads=8 --write-threads=4 --limit-memory=1024 \
  copy-back-and-apply-log
