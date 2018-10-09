#!/bin/python

import os
import sys

def dir():
    d=os.system('pwd')
    print(d)

def arg():
    i=sys.argv
    x=len(i)
    if x>1:
         print('imput is %s ' % repr(i))
    else:
         print('No imputted arguments!')

dir()
arg()
