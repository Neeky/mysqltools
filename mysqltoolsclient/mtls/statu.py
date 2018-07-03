#-*- coding:utf8 -*-

"""
为show global status 中的statu提供一个与之对应的类，以方便使用
"""

from .base import StatuBase

class AbortedClients(StatuBase):
    """
    The number of connections that were aborted because the client died without closing the connection properly.
    """
    statu_name="Aborted_clients"
    statu_type="intger"

class AbortedConnects(StatuBase):
    """
    The number of failed attempts to connect to the MySQL server
    """
    statu_name="Aborted_connects"
    statu_type="intger"

class BinlogCacheDiskUse(StatuBase):
    """
    The number of transactions that used the temporary binary log cache but that exceeded the value of binlog_cache_size and used a temporary file to store statements from the transaction.
    The number of nontransactional statements that caused the binary log transaction cache to be written to disk is tracked separately in the Binlog_stmt_cache_disk_use status variable.
    """
    statu_name="Binlog_cache_disk_use"
    statu_type="intger"

class BinlogCacheUse(StatuBase):
    """
    The number of transactions that used the binary log cache.
    """
    statu_name="Binlog_cache_use"
    statu_type="intger"

class BinlogStmtCacheDiskUse(StatuBase):
    """
    The number of nontransaction statements that used the binary log statement cache but that exceeded the value of binlog_stmt_cache_size and used a temporary file to store those statements.
    """
    statu_name="Binlog_stmt_cache_disk_use"
    statu_type="intger"

class BinlogStmtCacheUse(StatuBase):
    """
    The number of nontransactional statements that used the binary log statement cache.
    """
    statu_name="Binlog_stmt_cache_use"
    statu_type="intger"

class BytesReceived(StatuBase):
    """
    The number of bytes received from all clients.
    """
    statu_name="Bytes_received"
    statu_type="byte"

class BytesSent(StatuBase):
    """
    The number of bytes sent to all clients.
    """
    statu_name="Bytes_sent"
    statu_type="byte"

class ComBegin(StatuBase):
    statu_name="Com_begin"

class ComCallProcedure(StatuBase):
    statu_name="Com_call_procedure"

class ComChangeMaster(StatuBase):
    statu_name="Com_change_master"

class ComCommit(StatuBase):
    statu_name="Com_commit"

class ComDelete(StatuBase):
    statu_name="Com_delete"

class ComDeleteMulti(StatuBase):
    statu_name="Com_delete_multi"

class ComInsert(StatuBase):
    statu_name="Com_insert"

class ComInsertSelect(StatuBase):
    statu_name="Com_insert_select"

class ComSelect(StatuBase):
    statu_name="Com_select"

class ComUpdate(StatuBase):
    statu_name="Com_update"

class ComUpdateMulti(StatuBase):
    statu_name="Com_update_multi"

class Connections(StatuBase):
    """
    通过mysql-connector每获取一次这个值，这个值都会加1，这个返回与命令行执行得到的结果不同。
    """
    statu_name="Connections"
    statu_type="intger"

class CreatedTmpDiskTables(StatuBase):
    """
    The number of internal on-disk temporary tables created by the server while executing statements.
    If an internal temporary table is created initially as an in-memory table but becomes too large,
    MySQL automatically converts it to an on-disk table. The maximum size for in-memory temporary tables is the minimum 
    of the tmp_table_size and max_heap_table_size values. If Created_tmp_disk_tables is large, you may want to increase 
    the tmp_table_size or max_heap_table_size value to lessen the likelihood that internal temporary tables in memory will be 
    converted to on-disk tables.You can compare the number of internal on-disk temporary tables created 
    to the total number of internal temporary tables created by comparing the values of the Created_tmp_disk_tables and Created_tmp_tables variables.
    """
    statu_name="Created_tmp_disk_tables"

class CreatedTmpFiles(StatuBase):
    statu_name="Created_tmp_files"

