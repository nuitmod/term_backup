import threading
import time
import os

def clock(interval):
    while 1:
        print("The time is %s" % time.ctime())
        time.sleep(interval)
t = threading.Thread(target=clock, args=(15,))
t.daemon = True
t.start()

def p_pwd():
    i=0
    while i<5:
        print(os.system('pwd'))
        i+=1
p_pwd()
clock(0.8)

