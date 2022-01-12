#!/usr/bin/python3
import logging
global1 = "test"

# set debug to INFO to disable logging debug lines to console
def initlog():
  logging.basicConfig(level=logging.DEBUG)
  #logging.basicConfig(level=logging.INFO)

