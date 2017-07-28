
# mysqltools 是一个在实战中得出的，mysql dba 的运维工具

## deploy:
### ansible 
#### ansible playbook
### masterha
#### 用于实现mha想着依赖的解决,node,manager的安装


    1: maintancetool.py mysql数据库相关的运维操作
    2: mysql.conf       zabbix 自定义key时agent端的配置文件
    3: my.cnf-5.7.17    适用于myql-5.7及以上版本的mysql配置文件
    4: backup/mysqlbackup.sh mysqlbackup的一个备份脚本
    5: backup/mysqlbackup.sql 用于创建mysqlbackup要用到的数据库用户
    6: /monitor/monitormysql.py  mysql数据库的监控
    7: /monitor/zabbix_agent_mysql.conf zabbix-agent 端自定义mysql监控项的key定义
