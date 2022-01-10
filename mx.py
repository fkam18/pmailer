#!/usr/bin/python3

from util import getmx

domain = 'gmail.com'
mx = getmx(domain)
print(mx)
