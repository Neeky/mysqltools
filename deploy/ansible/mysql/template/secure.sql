alter user root@'localhost' identified by '{{ mysql_root_password }}' ;
create user root@'127.0.0.1' identified by '{{ mysql_root_password }}';
grant all on *.* to root@'127.0.0.1' with grant option;