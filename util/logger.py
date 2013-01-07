# Description: Logging function used by other processes. 

import multiprocessing
import time, datetime
import db


class Logger(object):

   def __init__(self):
      ##TODO: fork into a queue thread to send database functions to
      self.table = "log"

   def add(self, action, uid=None, level="INFO" ):
      """Function that listens for the type of event (ie Door open) and optionally, 
      the user associated to the activity (ie ibutton ID). The timestamp is automatically generated"""

      timestamp = str(datetime.datetime.now())
      values = [timestamp, level, action, uid]
      logdb = db.Sqlite()
      logdb.insert(self.table, values)

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
   logs = Logging()
   logs.log("Door open", "Mark")