class CreatedTmpTables(StatuBase):
    """
    The number of internal temporary tables created by the server while executing statements.
    You can compare the number of internal on-disk temporary tables created to the total number of internal temporary tables created by comparing the values of the Created_tmp_disk_tables and Created_tmp_tables variables.
    See also Section 8.4.4, “Internal Temporary Table Use in MySQL”.
    Each invocation of the SHOW STATUS statement uses an internal temporary table and increments
    the global Created_tmp_tables value.
    """
    statu_name="Created_tmp_tables"

class InnodbBufferPoolDumpStatus(StatuBase):
    statu_name="Innodb_buffer_pool_dump_status"
    statu_type="string"

class InnodbBufferPoolLoadStatus(StatuBase):
    statu_name="Innodb_buffer_pool_load_status"
    statu_type="string"

class InnodbBufferPoolResizeStatus(StatuBase):
    statu_name="Innodb_buffer_pool_resize_status"
    statu_type="string"

class InnodbBufferPoolBytesData(StatuBase):
    """
    The total number of bytes in the InnoDB buffer pool containing data. 
    The number includes both dirty and clean pages. 
    For more accurate memory usage calculations than with Innodb_buffer_pool_pages_data, 
    when compressed tables cause the buffer pool to hold pages of different sizes.
    """
    statu_name="Innodb_buffer_pool_bytes_data"
    statu_type="byte"

class InnodbBufferPoolPagesData(StatuBase):
    """
    The number of pages in the InnoDB buffer pool containing data. 
    The number includes both dirty and clean pages. When using compressed tables, 
    the reported Innodb_buffer_pool_pages_data value may be larger than Innodb_buffer_pool_pages_total (Bug #59550).
    """
    statu_name="Innodb_buffer_pool_pages_data"

class InnodbBufferPoolPagesDirty(StatuBase):
    """
    The total current number of bytes held in dirty pages in the InnoDB buffer pool. 
    For more accurate memory usage calculations than with Innodb_buffer_pool_pages_dirty, 
    when compressed tables cause the buffer pool to hold pages of different sizes.
    """
    statu_name="Innodb_buffer_pool_pages_dirty"

class InnodbBufferPoolBytesDirty(StatuBase):
    """
    The current number of dirty pages in the InnoDB buffer pool.
    """
    statu_name="Innodb_buffer_pool_bytes_dirty"
    statu_type="byte"

class InnodbBufferPoolPagesFlushed(StatuBase):
    """
    The number of requests to flush pages from the InnoDB buffer pool.
    """
    statu_name="Innodb_buffer_pool_pages_flushed"

class InnodbBufferPoolPagesFree(StatuBase):
    """
    The number of free pages in the InnoDB buffer pool.
    """
    statu_name="Innodb_buffer_pool_pages_free"

class InnodbBufferPoolPagesMisc(StatuBase):
    """
    The number of pages in the InnoDB buffer pool that are busy because they have
    been allocated for administrative overhead, such as row locks or the adaptive hash
    index. This value can also be calculated as 
    Innodb_buffer_pool_pages_total − Innodb_buffer_pool_pages_free − Innodb_buffer_pool_pages_data. 
    When using compressed tables, Innodb_buffer_pool_pages_misc may report an out-of-bounds value (Bug #59550).
    """
    statu_name="Innodb_buffer_pool_pages_misc"

class InnodbBufferPoolPagesTotal(StatuBase):
    """
    The total size of the InnoDB buffer pool, in pages. When using compressed tables, 
    the reported Innodb_buffer_pool_pages_data value may be larger 
    than Innodb_buffer_pool_pages_total (Bug #59550)
    """
    statu_name="Innodb_buffer_pool_pages_total"

class InnodbBufferPoolReadAhead(StatuBase):
    """
    The number of pages read into the InnoDB buffer pool by the read-ahead background thread.
    """
    statu_name="Innodb_buffer_pool_read_ahead"

class InnodbBufferPoolReadAheadEvicted(StatuBase):
    """
    The number of pages read into the InnoDB buffer pool by the read-ahead background thread 
    that were subsequently evicted without having been accessed by queries.
    """
    statu_name="Innodb_buffer_pool_read_ahead_evicted"

