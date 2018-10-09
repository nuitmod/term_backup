#!/usr/bin/env python3

class Wmn:
    def __init__(self, name, job):
        self.i=name
        self.j=job

    def show_wmn(self):
        w=('%s is a %s' % (self.i, self.j))
        print(w)

    def prv(self, level):
        self.l=level
        x=('%s level is %d' % (self.i, self.l))
        print(x)



wm1=Wmn('Maud', 'security')
wm2=Wmn('Ruth', 'programmer')

wm1.show_wmn()
wm2.show_wmn()
wm1.prv(2)
