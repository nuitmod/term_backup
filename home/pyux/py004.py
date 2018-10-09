#!/bin/python

import os
import sys

def model(nm):
    print('Model name is %s' % nm)

def inputfn():
    x = input('Input a model name ')
    return x


u=inputfn()
#print(u)
#inputfn()
model(u)
