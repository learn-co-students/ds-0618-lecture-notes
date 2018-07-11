import sqlite3, sys
sys.path.insert(0, '..')
from part_2_ctes import *

class SQLRunner:
    def __init__(self):
        self.connection = sqlite3.connect(':memory:')
        self.cursor = self.connection.cursor()

    def execute_seed_file(self):
        file = open("./seed.sql", 'r')
        sql = file.read()
        cursor = self.cursor.executescript(sql)
        file.close()
        return cursor

    def execute_cte_deletes_duplicates(self):
        cursor = self.cursor.execute(cte_deletes_duplicates())
        return cursor
