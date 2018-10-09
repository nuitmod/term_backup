#!/usr/bin/python

import os
import sys

myint1 = 2
myint2 = 8

i = myint1 + myint2

print(i)

mystr = "we like uzhik"

print(mystr + " " + repr(myint1))
#print(os.data)
print(sys.path)
print(sys.argv[0])
#print(sys.argv[1])

name = input("who are u?")
print("Hello " + name + "!")
