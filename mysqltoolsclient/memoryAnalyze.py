#!/usr/local/python/bin/python3
#coding:utf8

"""
用于计算当前mysql实例按配置来算，最多能消耗的总内存
计算方法:
    total=innodb_buffer_pool_size 							+
          innodb_log_buffer_size							+
          key_buffer_size         							+
          max_connections *(sort_buffer_size + read_buffer_size + binlog_cache_size)	+
          max_connections * 2MB
"""
import mysql.connector
import argparse
from mysqltoollib import Variable

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--user',default='root',help='user name for connect to mysql')
    parser.add_argument('--password',default='',help='user password for connect to mysql')
    parser.add_argument('--host',default='127.0.0.1',help='mysql host ip')
    parser.add_argument('--port',default=3306,type=int,help='mysql port')
    args=parser.parse_args()
    options=(args.user,args.password,args.host,args.port)
    innodb_buffer_pool_size=Variable('innodb_buffer_pool_size',*options).value
    innodb_log_buffer_size=Variable('innodb_log_buffer_size',*options).value
    key_buffer_size=Variable('key_buffer_size',*options).value
    sort_buffer_size=Variable('sort_buffer_size',*options).value
    read_buffer_size=Variable('read_buffer_size',*options).value
    binlog_cache_size=Variable('binlog_cache_size',*options).value
    max_connections=Variable('max_connections',*options).value
    
    total=(innodb_buffer_pool_size + innodb_log_buffer_size +
          + key_buffer_size + max_connections*(sort_buffer_size+read_buffer_size+binlog_cache_size)
          + max_connections * (2*1024*1024)
          )
    total=total/(1024*1024)
    print("max memory size of mysql can use {0} MB".format(total))





