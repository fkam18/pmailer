#!/usr/bin/python3

#from db import dbconn
#from db import dbcheck
#from db import dbpickjob
from globalvar import *
from db import *
from smtp import *
import time

# set your own organizational sender
orgsender = 'sales@38cloud.com'
#

initlog()
db = dbconn()
#dbcheck(db)
while True:
  job=dbpickjob(db)
  if (len(job) > 0):
    logging.debug(job['id'], job['tries'])
    if (delivermail(orgsender, job['recipient'], job['subject'], job['message']) ):
      logging.debug("job done")
      # the job log part needs to be done later
    else:
      dbretryjob(db, job['id'], job['tries']+1)
  else:
    logging.debug("no job found")
  time.sleep(1)
