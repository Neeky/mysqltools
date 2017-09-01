#!/bin/bash

#config information ...

username=mysql
datadir=/database/mysql/data/3306
mysqlversion=mysql-5.7.18-linux-glibc2.5-x86_64
installpacket=mysql-5.7.18-linux-glibc2.5-x86_64.tar.gz

#第一步：增加mysql用户
useradd mysql

#第二步：创建数据目录
mkdir -p $datadir && chown -R $username:$username $datadir

#第三步：解压安装介质
tar -xzvf $installpacket -C /usr/local/
ln -s /usr/local/$mysqlversion /usr/local/mysql

#第四步：初始化数据库
/usr/local/mysql/bin/mysqld --defaults-file=/etc/my.cnf --user=$username \
  --basedir=/usr/local/mysql/ --datadir=$datadir --initialize-insecure

#第五步：启动服务
cd /usr/local/mysql/
./bin/mysqld_safe --

#第五步：配置服务
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
chkconfig mysqld on
service mysqld start

#第六步：用户管理
/usr/local/mysql/bin/mysql -e'create user appuser@"%" identified by "Pass@123";'
/usr/local/mysql/bin/mysql -e'alter user root@"localhost" identified by "Root@123";'


