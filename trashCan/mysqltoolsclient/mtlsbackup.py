#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

"""
   融合mysqldump,xtrabackup,meb 三种备份方法     
"""

__all__ = ['Meb','Xtrabackup','MysqlDump']
__author__ = '蒋乐哥哥'
__version__ = '0.1'


import os,argparse,logging,configparser,argparse,shutil
from datetime import datetime
logging.basicConfig(level = logging.INFO,format='[%(asctime)s] [%(filename)s] [%(levelname)s] %(message)s', )



class BackupTool(object):
    """
    作为备份工具的基类
    """
    user = "backup"
    password = "DX3906"
    host = "127.0.0.1"
    port = 3306
    full_backup_days = "7"
    diff_backup_days = "1,2,3,4,5,6"
    backup_tool = "xtrabackup"
    backup_data_dir = "/database/backups/3306/data/"
    backup_log_dir = "database/backups/3306/log/"
    backup_temp_dir = "/database/backups/3306/temp/"
    current = None
    backup_types = {
        "full_backup":"FULLBACKUP",
        "diff_backup":"DIFFBACKUP",
        "increment_backup":"INCREMNETBACKUP"}

    def __init__(self,mtlsconf):
        """
        mtlsconf 是经过configparser处理过的字典
        """
        self.user = mtlsconf['global']['user'] if 'user' in mtlsconf['global'] else self.user
        self.password = mtlsconf['global']['password'] if 'password' in mtlsconf['global'] else self.password
        self.host = mtlsconf['global']['host'] if 'host' in mtlsconf['global'] else self.host
        self.port = int(mtlsconf['global']['port']) if 'port' in mtlsconf['global'] else self.port
        self.full_backup_days = mtlsconf['global']['full_backup_days'] if 'full_backup_days' in mtlsconf['global'] else self.full_backup_days
        self.diff_backup_days = mtlsconf['global']['diff_backup_days'] if 'diff_backup_days' in mtlsconf['global'] else self.diff_backup_days
        self.backup_tool = mtlsconf['global']['backup_tool'] if 'backup_tool' in mtlsconf['global'] else self.backup_tool
        self.backup_data_dir = mtlsconf['global']['backup_data_dir'] if 'backup_data_dir' in mtlsconf['global'] else self.backup_data_dir
        self.backup_log_dir = mtlsconf['global']['backup_log_dir'] if 'backup_log_dir' in mtlsconf['global'] else self.backup_log_dir
        self.backup_temp_dir = mtlsconf['global']['backup_temp_dir'] if 'backup_temp_dir' in mtlsconf['global'] else self.backup_temp_dir
        self.current = datetime.now()
        #开始检查环境信息
        self.preExec()

    def directorCheck(self,path):
        """
        在备份之前对目录进行检查
        """
        logging.info("开始检查 {path} ".format(path=path))
        if not os.path.exists(path):
            #目录不存在
            logging.warn("目录 {path} 不存在,准备创建... ".format(path=path))
            os.makedirs(path)
            logging.info("目录 {path} 创建完成 ...".format(path=path))
    

    def preExec(self):
        """
        在备份之前对环境进行检查
        """
        #检查backup_data_dir目录是否存在
        self.directorCheck(self.backup_data_dir)
        #检查backup_log_dir目录是否存在
        self.directorCheck(self.backup_log_dir)
        #检查backup_temp_dir目录是否存在
        self.directorCheck(self.backup_temp_dir)

    def backupDecisionByWeekDay(self):
        """
        根据日期(星期几)、分析应该是要全备还是要差异备份
        """
        weekday = str(self.current.weekday())
        if weekday in self.full_backup_days:
            logging.info("今天星期 {0} 根据配置文件中的备份计划，决定进行全备".format(weekday))
            return self.backup_types['full_backup']
        elif weekday in self.diff_backup_days: 
            logging.info("今天星期 {0} 根据配置文件中的备份计划，决定进行差异备份".format(weekday))
            return self.backup_types['diff_backup']

    @property
    def strCurrent(self):
        """
        以字符串的形式返回当前时间值(2018-07-26T16:42:00)
        """
        return self.current.isoformat(timespec='seconds')

    @property
    def latestBackupSet(self):
        """
        返回最新的备份集
        
        当没有任何备份集的时候返回None
        """
        #得到所有可用的备份集
        backup_sets = [backup_set for backup_set in os.listdir(self.backup_data_dir) if os.path.isdir(os.path.join(self.backup_data_dir,backup_set))]
        
        #作为能用逻辑这里返回最后一个备份集、为最新的可用备份集
        if len(backup_sets) >=1:
            return backup_sets[-1]
        else:
            return None

    def fullbackup(self):
        raise NotImplementedError("请在子类中实现全备功能")

    def diffbackup(self):
        raise NotImplementedError("请在子类中实现差异备份功能")

    def backup(self):
        """
        """
        decision=self.backupDecisionByWeekDay()
        
        if decision == self.backup_types['full_backup']:
            self.fullbackup()
        elif decision == self.backup_types['diff_backup']:
            self.diffbackup()
        else:
            self.fullbackup()



