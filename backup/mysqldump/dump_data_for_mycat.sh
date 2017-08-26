#!/bin/bash

#应用场景：
#   之前的一个项目，客户要把之前的环境的数据迁移到，新的环境；但是由于新的环境使用了
#   数据分片，中间件是用的mycat。所以迁移的方式就只能是通过mysqldump把数据导出来
#   然后再把数据导入mycat，这样数据就会根据分片的规则落入不同的分片了。

#注意事项：
#   --skip-extended-insert
    #由于单表的行数就已经超过一亿行，再加上mysqldump默认情况下一个表就对应一条insert 语句，
    #这个使得单条insert语句巨大无比，超过max_allowed_packet所能允许的值，报错。在这里选择
    #每条数据一条insert语句



mysqldump -h127.0.0.1 -P3306 -udumper -p'Pass@352' \
          --skip-extended-insert --no-create-db --no-create-info \
          --skip-lock-tables --skip-add-locks --set-gtid-purged=OFF --single-transaction \
          --databases tempdb > /tmp/tempdb.sql
