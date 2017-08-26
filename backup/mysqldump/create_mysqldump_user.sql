-- 创建一个叫dumper的用户，并赋予它相应的权限，使它可以备份整个mysql实例

create user dumper@'127.0.0.1' identified by 'Pass@352';
grant select on *.* to dumper@'127.0.0.1';
grant show view on *.* to dumper@'127.0.0.1';
grant lock tables on *.* to dumper@'127.0.0.1';
grant trigger on *.* to dumper@'127.0.0.1';