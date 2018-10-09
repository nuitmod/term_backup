#!/usr/bin/env python

import threading
import os, time, pexpect
import asyncio
from main_io import *

def test_1(): print("asynh start")
test_1()

def object_call():
  wm1=Wm("Ruth", "programmer")
  wm1.get_data()
#object_call()

def th_1():
  i=1
  while i<=9:
    dat=pexpect.run('pwd').rstrip()
    print("1t : {}__{}".format(i,dat));
    i+=1;time.sleep(0.8)

def th_2():
  i=1
  while i<=9:
    dat=os.system('uptime');
    print("2t__{}_{}".format(i,dat));i+=1;time.sleep(1.2)

def i_proc():
  t1=threading.Thread(target=th_1)
  t2=threading.Thread(target=th_2)
  print("1 potok:"); t1.start()
  time.sleep(1)
  print("2 potok: "); t2.start()
  t1.join(); t2.join()
  print("processes complite!")

i_proc()
