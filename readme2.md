
# mysqltools 权威指南

主编:**蒋乐兴**

微信: **jianglegege**

---

## 文档结构
- [概要](#概要)
  - [质量](#质量)
  - [效率](#效率)
  - [经济](#经济)
  - [技术介绍](#技术介绍)
- [安装mysqltools](#安装mysqltools)
  - [安装前的准备](#安装前的准备)
  - [下载并解压](#下载并解压)
  - [安装Python](#安装Python)
  - [安装ansible](#安装ansible)
  - [配置ansible和mysqltools](#配置ansible和mysqltools)
- [mysqltools快速开始](#mysqltools快速开始)
  - [mysqltools目录介绍](#mysqltools目录介绍)
  - [自动化mysql单实例安装](#自动化mysql单实例安装)
    - [进入mysql功能目录](#进入mysql功能目录)
    - [指定安装的目标主机](#指定安装的目标主机)
    - [执行自动化安装](#执行自动化安装)
  - [谈谈mysqltools如何实现高效](#谈谈mysqltools如何实现高效)
  - [谈谈mysqltools如何实现高质量](#谈谈mysqltools如何实现高质量)
- [赞助/交流/技术支持](#联系我)
- [mysql原生环境安装](#mysql原生环境安装)
  - [mysql单机](#mysql单机)
- [读写分离](#读写分离)
- [高可用](#高可用)
- [备份](#备份)
- [监控](#监控)
- [巡检](#巡检)


---


## 概要

   总的来说mysqltools源自于工作、一个dba的日常大概包括 数据库安装，读写分离、高可用、负载均衡等环境的配置，
   数据库备份策略拟定与实施，数据库相关的监控，数据库优化，故障分析，也有可能参与到数据库建模，SQL的编写。
   
   这样我们就面临两个问题 1、**质量** 质量表现在解决问题的深度(类似问题还会再出现吗？) 2、**效率** 效率表现在你单位时间内解决问题的数量(安装一百个库的用时是一个库的100倍   吗？)； 通常这两个目标并不是互斥的，也就是说我们可以两个都做到。

1. ## 质量
   **KFC** vs **学校后街的蛋炒饭**

   KFC根据既定的流程生产每一个汉堡，假设这个流程下公众对汉堡给出的评分是80分，那么不管哪个KFC的店它生产出来的汉堡都稳定在80分；一段时间后它发现这个流程中可以改进的项，把汉堡的质量提升到81分，那么它就能做到所有的店里的汉堡都能打81分。

   学校后街的蛋炒饭 好不好吃这个由事难说；因为好多事都影响到它，有可能老板今天心情不好，也有可能是今天客人太多他比较急，这些都会使得蛋炒饭不好吃。有一次我要买两盒，由于去的比较晚，老板只有一个鸡蛋了，你没有猜错！ 他就只放了一个蛋，按常理是要一盒一个的。

   表面上看**KFC** 流程化生产的好处在于它的东西质量有保障，**最要命的是KFC只做加法，它可以不断提升自己，学校后街的蛋炒饭上周一做好那个炒饭好吃，我们没办法确定那是不是他人生中做的最好吃的一次，蛋炒饭质量的方差太大了。**

   
   **对于DBA来说可以专门针对自己的日常工作开发一款工具，这样做的好处有 1:)由于工具已经把流程固定下来了所以“产出的质量”有保证 2:)随着自己技术的进步自己工个的输出也可以稳步提高。**  **这样我们在质量这个目标上就只做加法了。**
   
   
   ---

2. ## 效率
   
   **流水线** vs **手工作坊**

   流水线相对于手工作坊，那是生产力的巨大提升。我为什么要说这个？因为在MySQL的使用中可能会遇到一些场景，比如说“分库分表”，“高可用+读写分离”；特别是前者通常就是一个MyCAT后面有好几十个分片，上百个MySQL实例(通常它们会为一个分片做一主两从并加上高可用)，装100+个MySQL今晚加班不？ 配100+个主从今晚加班不？ 不要忘记还要给它们加
   高可用呢？ 好吧这只是测试环境生产环境和测试环境是1:1的，那接下来几天加班不？ 对于生产通常还要加备份，监控那接下来几天加班不？

   **这样的话DBA的工具不应该只是能输出高质量的产出，应该还要解放生产力，有排量管理的能力。**

   ---

3. ## 经济
   **mysqltools 是开源的&免费的&高质量的MySQL数据管理工具**

   ---

4. ## 技术介绍
   1、mysqltools的高质量源自于**蒋乐兴**也就是我写出来的高质量的play-book

   2、mysqltools的高效源自于**ansible**这个排量管理工具

   3、1 , 2 基本上解决了原生MySQL的环境(**单机**、**master -->slave**、**mysql-group-replication** 、**multi-source-replication**)的安装部署

   4、mysqltools在为MySQL做**高可用**时采用的是**MHA**这个方案，**读写分离用**的是**MyCAT**

   5、mysqltools在**备份**时支持到了 **xtrabackup**,**mysql enterprise backup**,**mysqldump**

   6、mysqltools在**监控**MySQL时用的是**zabbix**

   7、其它开源工具无法满足的功能通常自己编写**Python** 程序实现

   mysqltools的定位是一个**集中化管理平台**你只要**在一台主机上安装好mysqltools就可以了**，其它主机作为被管理都的角色。由于mysqltools是基于**Python-3.x**开发
   出来的所以你的**主控机**上应该事先安装好python-3.x、还要安装上ansible。 好在mysqltools已经包含有所有**Python**和**ansible**所有的包。

   ---

## 安装mysqltools

   假设我们有如下一套环境、把**172.16.192.131**这台主机作为主控机.
   
   **角色**     | **ip地址**         | **系统版本**   |
   -----------:|:-------------------|--------------|
   主控机       | 172.16.192.131     |centos-7.4    |
   被控机       | 172.16.192.132     |centos-7.4    |
   ...         | ...                |centos-7.x    |

   1. ### 安装前的准备
      1): **你的主控机上要配置有yum**、因为mysqltools要源码编译安装Python-3.6.2、这就涉及gcc ... 等依赖
   
      2): **有主控机的root账号(安装软件时会用到)**
   
      3): **被控机上也要配置好yum**
   
   
      ---

   2. ### 下载并解压
      **mysqltools是开源在github上的、下载地址如下：https://github.com/Neeky/mysqltools/archive/master.zip** 
   
      linux可以直接执行如下命令完成下载并解压到/usr/local/
   
      ```bash
      cd /tmp/
      wget https://github.com/Neeky/mysqltools/archive/master.zip &
   
      ll -h /tmp/                                                                           
      -rwxr-xr-x. 1 root  root  194M 3月  23 11:52 master.zip
   
      unzip master.zip
   
      mv mysqltools-master /usr/local/mysqltools
      ```
   
      ---

   3. ### 安装Python
      **mysqltools包含了Python的自动化安装脚本、前提是yum已经可用**
   
      ```bash
      cd /usr/local/mysqltools/deploy/packages/python/
      bash install.sh
   
      ```
      安装成功后的最后几行输出如下：
      ```bash
      Collecting setuptools
      Collecting pip
      Installing collected packages: setuptools, pip
      Successfully installed pip-9.0.1 setuptools-28.8.0
      ```
   
      检查python3是否安装成功
      ```bash
      source /etc/profile
    
      python3 --version
      Python 3.6.2
      ```
   
      ---
   
   4. ### 安装ansible
      **ansible和它相关的依赖我都打包到mysqltools中了、也和上面安装python一样一行命令就行**
   
      ```bash
      source /etc/profile
      cd /usr/local/mysqltools/deploy/packages/ansible
      bash install.sh 
   
      ```
      安装成功后可以看到如下输出
      ```bash
      Using /usr/local/python-3.6.2/lib/python3.6/site-packages
      Finished processing dependencies for ansible==2.4.0.0
      ```
   
      ---

   5. ### 配置ansible和mysqltools
      1): **增加ansible的配置文件**

      ```bash
      # 增加ansible的配置文件
      mkdir -p /etc/ansible
      touch /etc/ansible/hosts
      ```
      /etc/ansible/hosts文件如下：
      ```
      host_131 ansible_user=root ansible_host=172.16.192.131
      host_132 ansible_user=root ansible_host=172.16.192.132
      ```

      ---

      2): **配置主控机与被控机之间的ssh信任**

      ```bash
      ssh-keygen
      ssh-copy-id root@172.16.192.131
      ssh-copy-id root@172.16.192.132
      ```
      命令输出大致如下：
      ```bash
      ssh-keygen # 一直回车就能生成钥匙对了
      Generating public/private rsa key pair.
      Enter file in which to save the key (/root/.ssh/id_rsa): 
      Enter passphrase (empty for no passphrase): 
      Enter same passphrase again: 
      Your identification has been saved in /root/.ssh/id_rsa.
      Your public key has been saved in /root/.ssh/id_rsa.pub.
      The key fingerprint is:
      SHA256:D9kR6/ehu5O99p/LRJlZWNqwZ0tzU4+jvPegq7j/Pq8 root@studio2018
      The keys randomart image is:
      +---[RSA 2048]----+
      |          .   . o|
      |           o   Oo|
      |          o   *+B|
      |         + o ..+X|
      |        S o + .* |
      |         o . +.. |
      |          . oo+. |
      |         .  ++=o.|
      |        ooo+EOo**|
      +----[SHA256]-----+
   
   
      ssh-copy-id root@172.16.192.131 # 回答yes、然后输入目标主机的root密码
      /usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/root/.ssh/id_rsa.pub"
      The authenticity of host '172.16.192.131 (172.16.192.131)' can't be established.
      ECDSA key fingerprint is SHA256:qdoqi3B2aqO3ssOIphwOiWLywSlAoflX2YH+LCG7T/E.
      ECDSA key fingerprint is MD5:8f:78:6e:20:ab:d0:2a:6b:c0:1a:e5:09:ac:82:7d:04.
      Are you sure you want to continue connecting (yes/no)? 
      root@172.16.192.131's password: 
      
      Number of key(s) added: 1
      
      Now try logging into the machine, with:   "ssh 'root@172.16.192.131'"
      and check to make sure that only the key(s) you wanted were added.
   
      .... ....
   
      ```
   
      ---

      3): **测试ansible是否配置成功**
      ```bash
      ansible -m ping host_132
   
      host_132 | SUCCESS => {
          "changed": false,
          "failed": false,
          "ping": "pong"
      }
      ```
   
      ---

      4): **配置mysqltools**
   
      mysqltools的配置文件是**mysqltools/config.yaml** 它是一个yaml格式的文件；配置项中最基本的有**mtls_base_dir、mysql_packages_dir、mysql_package**
   
      1、**mtls_base_dir用于配置mysqltools的安装路径**：在[下载并解压](#下载并解压)这个步骤中我们把mysqltools解压到了/usr/local/、所以mtls_base_dir的值就应该等   于"/usr/local/mysqltools/"
   
      2、**mysql_packages_dir用于配置MySQL二进制安装包保存的位置**：MySQL的安装包有600+MB、出于体量的原因mysqltools并没有直接把打包MySQL的二进制安装包、而是留有   mysql_packages_dir这个配置项，mysqltools会从这个目录中去找MySQL的二进制安装包，如果你把它设置成了/usr/local/src/mysql/那么MySQL的安装包就要保存到这里。
   
      3、**mysql_package用于配置MySQL安装包的名字**、有这个变量的因为是为了，可以做到有多个不同的MySQL的版本共存、默认值为   mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
      
      config.yaml的关键内容大致如下：
      ```yaml
      mtls_base_dir: /usr/local/mysqltools/
      mysql_packages_dir: /usr/local/src/mysql/
      mysql_package: mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
      ```
      注意：在mysqltools中所有的目录都是要以'/'号结尾的
   
      **如果你正确的完成了mysqltools相关的配置那么config.yaml看起来就应该是这样的**
      ```
      ---
      #----------------------------------mysqltools全局配置文件---------------------
      # section 1 #mysqltools所在的目录
      mtls_base_dir: /usr/local/mysqltools/
      #           #mysqltool自带的各类软件的安装文件所在路径(相对路径)
      mtls_packages: deploy/packages/
      #           #mysqltool自带的python脚本、下发到被控主机时所保存的路径
      mtls_client_base_dir: /usr/local/
      
      
      #  section 2  #mysqltools自带的各类软件安装文件 的全名、设置这些变量的作用是方便版本共存、mysql不在这里设置是因为
      #             #mysql的安装包太大了，mysqltools并没有把它打包进来         
      mtls_apr: apr-1.6.2.tar.gz
      mtls_apr_util: apr-util-1.6.0.tar.gz
      mtls_httpd: httpd-2.4.28.tar.gz
      mtls_php: php-5.6.31.tar.gz
      mtls_zabbix: zabbix-3.4.3.tar.gz
      mtls_python: python-3.6.2.tar.xz
      mtls_mysql_connector_python: mysql-connector-python-2.1.5.tar.gz
      mtls_mycat: mycat-server-1.6.5-linux.tar.gz
      mtls_mha_node: install_mha_node-for-centos-7.2.tar.gz
      mtls_mha_manager: install_mha_manager-for-centos7.2.tar.gz
      mtls_git: git-2.9.5.tar.gz
      mtls_nginx: nginx-1.13.7.tar.gz
      mtls_sysbench: sysbench-1.1.0.tar.gz
      mtls_meb: meb-4.1.0-linux-glibc2.5-x86-64bit.tar.gz
      
      #mysql与php-5.6.x 是否要同时安装在一台主机上、如果是就要把这个设置成yes、以为php导出mysqclient_r.so文件
      mtls_with_php: 1
      #通过ansible在被控机上安装python-3.x的时候，是否自动安装好mysql-connector-python
      mtls_with_mysql_conntor_python: 1
      #是否给mysql用户加密码
      mtls_make_mysql_secure: 1
      #
      mtls_with_mysql_group_replication: 0
      #----------------------------------mysqltools全局配置文件---------------------
      
      
      ####
      #### mysql 相关的配置
      ####
      #mysql 安装包所在的目录
      mysql_packages_dir: /usr/local/src/mysql/
      #mysql 安装包的名字
      mysql_package: mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
      #linux 系统级别mysql用户相关信息
      mysql_user: mysql
      mysql_group: mysql
      mysql_user_uid: 3306
      mysql_user_gid: 3306
      #mysql 安装目录
      mysql_base_dir: /usr/local/mysql/
      #mysql 真正的datadir就会是mysql_data_dir_base+mysql_port
      mysql_data_dir_base: /database/mysql/data/
      mysql_port: 3306
      mysql_root_password: mtls0352
      mysql_zabbix_password: mtls
      mysql_rple_user: rple
      mysql_rple_password: mtls0352
      mysql_mha_user: mha
      mysql_mha_password: mtls0352
      mysql_app_user: appuser
      mysql_app_password: mtls0352
      mysql_monitor_user: monitor
      mysql_monitor_password: monitor0352
      #mysql 配置文件模版
      mysql_binlog_format: row
      mysql_innodb_log_files_in_group: 8
      mysql_innodb_log_file_size: 128M
      mysql_innodb_log_buffer_size: 128M
      mysql_innodb_open_files: 65535
      #mysql 
      
      ####
      #### zabbix 相关的配置
      #####
      zabbix_server_ip: 172.16.192.10
   
      ```
      为了你能更加方便的使用mysqltools我提供了份linux上的标准配置文件**mysqltools/config.yaml-for-linux** 使用时只要把它重命名成**cofnig.yaml**就行了
   
      ---

      5): **下载MySQL**
   
      根据上面的配置可以知道MySQL的安装包要保存到**/usr/local/src/mysql/**目录下、包的版本为mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
      
      下载地址如下：https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
       
      ```bash
      cd /usr/local/src/mysql/
      wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
      
   
      ```

---

## mysqltools快速开始
   **mysqltools的目录组织是根据它的功能来定的**
   1. ### mysqltools目录介绍

      ```
      cd /usr/local/mysqltools/
      tree ./
      
      ├── backup                        # 与备份相关的功能
      │   ├── meb
      │   ├── extrabackup  
      │   └── mysqldump
      ├── config.yaml                   # 配置文件
      ├── config.yaml-for-linux         
      ├── deploy                        # 自动化安装部署各类环境
      │   ├── ansible                       # 通过ansible完成各类环境的自动化安装
      │   │   ├── mha
      │   │   ├── mycat
      │   │   |..........
      │   │   |..........
      │   │   ├── mysql
      │   │   └── zabbix
      │   └── packages                  # 为了方便使用mysqltools内置的一些第三方源码包
      │       ├── ansible
      |       |............
      |       |............
      │       └── zabbix
      ├── docs                          # 其它文档
      ├── monitor                       # 监控相关的功能
      ├── mysqltoolsclient              # mysqltools客户端脚本
      │   ├── memoryAnalyze.py
      │   ├── monitor.py
      │   └── mtls                          
      ├── readme2.md                    # mysqltools官方文档第二版
      ├── README.md                     # mysqltools官方文档第一版
      ├── trashCan                      # 垃圾箱
      └── tuning                        # 常用SQL分析语句
      ```
      
      ---

   2. ### 自动化mysql单实例安装
      **mysqltools/deploy/ansible/** 目录下的每一个子目录都对应一类软件环境的自动化安装、我们这次是要安装MySQL所以应该进入到mysql子目录
   
      1. #### 进入mysql功能目录
          ```
          cd /usr/local/mysqltools/deploy/ansible/mysql/
          ll 
          ```
          输出如下
          ```
          总用量 24
          drwxr-xr-x. 2 root root 4096 3月  19 15:01 common     # 通用组件
          -rw-r--r--. 1 root root  836 3月  19 15:01 install_group_replication.yaml         # 自动化安装mysql group replication
          -rw-r--r--. 1 root root  889 3月  19 15:01 install_master_slaves.yaml             # 自动化安装mysql 主从复制环境
          -rw-r--r--. 1 root root  924 3月  19 15:01 install_multi_source_replication.yaml  # 自动化安装mysql 多源复制
          -rw-r--r--. 1 root root  772 3月  26 13:20 install_single_mysql.yaml              # 自动化安装mysql 单机实例
          drwxr-xr-x. 3 root root  203 3月  19 15:01 template   # 通用模板        
          -rw-r--r--. 1 root root  892 3月  19 15:01 upgrad_single_mysql.yaml               # 自动化升级MySQL(不推荐)
          drwxr-xr-x. 2 root root   99 3月  19 15:01 vars       # 通用变量 
          ```
          由于/usr/local/mysqltools/deploy/ansible/下的每一个子目录都实现某一类功能，于是我们约定/usr/local/mysqltools/deploy/ansible/下的子目录叫**功能目录**,   功能目录下的会包含若干.yaml文件，每一个文件都实现了特定的功能，如install_single_mysql.yaml实现了自动化安装MySQL的功能。
       
       ---
       
      2. #### 指定安装的目标主机

         install_single_mysql.yaml的前几行大致如下

         ```yaml
         ---
          - hosts: cstudio
            remote_user: root
            become_user: yes
            vars_files:
             - ../../../config.yaml
            tasks:
             - name: create user and config file
               import_tasks: common/create_user_and_config_file.yaml
         
         ```
         其中的**- hosts: cstudio** 这一行中的cstudio 就是用来指定目标主机或主机组的，也就是说它指明了install_single_mysql.yaml将在哪里安装MySQL单机

         假设我们要在host_132这台主机上安装单机的MySQL所以我们要把cstudio改成host_132、注意这里的host_132引用的是/etc/ansible/hosts文件、修改后的install_single_mysql.yaml文件的前几行大致如下

         ```yaml
         ---
          - hosts: host_132
            remote_user: root
            become_user: yes
            vars_files:
             - ../../../config.yaml
            tasks:
             - name: create user and config file
               import_tasks: common/create_user_and_config_file.yaml
         ```
         
         ---
   
      3. #### 执行自动化安装
         正如上文所说的mysqltools是借助ansible来完成自动化的、那么我们调用ansible来完成自动化安装MySQL
         ```bash
         ansible-playbook install_single_mysql.yaml 
         
         ```
         输出如下

         ```
         
         PLAY [host_132] *********************************************************************************************
         
         TASK [Gathering Facts] **************************************************************************************
         ok: [host_132]
         
         TASK [create mysql user] ************************************************************************************
         changed: [host_132]
         
         TASK [create and config /etc/my.cnf] ************************************************************************
         changed: [host_132]
         
         TASK [install libaio-devel] *********************************************************************************
         ok: [host_132]
         
         TASK [install numactl-devel] ********************************************************************************
         ok: [host_132]
         
         TASK [transfer mysql install package to remote host and unarchive to /usr/local/] ***************************
         changed: [host_132]
         
         TASK [change owner to mysql user] ***************************************************************************
         changed: [host_132]
         
         TASK [make link /usr/local/mysql-xx.yy.zz to /usr/local/mysql] **********************************************
         changed: [host_132]
         
         TASK [export mysql share object (*.os)] *********************************************************************
         ok: [host_132]
         
         TASK [load share object] ************************************************************************************
         changed: [host_132]
         
         TASK [export path env variable] *****************************************************************************
         ok: [host_132]
         
         TASK [export path env to /root/.bashrc] *********************************************************************
         ok: [host_132]
         
         TASK [make link /usr/local/mysql-xx.yy.zz to /usr/local/mysql] **********************************************
         ok: [host_132]
         
         TASK [create libmysqlclient_r.so file for php-5.6] **********************************************************
         changed: [host_132]
         
         TASK [create datadir] ***************************************************************************************
         changed: [host_132]
         
         TASK [initialize-insecure] **********************************************************************************
         changed: [host_132]
         
         TASK [create systemd config file] ***************************************************************************
         changed: [host_132]
         
         TASK [start mysql(sytemctl)] ********************************************************************************
         changed: [host_132]
         
         TASK [config mysql.service start up on boot] ****************************************************************
         ok: [host_132]
         
         TASK [config sysv start script] *****************************************************************************
         skipping: [host_132]
         
         TASK [start mysql(service)] *********************************************************************************
         skipping: [host_132]
         
         TASK [config mysql.service start up on boot] ****************************************************************
         skipping: [host_132]
         
         TASK [transfer sleep script to /tmp/] ***********************************************************************
         changed: [host_132]
         
         TASK [sleep 15 seconds] *************************************************************************************
         changed: [host_132]
         
         TASK [remove /tmp/sleep_15.sh] ******************************************************************************
         changed: [host_132]
         
         TASK [transfer sql statement to remonte] ********************************************************************
         changed: [host_132]
         
         TASK [make mysql secure] ************************************************************************************
         changed: [host_132]
         
         TASK [remove temp file /tmp/make_mysql_secure.sql] **********************************************************
         changed: [host_132]
         
         PLAY RECAP **************************************************************************************************
         host_132                   : ok=25   changed=17   unreachable=0    failed=0 
         ```

         测试MySQL是否安装成功
         ```bash
         mysql -uroot -pmtls0352 
         ```
         输出如下
         ```                                                            
         mysql: [Warning] Using a password on the command line interface can be insecure.
         Welcome to the MySQL monitor.  Commands end with ; or \g.
         Your MySQL connection id is 3
         Server version: 5.7.21-log MySQL Community Server (GPL)
         
         Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
         
         Oracle is a registered trademark of Oracle Corporation and/or its
         affiliates. Other names may be trademarks of their respective
         owners.
         
         Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
         
         mysql> 
         ```
         
         ---

   3. ### 谈谈mysqltools如何实现高效 
      从上面的[自动化mysql单实例安装](#自动化mysql单实例安装)来看自动化安装的过程中我们只执行了**3个命令**
      ```bash
      cd 
      vim
      ansible-playbook
      ```
      其中 1、cd 用于进行mysql功能目录 2、vim用于指定playbook的目标主机或主机组 3、执行playbook

      高效的关键有两点：

      **1):自动化安装的方式相对于人肉来说要快很多**

      **2):支持排量操作也就是说可能同时在多台主机上执行、只要在hosts: 变量的值是一个主机组就行了**

      ---

   4. ### 谈谈mysqltools如何实现高质量

      **1、mysqltools是流程化的，如上面的安装MySQL就包含20+的小步骤，尽量做到面面俱到**  

      **2、mysqltools尽可能的在各个小步骤中都保持高的质量、比如/etc/my.cnf各个参数的配置都会根据主机当前的cpu & 内存进行配置**

      以下是一个host_132的/etc/my.cnf **这些都是由mysqltools针对单机环境动态生成的**

      ```cnf
      [mysql]
      auto-rehash
      
      
      [mysqld]
      ####: for global
      user                                =mysql                          #   mysql
      basedir                             =/usr/local/mysql/              #   /usr/local/mysql/
      datadir                             =/database/mysql/data/3306      #   /usr/local/mysql/data
      server_id                           =653                            #   0
      port                                =3306                           #   3306
      character_set_server                =utf8                           #   latin1
      explicit_defaults_for_timestamp     =off                            #    off
      log_timestamps                      =system                         #   utc
      socket                              =/tmp/mysql.sock                #   /tmp/mysql.sock
      read_only                           =0                              #   off
      skip_name_resolve                   =1                              #   0
      auto_increment_increment            =1                              #   1
      auto_increment_offset               =1                              #   1
      lower_case_table_names              =1                              #   0
      secure_file_priv                    =                               #   null
      open_files_limit                    =65536                          #   1024
      max_connections                     =256                            #   151
      thread_cache_size                   =128                              #   9
      table_open_cache                    =4096                           #   2000
      table_definition_cache              =2000                           #   1400
      table_open_cache_instances          =32                             #   16
      
      ####: for binlog
      binlog_format                       =row                          #     row
      log_bin                             =mysql-bin                      #   off
      binlog_rows_query_log_events        =on                             #   off
      log_slave_updates                   =on                             #   off
      expire_logs_days                    =7                              #   0
      binlog_cache_size                   =65536                          #   65536(64k)
      binlog_checksum                     =none                           #   CRC32
      sync_binlog                         =1                              #   1
      slave-preserve-commit-order         =ON                             #   
      
      ####: for error-log
      log_error                           =err.log                        #   /usr/local/mysql/data/localhost.localdomain.err
      
      general_log                         =off                            #   off
      general_log_file                    =general.log                    #   hostname.log
      
      ####: for slow query log
      slow_query_log                      =on                             #    off
      slow_query_log_file                 =slow.log                       #    hostname.log
      log_queries_not_using_indexes       =on                             #    off
      long_query_time                     =2.000000                       #    10.000000
      
      ####: for gtid
      gtid_executed_compression_period    =1000                          #    1000
      gtid_mode                           =on                            #    off
      enforce_gtid_consistency            =on                            #    off
      
      
      ####: for replication
      skip_slave_start                    =0                              #   
      master_info_repository              =table                         #    file
      relay_log_info_repository           =table                         #    file
      slave_parallel_type                 =logical_clock                 #    database | LOGICAL_CLOCK
      slave_parallel_workers              =4                             #    0
      rpl_semi_sync_master_enabled        =1                             #    0
      rpl_semi_sync_slave_enabled         =1                             #    0
      rpl_semi_sync_master_timeout        =1000                          #    1000(1 second)
      plugin_load_add                     =semisync_master.so            #
      plugin_load_add                     =semisync_slave.so             #
      binlog_group_commit_sync_delay      =500                          #    500(0.05%秒)、默认值0
      binlog_group_commit_sync_no_delay_count = 13                        #    0
      
      
      ####: for innodb
      default_storage_engine                          =innodb                     #   innodb
      default_tmp_storage_engine                      =innodb                     #   innodb
      innodb_data_file_path                           =ibdata1:64M:autoextend     #   ibdata1:12M:autoextend
      innodb_temp_data_file_path                      =ibtmp1:12M:autoextend      #   ibtmp1:12M:autoextend
      innodb_buffer_pool_filename                     =ib_buffer_pool             #   ib_buffer_pool
      innodb_log_group_home_dir                       =./                         #   ./
      innodb_log_files_in_group                       =8                          #   2
      innodb_log_file_size                            =128M                        #  50331648(48M)
      innodb_file_per_table                           =on                         #   on
      innodb_online_alter_log_max_size                =128M                  #   134217728(128M)
      innodb_open_files                               =65535                       #   2000
      innodb_page_size                                =16k                        #   16384(16k)
      innodb_thread_concurrency                       =0                          #   0
      innodb_read_io_threads                          =4                          #   4
      innodb_write_io_threads                         =4                          #   4
      innodb_purge_threads                            =4                          #   4
      innodb_print_all_deadlocks                      =on                         #   off
      innodb_deadlock_detect                          =on                         #   on
      innodb_lock_wait_timeout                        =50                         #   50
      innodb_spin_wait_delay                          =6                          #   6
      innodb_autoinc_lock_mode                        =2                          #   1
      innodb_io_capacity                              =200                        #   200
      innodb_io_capacity_max                          =2000                       #   2000
      #--------Persistent Optimizer Statistics
      innodb_stats_auto_recalc                        =on                         #   on
      innodb_stats_persistent                         =on                         #   on
      innodb_stats_persistent_sample_pages            =20                         #   20
      innodb_buffer_pool_instances                    =1
      innodb_adaptive_hash_index                      =on                         #   on
      innodb_change_buffering                         =all                        #   all
      innodb_change_buffer_max_size                   =25                         #   25
      innodb_flush_neighbors                          =1                          #   1
      #innodb_flush_method                             =                           #  
      innodb_doublewrite                              =on                         #   on
      innodb_log_buffer_size                          =128M                        #  16777216(16M)
      innodb_flush_log_at_timeout                     =1                          #   1
      innodb_flush_log_at_trx_commit                  =1                          #   1
      innodb_buffer_pool_size                         =1152M                  #       134217728(128M)
      autocommit                                      =1                          #   1
      #--------innodb scan resistant
      innodb_old_blocks_pct                           =37                         #    37
      innodb_old_blocks_time                          =1000                       #    1000
      #--------innodb read ahead
      innodb_read_ahead_threshold                     =56                         #    56 (0..64)
      innodb_random_read_ahead                        =OFF                        #    OFF
      #--------innodb buffer pool state
      innodb_buffer_pool_dump_pct                     =25                         #    25 
      innodb_buffer_pool_dump_at_shutdown             =ON                         #    ON
      innodb_buffer_pool_load_at_startup              =ON                         #    ON
      
      
      
      
      ####  for performance_schema
      performance_schema                                                      =on    #    on
      performance_schema_consumer_global_instrumentation                      =on    #    on
      performance_schema_consumer_thread_instrumentation                      =on    #    on
      performance_schema_consumer_events_stages_current                       =on    #    off
      performance_schema_consumer_events_stages_history                       =on    #    off
      performance_schema_consumer_events_stages_history_long                  =off   #    off
      performance_schema_consumer_statements_digest                           =on    #    on
      performance_schema_consumer_events_statements_current                   =on    #    on
      performance_schema_consumer_events_statements_history                   =on    #    on
      performance_schema_consumer_events_statements_history_long              =off   #    off
      performance_schema_consumer_events_waits_current                        =on    #    off
      performance_schema_consumer_events_waits_history                        =on    #    off
      performance_schema_consumer_events_waits_history_long                   =off   #    off
      performance-schema-instrument                                           ='memory/%=COUNTED'
      ```
      由上面的内容可以看到mysqltools生成的/etc/my.cnf在各个方面都是比较全面的(配置是在一个2core 2G的vm虚拟机上复制出来的)
   
      ---

## 联系我

   **赞助/交流/技术支持**

   如果我分享的知识对你有用、可以打赏任意金额；这些也是我花了许多业余时间才写出来的，也许可以请我喝一杯咖啡。如果你需要一名数据库建模、运维方面的专家也可也联系我、当然技术方面的交流也是欢迎的。

   <img src="./docs/imgs/jianglexing_alipay.JPG" width="240px" />
   <img src="./docs/imgs/jianglexing_donate_wechart.jpg" width="240px" />
   <img src="./docs/imgs/jiangleixng_wechart.jpg" width="240px" />
   
   ---

## mysql原生环境安装
   **原生环境安装主要包含 1、MySQL单机 2、主从复制 3、多源复制 4、组复制(mysql-group-replication)**
   如果这是你第一次使用mysqltools可以从[mysqltools快速开始](#mysqltools快速开始)章节开启你的mysqltools之旅

   1. ### mysql单机
      **1):进入mysql功能目录**
      ```bash
      cd /usr/local/mysqltools/deploy/ansible
      
      cd mysql  #进入mysql功能目录
      ```

      **2):指定install_single_mysql.yaml中的目标主机**

      假设我要在host_132主机上安装mysql那么install_single_mysql.yaml文件中的hosts变量应该设置为host_132
      ```yaml
      ---
       - hosts: host_132
      ```
      yaml格式对空间是非常敏感的、注意“:”后面是有个空格的

      **3):执行自动化安装**
      ```bash
      ansible-playbook install_single_mysql.yaml
      ```
      输出省略 ... ...

      **4):验证mysql是否成功安装**
      ```bash
      mysql -uroot -pmtls0352
      ```
      输出如下
      ```
      mysql: [Warning] Using a password on the command line interface can be insecure.
      Welcome to the MySQL monitor.  Commands end with ; or \g.
      Your MySQL connection id is 2
      Server version: 5.7.21-log MySQL Community Server (GPL)
      
      Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.
      
      Oracle is a registered trademark of Oracle Corporation and/or its
      affiliates. Other names may be trademarks of their respective
      owners.
      
      Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
      
      mysql>
      ```
      root用户的密码是在mysqltools/config.yaml文件中的mysql_root_password配置项指定的、你可以根据你的要求定制

      ---

   2. ### mysql主从复制  


      ---




---    
    






   





