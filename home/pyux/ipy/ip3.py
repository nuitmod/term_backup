#!/usr/bin/python3

from urllib import request
import sys

myurl="https://160dff42c3488015311d-78faca853cf0da794384b877826c58f1.ssl.cf5.rackcdn.com/uploads/images/0000/0081/9615/main_LOOK_04_153027W_027.jpg"
#myurl="https://totokaelo.com/calvin-klein-205w39nyc/flare-hem-silk-dress/black/L24EB9"
#myfile="/data/data/com.termux/files/home/pyux/ipy/mod1.jpg"
myfile="/storage/emulated/0/Download/dir1/mod2.jpg"
try:
    print("Start download from " + myurl)
    request.urlretrieve(myurl, myfile)

except Exception:
    print(sys.exc_info())
    exit

print("File downloaded!!")
