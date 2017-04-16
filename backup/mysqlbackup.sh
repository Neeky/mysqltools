#!/bin/bash

# 0001对整个实例进行备份
mysqlbackup --defaults-file=/etc/my.cnf --backup-dir=/tmp/ --with-timestamp \
  --host=127.0.0.1 --port=3306 --user=backupuser --password=1234567890 \
  --backup-image=/tmp/$(date +'%F=%H:%M:%S').mbi \
  backup-to-image

# 0002对备份集进行校验
mysqlbackup --backup-image=/tmp/2017-04-16=17:32:30.mbi \
  validate


# 0003还原mysql备份
mysqlbackup --defaults-file=/etc/my.cnf --backup-dir=/tmp \
  --backup-image=/tmp/2017-04-16=17:32:30.mbi \
  copy-back-and-apply-log