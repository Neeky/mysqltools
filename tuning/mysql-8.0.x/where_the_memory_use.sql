select 
    substring_index(event_name,'/',2) as code_area,       -- 代码域
    sys.format_bytes(sum(current_alloc)) as current_alloc -- 使用的内存的大小
from sys.x$memory_global_by_current_bytes 
group by substring_index(event_name,'/',2) 
order by sum(current_alloc) desc
limit 5;

-- +---------------------------+---------------+
-- | code_area                 | current_alloc |
-- +---------------------------+---------------+
-- | memory/innodb             | 323.48 MiB    |
-- | memory/performance_schema | 262.19 MiB    |
-- | memory/mysys              | 8.91 MiB      |
-- | memory/sql                | 8.75 MiB      |
-- | memory/temptable          | 1.00 MiB      |
-- +---------------------------+---------------+
-- 5 rows in set (0.00 sec)