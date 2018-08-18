select 
    event_name, -- 事件名
    count_star  -- 次数
from events_stages_summary_global_by_event_name
order by count_star desc limit 7;

-- +----------------------------------------------------+------------+
-- | event_name                                         | count_star |
-- +----------------------------------------------------+------------+
-- | stage/innodb/buffer pool load                      |          1 |
-- | stage/sql/After create                             |          0 |
-- | stage/sql/allocating local table                   |          0 |
-- | stage/sql/preparing for alter table                |          0 |
-- | stage/sql/altering table                           |          0 |
-- | stage/sql/committing alter table to storage engine |          0 |
-- | stage/sql/Changing master                          |          0 |
-- +----------------------------------------------------+------------+
-- 7 rows in set (0.00 sec)


select 
    event_name,     -- 事件名
    sum_timer_wait  -- 总时间
from events_stages_summary_global_by_event_name
order by sum_timer_wait desc limit 7;

-- +----------------------------------------------------+----------------+
-- | event_name                                         | sum_timer_wait |
-- +----------------------------------------------------+----------------+
-- | stage/innodb/buffer pool load                      |       88945000 |
-- | stage/sql/After create                             |              0 |
-- | stage/sql/allocating local table                   |              0 |
-- | stage/sql/preparing for alter table                |              0 |
-- | stage/sql/altering table                           |              0 |
-- | stage/sql/committing alter table to storage engine |              0 |
-- | stage/sql/Changing master                          |              0 |
-- +----------------------------------------------------+----------------+
-- 7 rows in set (0.00 sec)