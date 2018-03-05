# -*- coding:utf8 -*-
"""
定义所有与mgr相关的操作
"""


from .base import PsBase

class MgrBase(PsBase):
    """
    所以mysql-group-replication相关查询的基类
    """
    def raw_format(self,raw_data):
        return raw_data

    def to_string_format(self,raw_data):
        return raw_data.decode('utf8')

    @property
    def original_value(self):
        self.cursor.execute(self.scalar_stmt)
        node_count=self.cursor.fetchone()
        if len(node_count) == 1:
            formats={
                'raw_format': self.raw_format,
                'to_string_format': self.to_string_format,} 
            return formats[self.format_type](node_count[0])
        else:
            self.logger.error("get unexpected value ' {0} ' for MgrNodeCount".format(node_count))
            exit() 

    @property
    def value(self):
        return self.original_value

    scalar_stmt="select 'this is test info for MgrBase class' as msg ;"
    format_type="raw_format"  
    
class MgrTotalMemberCount(MgrBase):
    """
    mysql-group-replication的结点数量
    """
    scalar_stmt="select count(*) from performance_schema.replication_group_members ;"

class MgrOnLineMemberCount(MgrBase):
    """
    当前mysql-group-replication 集群中状态为online的结点数量
    """
    scalar_stmt="select count(*) from performance_schema.replication_group_members where member_state='ONLINE' ;"

class MgrMemberState(MgrBase):
    """
    查看当前结点的member_state 状态
    """
    scalar_stmt="""select member_state 
    from performance_schema.replication_group_members 
    where member_id=@@server_uuid;"""

    format_type="to_string_format"

class MgrCountTransactionsInQueue(MgrBase):
    """
    等待进行冲突检查的事务数量
    """
    scalar_stmt="""select count_transactions_in_queue 
    from performance_schema.replication_group_member_stats 
    where member_id=@@server_uuid;"""

class MgrCountTransactionsChecked(MgrBase):
    """
    已经完成冲突检测的事务数量
    """
    scalar_stmt="""select count_transactions_checked 
    from performance_schema.replication_group_member_stats 
    where member_id=@@server_uuid;"""

class MgrCountConflictsDetected(MgrBase):
    """
    没能通过冲突检测的事务数量
    """
    scalar_stmt="""
    select count_conflicts_detected
    from performance_schema.replication_group_member_stats 
    where member_id=@@server_uuid;
    """

class MgrTransactionsCommittedAllMembers(MgrBase):
    scalar_stmt=""" select transactions_committed_all_members
    from performance_schema.replication_group_member_stats 
    where member_id=@@server_uuid;
    """