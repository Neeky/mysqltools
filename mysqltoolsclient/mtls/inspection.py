# -*- coding:utf8 -*-

import logging 

from . import variable
from . import base
from . import statu


class Inspection(base.ConnectorBase):
    """
    巡检项的基类
    """
    name     =None
    _statu   =None
    _variable=None
    
    @property
    def value(self):
        self.logger.info("mts.inspection.Inspection.value function is abstract")
        self.close()
        exit()

    @property
    def suggestion(self):
        self.logger.info("mts.inspection.Inspection.suggestion function is abstract")
        self.close()
        exit()

    @property
    def logger(self):
        if self._logger != None:
            return self._logger
        else:
            self._logger=logging.getLogger("mts.inspection.{0}".format(self.__class__))
            stream_handler=logging.StreamHandler()
            formater=logging.Formatter("%(asctime)-24s %(levelname)-8s %(name)-24s : %(message)s")
            stream_handler.setFormatter(formater)
            self._logger.addHandler(stream_handler)
            self._logger.setLevel(logging.DEBUG)
            return self._logger