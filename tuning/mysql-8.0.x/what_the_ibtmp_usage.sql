-- 机器友好 --
select 
    file_name,                                -- 文件名
    tablespace_name,                          -- 表空间名
    engine,                                   -- 引擎
    initial_size,                             -- 初始大小
    total_extents*extent_size as total_size,  -- 当前大小
    data_free,                                -- 空闲的字节数
    maximum_size                              -- 允许的最大值
from information_schema.files 
where tablespace_name = 'innodb_temporary';

-- DBA友好 -- 
select 
    file_name,                                                   -- 文件名
    tablespace_name,                                             -- 表空间名
    engine,                                                      -- 引擎
    sys.format_bytes(initial_size) as total_size,                -- 初始大小
    sys.format_bytes(total_extents*extent_size) as current_size, -- 当前大小
    sys.format_bytes(data_free) as free_szie,                    -- 空闲大小
    sys.format_bytes(maximum_size) as maximum_size               -- 允许的最大值
from information_schema.files 
where tablespace_name = 'innodb_temporary';


-- +-----------+------------------+--------+------------+--------------+-----------+--------------+
-- | FILE_NAME | TABLESPACE_NAME  | ENGINE | total_size | current_size | free_szie | maximum_size |
-- +-----------+------------------+--------+------------+--------------+-----------+--------------+
-- | ./ibtmp1  | innodb_temporary | InnoDB | 12.00 MiB  | 12.00 MiB    | 6.00 MiB  | NULL         |
-- +-----------+------------------+--------+------------+--------------+-----------+--------------+
-- 1 row in set (0.00 sec)