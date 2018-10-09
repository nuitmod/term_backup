import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM, proto=0)
#ip="127.0.0.1"
ip="192.168.100.5"
#ip="192.168.1.186"
#ip='10.83.108.156'
#port=8888
port=8080
size=1024
print('ip = {} port={}'.format(ip, port))
s.bind((ip,port))

s.listen(12)
while 1:
    cli_sock, cli_addr= s.accept()
    print("Receive from {}".format(cli_addr))
    print("Socket client = {}".format(cli_sock))
    while 1:
        data=cli_sock.recv(size)
        if not data:
            print('recive error')
            break
        print("data is : {}".format(data))
       # cli_sock.sendall(data)
        msg="send data : {}".format(data)
        cli_sock.send(msg.encode())
    cli_sock.close()
