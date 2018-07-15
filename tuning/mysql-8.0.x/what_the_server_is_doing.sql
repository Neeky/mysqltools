select 
    thread_id,   -- 内部线程号
    event_name,  -- 事件名
    object_name, -- 对象名
    operation,   -- 操作
    timer_start, -- 开始时间
    timer_end,   -- 结束时间
    timer_wait,  -- timer_end - timer_start
    (case timer_wait when null then 'doing' else 'done' end) as statu -- 根据timer_wait的值确定事件的状态
from performance_schema.events_waits_current ;
 
-- +-----------+--------------------------------------+---------------------------------------+-----------+------------------+------------------+----------------+-------+
-- | thread_id | event_name                           | object_name                           | operation | timer_start      | timer_end        | timer_wait     | statu |
-- +-----------+--------------------------------------+---------------------------------------+-----------+------------------+------------------+----------------+-------+
-- |         1 | wait/io/file/innodb/innodb_data_file | /database/mysql/data/3306/mysql.ibd   | read      |    2671585525700 |    2671599838336 |       14312636 | done  |
-- |        10 | wait/io/file/innodb/innodb_data_file | /database/mysql/data/3306/undo_001    | sync      |    4047886926398 |    4048103070176 |      216143778 | done  |
-- |        13 | wait/io/file/innodb/innodb_data_file | /database/mysql/data/3306/undo_001    | write     |    4047344845776 |    4047360260768 |       15414992 | done  |
-- |        14 | wait/io/file/innodb/innodb_log_file  | /database/mysql/data/3306/ib_logfile0 | sync      |    4056243767518 |    4056579741822 |      335974304 | done  |
-- |        16 | wait/io/file/innodb/innodb_log_file  | /database/mysql/data/3306/ib_logfile0 | write     |    2627720528692 |    2627721772908 |        1244216 | done  |
-- |        17 | wait/io/file/innodb/innodb_log_file  | /database/mysql/data/3306/ib_logfile0 | sync      |    2627734007122 |    2627839909764 |      105902642 | done  |
-- |        25 | wait/io/file/innodb/innodb_data_file | /database/mysql/data/3306/undo_001    | read      |    2583839760658 |    2583928314514 |       88553856 | done  |
-- |        46 | idle                                 | NULL                                  | idle      | 1367713967526000 | 1408596309636000 | 40882342110000 | done  |
-- +-----------+--------------------------------------+---------------------------------------+-----------+------------------+------------------+----------------+-------+
-- 8 rows in set (0.00 sec)
