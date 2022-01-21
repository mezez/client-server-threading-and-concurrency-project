
import socket
import netutils

sock = socket.create_connection(('localhost', 5577))

sock.sendall(b'TEST TEST CLIENT\r\n')

l = netutils.read_line(sock)
print("RECEIVED: ", l)
