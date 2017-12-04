from .base import ConnectorBase

class InnodbStatuBase(ConnectorBase):
    
    def show_engine_innodb_status(self):
        self.cursor.execute("show innodb egine status ;")
        