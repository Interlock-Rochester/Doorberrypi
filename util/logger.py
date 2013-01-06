# Description: Logging function used by other processes. 

import multiprocessing
import time, datetime
import sqlite3


class Logging(object):

   def __init__(self, database ):
      conn = sqlite3.connect(database)
      conn.execute('CREATE TABLE IF NOT EXISTS log(date text, level text, action text, uid text)')
      conn.commit()
      self.conn = conn
      

   def log(self, action, uid=None, level="INFO" ):
      """Function that listens for the type of event (ie Door open) and optionally, 
      the user associated to the activity (ie ibutton ID). The timestamp is automatically generated"""


      #connect to sqlite database
      timestamp = str(datetime.datetime.now())
      sql = 'INSERT INTO log VALUES(?, ?, ?, ?)'
      self.conn.execute(sql, (timestamp, level, action, uid))
      self.conn.commit()

   def queue(self):
      self.queue = multiprocessing.Queue()



def worker(q):
   obj = q.get()
   obj.log()

if __name__ == '__main__':
   #queue = multiprocessing.Queue()

   #p = multiprocessing.Process(target=worker, args=(queue,))
   #p.start()

   #queue.put(Logging('Door Open', "Mark"))
   logs = Logging(DATABASE)
   logs.log("Door open", "Mark")

