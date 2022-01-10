#!/usr/bin/python3
from datetime import datetime

now = datetime.now()
print(now)
dtstr = now.strftime("%Y/%m/%d %H:%M:%S")
print(dtstr)
