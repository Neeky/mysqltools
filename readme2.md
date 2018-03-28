
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
- [自动化安装mysql相关环境](#自动化安装mysql相关环境)
  - [单实例安装](#单实例安装)

---


## 概要

总的来说mysqltools源自于工作、一个dba的日常大概包括 数据库安装，读写分离、高可用、负载均衡等环境的配置，
数据库备份策略拟定与实施，数据库相关的监控，数据库优化，故障分析，也有可能参与到数据库建模，SQL的编写。

这样我们就面临两个问题 1、**质量** 质量表现在解决问题的深度(类似问题还会再出现吗？) 2、**效率** 效率表现在你单位时间内解决问题的数量(安装一百个库的用时是一个库的100倍吗？)； 通常这两个目标并不是互斥的，也就是说我们可以两个都做到。


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

3. ### 安装ansible
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

4. ### 配置ansible和mysqltools
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

   1、**mtls_base_dir用于配置mysqltools的安装路径**：在[下载并解压](#下载并解压)这个步骤中我们把mysqltools解压到了/usr/local/、所以mtls_base_dir的值就应该等于"/usr/local/mysqltools/"

   2、**mysql_packages_dir用于配置MySQL二进制安装包保存的位置**：MySQL的安装包有600+MB、出于体量的原因mysqltools并没有直接把打包MySQL的二进制安装包、而是留有mysql_packages_dir这个配置项，mysqltools会从这个目录中去找MySQL的二进制安装包，如果你把它设置成了/usr/local/src/mysql/那么MySQL的安装包就要保存到这里。

   3、**mysql_package用于配置MySQL安装包的名字**、有这个变量的因为是为了，可以做到有多个不同的MySQL的版本共存、默认值为mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
   
   config.yaml的关键内容大致如下：
   ```yaml
   mtls_base_dir: /usr/local/mysqltools/
   mysql_packages_dir: /usr/local/src/mysql/
   mysql_package: mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
   ```
   注意：在mysqltools中所有的目录都是要以'/'号结尾的

   ---

   5): **下载MySQL**

   根据上面的配置可以知道MySQL的安装包要保存到**/usr/local/src/mysql/**目录下、包的版本为mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz

   下载地址如下：https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
   
   ```bash
   cd /usr/local/src/mysql/
   wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.21-linux-glibc2.12-x86_64.tar.gz
   

   ```
   

---




## 自动化安装mysql相关环境

1. ### 单实例安装
   **mysqltools/deploy/ansible/** 目录下的每一个子目录都对应一类软件环境的自动化安装、由于我们这次是要安装MySQL所以应该进入到MySQL子目录

   1): 进入mysql子目录
    ```
    cd /usr/local/mysqltools/deploy/ansible/mysql/
    ll 
    ```
    输出如下
    ```
    总用量 24
    drwxr-xr-x. 2 root root 4096 3月  19 15:01 common
    -rw-r--r--. 1 root root  836 3月  19 15:01 install_group_replication.yaml
    -rw-r--r--. 1 root root  889 3月  19 15:01 install_master_slaves.yaml
    -rw-r--r--. 1 root root  924 3月  19 15:01 install_multi_source_replication.yaml
    -rw-r--r--. 1 root root  772 3月  26 13:20 install_single_mysql.yaml
    drwxr-xr-x. 3 root root  203 3月  19 15:01 template
    -rw-r--r--. 1 root root  892 3月  19 15:01 upgrad_single_mysql.yaml
    drwxr-xr-x. 2 root root   99 3月  19 15:01 vars
    ```

   2): 






   





