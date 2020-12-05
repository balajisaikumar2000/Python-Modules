import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()    #when request is sent it must be encode
mysock.send(cmd)

while True:
    data = mysock.recv(5126)       #recv must have arguments
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
