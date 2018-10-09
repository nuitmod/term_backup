#!/bin/python

class Wmn:
#    a=0
#    b=0
#    c=0
    def __init__(self):
        print("Hellow root")
        #print('i : %d' % i)
    def getdata(self, x, y):
        self.a = x
        self.b = y
    def addnumber(self):
        self.c = self.a + self.b
    def vivod(self):
        print('sum = %d' % self.c)

class Iwmn(Wmn):
    def __init__(self):
        print('Hellow Iwmn')
    def ii(self):
        print('new class')

#wm = Wmn()
wm = Iwmn()
wm.getdata(2,9)
wm.addnumber()
wm.vivod()
wm.ii()
