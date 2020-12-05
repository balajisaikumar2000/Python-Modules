import socket
cltg = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cltg.connect((socket.gethostname(),1024))
msg  = cltg.recv(1024)
print(msg.decode("utf-8"))
