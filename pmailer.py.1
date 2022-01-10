#!/usr/bin/python3
import smtplib
from util import getmx


sender = 'sales@38cloud.com'
receivers = 'm@hmm.im'

message = """From: <sales@38cloud.com>
To: <m@hmm.im>
Subject: SMTP e-mail test


This is a test e-mail message.
"""

mxhost = getmx('hmm.im')
print(mxhost)

try:
  with smtplib.SMTP(mxhost,25) as s1:
#  s1.set_debuglevel(1)
#  s1.sendmail(sender, receivers, message)
      r=s1.docmd("ehlo", "v151.38cloud.com")
      print(r[0])
      print(r[1])
      print(f"<{sender}>")
      r=s1.docmd("MAIL FROM:", f"<{sender}>")
      print(r[0])
      print(r[1])
      if (r[0] > 499):
        raise Exception(r[0])
      print(f"<{receivers}>")
      r=s1.docmd("RCPT TO:", f"<{receivers}>")
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
#except smtplib.SMTPException as e:
#  print(e)
    #except smtplib.SMTPResponseException as e:
    #  print(e.smtp_error)
    #  print(e.smtp_code)
    #except smtplib.SMTPRecipientsRefused as e:
    #  print(e.recipients)
except Exception as e:
    #  print("error" + repr(e))
  print( e)
finally:
  print("finished")    
