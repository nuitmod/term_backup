#!/usr/bin/env python

import redis
import sys, time
from datetime import datetime

print(datetime.now())
try:
  r=redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

  r.set('ruth', 'progrmm')

  r_dat=r.get('ruth')

  print(str(r_dat).upper())

except Exception as e:
  print(e)
