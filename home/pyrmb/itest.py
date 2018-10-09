#!/usr/bin/env python

import os, time, pexpect

dat="innoir"
print\
(dat)

def tt_i():
  i=0
  for _ in range(0,9):
    data=pexpect.run('pwd').rstrip()
    print("i={}__{}".format(i,data))
    i+=1
    time.sleep(0.6)
  print("void is _over: i={}".format(_))

tt_i()
