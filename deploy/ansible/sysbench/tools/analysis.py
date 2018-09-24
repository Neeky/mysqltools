#!/usr/bin/env python3

import argparse
import os
import sys
from collections import Counter

def log_parser(args):
    """解析sysbench的日志
    """

    # 拼接出文件全名
    files = os.listdir(args.log_dir)
    files = [os.path.join(args.log_dir,f) for f in files]

    # 定义保存结果的变量
    mysql_release=None
    counter = Counter()

    # 专用于解析master_info.cnf
    def parser_cnf(file_name):
        with open(file_name) as master_info:
            for line in master_info:
                if 'mysql=' in line:
                    nonlocal mysql_release 
                    _,mysql_release = line.split('=')
    
    # 专用于解析sysbench的日志
    def parser_sysbench_log(file_name):
        nonlocal counter
        _,s = file_name.split('#')
        threads,_ = s.split('.')
        with open(file_name) as sysbench_log:
            for line in sysbench_log:
                if 'transactions:' in line:
                    _,s = line.split('(')
                    tps,_ = s.split('per')
                    tps = float(tps)
                    continue
                if 'queries:' in line:
                    _,s = line.split('(')
                    qps,_ = s.split('per')
                    qps = float(qps)
            
        total = int(tps) + int(qps)
        counter[threads]=total

    # sorted.key专用函数，按线程排序结果集
    def order_by_threads(item):
        return item[0]

    # 处理日志目标中的文件
    for file_name in files:
        if file_name.endswith('.cnf'):
            parser_cnf(file_name)
        elif file_name.endswith('.log'):
            parser_sysbench_log(file_name)

    # 在打印前对结果进行处理
    mysql_release = mysql_release.strip()
    t_s = counter.most_common()
    t_s = sorted(t_s,key=order_by_threads)
    ks=[k for k,v in t_s]
    vs=[v for k,v in t_s]

    # 打印结果
    print(mysql_release)
    print(ks)
    print(vs)


    

        

            



if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--log-dir',default='/tmp/mysql-5.7.32/',help='sysbench日志保存的目录')
    args=parser.parse_args()
    log_parser(args)
