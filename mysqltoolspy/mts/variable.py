#-*- coding:utf8 -*-
"""
为常用的MySQL variable 定义与之对应的类，以方便使用。
"""

from .base import VariableBase

#----------------------------------------------------
#全局配置相关的variable
#----------------------------------------------------
class ServerID(VariableBase):
    variable_name="server_id"
    variable_type="intger"

class BaseDir(VariableBase):
    variable_name="basedir"
    variable_type="string"

class DataDir(VariableBase):
    variable_name="datadir"
    variable_type="string"

class Port(VariableBase):
    variable_name="port"
    variable_type="intger"

class CharacterSetServer(VariableBase):
    variable_name="character_set_server"
    variable_type="string"

class Socket(VariableBase):
    variable_name="socket"
    variable_type="string"

class ReadOnly(VariableBase):
    variable_name="read_only"
    variable_type="intger"

class SkipNameResolve(VariableBase):
    variable_name="skip_name_resolve"
    variable_type="intger"

class LowerCaseTableNames(VariableBase):
    variable_name="lower_case_table_names"
    variable_type="intger"

class ThreadCacheSize(VariableBase):
    variable_name="thread_cache_size"
    variable_type="intger"

class TableOpenCache(VariableBase):
    variable_name="table_open_cache"
    variable_type="intger"

class TableDefinitionCache(VariableBase):
    variable_name="table_definition_cache"
    variable_type="intger"

class TableOpenCacheInstances(VariableBase):
    variable_name="table_open_cache_instances"
    variable_type="intger"



#----------------------------------------------------
#binlog配置相关的variable
#----------------------------------------------------
class BinlogFormat(VariableBase):
    variable_name="binlog_format"
    variable_type="string"

class LogBin(VariableBase):
    variable_name="log_bin"
    variable_type="string"

    @property
    def value(self):
        if self._value == None:
            self._value=self._get_value()
            if self._value==0:
                self._value='OFF'
            return self._value
        else:
            return self._value


class BinlogRowsQueryLogEvents(VariableBase):
    variable_name="binlog_rows_query_log_events"
    variable_type="bool"

class LogSlaveUpdates(VariableBase):
    variable_name="log_slave_updates"
    variable_type="bool"

class ExpireLogsDays(VariableBase):
    variable_name="expire_logs_days"
    variable_type="intger"

class BinlogCacheSize(VariableBase):
    variable_name="binlog_cache_size"
    variable_type="byte"
class SyncBinlog(VariableBase):
    variable_name="sync_binlog"
    variable_type="intger"


#----------------------------------------------------
#error log 配置相关的variable
#----------------------------------------------------
class ErrorLog(VariableBase):
    variable_name="log_error"
    variable_type="string"
#----------------------------------------------------
#gtid配置相关的variable
#----------------------------------------------------
class GtidMode(VariableBase):
    variable_name="gtid_mode"
    variable_type="bool"
class EnforceGtidConsistency(VariableBase):
    variable_name="enforce_gtid_consistency"
    variable_type="bool"
#----------------------------------------------------
#replication配置相关的variable
#----------------------------------------------------
class MasterInfoRepository(VariableBase):
    variable_name="master_info_repository"
    variable_type="string"
class RelayLogInfoRepository(VariableBase):
    variable_name="relay_log_info_repository"
    variable_type="string"
class SlaveParallelType(VariableBase):
    variable_name="slave_parallel_type"
    variable_type="string"
class SlaveParallelWorkers(VariableBase):
    variable_name="slave_parallel_workers"
    variable_type="intger"
#----------------------------------------------------
#innodb配置相关的variable
#----------------------------------------------------
class InnodbDataFilePath(VariableBase):
    variable_name="innodb_data_file_path"
class InnodbTempDataFilePath(VariableBase):
    variable_name="innodb_temp_data_file_path"
class InnodbBufferPoolFilename(VariableBase):
    variable_name="innodb_buffer_pool_filename "
class InnodbLogGroupHomeDir(VariableBase):
    variable_name="innodb_log_group_home_dir"
class InnodbLogFilesInGroup(VariableBase):
    variable_name="innodb_log_files_in_group"
    variable_type="intger"
class InnodbLogFileSize(VariableBase):
    variable_name="innodb_log_file_size"
    variable_type="byte"
class InnodbFileformat(VariableBase):
    variable_name="innodb_file_format"
class InnodbFilePerTable(VariableBase):
    variable_name="innodb_file_per_table"
    variable_type="bool"
class InnodbOnlineAlterLogMaxSize(VariableBase):
    variable_name="innodb_online_alter_log_max_size"
    variable_type="byte"
class InnodbOpenFiles(VariableBase):
    variable_name="innodb_open_files"
    variable_type="intger"
class InnodbPageSize(VariableBase):
    variable_name="innodb_page_size"
    variable_type="byte"
class InnodbThreadConcurrency(VariableBase):
    variable_name="innodb_thread_concurrency"
    variable_type="intger"
