#mysqlbackup 在备份时数据库层面用到的用户


-- 001 创建mysqlbackup备份工具所用的用户
create user mebuser@'127.0.0.1' identified by 'Pass@352';
grant reload,replication client,super,process on *.* to mebuser@'127.0.0.1';
grant create,insert,drop,update on mysql.backup_progress to mebuser@'127.0.0.1';
grant create,insert,select,drop,update on mysql.backup_history to mebuser@'127.0.0.1';
grant lock tables,select,create,alter on *.* to mebuser@'127.0.0.1';
grant create,insert,drop,update on mysql.backup_sbt_history to mebuser@'127.0.0.1';

create user mebuser@'localhost' identified by 'Pass@352';
grant reload,replication client,super,process on *.* to mebuser@'localhost';
grant create,insert,drop,update on mysql.backup_progress to mebuser@'localhost';
grant create,insert,select,drop,update on mysql.backup_history to mebuser@'localhost';
grant lock tables,select,create,alter on *.* to mebuser@'localhost';
grant create,insert,drop,update on mysql.backup_sbt_history to mebuser@'localhost';





