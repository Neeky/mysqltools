#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from mtls import statu,variable,mgr,replication
import argparse

#---------------------------------------
#monitor.py 用于实现对 mysql 的监控
#---------------------------------------

#定义最基本的mysql监控项
basic_items={
    #定义mysql绝大多数variable 主要用于信息收集 对于性能监控的意思不大 但是有助于分析问题
    'ServerID':variable.ServerID,
    'BaseDir':variable.BaseDir,
    'DataDir':variable.DataDir,
    'Port':variable.Port,
    'CharacterSetServer':variable.CharacterSetServer,
    'Socket':variable.Socket,
    'ReadOnly':variable.ReadOnly,
    'SkipNameResolve': variable.SkipNameResolve,
    'LowerCaseTableNames':variable.LowerCaseTableNames,
    'ThreadCacheSize':variable.ThreadCacheSize,
    'TableOpenCache':variable.TableOpenCache,
    'TableDefinitionCache':variable.TableDefinitionCache,
    'TableOpenCacheInstances':variable.TableOpenCacheInstances,
    'MaxConnections':variable.MaxConnections,
    'BinlogFormat':variable.BinlogFormat,
    'LogBin':variable.LogBin,
    'BinlogRowsQueryLogEvents':variable.BinlogRowsQueryLogEvents,
    'LogSlaveUpdates':variable.LogSlaveUpdates,
    'ExpireLogsDays':variable.ExpireLogsDays,
    'BinlogCacheSize':variable.BinlogCacheSize,
    'SyncBinlog':variable.SyncBinlog,
    'ErrorLog':variable.ErrorLog,
    'GtidMode':variable.GtidMode,
    'EnforceGtidConsistency':variable.EnforceGtidConsistency,
    'MasterInfoRepository': variable.MasterInfoRepository,
    'RelayLogInfoRepository':variable.RelayLogInfoRepository,
    'SlaveParallelType':variable.SlaveParallelType,
    'SlaveParallelWorkers':variable.SlaveParallelWorkers,
    'InnodbDataFilePath':variable.InnodbDataFilePath,
    'InnodbTempDataFilePath':variable.InnodbTempDataFilePath,
    'InnodbBufferPoolFilename':variable.InnodbBufferPoolFilename,
    'InnodbLogGroupHomeDir':variable.InnodbLogGroupHomeDir,
    'InnodbLogFilesInGroup':variable.InnodbLogFilesInGroup,
    'InnodbLogFileSize':variable.InnodbLogFileSize,
    'InnodbFileformat':variable.InnodbFileformat,
    'InnodbFilePerTable':variable.InnodbFilePerTable,
    'InnodbOnlineAlterLogMaxSize':variable.InnodbOnlineAlterLogMaxSize,
    'InnodbOpenFiles':variable.InnodbOpenFiles,
    'InnodbPageSize':variable.InnodbPageSize,
    'InnodbThreadConcurrency':variable.InnodbThreadConcurrency,
    'InnodbReadIoThreads':variable.InnodbReadIoThreads,
    'InnodbWriteIoThreads':variable.InnodbWriteIoThreads,
    'InnodbPurgeThreads':variable.InnodbPurgeThreads,
    'InnodbLockWaitTimeout':variable.InnodbLockWaitTimeout,
    'InnodbSpinWaitDelay':variable.InnodbSpinWaitDelay,
    'InnodbAutoincLockMode':variable.InnodbAutoincLockMode,
    'InnodbStatsAutoRecalc':variable.InnodbStatsAutoRecalc,
    'InnodbStatsPersistent':variable.InnodbStatsPersistent,
    'InnodbStatsPersistentSamplePages':variable.InnodbStatsPersistentSamplePages,
    'InnodbBufferPoolInstances':variable.InnodbBufferPoolInstances,
    'InnodbAdaptiveHashIndex': variable.InnodbAdaptiveHashIndex,
    'InnodbChangeBuffering':variable.InnodbChangeBuffering,
    'InnodbChangeBufferMaxSize':variable.InnodbChangeBufferMaxSize,
    'InnodbFlushNeighbors':variable.InnodbFlushNeighbors,
    'InnodbFlushMethod':variable.InnodbFlushMethod,
    'InnodbDoublewrite':variable.InnodbDoublewrite,
    'InnodbLogBufferSize':variable.InnodbLogBufferSize,
    'InnodbFlushLogAtTimeout':variable.InnodbFlushLogAtTimeout,
    'InnodbFlushLogAtTrxCommit':variable.InnodbFlushLogAtTrxCommit,
    'InnodbBufferPoolSize':variable.InnodbBufferPoolSize,
    'Autocommit':variable.Autocommit,
    'InnodbOldBlocksPct':variable.InnodbOldBlocksPct,
    'InnodbOldBlocksTime':variable.InnodbOldBlocksTime,
    'InnodbReadAheadThreshold':variable.InnodbReadAheadThreshold,
    'InnodbRandomReadAhead':variable.InnodbRandomReadAhead,
    'InnodbBufferPoolDumpPct':variable.InnodbBufferPoolDumpPct,
    'InnodbBufferPoolDumpAtShutdown':variable.InnodbBufferPoolDumpAtShutdown,
    'InnodbBufferPoolLoadAtStartup':variable.InnodbBufferPoolLoadAtStartup,

    #定义mysql绝大多数status 主要用于性能监控
    'AbortedClients':statu.AbortedClients,
    'AbortedConnects':statu.AbortedConnects,
    'BinlogCacheDiskUse':statu.BinlogCacheDiskUse,
    'BinlogCacheUse':statu.BinlogCacheUse,
    'BinlogStmtCacheDiskUse':statu.BinlogStmtCacheDiskUse,
    'BinlogStmtCacheUse':statu.BinlogStmtCacheUse,
    'BytesReceived':statu.BytesReceived,
    'BytesSent':statu.BytesSent,
    'ComBegin':statu.ComBegin,
    'ComCallProcedure':statu.ComCallProcedure,
    'ComChangeMaster':statu.ComChangeMaster,
    'ComCommit':statu.ComCommit,
    'ComDelete':statu.ComDelete,
    'ComDeleteMulti':statu.ComDeleteMulti,
    'ComInsert':statu.ComInsert,
    'ComInsertSelect':statu.ComInsertSelect,
    'ComSelect':statu.ComSelect,
    'ComUpdate':statu.ComUpdate,
    'ComUpdateMulti':statu.ComUpdateMulti,
    'Connections':statu.Connections,
    'CreatedTmpDiskTables':statu.CreatedTmpDiskTables,
    'CreatedTmpFiles':statu.CreatedTmpFiles,
    'CreatedTmpTables':statu.CreatedTmpTables,
    'InnodbBufferPoolDumpStatus':statu.InnodbBufferPoolDumpStatus,
    'InnodbBufferPoolLoadStatus':statu.InnodbBufferPoolLoadStatus,
    'InnodbBufferPoolResizeStatus':statu.InnodbBufferPoolResizeStatus,
    'InnodbBufferPoolBytesData':statu.InnodbBufferPoolBytesData,
    'InnodbBufferPoolPagesData':statu.InnodbBufferPoolPagesData,
    'InnodbBufferPoolPagesDirty':statu.InnodbBufferPoolPagesDirty,
    'InnodbBufferPoolBytesDirty':statu.InnodbBufferPoolBytesDirty,
    'InnodbBufferPoolPagesFlushed':statu.InnodbBufferPoolPagesFlushed,
    'InnodbBufferPoolPagesFree':statu.InnodbBufferPoolPagesFree,
    'InnodbBufferPoolPagesMisc':statu.InnodbBufferPoolPagesMisc,
    'InnodbBufferPoolPagesTotal':statu.InnodbBufferPoolPagesTotal,
    'InnodbBufferPoolReadAhead':statu.InnodbBufferPoolReadAhead,
    'InnodbBufferPoolReadAheadEvicted':statu.InnodbBufferPoolReadAheadEvicted,
    'InnodbBufferPoolReadRequests':statu.InnodbBufferPoolReadRequests,
    'InnodbBufferPoolReads':statu.InnodbBufferPoolReads,
    'InnodbBufferPoolWaitFree':statu.InnodbBufferPoolWaitFree,
    'InnodbBufferPoolWriteRequests':statu.InnodbBufferPoolWriteRequests,
    'InnodbDataFsyncs':statu.InnodbDataFsyncs,
    'InnodbDataPendingFsyncs':statu.InnodbDataPendingFsyncs,
    'InnodbDataPendingReads':statu.InnodbDataPendingReads,
    'InnodbDataPendingWrites':statu.InnodbDataPendingWrites,
    'InnodbDataRead':statu.InnodbDataRead,
    'InnodbDataReads':statu.InnodbDataReads,
    'InnodbDataWrites':statu.InnodbDataWrites,
    'InnodbDataWritten':statu.InnodbDataWritten,
    'InnodbDblwrPagesWritten':statu.InnodbDblwrPagesWritten,
    'InnodbDblwrWrites':statu.InnodbDblwrWrites,
    'InnodbLogWaits':statu.InnodbLogWaits,
    'InnodbLogWriteRequests':statu.InnodbLogWriteRequests,
    'InnodbLogWrites':statu.InnodbLogWrites,
    'InnodbOsLogFsyncs':statu.InnodbOsLogFsyncs,
    'InnodbOsLogPendingFsyncs':statu.InnodbOsLogPendingFsyncs,
    'InnodbOsLogPendingWrites':statu.InnodbOsLogPendingWrites,
    'InnodbOsLogWritten':statu.InnodbOsLogWritten,
    'InnodbPagesCreated':statu.InnodbPagesCreated,
    'InnodbPagesRead':statu.InnodbPagesRead,
    'InnodbPagesWritten':statu.InnodbPagesWritten,
    'InnodbRowLockCurrentWaits':statu.InnodbRowLockCurrentWaits,
    'InnodbRowLockTime':statu.InnodbRowLockTime,
    'InnodbRowLockTimeAvg':statu.InnodbRowLockTimeAvg,
    'InnodbRowLockTimeMax':statu.InnodbRowLockTimeMax,
    'InnodbRowLockWaits':statu.InnodbRowLockWaits,
    'InnodbRowsDeleted':statu.InnodbRowsDeleted,
    'InnodbRowsInserted':statu.InnodbRowsInserted,
    'InnodbRowsRead':statu.InnodbRowsRead,
    'InnodbRowsUpdated':statu.InnodbRowsUpdated,
    'InnodbAvailableUndoLogs':statu.InnodbAvailableUndoLogs,
    'OpenTableDefinitions':statu.OpenTableDefinitions,
    'OpenTables':statu.OpenTables,
    'OpenedTableDefinitions':statu.OpenedTableDefinitions,
    'OpenedTables':statu.OpenedTables,
    'TableOpenCacheOverflows':statu.TableOpenCacheOverflows,
    'ThreadsCached':statu.ThreadsCached,
    'ThreadsConnected':statu.ThreadsConnected,
    'ThreadsCreated':statu.ThreadsCreated,
    'ThreadsRunning':statu.ThreadsRunning,
    'Uptime':statu.Uptime
}

