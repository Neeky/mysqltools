set sql_log_bin=0;
create user rpl_user@'%' identified by '123456';
grant replication slave,replication client on *.* to rpl_user@'%';
create user rpl_user@'127.0.0.1' identified by '123456';
grant replication slave,replication client on *.* to rpl_user@'127.0.0.1';
create user rpl_user@'localhost' identified by '123456';
grant replication slave,replication client on *.* to rpl_user@'localhost';
set sql_log_bin=1;

change master to 
        master_user='rpl_user',
        master_password='123456'
        for channel 'group_replication_recovery';

install plugin group_replication soname 'group_replication.so';

set global group_replication_bootstrap_group=on;
start group_replication;
set global group_replication_bootstrap_group=off;


