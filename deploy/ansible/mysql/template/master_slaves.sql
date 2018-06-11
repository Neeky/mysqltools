{% if master_ip in ansible_all_ipv4_addresses %}
create user {{mysql_rple_user}}@'%' identified by '{{mysql_rple_password}}';
grant replication slave,replication client on *.* to {{mysql_rple_user}}@'%';

{% else %}
select sleep(10);

set @@global.read_only=on;

change master to
    master_host='{{master_ip}}',
    master_port={{mysql_port}},
    master_user='{{mysql_rple_user}}',
    master_password='{{mysql_rple_password}}',
    master_auto_position=1;

start slave;
{% endif %}
