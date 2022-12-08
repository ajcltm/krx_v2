from pathlib import Path
import sqlite3
import pymysql

class Connector:

    def __init__(self):
        self.dir_ = Path.home().joinpath('Desktop', 'krx.db')
    
    def get_connect(self, type):
        if type == 'sqlite':
            return sqlite3.connect(self.dir_)
        elif type == 'mysql':
            return pymysql.connect(host='192.168.35.243', port=3306, user='ajcltm', passwd='2642805Ab!', db='krx', charset='utf8')

