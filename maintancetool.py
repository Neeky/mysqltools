#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from __future__ import print_function
from mysql import connector
import argparse,sys,os

"""
作者:蒋乐兴
时间:2017年4月
目标:用于解决mysql常见的运维操作
"""
#create user monitoruser@'127.0.0.1' identified by '123456';
#grant replication client on *.* to monitoruser@'127.0.0.1';
#grant super on *.* to monitoruser@'127.0.0.1';
#create user monitoruser@'%' identified by '123456';
#grant replication client on *.* to monitoruser@'%';
#grant super on *.* to monitoruser@'%';

class BaseMysqlMaintance(object):
    """
    作为所有运维操作的基类
    """
    def __init__(self,user='monitoruser',password='123456',host='172.16.192.100',port=3306):
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

    def action(self):
        """定义想着的运维操作接口、具体的操作由子类实现"""
        raise NotImplemented("请在子类中实现具体操作...")


class PurgeBinaryLogs(BaseMysqlMaintance):
    """清理二进行日志文件"""
    #在清理二进制日志文件时留remainFileCount个文件不清理
    remainFileCount=2
    def action(self):
        #拿到当前的二进制文件信息
        self.cursor.execute("show master status")
        info=self.cursor.fetchone()[0].decode('utf-8')
        (currentFileName,currentFileIndex)=info.split('.')
        #根据当前的二进制文件信息 & 要保留的文件数量 确定出要执行的purge binary logs to {} 语句
        fileIndex=str(int(currentFileIndex)-self.remainFileCount)
        stmt="purge binary logs to '{0}.{1:0>6}' ;".format(currentFileName,fileIndex)
        #由于当前的mysql-connector不支持执行purge binary logs to 语句 所以只能去调用bash接口啦
        cmd="""mysql -h{0} -P{1} -u{2} -p{3} -e"{4}" &""".format(self.host,self.port,self.user,self.password,stmt)
        os.popen(cmd)







if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--user',default='monitoruser',help='user name for connect to mysql')
    parser.add_argument('--password',default='123456',help='user password for connect to mysql')
    parser.add_argument('--host',default='127.0.0.1',help='mysql host ip')
    parser.add_argument('--port',default=3306,type=int,help='mysql port')
    parser.add_argument('--version',default='1.0.0',help='1.0.0')
    args=parser.parse_args()
    mt=PurgeBinaryLogs()
    mt.action()

"""
git add maintancetool.py
git commit -m"bug fix"
git push origin master
"""

