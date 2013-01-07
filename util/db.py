import sqlite3
import os


class Sqlite:
   def __init__(self):
     self.database = 'doorberrypi.db'
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
     result = self.execute(sql, values)
     return result

   def select(self, table, where=None, values=None):
     """Select statement for sqlite3 databases"""
     if values == None:
       item = '*'
     else:
       for i in values:
         item += i + ","
       item = item[:-1]
     sql = 'SELECT %s from %s' % (item, table)
     if where: sql += " WHERE %s" % where
     result = self.execute(sql)
     return result
      
   def create(self, table):
     """Create the table structure based on the project's constraints"""
     

   def execute(self, sql, values):
     """Execute the sql query"""
     try: 
        conn = sqlite3.connect(self.database)
        result = conn.execute(sql, values).fetchall()
        conn.commit()
        conn.close()
     except:
  	result = None
        print("Could not execute query: \n %s" % sql)
     return result


def stripper(sql):
   """strip out dangerous or invalid values from sql statement"""
   return sql


   

