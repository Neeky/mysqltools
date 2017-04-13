#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from __future__ import print_function
from mysql import connector
import logging,argparse,sys


"""
作者:蒋乐兴
时间:2017年2月
目标:用于获取mysql状态信息、以此作为监控的基础
提需求+报bug:1721900707@qq.com
"""
#create user monitoruser@'127.0.0.1' identified by '123456';
#grant replication client on *.* to monitoruser@'127.0.0.1';
#grant super on *.* to monitoruser@'127.0.0.1';

class MonitorItem(object):
    """
    所有监控项的基类
    """
    def __init__(self,user='monitoruser',password='123456',host='127.0.0.1',port=3306):
        """初始化属性与到数据库端的连接"""
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        self.cnx=None
        self.cursor=None    
        try:
            config={'user':self.user,'password':self.password,'host':self.host,'port':self.port}
            self.cnx=connector.connect(**config)
            self.cursor=self.cnx.cursor(prepared=True)
        except connector.Error as err:
            """如果连接失败就赋空值"""
            self.cnx=None
            self.cursor=None
            sys.stderr.write(err.msg+'\n')


    def __str__(self):
        attrs={}
        attrs['user']=self.user
        attrs['password']=self.password
        attrs['host']=self.host
        attrs['port']=self.port
        return "instance of {0}  {1}".format(self.__class__,attrs)


    def __del__(self):
        """在python 进行垃圾回收时关闭连接"""
        if self.cnx != None:
            self.cnx.close() 


    def get_result(self):
        """返回监控项的状态,由子类实现相应的功能"""
        pass


    def print_result(self):
        """打印监控项的状态"""
        print(self.get_result())

    def action(self):
        """监控项达到阀值时可以触发的操作"""
        print("末定义任何有意义的操作")


#以下类用于检测MySQL数据库的正常与否
class IsAlive(MonitorItem):
    """监控MySQL数据库是否正常运行、{正常:on line,宕机:off line}"""
    def get_result(self):
        if self.cnx != None:
            return "on line"
        else:
            return "off line"


#以下类用于检测MySQL数据库的基本信息
class MysqlVariable(MonitorItem):
    """派生自MonitorItem类，用于所有variable 监控项的基类"""
    variable_name=None
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global variables like '{0}';""".format(self.variable_name)
                self.cursor.execute(stmt)
                return self.cursor.fetchone()[1].decode('utf8')
        except Exception as err:
            sys.stderr.write(err.__str__()+'\n')
            return -1

class MysqlPort(MonitorItem):
    """监控MySQL数据库监听是否正常、{正常:端口号,异常:-1}"""
    def get_result(self):
        if self.cnx != None:
            return self.port
        else:
            return -1

class MysqlBasedir(MysqlVariable):
    """监控MySQL安装目录所在位置，{正常:安装目录位置，异常:-1}"""
    variable_name="basedir"

class MysqlDatadir(MysqlVariable):
    """监控MySQL数据目录所在位置，{正常:数据目录位置，异常:-1}"""
    variable_name="datadir"

class MysqlVersion(MysqlVariable):
    """监控MySQL版本号，{正常:版本号，异常:-1}"""
    variable_name="version"

class MysqlServerId(MysqlVariable):
    """监控MySQL的server_id"""
    variable_name="server_id"

class MysqlLogBin(MysqlVariable):
    """binlog 是否有开启"""
    variable_name="log_bin"

class MysqlLogError(MysqlVariable):
    """errorlog文件名"""
    variable_name="log_error"

class MysqlPerformanceSchema(MysqlVariable):
    """performance_schema是否有开启"""
    variable_name="performance_schema"

class MysqlInnodbBufferPoolSize(MysqlVariable):
    """监控MySQL innodb_buffer_pool的大小，{正常:缓冲池大小(byte)，异常:-1}"""
    variable_name="innodb_buffer_pool_size"

class MysqlMaxConnections(MysqlVariable):
    """最大连接数"""
    variable_name="max_connections"


#派生自MonitorItem类，用于所有status 监控项的基类
class MysqlStatu(MonitorItem):
    """派生自MonitorItem类，用于所有statu 监控项的基类"""
    statu_name=None
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like '{0}';""".format(self.statu_name)
                self.cursor.execute(stmt)
                return self.cursor.fetchone()[1].decode('utf8')
        except Exception as err:
            sys.stderr.write(err.__str__()+'\n')
            return -1

