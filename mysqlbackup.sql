#mysqlbackup 在备份时数据库层面用到的用户


-- 001 创建备份用户
create user backupuser@'127.0.0.1' identified by '1234567890';
grant reload,replication client,super,process on *.* to backupuser@'127.0.0.1';
grant create,insert,drop,update on mysql.backup_progress to backupuser@'127.0.0.1';
grant create,insert,select,drop,update on mysql.backup_history to backupuser@'127.0.0.1';
grant lock tables,select,create,alter on *.* to backupuser@'127.0.0.1';
grant create,insert,drop,update on mysql.backup_sbt_history to backupuser@'127.0.0.1';

create user backupuser@'localhost' identified by '1234567890';
grant reload,replication client,super,process on *.* to backupuser@'localhost';
grant create,insert,drop,update on mysql.backup_progress to backupuser@'localhost';
grant create,insert,select,drop,update on mysql.backup_history to backupuser@'localhost';
grant lock tables,select,create,alter on *.* to backupuser@'localhost';
grant create,insert,drop,update on mysql.backup_sbt_history to backupuser@'localhost';





