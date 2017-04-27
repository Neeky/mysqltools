#
#   mysql 日常运维工作解决的问题、并对它进行了脚本化、希望再次遇到同类问题时能快速的解决

#目前工具集中包涵有如下组件


    1: maintancetool.py mysql数据库相关的运维操作
    2: mysql.conf       zabbix 自定义key时agent端的配置文件
    3: my.cnf-5.7.17    适用于myql-5.7及以上版本的mysql配置文件
    4: backup/mysqlbackup.sh mysqlbackup的一个备份脚本
    5: backup/mysqlbackup.sql 用于创建mysqlbackup要用到的数据库用户
    6: /monitor/monitormysql.py  mysql数据库的监控
    7: /monitor/zabbix_agent_mysql.conf zabbix-agent 端自定义mysql监控项的key定义
