create database if not exists zabbix char set utf8;
use zabbix;
create user if not exists zabbix@'%' identified by '{{ mysql_zabbix_password }}';
create user if not exists zabbix@'localhost' identified by '{{ mysql_zabbix_password }}';
create user if not exists zabbix@'127.0.0.1' identified by '{{ mysql_zabbix_password }}';

grant all on zabbix.* to zabbix@'%';
grant all on zabbix.* to zabbix@'localhost';
grant all on zabbix.* to zabbix@'127.0.0.1';

source /tmp/{{ mtls_zabbix | replace('.tar.gz','')}}/database/mysql/schema.sql ;

source /tmp/{{ mtls_zabbix | replace('.tar.gz','')}}/database/mysql/images.sql ;

source /tmp/{{ mtls_zabbix | replace('.tar.gz','')}}/database/mysql/data.sql ;
