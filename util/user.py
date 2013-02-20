# Description: User management function used by other processes. 

import multiprocessing
import time, datetime
import db


class User(object):

   def __init__(self):
      ##TODO: fork into a queue thread to send database functions to
      self.table = "users"
      database = "doorberrypi.db"
      self.db = db.Sqlite(database)

   def add(self, first, last, status="enabled", email=None, ):
      """
      Add a user to the system
      """
      #timestamp = str(datetime.datetime.now())
      values = [first, last, status, email ]
      #userdb = db.Sqlite(self.table)
      self.db.insert(self.table, values)

   def delete(self, uid):
      """
      delete a user account
      """
      expr = "uid=%s" (uid)
      self.userdb.delete(self.table, expr)

 
   def update(self, uid):
      """
      update an existing UID. 
      """

   def lookup(self, first=None, last=None, email=None, uid=None,):
      """
      returns one or more records
      """

   def activate(self, uid):
      """
      activate a user account
      """
      return result

   def deactivate(self, uid):
      """
      """
      return status

   def authorized(self, uid):
      """
      """
      return auth
      

   def queue(self):
      self.queue = multiprocessing.Queue()




#def worker(q):
#   obj = q.get()
#   obj.log()

#if __name__ == '__main__':
   #queue = multiprocessing.Queue()

   #p = multiprocessing.Process(target=worker, args=(queue,))
   #p.start()

   #queue.put(Logging('Door Open', "Mark"))
#   logs = Logging()
#   logs.log("Door open", "Mark")

