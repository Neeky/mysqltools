create user backup@'127.0.0.1' identified by 'DX3906';
create user backup@'localhost' identified by 'DX3906';

grant reload,lock tables on *.* to backup@'127.0.0.1';
grant replication client on *.* to backup@'127.0.0.1';
grant create tablespace  on *.* to backup@'127.0.0.1';
grant process            on *.* to backup@'127.0.0.1';
grant super              on *.* to backup@'127.0.0.1';
grant create,insert,select      on percona_schema.xtrabackup_history to backup@'127.0.0.1';

grant reload,lock tables on *.* to backup@'localhost';
grant replication client on *.* to backup@'localhost';
grant create tablespace  on *.* to backup@'localhost';
grant process            on *.* to backup@'localhost';
grant super              on *.* to backup@'localhost';
grant create,insert,select      on percona_schema.xtrabackup_history to backup@'localhost';

-- for mysqlbackup
grant create,insert,drop,update               on mysql.backup_progress to backup@'127.0.0.1';
grant create,insert,drop,update,select,alter  on mysql.backup_history  to backup@'127.0.0.1';

grant create,insert,drop,update               on mysql.backup_progress to backup@'localhost';
grant create,insert,drop,update,select,alter  on mysql.backup_history  to backup@'localhost';

grant select on performance_schema.replication_group_members to backup@'127.0.0.1';
grant select on performance_schema.replication_group_members to backup@'localhost';

-- mysqltools在并没有引入mysqlbackup TTS相关功能，这一功能要求的权限通常来说是比较敏感的，而且也不常用，mysqltools在些不支持它。

