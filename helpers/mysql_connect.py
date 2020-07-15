# -*- coding: utf-8 -*-
#!/usr/bin/env python

import MySQLdb
import MySQLdb.cursors
import time
from app import app

class Database:
    """ Wrapper untuk cursor connection dari MySQLdb
    agar tidak langsung buka koneksi tiap ada request.
    Untuk handling server MySQL yang kadang mati (MySQL server has gone away)
    dicoba connect ulang, kalau masih gagal sleep 2 seconds kemudian
    coba connect lagi. Dibiarkan error kalau masih gagal juga (3 retries)
    """
    db = None
    def connect(self):
        self.db = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD'],
            db=app.config['MYSQL_DB'],
            port=app.config['MYSQL_PORT'],
            charset='utf8',
            use_unicode=True,
            cursorclass=MySQLdb.cursors.DictCursor)

        self.db.autocommit(True)

    def query(self, sql, params=[]):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, params)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                self.connect()
            except:
                time.sleep(2)
                self.connect()
            cursor = self.db.cursor()
            cursor.execute(sql, params)
        return cursor

    def query_bulk(self, sql, param_list=[]):
        try:
            cursor = self.db.cursor()
            cursor.executemany(sql, param_list)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                self.connect()
            except:
                time.sleep(2)
                self.connect()
            cursor = self.db.cursor()
            cursor.executemany(sql, param_list)
        return cursor
