#!/usr/bin/python3
import smtplib
from util import getmx
from util import getdomain


# set to hostname of where pmailer runs
myhost = "v151.38cloud.com" 
#

def delivermail(sender, receiver, subject, msg):
  domain = getdomain(receiver)
  mxhost = getmx(domain)
  print(mxhost)
  message = f"From: <{sender}>\nTo: <{receiver}>\nSubject: {subject}\n\n{msg}\n" 
  try:
    with smtplib.SMTP(mxhost,25) as s1:
      r=s1.docmd("ehlo", myhost)
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
      print("now DATA")
      r=s1.docmd("DATA")
      print(r[0])
      print(r[1])
      if (r[0] >= 400):
        raise Exception(r[0])
      r=s1.docmd(f"{message}\r\n.\r\n")
      print(r[0])
      print(r[1])
      if (int(r[0]) >= 400):
        raise Exception(r[0])
      print("success")
      return True
  except smtplib.SMTPResponseException as e:
    # obviously no reason to raise a 250 exception so likely a smtplib bug; anyway treated as a handler
    print("smtp exception")
    print(e.smtp_code)
    if (e.smtp_code == 250):
      print("sent")
      return True
    else:
      print(repr(e))
      return False
  except Exception as e:
    print("general exception")
    print(repr(e))
    return False
  #finally:
  #  print("finished")    
