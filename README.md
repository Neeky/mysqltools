**文档目录**

<!-- 目录开始 -->
- [mysqltools简介](#mysqltools简介)
    - [mysqltools的安装与配置](#mysqltools的安装与配置)
        - [python的安装](#python的安装)
            - [python的安装第一步](#python的安装第一步)
            - [python的安装第二步](#python的安装第二步)
        - [ansible的安装](#mtls_install_self_ansible)
        - [其它依赖软件的安装](#mtls_install_self_others)
    - [mysql安装](#mtls_mysql_install)
        - [单机实例mysql的安装](#mtls_single_instance_install)
        - [master-slaves复制环境的安装](#mtls_master_slaves_install)
        - [mysql-group-replication环境的安装](#mtls_group_replication)
        - [innodb-cluster环境的安装](#mtls_innodb_cluster)
        - [mysql-cluster环境的安装](#mtls_mysql_cluster)
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
mysqltools 是一个用于快速构建大规模，高质量，全自动化的 mysql分布式集群环境的工具

## mysqltools的安装与配置
mysqltools 提供的自动化，集中化运维能力是建立在ansible的基础之上，所以安装ansible 就成了使用mysqltools先决条件；
ansible 这个软件又是由python写出来的，实际上绝大部分linux操作系统都已经安装上了python2.x，作为一个面向未来的软件
mysqltools并没有使用python2.x而是基于python3.6.x上开发完成的。所以在你安装ansible之前还要先安装上python.3.6.x
好在所以的安装包mysqltool都已经为你准备好了，mysqltools/deploy/packages/目录下；不只是这样，为们还把安装流程写成
了脚本，这样你就只要运行一下mysqltools给出的安装脚本就能自动化安装mysqltools了。

### python的安装
python3.6.x 的安装包已经打包到了mysqltools/deploy/packages/python中

#### python的安装第一步
安装python3.6.x 的相关依赖包

    sudo yum -y install gcc gcc-c++ libffi libffi-devel zlib zlib-devel openssl openssl-devel libyaml sqlite-devel libxml2 libxslt-devel libxml2-devel

#### python的安装第二步
安装python-3.6.x 

    cd mysqltools/deploy/packages/python
    tar -xvf python-3.6.2.tar.xz -C /tmp/
    cd /tmp/Python-3.6.2/
    ./configure --prefix=/usr/local/python-3.6.2/
    make -j 2
    make install
    cd /usr/local/
    ln -s /usr/local/python-3.6.2  python
    echo 'export PATH=/usr/local/python/bin/:$PATH' >> /etc/profile
    source /etc/profile


