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


