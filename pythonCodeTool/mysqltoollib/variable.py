import mysql.connector
class Variable(object):
    def __init__(self,variablename,user,password,host,port,valueType=int):
        self._variableName=variablename
        self._user=user
        self._password=password
        self._host=host
        self._port=port
        self._value=valueType

    @property
    def value(self):
        cnx=None
        cursor=None
        try:
            cnx=mysql.connector.connect(user=self._user,password=self._password,host=self._host,port=self._port)
            cursor=cnx.cursor()
            cursor.execute("select @@{0}".format(self._variableName))
            rs=cursor.fetchone()
            return self._value(rs[0])
        except Exception as e:
            print(e)
            return None
        finally:
            if cnx != None:
                cnx.close()

    def __str__(self):
        return "mysql variable {0} = {1} .".format(self._variableName,self.value)


