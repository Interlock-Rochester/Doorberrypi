# Description: Logging function used by other processes. 

import multiprocessing
import time, datetime
import sqlite3

DATABASE = 'doorberrypi.db'

class Logging(object):

   def __init__(self ):
      print("Some shit")

   def log(self, action, uid=None, level="INFO" ):
      """Function that listens for the type of event (ie Door open) and optionally, 
      the user associated to the activity (ie ibutton ID). The timestamp is automatically generated"""
      proc_name = multiprocessing.current_process().name

      #connect to sqlite database
      conn = sqlite3.connect(DATABASE)
      cur = conn.cursor()
      timestamp = str(datetime.datetime.now())
      sql = 'INSERT INTO log VALUES(?, ?, ?, ?)'
      cur.execute(sql, level, action, uid, timestamp)
      cur.commit()
      conn.close()

   def queue(self):
      self.queue = multiprocessing.Queue()



def worker(q):
   obj = q.get()
   obj.log()

if __name__ == '__main__':
   queue = multiprocessing.Queue()

   p = multiprocessing.Process(target=worker, args=(queue,))
   p.start()

   #queue.put(Logging('Door Open', "Mark"))
   log = Logging()
   log.log("Door open", "Mark")


   queue.close()
   queue.join_thread()
   p.join()
#sqlite connection

def sqliteconnect():
  conn = sqlite3.connect(DATABASE)
  cur = conn.cursor()
  return conn,cur

#sqlite table setup


#sqlite adding content


#maintaining state
