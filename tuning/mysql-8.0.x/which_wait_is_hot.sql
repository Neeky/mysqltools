select 
    event_name, -- 事件名
    count_star  -- 等待次数
from performance_schema.events_waits_summary_global_by_event_name
order by count_star desc limit 7;

-- +--------------------------------------+------------+
-- | event_name                           | count_star |
-- +--------------------------------------+------------+
-- | wait/io/file/innodb/innodb_data_file |       1157 |
-- | idle                                 |        246 |
-- | wait/io/file/innodb/innodb_log_file  |         76 |
-- | wait/io/file/sql/binlog              |         21 |
-- | wait/io/file/sql/binlog_index        |         15 |
-- | wait/io/file/sql/casetest            |         10 |
-- | wait/io/file/sql/slow_log            |          6 |
-- +--------------------------------------+------------+
-- 7 rows in set (0.00 sec)







-- waits is timed by CYCLE
select timer_frequency into @frequency  
    from performance_schema.performance_timers 
where timer_name='CYCLE';

select 
    event_name,     -- 事件名
    sum_timer_wait /@frequency as sum_timer_wait_by_second   -- 总等待时间
from performance_schema.events_waits_summary_global_by_event_name
order by sum_timer_wait desc limit 7;

-- +--------------------------------------+------------------+
-- | event_name                           | sum_timer_wait   |
-- +--------------------------------------+------------------+
-- | idle                                 | 2643499741276000 |
-- | wait/io/file/innodb/innodb_data_file |      29484284775 |
-- | wait/io/file/innodb/innodb_log_file  |       7200031320 |
-- | wait/io/file/sql/binlog              |       1617050880 |
-- | wait/io/file/sql/ERRMSG              |        917809020 |
-- | wait/io/file/sql/binlog_index        |        394112130 |
-- | wait/io/file/sql/casetest            |         90883695 |
-- +--------------------------------------+------------------+
-- 7 rows in set (0.01 sec)