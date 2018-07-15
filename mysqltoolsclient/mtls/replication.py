#-*- coding:utf8 -*-

"""
为show global status 中的statu提供一个与之对应的类，以方便使用
"""
from .base import StatuBase,ShowSlave

__all__=['RplSemiSyncMasterClients','RplSemiSyncMasterStatus','RplSemiSyncMasterNoTx',
         'RplSemiSyncMasterYesTx','RplSemiSyncSlaveStatus','SlaveIORunning','SlaveSQLRunning',
         'SecondsBehindMaster']


class RplSemiSyncMasterClients(StatuBase):
    """
    The number of semisynchronous slaves
    """
    statu_name="Rpl_semi_sync_master_clients"

class RplSemiSyncMasterStatus(StatuBase):
    """
    The value is 1 if the plugin has been enabled  It is 0 if the plugin is not enabled
    """
    statu_name="Rpl_semi_sync_master_status"

class RplSemiSyncMasterNoTx(StatuBase):
    """
    The number of commits that were not acknowledged successfully by a slave
    """
    statu_name="Rpl_semi_sync_master_no_tx"

class RplSemiSyncMasterYesTx(StatuBase):
    """
    The number of commits that were acknowledged successfully by a slave
    """
    statu_name="Rpl_semi_sync_master_yes_tx"

class RplSemiSyncSlaveStatus(StatuBase):
    """
    Whether semisynchronous replication currently is operational on the slave. This is 1 if the plugin has been enabled and the slave I/O thread is running, 0 otherwise.
    """
    statu_name="Rpl_semi_sync_slave_status"

class SlaveIORunning(ShowSlave):
    """
    1 --> yes
    0 --> 其它可能的情况
    """
    show_slave_name="Slave_IO_Running"
    
    def _get_value(self):
        value = super()._get_value()
        if value == 'this node is master':
            return -1 # 直接返回 -1 
        if value.upper() == 'YES':
            self._value = 1
            return self._value
        else:
            self._value = 0
            return self._value

class SlaveSQLRunning(ShowSlave):
    """
    1 --> yes
    0 --> 其它可能的情况
    """
    show_slave_name="Slave_SQL_Running"

    def _get_value(self):
        value = super()._get_value()
        if value == 'this node is master':
            return -1 # 直接返回 -1 
        if value.upper() == 'YES':
            self._value = 1
            return self._value
        else:
            self._value = 0
            return self._value

class SecondsBehindMaster(ShowSlave):
    """
    """
    show_slave_name="Seconds_Behind_Master"

    def _get_value(self):
        value = super()._get_value()
        if value == 'this node is master':
            return -1 # 直接返回 1 
        else:
            return value
