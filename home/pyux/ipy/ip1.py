#!/usr/bin/python

from urllib import request, parse
import sys

myurl="https://totokaelo.com/calvin-klein-205w39nyc/flare-hem-silk-dress/black/L24EB9"

otvet = request.urlopen(myurl)
mytext = otvet.read()
mytext2 = otvet.readlines()

print(otvet)
#print(mytext)
#for i in mytext2:
#    print(i)