class MysqlCurrentClient(MysqlStatu):
    """当前的客户端连接数"""
    statu_name="Threads_connected"

class MysqlTableOpenCacheHitRate(MysqlStatu):
    """表缓存命中率"""
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like 'table_open_cache_hits';"""
                self.cursor.execute(stmt)
                hit=float((self.cursor.fetchone()[1].decode('utf8')))
                stmt=r"""show global status like 'table_open_cache_misses';"""
                self.cursor.execute(stmt)
                miss=float(self.cursor.fetchone()[1].decode('utf8'))
                return hit/(hit+miss)
        except Exception as err:
            sys.stderr.write(err.__str__())
            return -1

class MysqlTableOpenCacheOverflows(MysqlStatu):
    """表缓存溢出次数，如果大于0,可以增大table_open_cache和table_open_cache_instances."""
    statu_name="Table_open_cache_overflows"

class MysqlTableLocksWaited(MysqlStatu):
    """因不能立刻获得表锁而等待的次数"""
    statu_name="table_locks_waited"

class MysqlSlowqueries(MysqlStatu):
    """执行时间超过long_query_time的查询次数，不管慢查询日志有没有打开"""
    statu_name="slow_queries"

class MysqlSortScan(MysqlStatu):
    """全表扫描之后又排序(排序键不是主键)的次数"""
    statu_name="sort_scan"

class MysqlSortRows(MysqlStatu):
    """与sortscan差不多，前者指的是sortscan的次数，srotrows指的是sort操作影响的行数"""
    statu_name="sort_rows"

class MysqlSortRange(MysqlStatu):
    """根据索引进行范围扫描之后再进行排序(排序键不能是主键)的次数"""
    statu_name="sort_range"

class MysqlSortMergePasses(MysqlStatu):
    """排序时归并的次数，如果这个值比较大(要求高一点大于0)那么可以考虑增大sort_buffer_size的大小"""
    statu_name="sort_merge_passes"

class MysqlSelectRangeCheck(MysqlStatu):
    """如果这个值不是0那么就要好好的检查表上的索引了"""
    statu_name="select_range_check"

class MysqlQuestions(MysqlStatu):
    """erver端执行的语句数量，但是每执行一个语句它又只增加一，这点让我特别被动"""
    statu_name="Questions"

class MysqlQcacheFreeMemory(MysqlStatu):
    """query cache 的可用内存大小"""
    statu_name="qcache_free_memory"

class MysqlPreparedStmtCount(MysqlStatu):
    """由于本监控程序就是通过prepare语句完成的，所以这个监控项的值最少会是1不是0"""
    statu_name="prepared_stmt_count"

class MysqlOpenedTables(MysqlStatu):
    """mysql数据库打开过的表，如果这个值过大，应该适当的增大table_open_cache的值"""
    statu_name="opened_tables"

class MysqlOpenTables(MysqlStatu):
    """当前mysql数据库打开的表数量"""
    statu_name="open_tables"

class MysqlServerLevelOpenFiles(MysqlStatu):
    """mysql数据库的server层当前正打开的文件数据"""
    statu_name="open_files"

class MysqlInnodbAvailableUndoLogs(MysqlStatu):
    """innodb当前可用的undo段的数据"""
    statu_name="innodb_available_undo_logs"

class MysqlInnodbNumOpenFiles(MysqlStatu):
    """innodb当前打开的文件数量"""
    statu_name="innodb_num_open_files"

class MysqlInnodbRowsUpdated(MysqlStatu):
    """innodb层面执行的update所影响的行数"""
    statu_name="innodb_rows_updated"

class MysqlInnodbRowsRead(MysqlStatu):
    """innodb 层面受读操作所影响的行数"""
    statu_name="innodb_rows_read"

class MysqlInnodbRowsInserted(MysqlStatu):
    """innodb 层面受insert操作所影响的行数"""
    statu_name="innodb_rows_inserted"

class MysqlInnodbRowsDeleted(MysqlStatu):
    """innodb 层面受delete操作所影响的行数"""
    statu_name="innodb_rows_deleted"

class MysqlInnodbRowLockWaits(MysqlStatu):
    """innodb 行锁等待的次数"""
    statu_name="innodb_row_lock_waits"

class MysqlInnodbRowLockTimeMax(MysqlStatu):
    """innodb层面行锁等待的最大毫秒数"""
    statu_name="innodb_row_lock_time_max"

class MysqlInnodbRowLockTimeAvg(MysqlStatu):
    """innodb层面行锁等待的平均毫秒数"""
    statu_name="Innodb_row_lock_time_avg"

class MysqlInnodbRowLockTime(MysqlStatu):
    """innodb层面行锁等待的总毫秒数"""
    statu_name="Innodb_row_lock_time"

class MysqlInnodbPagesWritten(MysqlStatu):
    """innodb层面写入磁盘的页面数"""
    statu_name="Innodb_pages_written"

class MysqlInnodbPagesRead(MysqlStatu):
    """从innodb buffer pool 中读取的页数"""
    statu_name="Innodb_pages_read"

class MysqlInnodbOsLogWritten(MysqlStatu):
    """innodb redo 写入字节数"""
    statu_name="Innodb_os_log_written"

class MysqlInnodbOsLogPendingWrites(MysqlStatu):
    """innodb redo log 被挂起的写操作次数"""
    statu_name="Innodb_os_log_pending_writes"

class MysqlInnodbOsLogPendingFsyncs(MysqlStatu):
    """innodb redo log 被挂起的fsync操作次数"""
    statu_name="Innodb_os_log_pending_fsyncs"

class MysqlInnodbOsLogFsyncs(MysqlStatu):
    """innodb redo log fsync的次数"""
    statu_name="Innodb_os_log_fsyncs"

class MysqlInnodbLogWrites(MysqlStatu):
    """innodb redo log 物理写的次数"""
    statu_name="innodb_log_writes"

class MysqlInnodbLogWriteRequests(MysqlStatu):
    """innodb redo log 逻辑写的次数"""
    statu_name="Innodb_log_write_requests"

class MysqlInnodbLogWaits(MysqlStatu):
    """innodb 写redo 之前必须等待的次数"""
    statu_name="Innodb_log_waits"

class MysqlInnodbDblwrWrites(MysqlStatu):
    """innodb double write 的次数"""
    statu_name="Innodb_dblwr_writes"

class MysqlInnodbDblwrPagesWritten(MysqlStatu):
    """innodb double write 的页面数量"""
    statu_name="Innodb_dblwr_pages_written"

class MysqlInnodbDoubleWriteLoader(MysqlStatu):
    """innodb double write 压力1~64、数值越大压力越大"""
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like 'innodb_dblwr_pages_written';"""
                self.cursor.execute(stmt)
                pages=float((self.cursor.fetchone()[1].decode('utf8')))
                stmt=r"""show global status like 'innodb_dblwr_writes';"""
                self.cursor.execute(stmt)
                requests=float(self.cursor.fetchone()[1].decode('utf8'))
                if requests == 0:
                    return 0
                return pages/requests
        except Exception as err:
            sys.stderr.write(err.__str__())
            return -1

