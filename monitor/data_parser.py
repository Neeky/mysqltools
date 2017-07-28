#!/usr/bin/env python3.5
import sys
import os
import argparse
import json

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--file-path',default='/tmp/datas/',help='the inspection file path ...')
    args=parser.parse_args()
    file_list=[args.file_path+file_name for file_name in os.listdir(args.file_path)]
    file_list=sorted(file_list)
    filter=[
        'Up for',
        'Data in InnoDB tables',
        'Reads / Writes',
        'Slow queries',
        'Highest usage of available connections',
        'nnoDB log waits',
        'InnoDB Read buffer efficiency',
        'Read Key buffer hit rate',
        'Thread cache hit rate',
        'Table cache hit rate',
        'Temporary tables created on disk'
    ]
    def line_in_filter(line):
        for item in filter:
            if item in line: return True
        return False

    data={}
    for file in file_list:
        data[file]=[line for line in open(file) if line_in_filter(line) ]
    print(json.dumps(data,indent=4))
    #print(len(data.keys()))


