#!/usr/bin/python

from urllib import request, parse
import os

myurl="https://www.google.com/search?"
value = {'q' : 'yoox'}

try:
    mydata=parse.urlencode(value)
    print(mydata)
    myurl = myurl + mydata
    req = request.Request(myurl)
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    for line in otvet:
        print(line)
except Exception:
    print("Error whyle web request!!")
    print(sys.exc.info()[1])
