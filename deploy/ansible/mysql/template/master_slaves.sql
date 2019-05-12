{% if master_ip in ansible_all_ipv4_addresses %}
    {% if '8.0' in mysql_package %}
        create user {{mysql_rple_user}}@'%' identified with 'mysql_native_password' by '{{mysql_rple_password}}';
        grant replication slave,replication client on *.* to {{mysql_rple_user}}@'%';
    {% else %}
        create user {{mysql_rple_user}}@'%' identified by '{{mysql_rple_password}}';
        grant replication slave,replication client on *.* to {{mysql_rple_user}}@'%';
    {% endif %}

    flush privileges;

{% else %}
select sleep(17);

set @@global.read_only=on;

change master to
    master_host='{{master_ip}}',
    master_port={{mysql_port}},
    master_user='{{mysql_rple_user}}',
    master_password='{{mysql_rple_password}}',
    master_auto_position=1;

start slave;
{% endif %}
