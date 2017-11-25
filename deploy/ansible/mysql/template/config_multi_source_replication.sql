set sql_log_bin=0;
    create user rple_user@'%' identified by 'rple0352';
    grant replication slave,replication client on *.* to rple_user@'%';
    create user rple_user@'127.0.0.1' identified by 'rple0352';
    grant replication slave,replication client on *.* to rple_user@'127.0.0.1';
    create user rple_user@'localhost' identified by 'rple0352';
    grant replication slave,replication client on *.* to rple_user@'localhost';
set sql_log_bin=1;


{% if slave_ip in ansible_all_ipv4_addresses %}
    {% for ip in master_ips %}
    change master to 
            master_host='{{ip}}',
            master_user='rple_user',
            master_port={{mysql_port}},
            master_password='rple0352',
            master_auto_position=1 
            for channel '{{"master" + (loop.index | string)}}' ;
        start slave for channel '{{"master" + (loop.index | string)}}'; 
    
    {% endfor %}
{% endif %}