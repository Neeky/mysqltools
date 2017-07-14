select 
    lw.blocking_trx_id,     -- 已经持有锁的事务
    lw.requesting_trx_id    -- 被动进入等待的事务
from information_schema.innodb_lock_waits as lw;

-- 锁的详细信息
select 
    plist.id,           -- 连接的id
    trx.trx_id,         -- 事务id
    trx.trx_started,    -- 事务开始的时间
    trx.trx_state,      -- 事务当前的状态
    lk.lock_mode,       -- 锁的模式 X | S
    lk.lock_type,       -- 锁的类型 Recorde | gap | next key
    lk.lock_table,      -- 锁关联到的表
    lk.lock_index,      -- 锁关联到的索引
    plist.info          -- 当前的sql语句
from information_schema.innodb_trx as trx 
    join information_schema.processlist as plist
        on plist.id = trx.trx_mysql_thread_id
    join information_schema.innodb_locks as lk
        on lk.lock_trx_id = trx.trx_id
order by trx.trx_id;
