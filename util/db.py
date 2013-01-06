import sqlite3
import os


class Sqlite:
   def __init__(self):
     self.database = '../doorberrypi.db'
     if not os.path.exists(self.database):
       print("Database %s not found" % self.database)
       exit()

   def insert(self, table, values):
     """Insert a value into a designated table. Takes two arguments, the name of the 
     table and a list of values to insert"""

     #list of valid tables
     #tables = ["log"]
     #if table in tables: print("hurray!")


     qm = "?," * len(values)
     qm = qm[:-1]
     sql = 'INSERT INTO %s VALUES(%s)' % (table, qm)
     sql = stripper(sql)
     conn = sqlite3.connect(self.database) ##TODO fix
     conn.execute(sql, values)
     conn.commit()

   def select(self, table, values=None):
     """Select statement for sqlite3 databases"""
     print("You are using the select method")

   def create(self, table):
     """Create the table structure based on the project's constrains"""


def stripper(sql):
   """strip out dangerous or invalid values from sql statement"""
   return sql

   

