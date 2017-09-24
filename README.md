
# mysqltools 简介：
>mysql dba 的工作大了说大致包涵 环境部署，监控，故障处理，调优。就拿环境部署来说，不管是简单的单机环境，还是高大上的高可用集群(mha,mysql group replication ... )，读写分离，负载均衡集群(mycat,atlas,action-dbproxy) 都可以通过程序的方式把部署过程固化下来，下次要部署环境时只要执行一行命令就能完成，这无疑是提高生产力的好方式；

## deploy:安装与部署
###        masterha
+          mha_manager_installer-centos7.2.tar.gz mha namager 结点的全自动化安装
+          mha_node_installer-centos7.2.tar.gz    mha node    结点的全自动化安装
###        my.cnf-5.7.17+
+          mysql-5.7.17 以上版本的配置文件
###        ansible
+          通过ansible-playbook 完成各种部署时要用到的playbook
###        python-3.6.2
+          install_python.yaml 自动化安装python-3.6.2 的playbook
+          python-3.6.2.tar.xz python-3.6.2的安装文件

##         monitor:监控
+          monitormysql.py mysql 各个监控项的实现
+          zabbix_agent_mysql.conf 与zabbix结合的一个实例配置

##         backup:备份
##         ops:运维
+          maintancetool.py 常见运维任务的自动化
##         tuning:优化
+          analyzeNoneInnodbTable.sql 分析mysql实例中所包涵的MyISAM引擎表
+          lockAnalysi.sql 分析 死锁、阻塞 的这类的锁问题

