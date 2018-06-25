{% if 'mysql-8.0' in mysql_package %}
set sql_log_bin=0;
    create database tempdb charset utf8;
    create user sysbench@'%' identified with mysql_native_password by 'sysbench';
    grant all on tempdb.* to sysbench@'%';   
set sql_log_bin=1;

{% else %}
set sql_log_bin=0;
    create database tempdb charset utf8;
    create user sysbench@'%' identified by 'sysbench';
    grant all on tempdb.* to sysbench@'%';
set sql_log_bin=1;
{% endif %}