{% if 'mysql-5.6' in mysql_package %}
set sql_log_bin=0;
    update mysql.user set password=password('{{ mysql_root_password }}') where user='root';
    create user {{mysql_monitor_user}}@'127.0.0.1' identified by '{{ mysql_monitor_password }}' ;
    flush privileges; 
set sql_log_bin=1;

{% else %}

set sql_log_bin=0;
    create user {{mysql_monitor_user}}@'127.0.0.1' identified by '{{ mysql_monitor_password }}' ;
    
    alter user root@'localhost' identified by '{{ mysql_root_password }}' ;
    create user root@'127.0.0.1' identified by '{{ mysql_root_password }}';
    grant all on *.* to root@'127.0.0.1' with grant option;

set sql_log_bin=1;

{% endif %}

