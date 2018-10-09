#!/usr/bin/python3

import os
import time

def b_door(cmd,dly):
    while 1:
        x=os.system(cmd)
        print(x)
        time.sleep(dly)

b_door('date',1)
