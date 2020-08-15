import cx_Oracle
import psycopg2
import pyodbc
import sqlalchemy
import urllib
class DBECC:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        #test-SSID,username-abc ,password:abc1
        self.conn = cx_Oracle.connect("abc/abc1@192.220.1.90:999/test")
        self.cur = self.conn.cursor()
    def close(self):
        self.conn.close()

class DBIPS:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = cx_Oracle.connect("abc/abc1@192.220.1.90:999/test")
        self.cur = self.conn.cursor()
    def close(self):
        self.conn.close()



class DBCIPS:
    def  __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(host = 'ip here', port=8080, user='db',password='db user',database='test')
        self.cur = self.conn.cursor()
        

    def close(self):
        self.conn.close()


class DBCRM:
    def  __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = pyodbc.connect(driver='{SQL Server}',server='ip',database='DBname',uid='pp',pwd='pesss')
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()




