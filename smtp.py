#!/usr/bin/python3
import smtplib
from util import getmx
from util import getdomain


# set to hostname of where pmailer runs
myself = "v151.38cloud.com" 
#

def delivermail(sender, receiver, subject, msg):
  domain = getdomain(receiver)
  mxhost = getmx(domain)
  print(mxhost)
  message = f"From: <{sender}>\nTo: <{receiver}>\nSubject: {subject}\n\n{msg}\n" 
  try:
    with smtplib.SMTP(mxhost,25) as s1:
      r=s1.docmd("ehlo", myself)
      print(r[0])
      print(r[1])
      print(f"<{sender}>")
      r=s1.docmd("MAIL FROM:", f"<{sender}>")
      print(r[0])
      print(r[1])
      if (r[0] > 499):
        raise Exception(r[0])
      print(f"<{receiver}>")
      r=s1.docmd("RCPT TO:", f"<{receiver}>")
      print(r[0])
      print(r[1])
      if (r[0] > 499):
        raise Exception(r[0])
      r=s1.docmd("DATA", f"\n{message}\n.\n")
      print(r[0])
      print(r[1])
      if (r[0] != 250):
        raise Exception(r[0])
      print("success")
  except Exception as e:
    print(repr(e))
  finally:
    print("finished")    
