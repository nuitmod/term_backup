from urllib import request
import sys

url=input("Input an url: ")
file=input("Please, name a file: ")
name=file + '.jpg'
dir="/storage/emulated/0/Download/dir1/"+name

#print(name)
#print(dir)
try:
    print("Start download from: " + url)
    request.urlretrieve(url, dir)

except Exception:
    print(sys.exc_info())
    exit

print("Download is over!")
