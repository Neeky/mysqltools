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

__all__=['Meb','Xtrabackup','MysqlDump']
__author__='蒋乐哥哥'
__version__='0.1'


import os,argparse,logging,configparser,argparse
from datetime import datetime

logging.basicConfig(level = logging.INFO,format='[%(asctime)s] [%(filename)s] [%(levelname)s] %(message)s', )


class BackupTool(object):
    host =' 127.0.0.1'        #ip地址
    port = 3306               #端口号
    user = 'backup'         #用户名
    password = 'DX3906'     #密码
    args = None               #命令行参数
    backup_script = None      #备份脚本
    backup_save_dir = '/database/backup/mysql/' #备份保存目录
    _timestring = None        #发起时间


    def __repr__(self):
        return "{self.__class__.__name__}(host={self.host} port={self.port} user='{self.user}' password='{self.password})' ".format(self=self)

    def __init__(self,*args,**kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)

    @property
    def currentTimeString(self):
        if self._timestring == None:
            self._timestring="{now.year}-{now.month}-{now.day}T{now.hour}:{now.minute}:{now.second}".format(now=datetime.now())
        return self._timestring

    def readConfig(self):
        logging.info("{self.__class__.__name__} 开始读{self.args.config_file}取配置文件".format(self=self))
        config = configparser.ConfigParser()
        config.read(self.args.config_file)
        default = dict(config['default'])

        self.host = default.get('host',self.host)
        logging.info("{0:>20} = {self.host:<40}".format('host',self=self))

        self.port = default.get('port',self.port)
        logging.info("{0:>20} = {self.port:<40}".format('port',self=self))

        self.user = default.get('user',self.user)
        logging.info("{0:>20} = {self.user:<40}".format('user',self=self))

        self.password = default.get('password',self.password)
        logging.info("{0:>20} = {self.password:<40}".format('password',self=self))

        self.backup_save_dir = os.path.join(default.get('backup_save_dir',self.backup_save_dir),str(self.port))
        logging.info("{0:>20} = {self.backup_save_dir:<40}".format('backup_save_dir',self=self))

        self.backup_work_dir = os.path.join(default.get('backup_work_dir',self.backup_save_dir),str(self.port))
        logging.info("{0:>20} = {self.backup_work_dir:<40}".format('backup_work_dir',self=self))

    def makeFullBackup(self,options=None):
        self.readConfig()
        #raise NotImplementedError("请在子类中实现对MySQL数据的全备功能.")

    def makeIncreaseBackup(self):
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

class Xtrabackup(BackupTool):
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
            pass
        else:
            os.makedirs(instance_backup_dir)
        os.system(self.backup_script.format(self=self,backup_save_path=backup_save_path))
        

        


if __name__=="__main__":
    logging.info('准备进行命令行参数处理')
    parser=argparse.ArgumentParser()
    parser.add_argument('--config-file',default='/etc/mxb.cnf',help='默认配置文件./mxb.cnf')
    args=parser.parse_args()
    md = MysqlDump(args=args)
    md.readConfig()
    
    