#定义mysql主从复制时用到的监控项
repl_items={}

#定义mysql-group-replication时用到的监控项
mgr_items={
    'MgrTotalMemberCount':mgr.MgrTotalMemberCount,
    'MgrOnLineMemberCount':mgr.MgrOnLineMemberCount,
    'MgrMemberState':mgr.MgrMemberState,
    'MgrCountTransactionsInQueue':mgr.MgrCountTransactionsInQueue,
    'MgrCountTransactionsChecked':mgr.MgrCountTransactionsChecked,
    'MgrCountConflictsDetected':mgr.MgrCountConflictsDetected,
    'MgrTransactionsCommittedAllMembers':mgr.MgrTransactionsCommittedAllMembers
}

replication_items = {
    'RplSemiSyncMasterClients':replication.RplSemiSyncMasterClients,
    'RplSemiSyncMasterStatus':replication.RplSemiSyncMasterStatus,
    'RplSemiSyncMasterNoTx':replication.RplSemiSyncMasterNoTx,
    'RplSemiSyncMasterYesTx':replication.RplSemiSyncMasterYesTx,
    'RplSemiSyncSlaveStatus':replication.RplSemiSyncSlaveStatus,
    'SlaveIORunning':replication.SlaveIORunning,
    'SlaveSQLRunning':replication.SlaveSQLRunning,
    'SecondsBehindMaster':replication.SecondsBehindMaster,
}