class InnodbBufferPoolReadRequests(StatuBase):
    """
    The number of logical read requests.
    """
    statu_name="Innodb_buffer_pool_read_requests"

class InnodbBufferPoolReads(StatuBase):
    """
    The number of logical reads that InnoDB could not satisfy from the buffer pool, 
    and had to read directly from disk.
    """
    statu_name="Innodb_buffer_pool_reads"

class InnodbBufferPoolWaitFree(StatuBase):
    """
    Normally, writes to the InnoDB buffer pool happen in the background. 
    When InnoDB needs to read or create a page and no clean pages are available, 
    InnoDB flushes some dirty pages first and waits for that operation to finish. 
    This counter counts instances of these waits. If innodb_buffer_pool_size has been set properly, 
    this value should be small.
    """
    statu_name="Innodb_buffer_pool_wait_free"

class InnodbBufferPoolWriteRequests(StatuBase):
    """
    The number of writes done to the InnoDB buffer pool.
    """
    statu_name="Innodb_buffer_pool_write_requests"

class InnodbDataFsyncs(StatuBase):
    """
    The number of fsync() operations so far. The frequency of fsync() calls is influenced by the
    setting of the innodb_flush_method configuration option.
    """
    statu_name="Innodb_data_fsyncs"

class InnodbDataPendingFsyncs(StatuBase):
    """
    The current number of pending fsync() operations. The frequency of fsync() calls is influenced 
    by the setting of the innodb_flush_method configuration option.
    """
    statu_name="Innodb_data_pending_fsyncs"

class InnodbDataPendingReads(StatuBase):
    """
    The current number of pending reads.
    """
    statu_name="Innodb_data_pending_reads"

class InnodbDataPendingWrites(StatuBase):
    """
    The current number of pending writes.
    """
    statu_name="Innodb_data_pending_writes"

class InnodbDataRead(StatuBase):
    """
    The amount of data read since the server was started (in bytes).
    """
    statu_name="Innodb_data_read"
    statu_type="byte"

class InnodbDataReads(StatuBase):
    """
    The total number of data reads (OS file reads).
    """
    statu_name="Innodb_data_reads"

class InnodbDataWrites(StatuBase):
    """
    The total number of data writes.
    """
    statu_name="Innodb_data_writes"

class InnodbDataWritten(StatuBase):
    """
    The amount of data written so far, in bytes.
    """
    statu_name="Innodb_data_written"
    statu_type="byte"

class InnodbDblwrPagesWritten(StatuBase):
    """
    The number of pages that have been written to the doublewrite buffer. See Section 14.12.1, “InnoDB Disk I/O”.
    """
    statu_name="Innodb_dblwr_pages_written"

class InnodbDblwrWrites(StatuBase):
    """
    The number of doublewrite operations that have been performed. See Section 14.12.1, 
    “InnoDB DiskI/O”.
    """
    statu_name="Innodb_dblwr_writes"

class InnodbLogWaits(StatuBase):
    """
    The number of times that the log buffer was too small and a wait was required for it to be flushed before continuing.
    """
    statu_name="Innodb_log_waits"

class InnodbLogWriteRequests(StatuBase):
    """
    The number of write requests for the InnoDB redo log.
    """
    statu_name="Innodb_log_write_requests"

class InnodbLogWrites(StatuBase):
    """
    The number of physical writes to the InnoDB redo log file.
    """
    statu_name="Innodb_log_writes"

class InnodbOsLogFsyncs(StatuBase):
    """
    The number of fsync() writes done to the InnoDB redo log files.
    """
    statu_name="Innodb_os_log_fsyncs"

class InnodbOsLogPendingFsyncs(StatuBase):
    """
    The number of pending fsync() operations for the InnoDB redo log files.
    """
    statu_name="Innodb_os_log_pending_fsyncs"

class InnodbOsLogPendingWrites(StatuBase):
    """
    The number of pending writes to the InnoDB redo log files.
    """
    statu_name="Innodb_os_log_pending_writes"

