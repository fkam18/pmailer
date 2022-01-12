#!/usr/bin/python3
from globalvar import *
from datetime import datetime
import sys
import pymysql

initlog()
dbuser = "pmailer"
dbpass = "1Pm3aIl4e5r"
dbname = "pmailer"

def dbconn():
  db = pymysql.connect(host="localhost",user=dbuser,password=dbpass,database=dbname, cursorclass=pymysql.cursors.DictCursor, charset='utf8mb4')
  try:
    c1 = db.cursor()
    sql = "SET AUTOCOMMIT=0"
    r1=c1.execute(sql)
    db.commit()
    #logging.debug(repr(r1))
  except Exception as e:
    logging.debug(repr(e))
    db.rollback()
    sys.exit()
  return db

def dbcheck(db):
  try:
    c1 = db.cursor()
    sql = "select @@autocommit"
    r1=c1.execute(sql)
    db.commit()
    logging.debug(repr(r1))
    r2 = c1.fetchone()
    logging.debug(repr(r2))
  except Exception as e:
    logging.debug(repr(e))
    db.rollback()
    sys.exit()

def dbinsertjob(db, receiver, subject, message, submittime):
  try:
    c1 = db.cursor()
    sql = f"insert into mails (recipient, subject, message, tries, submitted, sent) values ('{receiver}', '{subject}', '{message}', 0, '{submittime}', '{submittime}')"
    #logging.debug(sql)
    r1 = c1.execute(sql)
    db.commit()
    return True
  except Exception as e:
    logging.debug("Error:")
    logging.debug(repr(e))
    db.rollback()
    return False
   
def dbpickjob(db):
  r2 = ()
  try:
    c1 = db.cursor()
    sql = "select * from mails where tries >= 0 order by tries asc limit 1 for update"
    r1=c1.execute(sql)
    logging.debug(repr(r1))
    if (r1 > 0):
      r2 = c1.fetchone()
      logging.debug(repr(r2))
      logging.debug('id:' + repr(r2['id']))
      now = datetime.now()
      dtstr = now.strftime("%Y/%m/%d %H:%M:%S")
      sql = f"update mails set tries=-1, sent='{dtstr}' where id={r2['id']}"
      r1=c1.execute(sql)
      db.commit()
    else:
      logging.debug("no job")
  except Exception as e:
    logging.debug(repr(e))
    db.rollback()
    sys.exit()
  return r2 

def dbretryjob(db, rowid, newcnt):
  try:
    c1 = db.cursor()
    sql = f"update mails set tries={newcnt} where id={rowid}"
    logging.debug(sql)
    r1 = c1.execute(sql)
    db.commit()
  except Exception as e:
    logging.debug(repr(e))
    db.rollback()
    sys.exit()
  