def export_zabbix_agent_config_file():
    """
    monitor.py 主要是用于zabbix监控mysql、所以在这里提供一个自动生成zabbix自定义key值的文件
    方便后面使用
    """
    fmt="UserParameter=mysql{0}[*],/usr/local/mtls/monitor.py -u=$1 -p=$2 -s=$3 -P=$4 {0} 2>>/var/log/mtls/monitor.log"
    lines=[fmt.format(line) for line in monitor_item_names if line != 'export']
    for line in lines:
        print(line)

monitor_items={}
monitor_items.update(basic_items)
monitor_items.update(mgr_items)
monitor_items.update(replication_items)
monitor_items.update({'export':export_zabbix_agent_config_file})

#已经定义好了的监控项名
monitor_item_names=[key for key in monitor_items.keys()]


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-u','--user',default='monitor',help='user name for connect to mysql')
    parser.add_argument('-p','--password',default='mtls0352',help='user password for connect to mysql')
    parser.add_argument('-s','--host',default='127.0.0.1',help='mysql host ip')
    parser.add_argument('-P','--port',default=3306,type=int,help='mysql port')
    parser.add_argument('-d','--database',default='information_schema',help='current database default information_schema')
    parser.add_argument('monitor_item_name',choices=monitor_item_names)
    args=parser.parse_args()
    if args.monitor_item_name =='export':
        export_zabbix_agent_config_file()
        exit()
    m=monitor_items[args.monitor_item_name](host=args.host,port=args.port,user=args.user,password=args.password,database=args.database)
    print(m.original_value)