class Xtrabackup(BackupTool):
    """
    extrabackup包装类
    """
    full_backup_script = None
    diff_backup_script = None

    def __init__(self,mtlsconf):
        super().__init__(mtlsconf)
        self.full_backup_script = mtlsconf['xtrabackup']['full_backup_script']
        self.diff_backup_script = mtlsconf['xtrabackup']['diff_backup_script']

    @property
    def isLatestFullBackupSuccess(self):
        """
        用于确定最后一次全备是否成功!
        """
        logging.info("准备检查最近一次的全备是否成功...")
        #如果备份集为None，也就是说不可能有成功的全备，所以返回False
        if super().latestBackupSet == None:
            logging.warn("没有可用的备份集(全备))")
            return False
        else:
            #拼接出最新一个可用备份集的目录
            logging.info("检查最后一个备份集{0}的可用性".format(self.latestBackupSet))
            xtrabackup_log = os.path.join(self.backup_data_dir,self.latestBackupSet,self.latestBackupSet+'-full.log')
            logging.info("检查{0}".format(xtrabackup_log))
            if (not os.path.exists(xtrabackup_log)) or (not os.path.isfile(xtrabackup_log)):
                logging.warn("{0} 不存在或它并不是一个文件".format(xtrabackup_log))
                return False

            with open(xtrabackup_log) as xlf:
                last = [line for line in xlf ][-1]
                if 'completed OK!' in last:
                    logging.warn("检查到最后一个全备 备份成功")
                    xtrabackup_checkpoints = os.path.join(self.backup_log_dir,self.latestBackupSet,'xtrabackup_checkpoints')
                    with open(xtrabackup_checkpoints) as xcf:
                        line = [line for line in xcf if 'to_lsn' in line][0]
                        *_,tolsn = line.split(' ')
                        self.tolsn=tolsn.strip()
                        logging.info("从xtrabackup_checkpoints文件中读到tolsn={0}".format(self.tolsn))
                    return True
                else:
                    logging.warn("检查到最后一个全备 没有备份成功")
                    return False

    def clearnBackupSets(self):
        """
        清理备份集(一个全备加上若干差异备份)
        """
        backup_sets = [backup_set for backup_set in os.listdir(self.backup_data_dir) if os.path.isdir(os.path.join(self.backup_data_dir,backup_set))]
        if len(backup_sets) >=2:
            logging.info("备份集的数量为{0}大于2 准备清理备份集".format(len(backup_sets)))
            backup_sets = sorted(backup_sets)
            for backup_set in backup_sets[0:-1]:
                temp = os.path.join(self.backup_data_dir,backup_set)
                logging.info("清理备份集 {0}".format(temp))
                shutil.rmtree(temp)

                #清理备份集相关的lsn日志文件
                lsns = [lsn for lsn in os.listdir(self.backup_log_dir) if os.path.isdir(os.path.join(self.backup_log_dir,lsn)) and lsn<=backup_set]
                for lsn in lsns:
                    temp = os.path.join(self.backup_log_dir,lsn)
                    logging.info("清理lsn日志 {0}".format(temp))
                    shutil.rmtree(temp)

    def fullbackup(self):
        """
        执行全备
        """
        self.clearnBackupSets()

        #拼接出保留全备的的路径(/database/backups/3306/data/2018-07-26T16:42:00/)
        full_backup_dir = os.path.join(self.backup_data_dir,self.strCurrent)

        full_backup_file = os.path.join(self.backup_data_dir,self.strCurrent,self.strCurrent+'-full.xbstream')
        full_backup_log_file = os.path.join(self.backup_data_dir,self.strCurrent,self.strCurrent+'-full.log')
        
        self.full_backup_file = full_backup_file
        self.full_backup_log_file = full_backup_log_file

        #拼接出用于保留lsn的路径
        self.lsndir=os.path.join(self.backup_log_dir,self.strCurrent)
        os.makedirs(self.lsndir)

        #创建出保留全备的的路径(/database/backups/3306/data/2018-07-26T16:42:00/)
        logging.info("创建用于保存全备的目录 {0}".format(full_backup_dir))
        os.makedirs(full_backup_dir)

        #根据实例属性格式化全备命令行
        full_backup_script = self.full_backup_script.format(self=self)

        #拼接出完整的全备命令
        logging.info("使用如下命令对MySQL数据库进行全备 {full_backup_script}".format(full_backup_script=full_backup_script))

        #执行全备
        os.system( full_backup_script )

    def diffbackup(self):
        """
        在全备的基础之上执行差异备份
        """
        logging.info("进入差异备份流程")
        #差异备份是在全备之上建立的、所以在进行差异备份之前应该先检查最后一个全备是否成功
        if self.isLatestFullBackupSuccess:
            # 如果最后一个全备是成功的、那么进入差异备份流程

            #创建用于保存lsn的目录
            self.lsndir=os.path.join(self.backup_log_dir,self.strCurrent)
            os.makedirs(self.lsndir)

            #拼接出用于保存差异备份的目录/这个目录就是备份集的目录
            diff_backup_dir = os.path.join(self.backup_data_dir,self.latestBackupSet)
            self.diff_backup_file = os.path.join(diff_backup_dir,self.strCurrent + '-diff.xbstream')
            self.diff_backup_log_file = os.path.join(diff_backup_dir,self.strCurrent  + '-diff.log')

            #根据实例属性格式化差异备命令行
            diff_backup_script = self.diff_backup_script.format(self=self)

            logging.info("使用如下命令对MySQL数据库进行差异备 {0} ".format(diff_backup_script))

            os.system(diff_backup_script)

        else:
            # 跳转到全备流程
            self.fullbackup()
            

class Meb(BackupTool):
    pass


class MysqlDump(BackupTool):
    pass            



backup_tools_map = {
    'xtrabackup':Xtrabackup
}


def main(mtlsconf):
    logging.info("read config file {0}".format(mtlsconf))
    config = configparser.ConfigParser(inline_comment_prefixes=('#',';'))
    config.read(mtlsconf)
    tool_name = config['global']['backup_tool']
    tool = backup_tools_map[tool_name](config)
    tool.backup()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('-c','--conf',default='/etc/mtlsbackup.cnf',help='mtlsbackup.py config file')
    args=parser.parse_args()
    main(args.conf)