class MysqlInnodbBufferPoolHitRate(MysqlStatu):
    """innodb buffer pool 命中率"""
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like 'innodb_buffer_pool_read_requests';"""
                self.cursor.execute(stmt)
                hit_read=float((self.cursor.fetchone()[1].decode('utf8')))
                stmt=r"""show global status like 'innodb_buffer_pool_reads';"""
                self.cursor.execute(stmt)
                miss_read=float(self.cursor.fetchone()[1].decode('utf8'))
                total_read=(miss_read+hit_read)
                if total_read == 0:
                    return 0
                return hit_read/total_read
        except Exception as err:
            sys.stderr.write(err.__str__())
            return -1

class MysqlInnodbBufferPoolFreePagePercent(MysqlStatu):
    """innodb buffer pool free page 百分比"""
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like 'innodb_buffer_pool_pages_total';"""
                self.cursor.execute(stmt)
                total_page=float((self.cursor.fetchone()[1].decode('utf8')))
                stmt=r"""show global status like 'innodb_buffer_pool_pages_free';"""
                self.cursor.execute(stmt)
                free_page=float(self.cursor.fetchone()[1].decode('utf8'))
                return free_page/total_page
        except Exception as err:
            sys.stderr.write(err.__str__())
            return -1

class MysqlInnodbBufferPoolDirtyPercent(MysqlStatu):
    """innodb buffer pool dirty page 百分比"""
    def get_result(self):
        try:
            if self.cursor != None:
                stmt=r"""show global status like 'innodb_buffer_pool_pages_total';"""
                self.cursor.execute(stmt)
                total_page=float((self.cursor.fetchone()[1].decode('utf8')))
                stmt=r"""show global status like 'innodb_buffer_pool_pages_dirty';"""
                self.cursor.execute(stmt)
                dirty_page=float(self.cursor.fetchone()[1].decode('utf8'))
                return dirty_page/total_page
        except Exception as err:
            sys.stderr.write(err.__str__())
            return -1

