# -*- coding:utf8 -*-
from mtls import mgr
"""
main.py 只是在mtls这个package在开发时的一个入口点、只用于测试目的。
"""

if __name__=="__main__":
    psc = mgr.MgrTransactionsCommittedAllMembers(host='10.186.19.17',port=3306,user='mtlsuser',password='mtls0352')
    print(psc.value)

