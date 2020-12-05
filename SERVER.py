import socket                         #this is a module for using sockets
#here we created a server side socket;;and parameters here referred to below bind method;
#AF_INET refers to host name or ip address and SOCK_STREAM refers to TCP protocol
svr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#The bind() method of Python's socket class assigns an IP address and a port number to a socket instance.
svr.bind((socket.gethostname(),1024))   #gethostname is used when we execute program(server,client) on same computer
#gethostname() refers to local host
svr.listen(5)  #Calling listen() makes a socket ready for accepting connections.
#this should be called  before accept()

while True:
    clt,adr=svr.accept()                                     #accepts connection in the queue
    clt.send(bytes("Hey..fellos this is Socket programming in python","utf-8"))

#accept():  will two objects
#simply:clt is object used to send data and adr is the address of requested socket
#Accept a connection. The socket must be bound to an address and listening for connections.
#  The return value is a pair (conn, address) where conn is a new socket object usable to send and
#  receive data on the connection, and address is the address bound to the socket on the other end of the connection.