class MysqlCreated_tmp_disk_tables(MysqlStatu):
    """mysql运行时所创建的磁盘临时表的数量，如果这个数值比较大，可以适当的增大 tmp_table_size | max_heap_table_size"""
    statu_name="Created_tmp_disk_tables"

class MysqlComSelect(MysqlStatu):
    """select 语句执行的次数"""
    statu_name="com_select"

class MysqlComInsert(MysqlStatu):
    """insert 语句执行的次数"""
    statu_name="com_insert"

class MysqlComDelete(MysqlStatu):
    """delete 语句执行的次数"""
    statu_name="com_delete"

class MysqlComUpdate(MysqlStatu):
    """update 语句执行的次数"""
    statu_name="com_update"

class MysqlBinlogCacheDiskUse(MysqlStatu):
    """事务引擎因binlog缓存不足而用到临时文件的次数，如果这个值过大，可以通过增大binlog_cache_size来解决"""
    statu_name="Binlog_cache_disk_use"

class MysqlBinlogStmtCacheDiskUse(MysqlStatu):
    """非事务引擎因binlog缓存不足而用到临时文件的次数，如果这个值过大，可以通过增大binlog_stmt_cache_size来解决"""
    statu_name="Binlog_stmt_cache_disk_use"

class MysqlReplication(MonitorItem):
    """所有监控mysql replication的基类"""
    def __init__(self,user='monitoruser',password='123456',host='127.0.0.1',port=3306):
        MonitorItem.__init__(self,user,password,host,port)
        try:
            if self.cursor != None:
                stmt="show slave status;"
                self.cursor.execute(stmt)
                self.replication_info=self.cursor.fetchone()
        except Exception as err:
            pass

class MysqlReplicationIsRunning(MysqlReplication):
    """mysql replication 是否正常运行"""
    def get_result(self):
        if self.replication_info == None:
            return "replication is not running"
        else:
            slave_io_running=self.replication_info[10].decode('utf8')
            slave_sql_running=self.replication_info[11].decode('utf8')
            if slave_io_running == 'Yes' and slave_sql_running == 'Yes':
                return "running"
            return "replication is not running"

class MysqlReplicationBehindMaster(MysqlReplication):
    """监控seconde behind master """
    def get_result(self):
        if self.replication_info != None:
            return self.replication_info[32]
        else:
            return -1




