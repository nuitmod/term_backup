#Сервер

import socket
from threading import Thread

def handler(client_socket, cli_address):
    print(client_address, 'was connected')
    while 1:
        recieve_message = client_socket.recv(1024)

client_socket.send(recieve_message.upper())
server_socket=socket.socket(socket.AF_INET, 
socket.SOCK_STREAM) 

server_socket.bind(('127.0.0.1', 5000))

print('server starts')

server_socket.listen(1)
while 1:
    client_socket, client_address =server_socket.accept()
    Thread(target=handler, 
args=(client_socket, client_address)).start()

#----------------------------------------- 
#Клиент

import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5000))

while 1:
    message = input()
    client_socket.send(message.encode())
    recieve_message = client_socket.recv(1024)
    print(recieve_message.decode())
