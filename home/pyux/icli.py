import socket

cli_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip='192.168.100.5'
port=8080
cli_sock.connect((ip, port))

cli_sock.sendall(('Hello, Ruth!').encode())
data=cli_sock.recv(1024)
cli_sock.close()
print('Received : {}'.format(repr(data)))
