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

class BackupTool(object):
    host='127.0.0.1'
    port=3306
    user='backuper'
    password='mtls0352'

    def __init__(self,host='127.0.0.1',port=3306,user='backuper',password='mtls0352'):
        self.host=host
        self.port=port
        self.user=user
        self.password=password

    def fullBackup(self):
        raise NotImplementedError("请在子类中实现对MySQL数据的全备功能.")

    def increaseBackup(self):
        raise NotImplementedError("请在子类中实现对MySQL数据的增备功能.")

    def validateBackup(self):
        raise NotImplementedError("请在子类中实现对备份的校验功能.")

    def restoreBackup(self):
        raise NotImplementedError("请在子类中实现对备份的校验功能.")

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
    pass


if __name__=="__main__":
    print('hello world ...2')