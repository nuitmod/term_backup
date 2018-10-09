import socket

host='192.168.100.5'
port=50000
size=1024

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))
s.send(('hello').encode())
data=s.recv(size)
s.close()
print('Recived from server: %s' % data)

