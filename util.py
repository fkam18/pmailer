#!/usr/bin/python3
import dns.resolver

def getdomain(email):
  r1 = email.split('@')
  return r1[1]

def getmx(domain):
# better to sort the return list by mx priority; right now just take the 1st one
  for x in dns.resolver.resolve(domain, 'MX'):
    mxline = x.to_text()
    break 
  mx = mxline.split(' ')
  mxhost = mx[1]
  if (mxhost[-1] == '.'):
    mxhost = mxhost[:-1]
  return mxhost
