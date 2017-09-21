# -*- coding:utf8 -*-
"""

"""

__all__ = ['ConnectorBase','VariableBase']

import mysql.connector
import logging


class ConnectorBase(object):
    user='mtsuser'
    password='mts10352'
    host='127.0.0.1'
    port=3306
    _cnx=None
    _cursor=None
    _logger=None

    def __init__(self,host='127.0.0.1',port=3306,user='mtsuser',password='mts10352',*args,**kws):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self._cnx=None
        self._cursor=None
        self._logger=None
        

    @property
    def cursor(self):
        if self._cursor != None:
            return self._cursor
        else:
            try:
                self._cnx=mysql.connector.connect(user=self.user,password=self.password,host=self.host,port=self.port)
                self._cursor=self._cnx.cursor()
                return self._cursor
            except Exception as e:
                error_message=str(e)
                self.logger.info(e)
                self.logger.info("exit")
                exit()

    def format_string_value(self,raw_value):
        if isinstance(raw_value,str):
            return raw_value
        else:
            self.logger.info(raw_value)
            return 'invalidate str value'

    def format_byte_value(self,raw_value):
        if isinstance(raw_value,int):
            kb_raw_value=raw_value/1024
            if kb_raw_value >1024:
                mb_raw_value=kb_raw_value/1024
                if mb_raw_value>1024:
                    gb_raw_value=mb_raw_value/1024
                    if gb_raw_value >1024:
                        return "{0}TB".format(gb_raw_value/1024)
                    else:
                        return "{0}GB".format(gb_raw_value)
                else:
                    return "{0}MB".format(mb_raw_value)
            else:
                return "{0}KB".format(kb_raw_value)
        else:
            return "invalidate byte value"
    
    @property
    def logger(self):
        if self._logger != None:
            return self._logger
        else:
            self._logger=logging.getLogger("mts.base.{0}".format(self.__class__))
            stream_handler=logging.StreamHandler()
            formater=logging.Formatter("%(asctime)-24s %(levelname)-8s %(name)-24s : %(message)s")
            stream_handler.setFormatter(formater)
            self._logger.addHandler(stream_handler)
            self._logger.setLevel(logging.DEBUG)
            return self._logger

    def __str__(self):
        obj_str="{0.__class__} instance (host={0.host},port={0.port},user={0.user},password={0.password} )".format(self)
        return obj_str

    def __del__(self):
        if self._cnx != None:
            self._cnx.close()
        


class VariableBase(ConnectorBase):
    variable_name=None
    variable_type="string"
    _variable_types=("string","byte","intger","percent","bool")
    _value=None

    def __init__(self,host='127.0.0.1',port=3306,user='mtsuser',password='mts10352',
    variable_name="version",variable_type="string",*args,**kws):
        super(VariableBase,self).__init__(host,port,user,password)
        self.variable_name=variable_name
        self.variable_type=variable_type

    
    def _get_value(self):
        try:
            self.cursor.execute("select @@{0} ;".format(self.variable_name))
            tmp_value=self.cursor.fetchone()
            if tmp_value != None and len(tmp_value)==1:
                return tmp_value[0]
            else:
                self.logger.info("variable {0} has a bad value {1}".format(self.variable_name,tmp_value))
                exit()
        except Exception as e:
                errore_message=str(e)
                self.logger.info(errore_message)
                self.logger.info("exit")
                exit()            

    
    @property
    def value(self):
        format_mapper={'string':self.format_string_value,
                       'byte'  :self.format_byte_value,
        }
        if self._value == None:
            self._value=self._get_value()
        return format_mapper[self.variable_type](self._value)

        
class StatuBase(ConnectorBase):
    statu_name="uptime"
    statu_type="intger"



vb=VariableBase(variable_name="gtid_mode",variable_type="string")
vb.logger.info('123')
print(vb.value)