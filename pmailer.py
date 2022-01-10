#!/usr/bin/python3

#from db import dbconn
#from db import dbcheck
#from db import dbpickjob
from db import *
from smtp import *
import time

# set your own organizational sender
orgsender = 'sales@38cloud.com'
#

db = dbconn()
#dbcheck(db)
while True:
  job=dbpickjob(db)
  if (len(job) > 0):
    print(job['id'], job['tries'])
    if (delivermail(orgsender, job['recipient'], job['subject'], job['message']) ):
      print("job done")
      # the job log part needs to be done later
    else:
      dbretryjob(db, job['id'], job['tries']+1)
  else:
    print("no job found")
  time.sleep(1)
