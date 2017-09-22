#-*- coding:utf8 -*-
"""
为常用的MySQL variable 定义与之对应的类，以方便使用。
"""

from .base import VariableBase

#----------------------------------------------------
#全局配置相关的variable
#----------------------------------------------------

class ServerID(VariableBase):
    variable_name="server_id"
    variable_type="intger"

class BaseDir(VariableBase):
    variable_name="basedir"
    variable_type="string"

class DataDir(VariableBase):
    variable_name="datadir"
    variable_type="string"

class Port(VariableBase):
    variable_name="port"
    variable_type="intger"

class CharacterSetServer(VariableBase):
    variable_name="character_set_server"
    variable_type="string"

