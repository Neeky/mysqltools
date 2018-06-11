
-- 1): 检查mysql group replication 环境是否正常

select 
    member_host, -- 主机名
    member_port, -- 端口号
    member_state -- 状态
    
from performance_schema.replication_group_members;

/*  #### 
    ####    +-------------+-------------+--------------+
    ####    | member_host | member_port | member_state |
    ####    +-------------+-------------+--------------+
    ####    | actionsky16 |        3306 | ONLINE       |
    ####    | actionsky17 |        3306 | ONLINE       |
    ####    | actionsky15 |        3306 | ONLINE       |
    ####    +-------------+-------------+--------------+

    期望返回样式、注意member_port并不是gcl用的端口它返回的是正常的sql服务端口、online表示正常
*/




-- 2): 检查组中各个server的状态(面向mysql-5.7.x)

select 
    b.member_host, -- 主机名
    b.member_port, -- 端口号
    a.count_transactions_in_queue as ctiq, -- 处于冲突检测中的事务数
    a.count_transactions_checked  as ctc,  -- 完成冲突检测的事务数
    a.transactions_committed_all_members as tcam -- 所有成员都提交了的事务总数

from performance_schema.replication_group_member_stats as a
    join performance_schema.replication_group_members  as b
        on a.member_id = b.member_id;

/*
    ####    +-------------+-------------+------+-----+------------------------------------------+
    ####    | member_host | member_port | ctiq | ctc | tcam                                     |
    ####    +-------------+-------------+------+-----+------------------------------------------+
    ####    | actionsky15 |        3306 |    0 |   0 | aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa:1-3 |
    ####    +-------------+-------------+------+-----+------------------------------------------+

    期望返回样式、ctiq为0 ctc为0

*/



-- 3): 检查组中各个server的状态(面向mysql-8.0.x)

-- select 
--     b.member_host, -- 主机名
--     b.member_port, -- 端口号
--     a.count_transactions_in_queue as ctiq, -- 处于冲突检测中的事务数
--     a.count_transactions_checked  as ctc,  -- 完成冲突检测的事务数
--     a.transactions_committed_all_members as tcam -- 所有成员都提交了的事务总数
-- 
-- from performance_schema.replication_group_member_stats as a
--     join performance_schema.replication_group_members  as b
--         on a.member_id = b.member_id;



-- 4): 检查连接的状态

select 
    last_error_number,    -- 错误代码
    last_error_timestamp, -- 发生错误的时间
    last_error_message    -- 错误信息     
    from performance_schema.replication_connection_status;


/*
    ####    +-------------------+----------------------+--------------------+
    ####    | last_error_number | last_error_timestamp | last_error_message |
    ####    +-------------------+----------------------+--------------------+
    ####    |                 0 | 0000-00-00 00:00:00  |                    |
    ####    +-------------------+----------------------+--------------------+

    期望返回样式、last_error_number=0,last_error_message=''
*/



-- 5): 检查当前的primary主机是谁
show global status like 'group_replication_primary_member';
/*
    ####    +----------------------------------+-------+
    ####    | Variable_name                    | Value |
    ####    +----------------------------------+-------+
    ####    | group_replication_primary_member |       |
    ####    +----------------------------------+-------+
    ####    1 row in set (0.00 sec)
    期望返回样式、group_replication_single_primary_mode=off的时候group_replication_primary_member应该是空的
    不然它就是primary的server_uuid
*/
