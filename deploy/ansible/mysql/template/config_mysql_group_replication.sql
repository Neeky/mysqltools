
set sql_log_bin=0;
create user mgr_usr@'%' identified by 'mgr10352';
grant replication slave,replication client on *.* to mgr_usr@'%';
create user mgr_usr@'127.0.0.1' identified by 'mgr10352';
grant replication slave,replication client on *.* to mgr_usr@'127.0.0.1';
create user mgr_usr@'localhost' identified by 'mgr10352';
grant replication slave,replication client on *.* to mgr_usr@'localhost';
set sql_log_bin=1;

change master to 
    master_user='mgr_usr',
    master_password='mgr10352'
    for channel 'group_replication_recovery';

install plugin group_replication soname 'group_replication.so';

{% if mysql_mgr_hosts[0] in ansible_all_ipv4_addresses %}
    set global group_replication_bootstrap_group=on;
    start group_replication;
    set global group_replication_bootstrap_group=off;
{% else %}
    select sleep(15);
    start group_replication;
{% endif %}
