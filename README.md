**文档目录**

<!-- 目录开始 -->
- [mysqltools](#mtls)
    - [mysql安装](#mtls_mysql_install)
        - [单机实例mysql的安装](#mtls_single_instance_install)
        - [master-slaves复制环境的安装](#mtls_master_slaves_install)
        - [mysql-group-replication环境的安装](#mtls_group_replication)
    - [Master High Availability(mha)环境的安装](#mtls_mha)
        - [manger 节点的安装](#mtls_mha_manager)
        - [node   节点的安装](#mtls_mha_node)
    - [mysql 中间件(读写分离，负载均衡，数据分片)](#mtls_mysql_proxy)
        - [mycat](#mtls_mysql_proxy_mycat)
        - [atlas](#mtls_mysql_proxy_atlas)
    - [mysql备份生命周期管理](#mtls_mysql_backups)
        - [基于MySQL Enterprise Backup(meb)备份周期的管理](#mtls_meb_backup)
        - [基于percona-xtrabackup(xtrabackup)备份周期的管理](#mtls_xbk_backup)
    - [mysql监控环境的安装](#mysql_monitor)
        - [zabbix-server的安装](#mtls_zabbix_server_install)
        - [zabbix-agent的安装](#mtls_zabbix_agent_install)
        - [zabbix 自动化监控mysql的配置](#mtls_zabbix_config)
    - [mysql深度巡检](#mtls_mysql_inspection)
    - [mysql 优化](#mtls_mysql_tuning)
        - [mysql 参数优化](#mtls_mysql_tuning_parta)
        - [sql 语句优化](#mtls_mysql_tuning_partb)
    - [私人定制/商务合作/学习交流](#mtls_contact)

<!-- 目录结束 -->

<!-- 正文开始 -->
# mysqltools简介

mysqltools 是一个用于快速建设大规模高质量mysql数据库集群的工具
