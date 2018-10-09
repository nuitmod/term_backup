import os
import time
import subprocess

n=input("Puts your name: ")
print("Hello, %s!" % n)
def user():
    z='Dear, '+n
#    n=input("Puts your name: ")
#    print("Hello, %s!" % n)
    return z

def p_dat():
    data=input("Please, input a commamd ")
    i=0
    while i<4:
        x=os.system(data)
        print(x)
        i+=1
        time.sleep(0.9)
    print("Finished, %s!" % user())

user()
p_dat()
