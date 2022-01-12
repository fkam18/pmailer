#!/usr/bin/python3
from globalvar import *
from db import *
from datetime import datetime
import sys

initlog()
if (len(sys.argv) != 3):
  print("Synopsis: cat emailfile | ./submit.py 'recipient' 'subject'");
  quit()

program, recipient, subject = sys.argv
now = datetime.now()
dtstr = now.strftime("%Y/%m/%d %H:%M:%S")

message = ""
for line in sys.stdin:
  message = message + line

db = dbconn()
if (dbinsertjob(db, recipient, subject, message, now)):
  logging.debug("done")
else:
  logging.debug("something went wrong; not done")
quit()