class InnodbOsLogWritten(StatuBase):
    """
    The number of bytes written to the InnoDB redo log files.
    """
    statu_name="Innodb_os_log_written"

class InnodbPagesCreated(StatuBase):
    """
    The number of pages created by operations on InnoDB tables.
    """
    statu_name="Innodb_pages_created"

class InnodbPagesRead(StatuBase):
    """
    The number of pages read from the InnoDB buffer pool by operations on InnoDB tables.
    """
    statu_name="Innodb_pages_read"

class InnodbPagesWritten(StatuBase):
    """
    The number of pages written by operations on InnoDB tables.
    """
    statu_name="Innodb_pages_written"

class InnodbRowLockCurrentWaits(StatuBase):
    """
    The number of row locks currently being waited for by operations on InnoDB tables.
    """
    statu_name="Innodb_row_lock_current_waits"

class InnodbRowLockTime(StatuBase):
    """
    The total time spent in acquiring row locks for InnoDB tables, in milliseconds.
    """
    statu_name="Innodb_row_lock_time" 

class InnodbRowLockTimeAvg(StatuBase):
    """
    The average time to acquire a row lock for InnoDB tables, in milliseconds.
    """
    statu_name="Innodb_row_lock_time_avg"

class InnodbRowLockTimeMax(StatuBase):
    """
    The maximum time to acquire a row lock for InnoDB tables, in milliseconds.
    """
    statu_name="Innodb_row_lock_time_max"

class InnodbRowLockWaits(StatuBase):
    """
    The number of times operations on InnoDB tables had to wait for a row lock.
    """
    statu_name="Innodb_row_lock_waits"

class InnodbRowsDeleted(StatuBase):
    """
    The number of rows deleted from InnoDB tables.
    """
    statu_name="Innodb_rows_deleted"

class InnodbRowsInserted(StatuBase):
    """
    The number of rows inserted into InnoDB tables.
    """
    statu_name="Innodb_rows_inserted"

class InnodbRowsRead(StatuBase):
    """
    The number of rows read from InnoDB tables.
    """
    statu_name="Innodb_rows_read"

class InnodbRowsUpdated(StatuBase):
    """
    The number of rows updated in InnoDB tables.
    """
    statu_name="Innodb_rows_updated"

class InnodbAvailableUndoLogs(StatuBase):
    """
    The number of times output from the SHOW ENGINE INNODB STATUS statement has been truncated.
    """
    statu_name="Innodb_available_undo_logs"

class OpenTableDefinitions(StatuBase):
    """
    The number of cached .frm files.
    """
    statu_name="Open_table_definitions"

class OpenTables(StatuBase):
    """
    The number of tables that are open.
    """
    statu_name="Open_tables"

class OpenedTableDefinitions(StatuBase):
    """
    The number of .frm files that have been cached.
    """
    statu_name="Opened_table_definitions"

class OpenedTables(StatuBase):
    """
    The number of tables that have been opened. If Opened_tables is big, your table_open_cache
    value is probably too small.
    """
    statu_name="Opened_Tables"

class TableOpenCacheOverflows(StatuBase):
    """
    The number of overflows for the open tables cache. This is the number of times, 
    after a table is opened or closed, a cache instance has an unused entry and the size of the instance is larger 
    than table_open_cache / table_open_cache_instances.
    """
    statu_name="Table_open_cache_overflows"

class ThreadsCached(StatuBase):
    """
    The number of threads in the thread cache.
    """
    statu_name="Threads_cached"

class ThreadsConnected(StatuBase):
    """
    The number of currently open connections.
    """
    statu_name="Threads_connected"

class ThreadsCreated(StatuBase):
    """
    The number of threads created to handle connections. If Threads_created is big,
    you may want to increase the thread_cache_size value. The cache miss rate can be calculated 
    as Threads_created/Connections.
    """
    statu_name="Threads_created"

class ThreadsRunning(StatuBase):
    """
    The number of threads that are not sleeping.
    """
    statu_name="Threads_running"

class Uptime(StatuBase):
    """
    The number of seconds that the server has been up.
    """
    statu_name="Uptime"