#监控项字典
items={
	#实例配置信息收集项
	'port'				:MysqlPort,
	'baseDir'			:MysqlBasedir,
	'dataDir'			:MysqlDatadir,
	'version'			:MysqlVersion,
	'serverId'			:MysqlServerId,
	'isBinlogEnable'		:MysqlLogBin,
	'isErrorlogEnable'		:MysqlLogError,
	'isPerformanceScheamEnable'	:MysqlPerformanceSchema,
	'innodbBufferPoolSize'		:MysqlInnodbBufferPoolSize,
	'maxConnections'		:MysqlMaxConnections,


	#实例运行时信息收集项
	'isOnline'			:IsAlive,
	'currentConnections'		:MysqlCurrentClient,
	'tableCacheHitRate'		:MysqlTableOpenCacheHitRate,
	'tableOpenCacheOverflows'	:MysqlTableOpenCacheOverflows,
	'tableLocksWaited'		:MysqlTableLocksWaited,
	'slowqueries'			:MysqlSlowqueries,
	'sortScan'			:MysqlSortScan,
	'sortRows'			:MysqlSortRows,
	'sortRange'			:MysqlSortRange,
	'sortMergePasses'		:MysqlSortMergePasses,
	'selectRangeCheck'		:MysqlSelectRangeCheck,
	'questions'			:MysqlQuestions,
	'qcacheFreeMemory'		:MysqlQcacheFreeMemory,
	'preparedStmtCount'		:MysqlPreparedStmtCount,
	'openedTables'			:MysqlOpenedTables,
	'openTables'			:MysqlOpenTables,
	'serverLevelOpenFiles'		:MysqlServerLevelOpenFiles,
	'created_tmp_disk_tables'	:MysqlCreated_tmp_disk_tables,
	'comSelect'			:MysqlComSelect,
	'comInsert'			:MysqlComInsert,
	'comDelete'			:MysqlComDelete,
	'comUpdate'			:MysqlComUpdate,
	'binlogCacheDiskUse'		:MysqlBinlogCacheDiskUse,
	'binlogStmtCacheDiskUse'	:MysqlBinlogStmtCacheDiskUse,

	#innodb运行时信息收集项
	'innodbAvailableUndoLogs'	:MysqlInnodbAvailableUndoLogs,
	'innodbOpenFiles'		:MysqlInnodbNumOpenFiles,
	'innodbRowsUpdated'		:MysqlInnodbRowsUpdated,
	'innodbRowsRead'		:MysqlInnodbRowsRead,
	'innodbRowsInserted'		:MysqlInnodbRowsInserted,
	'innodbRowsDeleted'		:MysqlInnodbRowsDeleted,
	'innodbRowLockWaits'		:MysqlInnodbRowLockWaits,
	'innodbRowLockTimeMax'		:MysqlInnodbRowLockTimeMax,
	'innodbRowLockTimeAvg'		:MysqlInnodbRowLockTimeAvg,
	'innodbRowLockTime'		:MysqlInnodbRowLockTime,
	'innodbPagesWritten'		:MysqlInnodbPagesWritten,
	'innodbPagesRead'		:MysqlInnodbPagesRead,
	'innodbOsLogWritten'		:MysqlInnodbOsLogWritten,
	'innodbOsLogPendingWrites'	:MysqlInnodbOsLogPendingWrites,
	'innodbOsLogPendingFsyncs'	:MysqlInnodbOsLogPendingFsyncs,
	'innodbOsLogFsyncs'		:MysqlInnodbOsLogFsyncs,
	'innodbLogWrites'		:MysqlInnodbLogWrites,
	'innodbLogWriteRequests'	:MysqlInnodbLogWriteRequests,
	'innodbLogWaits'		:MysqlInnodbLogWaits,
	'innodbDblwrWrites'		:MysqlInnodbDblwrWrites,
	'innodbDblwrPagesWritten'	:MysqlInnodbDblwrPagesWritten,
	'innodbDoubleWriteLoader'	:MysqlInnodbDoubleWriteLoader,
	'innodbBufferPoolHitRate'	:MysqlInnodbBufferPoolHitRate,
	'innodbBufferPoolFreePagePercent'	:MysqlInnodbBufferPoolFreePagePercent,
	'innodbBufferPoolDirtyPercent'	:MysqlInnodbBufferPoolDirtyPercent,
	
	#对mysql replication 的监控
	'replicationIsRunning'		:MysqlReplicationIsRunning,
	'replicationBehindMaster'	:MysqlReplicationBehindMaster,
}

#
item_key_names=[name for name in items.keys()]

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--user',default='monitoruser',help='user name for connect to mysql')
    parser.add_argument('--password',default='123456',help='user password for connect to mysql')
    parser.add_argument('--host',default='127.0.0.1',help='mysql host ip')
    parser.add_argument('--port',default=3306,type=int,help='mysql port')
    parser.add_argument('--version',default='1.0.0',help='1.0.0')
    parser.add_argument('monitor_item_name',choices=item_key_names)
    args=parser.parse_args()
    m=items[args.monitor_item_name](host=args.host,port=args.port,user=args.user,password=args.password)
    m.print_result()





