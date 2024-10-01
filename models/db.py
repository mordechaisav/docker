import sqlite3
import os

class Database:
    def __init__(self, db_name='users.db'):
        #self.conn = sqlite3.connect(db_name)
        db_file_name = os.path.join('/app/data', db_name)
        self.conn = sqlite3.connect(db_file_name)
        self.conn.row_factory = sqlite3.Row

    def execute_query(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor

    def execute_many(self, query, param_list):
        cursor = self.conn.cursor()
        cursor.executemany(query, param_list)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()