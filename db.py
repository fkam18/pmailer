#!/usr/bin/python3
from datetime import datetime
import sys
import pymysql

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
    print(repr(r1))
  except Exception as e:
    print(repr(e))
    db.rollback()
    sys.exit()
  return db

def dbcheck(db):
  try:
    c1 = db.cursor()
    sql = "select @@autocommit"
    r1=c1.execute(sql)
    db.commit()
    print(repr(r1))
    r2 = c1.fetchone()
    print(repr(r2))
  except Exception as e:
    print(repr(e))
    db.rollback()
    sys.exit()
  
def dbpickjob(db):
  r2 = ()
  try:
    c1 = db.cursor()
    sql = "select * from mails where tries >= 0 order by tries asc limit 1 for update"
    r1=c1.execute(sql)
    print(repr(r1))
    if (r1 > 0):
      r2 = c1.fetchone()
      print(repr(r2))
      print('id:' + repr(r2['id']))
      now = datetime.now()
      dtstr = now.strftime("%Y/%m/%d %H:%M:%S")
      sql = f"update mails set tries=-1, sent='{dtstr}' where id={r2['id']}"
      r1=c1.execute(sql)
      db.commit()
    else:
      print("no job")
  except Exception as e:
    print(repr(e))
    db.rollback()
    sys.exit()
  return r2 

def dbretryjob(db, rowid, newcnt):
  try:
    c1 = db.cursor()
    sql = f"update mails set tries={newcnt} where id={rowid}"
    print(sql)
    r1 = c1.execute(sql)
    db.commit()
  except Exception as e:
    print(repr(e))
    db.rollback()
    sys.exit()
  
