**文档目录**

<!-- 目录开始 -->
- [mysqltools简介](#mysqltools简介)
    - [mysqltools特性](#mysqltools特性)
        - 1 mysql、master-slaves、innodb-cluster、mysql-group-replication等mysql相关环境的自动化安装与配置
        - 2 mysql高可用、读写分离、负载均衡 集群的自动化安装与配置
        - 3 mysql全备、增备、验证、还原 整个生命周期的管理
        - 4 mysql监控环境的自动化安装、配置
        - 5 mysql巡检
        - 6 mysql优化
        - 7 私人定制/商务合作/学习交流/技术支持
    - [mysqltools所遵循的标准](#mysqltools所遵循的标准)
        - [标准化的意义](#标准化的意义)
        - [mysqltools中mysql相关的标准](#mysqltools中mysql相关的标准)
    - [安装与配置mysqltools](#安装与配置mysqltools)
        - [安装python](#安装python)
            - [安装python第一步](#安装python第一步)
            - [安装python第二步](#安装python第二步)
            - [自动化安装python](#自动化安装python)
        - [安装ansible](#安装ansible)
            - [安装ansibe第一步解决依赖问题](#安装ansibe第一步解决依赖问题)
                - [安装pycparser](#安装pycparser)
                - [安装six](#安装six)
                - [安装asn1crypto](#安装asn1crypto)
                - [安装idna](#安装idna)
                - [安装cryptography](#安装cryptography)
                - [安装pyasn1](#安装pyasn1)
                - [安装pPyNaCl](#安装pPyNaCl)
                - [安装bcrypt](#安装bcrypt)
                - [安装paramiko](#安装paramiko)
                - [安装PyYAML](#安装PyYAML)
                - [安装MarkupSafe](#安装MarkupSafe)
                - [安装Jinja2](#安装Jinja2)
            - [安装ansibe第二步安装ansible](#安装ansibe第二步安装ansible)
            - [自动化安装ansible](#自动化安装ansible)
        - [其它依赖软件的安装](#mtls_install_self_others)
- [mysqltools功能列表](#mysqltools功能列表)
    - [mysql安装](#mysql安装)
        - [单机实例mysql的安装](#单机实例mysql的安装)
        - [master-slaves复制环境的安装](#mtls_master_slaves_install)
        - [mysql-group-replication环境的安装](#mtls_group_replication)
        - [innodb-cluster环境的安装](#mtls_innodb_cluster)
        - [mysql-cluster环境的安装](#mtls_mysql_cluster)
    - [Master High Availability(mha)环境的安装](#mtls_mha)
        - [manger 节点的安装](#mtls_mha_manager)
        - [node   节点的安装](#mtls_mha_node)
    - [mysql 中间件(读写分离，负载均衡，数据分片)](#mtls_mysql_proxy)
        - [dble](#爱可生分布式中间件)
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
mysqltools 是一个用于快速构建或管理 大规模，高质量，全自动化，mysql分布式集群环境的工具；mysqltools的目标是
能在一天之内交付数以千记的高质量结点组成的环境。

## 标准化的意义
总的来说标准化是自动化的基础，没有标准化就谈不上自动化。举个例子，比较说我管理着400多台mysql主机，现在由于一些安全方面的问题要对这400多台主机上的mysql进行升级；如果个400台主机上的mysql它们的安装目录、配置文件、都各有各的特色；
比如有的安装在/usr/local/mysql，有的安装在/home/mysql/mysql/，有的又安装在/var/mysql/，这样的话就不能用同一个升级步骤去应对所有的主机，这就意味着不能批量的对这400台主机做升级了。

## 安装与配置mysqltools
mysqltools 提供的自动化，集中化运维能力是建立在ansible的基础之上，所以安装ansible 就成了使用mysqltools先决条件；
ansible 这个软件又是由python写出来的，实际上绝大部分linux操作系统都已经安装上了python2.x，作为一个面向未来的软件
mysqltools并没有使用python2.x而是基于python3.6.x上开发完成的。所以在你安装ansible之前还要先安装上python.3.6.x
好在所以的安装包mysqltool都已经为你准备好了，mysqltools/deploy/packages/目录下；不只是这样，为们还把安装流程写成
了脚本，这样你就只要运行一下mysqltools给出的安装脚本就能自动化安装mysqltools了。

### 安装python
为了方便离线安装python3.6.x 的安装包已经打包到了mysqltools/deploy/packages/python中 注意安装的过程要用root用户

#### 安装python第一步
安装python3.6.x 的相关依赖包

    yum -y install gcc gcc-c++ libffi libffi-devel zlib zlib-devel openssl openssl-devel libyaml sqlite-devel libxml2 libxslt-devel libxml2-devel

#### 安装python第二步
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

#### 自动化安装python
事实上mysqltools/deplay/packages/python/install.sh 脚本中包涵了上面两个步骤的命令可以用root用户直接运它以完成python的安装

    bash install.sh

### 安装ansible
为了方便离线安装 ansible-2.4.0.0 的安装包和与之相关的依赖包都已经保存到mysqltool/deploy/packages/ansible目录下


#### 安装ansibe第一步解决依赖问题

##### 安装pycparser
    cd mysqltool/deploy/packages/ansible
    tar -xvf pycparser-2.18.tar.gz -C /tmp/
    cd /tmp/pycparser-2.18
    python3 setup.py build
    python3 setup.py install

##### 安装six
    cd mysqltool/deploy/packages/ansible
    tar -xvf six-1.11.0.tar.gz -C /tmp/
    cd /tmp/six-1.11.0
    python3 setup.py build
    python3 setup.py install

##### 安装asn1crypto
    cd mysqltool/deploy/packages/ansible
    tar -xvf asn1crypto-0.23.0.tar.gz -C /tmp/
    cd /tmp/asn1crypto-0.23.0
    python3 setup.py build
    python3 setup.py install

##### 安装idna
    cd mysqltool/deploy/packages/ansible
    tar -xvf idna-2.6.tar.gz -C /tmp/
    cd /tmp/idna-2.6
    python3 setup.py build
    python3 setup.py install

##### 安装cryptography
    cd mysqltool/deploy/packages/ansible
    tar -xvf cryptography-2.1.1.tar.gz -C /tmp/
    cd /tmp/cryptography-2.1.1/
    python3 setup.py build
    python3 setup.py install

##### 安装pyasn1
    cd mysqltool/deploy/packages/ansible
    tar -xvf pyasn1-0.3.7.tar.gz -C /tmp/
    cd /tmp/pyasn1-0.3.7
    python3 setup.py build
    python3 setup.py install

##### 安装pPyNaCl
    cd mysqltool/deploy/packages/ansible
    tar -xvf PyNaCl-1.1.2.tar.gz -C /tmp/
    cd /tmp/PyNaCl-1.1.2
    python3 setup.py build
    python3 setup.py install 

##### 安装bcrypt
    cd mysqltool/deploy/packages/ansible
    tar -xvf bcrypt-3.1.4.tar.gz -C /tmp/
    cd /tmp/bcrypt-3.1.4 
    python3 setup.py build
    python3 setup.py install 

##### 安装paramiko
    cd mysqltool/deploy/packages/ansible
    tar -xvf paramiko-2.3.1.tar.gz -C /tmp/
    cd /tmp/paramiko-2.3.1
    python3 setup.py build
    python3 setup.py install 

##### 安装PyYAML
    cd mysqltool/deploy/packages/ansible
    tar -xvf PyYAML-3.12.tar.gz -C /tmp/
    cd /tmp/PyYAML-3.12
    python3 setup.py build
    python3 setup.py install 

##### 安装MarkupSafe
    cd mysqltool/deploy/packages/ansible
    tar -xvf MarkupSafe-1.0.tar.gz -C /tmp/
    cd /tmp/MarkupSafe-1.0
    python3 setup.py build
    python3 setup.py install    

##### 安装Jinja2
    cd mysqltool/deploy/packages/ansible
    tar -xvf Jinja2-2.9.6.tar.gz -C /tmp/
    cd/tmp/Jinja2-2.9.6
    python3 setup.py build
    python3 setup.py install 

#### 安装ansibe第二步安装ansible
    cd mysqltools/deploy/packages/ansible/
    tar -xvf ansible-2.4.0.0.tar.gz -C /tmp/
    python3 setup.py build
    python3 setup.py install 

#### 自动化安装ansible
作为一个着眼于自动化的工具当然是不应该有这么困难的安装方式的，mysqltools为自己写好自动化安装的脚本，注意这个要用root身份运行

    cd mysqltools/deploy/package/ansible
    bash install.sh

# mysqltools功能列表

## mysql安装
### 单机实例mysql的安装
- 1. 1 进入mysql工具所在的目录

        cd mysqltools/deploy/ansible/mysql/

- 2. 2 设置install_single_mysql.yaml文件中的hosts字段的值为你要执行mysql包安装的目标机器

- 3. 3 调用ansible-playbook完成自动化安装过程

        ansible-playbook install_single_mysql.yaml
        PLAY [cstudio] ******************************************************************
        TASK [Gathering Facts] **************************************************************
        ok: [cstudio]
        TASK [create mysql user] ************************************************************
        changed: [cstudio]
        TASK [create and config /etc/my.cnf] ************************************************
        changed: [cstudio]

TASK [transfer mysql install package to remote host and unarchive to /usr/local/] ***
changed: [cstudio]

TASK [change owner to mysql user] ***************************************************
changed: [cstudio]

TASK [make link /usr/local/mysql-xx.yy.zz to /usr/local/mysql] **********************
changed: [cstudio]

TASK [export mysql share object (*.os)] *********************************************
ok: [cstudio]

TASK [load share object] ************************************************************
changed: [cstudio]

TASK [export path env variable] *****************************************************
ok: [cstudio]

TASK [export path env to /root/.bashrc] *********************************************
ok: [cstudio]

TASK [make link /usr/local/mysql-xx.yy.zz to /usr/local/mysql] **********************
ok: [cstudio]

TASK [create datadir] ***************************************************************
changed: [cstudio]

TASK [initialize-insecure] **********************************************************
changed: [cstudio]

TASK [create libmysqlclient_r.so file for php-5.6] **********************************
changed: [cstudio]

TASK [create systemd config file] ***************************************************
skipping: [cstudio]

TASK [enable mysqld service] ********************************************************
skipping: [cstudio]

TASK [start mysql(sytemctl)] ********************************************************
skipping: [cstudio]

TASK [config mysql.service start up on boot] ****************************************
skipping: [cstudio]

TASK [config sysv start script] *****************************************************
changed: [cstudio]

TASK [start mysql(service)] *********************************************************
changed: [cstudio]

TASK [config mysql.service start up on boot] ****************************************
changed: [cstudio]

TASK [transfer sql statement to remonte] ********************************************
ok: [cstudio]

TASK [make mysql secure] ************************************************************
changed: [cstudio]

PLAY RECAP **************************************************************************
cstudio                : ok=19   changed=13   unreachable=0    failed=0

## mysql监控环境的安装

### zabbix-server的安装
- 1 在zabbix-server 所在的主机上安装mysql数据库

    cd mysqltools/deplay/ansible/mysql/
    ansible-playbook install_single_mysql.yaml

- 2 增加zabbix用户

    cd mysqltools/deplay/ansible/mysql/
    
