
import socket
import netutils

print("Creating connection")
s = socket.create_connection(('localhost', 5577))
print("created")

s.sendall(b'HI FROM SIMPLE CLIENT\r\n')
print("sent")
l = netutils.read_line(s)
print("got reply:", l)