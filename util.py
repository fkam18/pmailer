#!/usr/bin/python3
import dns.resolver

def getdomain(email):
  r1 = email.split('@')
  return r1[1]

def getmx(domain):
  # return the MX with the lowest weight
  lowestWeight = 9999
  targetmx = ""
  for x in dns.resolver.resolve(domain, 'MX'):
    mxline = x.to_text()
    mx = mxline.split(' ')
    weight = int(mx[0])
    #logging.debug(weight)
    if (weight < lowestWeight):
      lowestWeight = weight
      targetmx = mx[1]
  if (targetmx[-1] == '.'):
    targetmx = targetmx[:-1]
  return targetmx
