#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

"""
    mxb(Mysql Percona Backup)的定位:
        1、内部封装 MySQL Enterprise Backup & Percona XtraBackup 
        2、集“全备”，“增备”，“备份校验”，“还原(考虑中)” 等各项功能于一身

    mxb 的备份工作流程
    1、从/etc/mxb.cnf中读取配置
    2、根据配置文件中的备份计划、决定这次是全备 | 增备 中的哪一种
    3、根据配置文件中的备份工具、决定这次是使用xtrabackup | meb

    mxb 的还原工作流程
        1、从/etc/mxb.cnf中读取配置
        2、.....
        
"""

import os,argparse
from datetime import datetime

class BackupTool(object):
    host='127.0.0.1'
    port=3306
    user='backuper'
    password='mtls0352'
    backup_script=None
    backup_save_dir='/database/backup/mysql/'

    def __init__(self,host='127.0.0.1',port=3306,user='backuper',password='mtls0352',backup_save_dir='/database/backup/mysql/'):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.backup_save_dir=backup_save_dir

    def fullBackup(self,options=None):
        raise NotImplementedError("请在子类中实现对MySQL数据的全备功能.")

    def increaseBackup(self):
        raise NotImplementedError("请在子类中实现对MySQL数据的增备功能.")

    def validateBackup(self):
        raise NotImplementedError("请在子类中实现对备份的校验功能.")

    def restoreBackup(self):
        raise NotImplementedError("请在子类中实现对备份的校验功能.")

    def __repr__(self):
        return "BackupTool(host={self.host} port={self.port} user={self.user} password={self.password} backup_script={self.backup_script})".format(self=self)

class Meb(BackupTool):  
    """
    用MySQL Enterprise Backup完成MySQL数据库的备份
    """ 
    pass

class Xtra(BackupTool):
    """
    用Percona XtraBackup完成MySQL数据库的备份
    """
    pass

class MysqlDump(BackupTool):
    """
    用mysqldump完成MySQL数据库的备份
    """

    backup_script="""mysqldump -u{self.user} -p{self.password} -h{self.host} -P{self.port} \
    --all-databases --triggers --routines --events--set-gtid-purged=ON > {backup_save_path} &
    """

    def __repr__(self):
        return self.backup_script.format(self=self)

    def fullBackup(self,options):
        """
        用mysqldump完成全备
        """
        #创建备份的完整路径形式如
        #/database/backup/mysql/3306/2018-4-24T21:19:44-fullbackup.sql
        backup_save_path = os.path.join(self.backup_save_dir,
            "{self.port}/{now.year}-{now.month}-{now.day}T{now.hour}:{now.minute}:{now.second}-fullbackup.sql".format(self=self,now=datetime.now()))
        instance_backup_dir=os.path.dirname(backup_save_path)
        if os.path.exists(instance_backup_dir):
            #目录已经存在
        else:
            os.makedirs(instance_backup_dir)
        os.system(self.backup_script.format(self=self,backup_save_path=backup_save_path))
        

        


if __name__=="__main__":
    mysqldump = MysqlDump()
    mysqldump.fullBackup(1)