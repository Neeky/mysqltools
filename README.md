
# mysqltools 是一个在实战中得出的，mysql dba 的运维工具

## deploy:安装与部署
###        masterha
+          mha_manager_installer-centos7.2.tar.gz mha namager 结点的全自动化安装
+          mha_node_installer-centos7.2.tar.gz    mha node    结点的全自动化安装
###        my.cnf-5.7.17+
+          mysql-5.7.17 以上版本的配置文件
###        ansible
+          通过ansible-playbook 完成各种部署时要用到的playbook

##         monitor:监控
+          monitormysql.py mysql 各个监控项的实现
+          zabbix_agent_mysql.conf 与zabbix结合的一个实例配置

##         backup:备份

