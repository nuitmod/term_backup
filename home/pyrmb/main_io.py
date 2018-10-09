#!/usr/bin/env python

class Wm:
  def __init__(self, name, job):
      self.name=name
      self.job=job
  def get_data(self):
      print("{} is a {}!".format(self.name,self.job))

"""wm1=Wm("Ruth", "programmer")
wm1.get_data()"""

def inside_m():
    print("inside function!")
