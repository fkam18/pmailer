#!/usr/bin/python3

#from db import dbconn
#from db import dbcheck
#from db import dbpickjob
from db import *

db = dbconn()
dbcheck(db)
job=dbpickjob(db)
if (len(job) > 0):
  print(job['id'], job['tries'])
  dbretryjob(db, job['id'], job['tries']+1)
else:
  print("no job found")
